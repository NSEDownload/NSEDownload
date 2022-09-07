import datetime
import math
import re
import threading
from io import StringIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry

from NSEDownload.static_data import get_headers, get_adjusted_headers, get_symbol_mapping_url, get_company_events_url, \
    get_symbol_count_url

interim_dfs = []


def process_window(stage, url):
    response = make_get_request(url)
    try:
        interim_dfs[stage] = process_html_response(response)
    except AttributeError:
        pass


def process_html_response(response):
    page_content = BeautifulSoup(response, "html.parser")
    lines = page_content.find(id="csvContentDiv").get_text()
    lines = lines.replace(':', ", \n")
    df = pd.read_csv(StringIO(lines))
    df.set_index("Date", inplace=True)
    df = df[::-1]
    return df


def make_get_request(url):
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    response = session.get(url, timeout=10, headers=get_headers())
    session.close()
    return response.content


def scrape_data(start_date, end_date, request_type,
                index_name=None, url=None, stock_symbol=None, symbol_count=None, series="EQ"):
    """Called by stocks and indices to scrape data. Create threads for different requests, parses data, combines them and returns dataframe

    Args:
        start_date (datetime): start date
        end_date (datetime): end date
        request_type (str): Either 'stock' or 'index'
        index_name (str, optional): If type index then this gives name of index. Defaults to None.
        url (str, optional): URL to scrape from. Defaults to None.
        stock_symbol (str, optional): If type stock then this gives stock symbol. Defaults to None.
        symbol_count (str, optional): Intermediate variable needed for scraping. Defaults to None.
        series(str, optional): By default set to EQ, but can choose any series or All

    Returns:
        Pandas DataFrame: df containing data for stocksymbol for provided date range
    """

    total_stages = math.ceil((end_date - start_date).days / 365)
    global interim_dfs
    interim_dfs = [pd.DataFrame()] * total_stages

    threads = []
    for stage in range(total_stages):

        window_start_date = start_date + stage * datetime.timedelta(days=365)
        window_end_date = window_start_date + datetime.timedelta(days=364)

        if window_start_date > end_date:
            break

        if window_end_date > end_date:
            window_end_date = end_date

        if request_type == 'stock':
            final_url = get_symbol_mapping_url() + '?symbol=' + stock_symbol + '&segmentLink=3&symbolCount' \
                        + symbol_count + "&series=" + series + "&dateRange=+&fromDate=" + \
                        window_start_date.strftime(
                            "%d-%m-%Y") + "&toDate=" + window_end_date.strftime(
                "%d-%m-%Y") + "&dataType=PRICEVOLUMEDELIVERABLE"

        if request_type == 'index':
            final_url = url + '?indexType=' + index_name + \
                        '&fromDate=' + \
                        window_start_date.strftime("%d-%m-%Y") + '&toDate=' + \
                        window_end_date.strftime("%d-%m-%Y")

        thread = threading.Thread(target=process_window, args=[stage, final_url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    result = pd.DataFrame()
    for stage in range(total_stages):
        result = pd.concat([result, interim_dfs[stage]])
    result.index = pd.to_datetime(result.index)
    result.sort_index(inplace=True)

    return result


def scrape_bonus_splits(symbol, event_type):
    """Scrapes for bonuses and splits

    Args:
        symbol (str): Stock Symbol
        event_type (str): Type of Event

    Returns:
        list: Returns list of dates of event and ratio of original and new price
    """

    event_dates, event_ratio = [], []
    if not (event_type == "SPLIT" or event_type == "BONUS"):
        print("Event type not understood")
        return [event_ratio, event_dates]

    url = get_company_events_url() + symbol + \
          "&Industry=&ExDt=More%20than%2024%20" \
          "Months&exDt=More%20than%2024%20Months" \
          "&recordDt=&bcstartDt=&industry" \
          "=&CAType=" + event_type

    response = requests.get(url, timeout=60, headers=get_adjusted_headers())
    page_content = BeautifulSoup(response.content, "html.parser").text.replace('\n', '').replace('\t', '')
    start_date = page_content.find('exDt:"')
    end_date = page_content.find(',', start_date)

    while start_date != -1:

        sub_start = page_content.find('Spl')
        if sub_start == -1:
            sub_start = page_content.find("sub")

        if event_type == "BONUS":
            sub_start = page_content.find('Bonus')

        sub_end = page_content.find(',', sub_start)
        num = re.findall('\d+', page_content[sub_start:sub_end])

        if len(num) < 2:
            print("Unable to parse given message" + page_content)
        elif event_type == "BONUS":
            event_ratio.append((int(num[0]) + int(num[1])) / int(num[1]))
        else:
            event_ratio.append(int(num[0]) / int(num[1]))

        event_dates.append(page_content[start_date + 6:end_date - 1])
        page_content = page_content[end_date:-1]

        start_date = page_content.find('exDt:"')
        end_date = page_content.find(',', start_date)

    return [event_ratio, event_dates]


def scrape_symbol(symbol):
    """Scraping intermediate variable symbol Count

    Args:
        symbol (str): Stock Symbol

    Raises:
        SystemExit: Exit on any exception to request

    Returns:
        str: Symbol Count
    """

    try:
        response = requests.post(get_symbol_count_url(),
                                 data={"symbol": symbol},
                                 headers=get_headers(),
                                 timeout=60)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if response.status_code != requests.codes.ok:
        response.raise_for_status()

    return str(BeautifulSoup(response.content, "html.parser"))
