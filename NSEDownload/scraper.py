import json
from concurrent.futures import ALL_COMPLETED

from bs4 import BeautifulSoup
import datetime
import requests
import re
import math
import pandas as pd
from NSEDownload.static_data import get_adjusted_headers, get_company_events_url
import urllib.parse
import concurrent.futures
import logging

HISTORICAL_DATA_URL = 'https://www.nseindia.com/api/historical/cm/equity?series=[%22EQ%22]&'
BASE_URL = 'https://www.nseindia.com/'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def fetch_cookies():
    response = requests.get(BASE_URL, timeout=30, headers=get_adjusted_headers())
    if response.status_code != requests.codes.ok:
        logging.error("Fetched url: %s with status code: %s and response from server: %s" % (
            BASE_URL, response.status_code, response.content))
        raise ValueError("Please try again in a minute.")
    return response.cookies.get_dict()


def fetch_url(url, cookies):
    """
        This is the function call made by each thread. A get request is made for given start and end date, response is
        parsed and dataframe is returned
    """

    response = requests.get(url, timeout=30, headers=get_adjusted_headers(), cookies=cookies)
    if response.status_code == requests.codes.ok:
        json_response = json.loads(response.content)
        return pd.DataFrame.from_dict(json_response['data'])
    else:
        logging.error("Fetched url: %s with status code: %s and response from server: %s" % (
            BASE_URL, response.status_code, response.content))
        raise ValueError("Please try again in a minute.")


def scrape_data(start_date, end_date, input_type, name):
    """
    Called by stocks and indices to scrape data.
    Create threads for different requests, parses data, combines them and returns dataframe

    Args:
        start_date (datetime.datetime): start date
        end_date (datetime.datetime): end date
        input_type (str): Either 'stock' or 'index'
        name (str, optional): stock symbol or index name. Defaults to None.

    Returns:
        Pandas DataFrame: df containing data for stocksymbol for provided date range
    """

    stage, total_stages = 0, math.ceil((end_date - start_date).days / 50)
    threads, url_list = [], []
    cookies = fetch_cookies()

    for stage in range(total_stages):
        fetch_end_date = end_date - stage * datetime.timedelta(days=50)
        fetch_start_date = fetch_end_date - datetime.timedelta(days=50)
        if input_type == 'stock':
            params = {'symbol': name,
                      'from': fetch_start_date.strftime("%d-%m-%Y"),
                      'to': fetch_end_date.strftime("%d-%m-%Y")}
            url = HISTORICAL_DATA_URL + urllib.parse.urlencode(params)
            url_list.append(url)

    result = pd.DataFrame()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(fetch_url, url, cookies): url for url in url_list}
        concurrent.futures.wait(future_to_url, return_when=ALL_COMPLETED)
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                df = future.result()
                result = pd.concat([result, df])
            except Exception as exc:
                logging.error('%r generated an exception: %s. Please try again later.' % (url, exc))
                raise exc

    return format_dataframe_result(result)


def format_dataframe_result(result):
    columns_required = ["TIMESTAMP", "CH_SYMBOL", "CH_SERIES", "CH_TRADE_HIGH_PRICE",
                        "CH_TRADE_LOW_PRICE", "CH_OPENING_PRICE", "CH_CLOSING_PRICE", "CH_LAST_TRADED_PRICE",
                        "CH_PREVIOUS_CLS_PRICE", "CH_TOT_TRADED_QTY", "CH_TOT_TRADED_VAL", "CH_52WEEK_HIGH_PRICE",
                        "CH_52WEEK_LOW_PRICE"]
    result = result[columns_required]
    result = result.set_axis(
        ['Date', 'Symbol', 'Series', 'High Price', 'Low Price', 'Open Price', 'Close Price', 'Last Price',
         'Prev Close Price', 'Total Traded Quantity', 'Total Traded Value', '52 Week High Price',
         '52 Week Low Price'], axis=1)
    result.set_index('Date', inplace=True)
    result.sort_index(inplace=True)
    return result


def scrape_bonus_splits(stock_symbol, event_type):
    """Scrapes for bonuses and splits

    Args:
        stock_symbol (str): Stock Symbol
        event_type (str): Type of Event

    Returns:
        list: Returns list of dates of event and ratio of original and new price
    """
    dates, ratio = [], []

    if not (event_type == "SPLIT" or event_type == "BONUS"):
        print("Event input_type not understood")
        return [ratio, dates]

    url = get_company_events_url() + stock_symbol + \
          "&Industry=&ExDt=More%20than%2024%20Months&exDt=More%20than%2024%20Months" \
          "&recordDt=&bcstartDt=&industry=&CAType=" + event_type
    response = requests.get(url, timeout=60, headers=get_adjusted_headers())

    page_content = BeautifulSoup(response.content, "html.parser")
    page_content = page_content.text.replace('\n', '').replace('\t', '')

    date_start = page_content.find('exDt:"')
    date_end = page_content.find(',', date_start)

    while date_start != -1:

        sub_start = page_content.find('Spl')
        if sub_start == -1:
            sub_start = page_content.find("sub")

        if event_type == "BONUS":
            sub_start = page_content.find('Bonus')

        sub_end = page_content.find(',', sub_start)

        num = re.findall("\d+", page_content[sub_start:sub_end])

        if len(num) < 2:
            print("Unable to parse given message" + page_content)
        else:
            if event_type == "BONUS":
                ratio.append((int(num[0]) + int(num[1])) / int(num[1]))
            else:
                ratio.append(int(num[0]) / int(num[1]))

        dates.append(page_content[date_start + 6:date_end - 1])
        page_content = page_content[date_end:-1]

        date_start = page_content.find('exDt:"')
        date_end = page_content.find(',', date_start)

    return [ratio, dates]
