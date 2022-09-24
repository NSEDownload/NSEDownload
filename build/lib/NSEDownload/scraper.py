import datetime
import json
import math
import pandas as pd
import re
import requests
import threading
from bs4 import BeautifulSoup
from io import StringIO
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


def add_quotes_to_field(match):
    match = match.group()
    return match[0] + '"' + match[1:-1] + '":'


def scrape_bonus_splits(symbol):
    """Scrapes for bonuses and splits

    Args:
        symbol (str): Stock Symbol

    Returns:
        list: Returns list of dates of event and ratio of original and new price
    """

    event_dates, event_ratio = [], []
    url_more_than_24 = get_company_events_url() + symbol + \
                       "&Industry=&ExDt=More%20than%2024%20" \
                       "Months&exDt=More%20than%2024%20Months" \
                       "&recordDt=&bcstartDt=&industry" \
                       "=&CAType="

    url_last_24 = get_company_events_url() + symbol + \
                  "&Industry=&ExDt=Last%2012%20Months" \
                  "&exDt=Last%2012%20Months&" \
                  "&recordDt=&bcstartDt=&industry" \
                  "=&CAType="

    for url in [url_more_than_24, url_last_24]:

        response = requests.get(url, timeout=60, headers=get_adjusted_headers())
        page_content = "{" + BeautifulSoup(response.content, "html.parser").text.replace('\n', '').replace('\t', '')[16:]
        json_input = re.sub(r'[{,][a-zA-Z]+:', add_quotes_to_field, page_content)
        json_content = json.loads(json_input)
        corporate_actions = json_content["rows"]

        for row in corporate_actions:

            subject = row["sub"].lower()
            date = row["exDt"]
            if date not in event_dates:

                # Scraping for Splits
                if subject.find("split") != -1 or subject.find("division") != -1:
                    num = re.findall('\d+', subject)
                    if len(num) < 2:
                        continue
                    event_ratio.append(int(num[0]) / int(num[1]))
                    event_dates.append(date)
                    print("Split event on: " + date)

                # Scraping for Bonus
                if subject.find("bonus") != -1:
                    num = re.findall('\d+', subject)
                    if len(num) < 2:
                        continue
                    event_ratio.append((int(num[0]) + int(num[1])) / int(num[1]))
                    event_dates.append(date)
                    print("Bonus event on: " + date)

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
