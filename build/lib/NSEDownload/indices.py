import datetime

from NSEDownload.scraper import scrape_data
from NSEDownload.static_data import get_historical_index_url, get_tri_index_url, \
    get_formatted_names_indices, get_common_names_indices


def get_data(index_name, full_data=False, start_date=None, end_date=None, indextype=None):
    """
    To get data for indices using dates or full_data

    Args:
        index_name (str): Name of index to scrape
        full_data (bool, optional): If set to True, then complete data is scrape. Defaults to False.
        start_date (str, optional): start date of date range in YYYY-MM-DD or DD-MM-YYYY format. Defaults to None.
        end_date (str, optional): end date of date range in YYYY-MM-DD or DD-MM-YYYY format. Defaults to None.
        indextype (str, optional): 'historical' or 'TRI'. Defaults to None.

    Raises:
        ValueError: If no dates are provided/ Incorrect format of dates/ If start date > end date

    Returns:
        DataFrame: DataFrame containing data for index for given date range

    ##Example:
    ```
    from NSEDownload import indices
    # Getting historical data for index using date range
    df = indices.get_data(indexName = "NIFTY Shariah 25",start_date="09-01-2017",end_date="14-08-2019")
    ```

    Output
    ```
            Open High Low    Close    Shares Traded Turnover (Rs. Cr)   
    Date                                                                   
    2017-01-09    -    -   -  3281.54                -                 -   
    2017-01-10    -    -   -  3295.08                -                 -   
    2017-01-11    -    -   -  3327.22                -                 -   
    2017-01-12    -    -   -  3323.66                -                 -   
    2017-01-13    -    -   -  3306.55                -                 -   
    ...         ...  ...  ..      ...              ...               ... ..
    2018-01-02    -    -   -  4279.85         48401645           2403.21   
    2018-01-03    -    -   -  4277.67         46232696           3194.03   
    2018-01-04    -    -   -  4323.68         50699017           3333.30   
    2018-01-05    -    -   -  4354.23         56414034           3668.95   
    2018-01-08    -    -   -  4382.23         42746996           2925.44   

    [249 rows x 7 columns]
    ```

    ```
    from NSEDownload import indices
    # Using full_data argument to get complete data since inception
    df = indices.get_data(indexName = "NIFTY 100", full_data=True)

    # Getting TRI data 
    df = indices.get_data(indexName = "NIFTY 100", full_data=True, indextype="TRI")

    ```

    """

    index_name = check_name(index_name)

    url = get_historical_index_url()
    if indextype == "TRI" or indextype == "tri" or indextype == "T" or indextype == 't':
        url = get_tri_index_url()

    if full_data is False:

        if start_date is None or end_date is None:
            raise ValueError("Provide start and end date.")

        parsed_start_date, parsed_end_date = parse_date(start_date), parse_date(end_date)

        if parsed_start_date > parsed_end_date:
            raise ValueError("Starting date is greater than end date.")

    else:

        parsed_start_date = datetime.datetime.strptime('1-1-1990', "%d-%m-%Y")
        parsed_end_date = datetime.datetime.today()

    return scrape_data(parsed_start_date, parsed_end_date, 'index', index_name=index_name, url=url)


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


def check_name(name):
    """Checking for proper index name and returning with proper formatting

    Args:
        name (str): Name of stock or index

    Raises:
        ValueError: If the name is not in the list then raises error
    """

    formatted_names, common_names = get_formatted_names_indices(), get_common_names_indices()
    for i in range(len(formatted_names)):
        if formatted_names[i] == name or common_names[i] == name:
            return formatted_names[i]

    raise ValueError("Please check symbol " + name)
