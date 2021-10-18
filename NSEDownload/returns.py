import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'


def calculate_returns(data, name = None, make_csv = False):

    if(name != None):
        print("Calculating returns for " + name)
    else:
        print("Calculating returns")

    if(len(data) == 0):
        print("Dataframe given is empty.")
        return

    df = data
    if(len(df) > 1200):
        df = df.iloc[:1200, :]
        print("Size reduced to 1200 rows")

    df["Date"] = df.index
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df = df.rename({'Close Price': 'Close'}, axis='columns')

    startActual  = (df.iloc[0]["Date"]).strftime('%Y-%m-%d')
    endActual = (df.iloc[-1]["Date"]).strftime('%Y-%m-%d')

    df = df.drop_duplicates()
    try:
        df = df.pivot(index="Date", columns="Close")
    except KeyError as e:
        print("Check data provided and index type")
        return

    start_date = df.index.min() - pd.DateOffset(day=1)
    end_date = df.index.max() + pd.DateOffset(day=31)
    dates = pd.date_range(start_date, end_date, freq='D')
    dates.name = 'Date'
    df = df.reindex(dates, method='ffill')
    df = df.stack('Close')
    df = df.sort_index(level=0)
    df = df.reset_index()

    df.index = df["Date"]
    df = (df[startActual:endActual])
    df = df.asfreq(freq="1D")
    df["Date"] = pd.to_datetime(df["Date"])

    # df["1 Day Date"] = (df.Date.shift(1)).dt.date
    # df["1 Day Price"] = ( df["Close"].shift(1) )
    df["1 Day Returns"] = round((df["Close"]/df["Close"].shift(1)) - 1, 4)

    # df["1 Week Date"] = (df.Date.shift(7)).dt.date
    # df["1 Week Price"] = ( df["Close"].shift(7) )
    df["1 Week Returns"] = round((df["Close"]/df["Close"].shift(7)) - 1, 4)

    # df["2 Week Date"] = (df.Date.shift(14)).dt.date
    # df["2 Week Price"] = ( df["Close"].shift(14) )
    df["2 Week Returns"] = round((df["Close"]/df["Close"].shift(14)) - 1, 4)

    # df["1 Month Date"] = (df.Date.shift(30)).dt.date
    # df["1 Month Price"] = ( df["Close"].shift(30) )
    df["1 Month Returns"] = round((df["Close"]/df["Close"].shift(30)) - 1, 4)

    # df["2 Month Date"] = (df.Date.shift(61)).dt.date
    # df["2 Month Price"] = ( df["Close"].shift(61) )
    df["2 Month Returns"] = round((df["Close"]/df["Close"].shift(61)) - 1, 4)

    # df["3 Month Date"] = (df.Date.shift(91)).dt.date
    # df["3 Month Price"] = ( df["Close"].shift(91) )
    df["3 Month Returns"] = round((df["Close"]/df["Close"].shift(91)) - 1, 4)

    # df["6 Month Date"] = (df.Date.shift(182)).dt.date
    # df["6 Month Price"] = ( df["Close"].shift(182) )
    df["6 Month Returns"] = round((df["Close"]/df["Close"].shift(182)) - 1, 4)

    # df["9 Month Date"] = (df.Date.shift(273)).dt.date
    # df["9 Month Price"] = ( df["Close"].shift(273) )
    df["9 Month Returns"] = round((df["Close"]/df["Close"].shift(273)) - 1, 4)

    # df["1 Year Date"] = (df.Date.shift(365)).dt.date
    # df["1 Year Price"] = ( df["Close"].shift(365) )
    df["1 Year Returns"] = round((df["Close"]/df["Close"].shift(365)) - 1, 4)

    # df["2 Year Date"] = (df.Date.shift(730)).dt.date
    # df["2 Year Price"] = ( df["Close"].shift(730) )
    df["2 Year Returns"] = round((df["Close"]/df["Close"].shift(730)) - 1, 4)

    # df["5 Year Date"] = (df.Date.shift(1826)).dt.date
    # df["5 Year Price"] = ( df["Close Price"].shift(1826) )
    # df["5 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(1826) ) -1

    ar = (np.where(df["1 Day Returns"] == 0))
    df.drop(df.index[ar], inplace = True)

    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df.index = df["Date"]
    df.drop(columns="Date", inplace = True)

    try:
        df = df[["Close", "Symbol", "1 Day Returns", "1 Week Returns", "2 Week Returns", "1 Month Returns",
                 "2 Month Returns", "3 Month Returns", "6 Month Returns", "9 Month Returns", "1 Year Returns", "2 Year Returns"]]
    except KeyError as e:
        df = df[["Close", "1 Day Returns", "1 Week Returns", "2 Week Returns", "1 Month Returns", "2 Month Returns",
                 "3 Month Returns", "6 Month Returns", "9 Month Returns", "1 Year Returns", "2 Year Returns"]]

    df = df.iloc[::-1]

    if(make_csv == True):

        if(name == None):
            df.to_excel("data.csv")
            print("File created : data.csv")
        else:
            df.to_excel("{}.csv".format(name))
            print("File created : {}.csv".format(name))

        return

    return df
