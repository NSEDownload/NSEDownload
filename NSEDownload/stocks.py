from NSEDownload.scraper import scrape_data
import pandas as pd
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
pd.options.mode.chained_assignment = None


def get_data(stock_symbol, full_data=False, start_date=None, end_date=None):
    """
    Function to get un-adjusted data for stocks

    Args:
        stock_symbol (str): Scrip or Stock symbol in uppercase only
        full_data (bool, optional): Parameter to get complete data since inception. Defaults to False.
        start_date ([input_type], optional): start date of date range in YYYY-MM-DD or DD-MM-YYYY format.
        Defaults to None.
        end_date ([input_type], optional): end date of date range in YYYY-MM-DD or DD-MM-YYYY format. Defaults to None.

    Raises:
        ValueError: If no dates are provided/ Incorrect format of dates/ If start date > end date

    Returns:
        DataFrame: Data for stocksymbol for given date range

    ##Example
    ```
    # Providing date range
    df = stocks.get_data(stock_symbol="RELIANCE", start_date='15-9-2021', end_date='1-10-2021')
    ```
    Output
    ```
    | Date                     | Symbol | Series | High Price | Low Price | Open Price | Close Price | Last Price | Prev Close Price | Total Traded Quantity | Total Traded Value | 52 Week High Price | 52 Week Low Price |
    |--------------------------|--------|--------|------------|-----------|------------|-------------|------------|------------------|-----------------------|--------------------|--------------------|-------------------|
    | 2021-08-11T18:30:00.000Z | HDFC   | EQ     | 2675.25    | 2646.6    | 2656.6     | 2668.75     | 2666.0     | 2658.5           | 1702479               | 4532596291.9       | 2896               | 1623              |
    | 2021-08-12T18:30:00.000Z | HDFC   | EQ     | 2715.0     | 2662.0    | 2662.0     | 2704.15     | 2702.1     | 2668.75          | 3248615               | 8774705017.55      | 2896               | 1623              |
    | 2021-08-15T18:30:00.000Z | HDFC   | EQ     | 2734.45    | 2693.8    | 2696.8     | 2731.15     | 2732.7     | 2704.15          | 2465887               | 6709996706.95      | 2896               | 1623              |
    | 2021-08-16T18:30:00.000Z | HDFC   | EQ     | 2750.0     | 2707.15   | 2729.95    | 2738.4      | 2745.6     | 2731.15          | 2795510               | 7620988084.3       | 2896               | 1623              |
    | 2021-08-17T18:30:00.000Z | HDFC   | EQ     | 2770.3     | 2698.0    | 2750.0     | 2710.75     | 2710.0     | 2738.4           | 2501410               | 6828940469.75      | 2896               | 1623              |

    ```

    ```
    # Using full_data argument
    df = stocks.get_data(stock_symbol='RELIANCE', full_data=True)

    ```

    """

    stock_symbol = stock_symbol.replace('&', '%26')

    if full_data is True:
        parsed_start_date = datetime.datetime.strptime('1-1-1992', "%d-%m-%Y")
        parsed_end_date = datetime.datetime.today()

    else:
        if start_date is None or end_date is None:
            raise ValueError("Provide start and end date.")

        parsed_start_date = parse_date(start_date)
        parsed_end_date = parse_date(end_date)

        if parsed_start_date > parsed_end_date:
            raise ValueError("Starting date is greater than end date.")

    result = scrape_data(start_date=parsed_start_date, end_date=parsed_end_date, input_type='stock', name=stock_symbol)
    return result


def parse_date(text):
    """
    Parses date in either YYYY-MM-DD or DD-MM-YYYY format
    """

    for fmt in ('%Y-%m-%d', '%d-%m-%Y'):
        try:
            return datetime.datetime.strptime(text, fmt)
        except ValueError:
            pass

    raise ValueError('Dates should be in YYYY-MM-DD or DD-MM-YYYY format')
