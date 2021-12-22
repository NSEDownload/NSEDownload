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
        start_date ([str], optional): [start date of date range]
                                        Defaults to None.
        end_date ([str], optional)  : [end date of date range]
                                        Defaults to None.
        indextype ([str], optional) : ['historical' or 'TRI']
                                        Defaults to None.
        check_index (bool, optional): [To check if index name is correct]
                                        Defaults to True.

    Raises:
        ValueError: [If no dates are provided]
        ValueError: [If start date > end date]

    Returns:
        [Pandas DataFrame]: [df containing data for index for given date range]
    """
    url, Array, Values = get_historical_index_url(), arr, values

    if(indextype == "TRI" or indextype == "tri" or indextype == "T" or indextype == 't'):
        url, Array, Values = get_TRI_index_url(), arrTRI, valuesTRI

    if(check_index is True):
        check_name(Array, Values, indexName)

    if(full_data is None or full_data == "No"):
        x = datetime.datetime.strptime(start_date, "%d-%m-%Y")
        y = datetime.datetime.strptime(end_date, "%d-%m-%Y")

        if(x > y):
            raise ValueError("Starting date is greater than end date.")

    elif(full_data == "Yes" or full_data == "yes" or full_data is True or full_data == "Y"):
        x = datetime.datetime.strptime('1-1-1990', "%d-%m-%Y")
        y = datetime.datetime.today()

        if(x > y):
            raise ValueError("Starting date is greater than end date.")

    result = scrape_data(x, y, 'index', indexName=indexName, url=url)
    return result
