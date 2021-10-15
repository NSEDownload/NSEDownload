import datetime
from NSEDownload.static_data import values, arr, valuesTRI, arrTRI, get_historical_index_url, get_TRI_index_url
from NSEDownload.check import check_name
from NSEDownload.scraper import scrape_data


def get_data(indexName, full_data=None, start_date=None, end_date=None, indextype=None):

    Array, Values = arr, values

    url = get_historical_index_url()

    if(indextype == "TRI" or indextype == "tri" or indextype == "T" or indextype == 't'):
        url, Values, Array = get_TRI_index_url, valuesTRI, arrTRI

    check_name(Array, Values, indexName)

    if(full_data == None or full_data == "No"):

        x = datetime.datetime.strptime(start_date, "%d-%m-%Y")
        y = datetime.datetime.strptime(end_date, "%d-%m-%Y")

        if(x > y):
            raise ValueError("Starting date is greater than end date.")

    elif(full_data == "Yes" or full_data == "yes" or full_data == True or full_data == "Y"):

        x = datetime.datetime.strptime('1-1-1992', "%d-%m-%Y")
        y = datetime.datetime.today()

        if(x > y):
            raise ValueError("Starting date is greater than end date.")

    result = scrape_data(x, y, 'index', indexName, url)
    return result
