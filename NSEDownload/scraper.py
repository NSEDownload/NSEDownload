from concurrent.futures import ALL_COMPLETED

import json
import datetime
import requests
import math
import pandas as pd
import urllib.parse
import concurrent.futures
import logging

HISTORICAL_DATA_URL = 'https://www.nseindia.com/api/historical/cm/equity?series=[%22EQ%22]&'
BASE_URL = 'https://www.nseindia.com/'
CORPORATE_EVENTS_URL = 'https://www.nseindia.com/api/corporate-announcements?'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def get_headers():
    return {
        "Host": "www1.nseindia.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
        'Content-Type': 'application/start_date-www-form-urlencoded; charset=UTF-8'
    }


def get_adjusted_headers():
    return {
        'Host': 'www.nseindia.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
    }


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
