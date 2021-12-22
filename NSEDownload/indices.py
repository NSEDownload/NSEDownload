import datetime
from NSEDownload.static_data import values, arr, valuesTRI, arrTRI, get_historical_index_url, get_TRI_index_url
from NSEDownload.check import check_name
from NSEDownload.scraper import scrape_data


def get_data(indexName, full_data=None, start_date=None, end_date=None, indextype=None, check_index=True):
    """[summary]

    Args:
        indexName ([str])           : [Name of index to scrape]
        full_data ([bool], optional): [If set to True, then complete data is scrape]
                                        Defaults to None.
        start_date ([str], optional): [start date of date range in YYYY-MM-DD or DD-MM-YYYY format]
                                        Defaults to None.
        end_date ([str], optional)  : [end date of date range in YYYY-MM-DD or DD-MM-YYYY format]
                                        Defaults to None.
        indextype ([str], optional) : ['historical' or 'TRI']
                                        Defaults to None.
        check_index (bool, optional): [To check if index name is correct]
                                        Defaults to True.

    Raises:
        ValueError: [If no dates are provided]
        ValueError: [Incorrect format of dates]
        ValueError: [If start date > end date]

    Returns:
        [Pandas DataFrame]: [df containing data for index for given date range]
    """
    url, Array, Values = get_historical_index_url(), arr, values

    if(indextype == "TRI" or indextype == "tri" or indextype == "T" or indextype == 't'):
        url, Array, Values = get_TRI_index_url(), arrTRI, valuesTRI

    if(check_index is True):
        check_name(Array, Values, indexName)

    if(full_data is None or full_data is False):

        if(start_date is None or end_date is None):
            raise ValueError("Provide start and end date. ")

        try:
            x = datetime.datetime.strptime(start_date, "%d-%m-%Y")
            y = datetime.datetime.strptime(end_date, "%d-%m-%Y")

        except ValueError:
            try:
                x = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                y = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Dates should be in YYYY-MM-DD or DD-MM-YYYY format")

        if(x > y):
            raise ValueError("Starting date is greater than end date.")

    else:
        print("Downloading Full data for", indexName)
        x = datetime.datetime.strptime('1-1-1990', "%d-%m-%Y")
        y = datetime.datetime.today()

    result = scrape_data(x, y, 'index', indexName=indexName, url=url)
    return result
