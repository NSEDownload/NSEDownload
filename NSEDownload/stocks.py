from NSEDownload.scraper import scrape_data, scrape_bonus_splits, scrape_symbolCount
from NSEDownload.check import check_name
from NSEDownload.static_data import stocks_values
import pandas as pd
import datetime

pd.options.mode.chained_assignment = None


def get_data(stockSymbol, full_data=None, start_date=None, end_date=None):

    check_name(stocks_values, stocks_values, stockSymbol)
    stockSymbol = stockSymbol.replace('&', '%26')
    symbolCount = scrape_symbolCount(stockSymbol)

    if(full_data == None or full_data == "No"):
        x = datetime.datetime.strptime(start_date, "%d-%m-%Y")
        y = datetime.datetime.strptime(end_date, "%d-%m-%Y")

    elif(full_data == "Yes" or full_data == "yes" or full_data == True or full_data == "Y"):
        x = datetime.datetime.strptime('1-1-1992', "%d-%m-%Y")
        y = datetime.datetime.today()

    if(x > y):
        raise ValueError("Starting date is greater than end date.")

    result = scrape_data(
        x, y, 'stock', stockSymbol=stockSymbol, symbolCount=symbolCount)
    return result


def get_adjusted_data(stockSymbol, df):

    events = ['SPLIT', 'BONUS']
    arr = ['Open Price', 'High Price', 'Low Price',
           'Last Price', 'Close Price', 'Average Price']

    stockSymbol = stockSymbol.replace('&', '%26')

    if(df.empty):
        print("Please check data. Dataframe is empty")
        return df

    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    try:
        df = df.drop(['Prev Close'], axis=1)
    except KeyError:
        pass

    for event in events:

        ratio, dates = scrape_bonus_splits(stockSymbol, event)
        for i in range(len(dates)):

            date = datetime.datetime.strptime(dates[i], '%d-%b-%Y')
            print(event, " on : ", dates[i], " and ratio is : ", ratio[i])

            changed_data = df.loc[df.index < date]
            same_data = df.loc[df.index >= date]

            for j in arr:

                try:
                    changed_data.loc[:, j] = changed_data.loc[:, j]/ratio[i]
                except TypeError:
                    pass

            df = pd.concat([changed_data, same_data])

    return df
