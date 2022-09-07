import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


def calculate_returns(daily_data, include_date=False, include_price=False, make_csv=False, name=None):
    """

    Calculates trailing returns over different time periods and returns df or makes csv file. The time periods are : 1 Day, 1 Week, 2 Weeks, 1 Month, 3 Months, 6 Months, 9 Months, 1 Year, 2 Years.

    Args:
        daily_data (DataFrame): Stock or index data
        include_date (bool, optional): If set to true, date of stock for given time period is added as a column in the dataframe. Defaults to False.
        include_price (bool, optional): If set to true, price of stock for given time period is added as a column in the dataframe. Defaults to False.
        make_csv (bool, optional): To make a csv file of returns. Defaults to False.
        name (type, optional): Name of csv file. Defaults to None.

    Returns:
        DataFrame: DataFrame containing returns

    ##Example
    ```
    from NSEDownload import returns
    stock_returns = returns.calculate_returns(df, make_csv = True, name = "Returns")
    ```

    The returns should look like: (Columns truncated for visualization)


    | Date       |    Close | 1 Day Returns   | 1 Week Returns   | 2 Week Returns   | 1 Month Returns   | 2 Month Returns   | 3 Month Returns   | 6 Month Returns   |
    |:----------:|:--------:|:---------------:|:----------------:|:----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|
    | 2021-10-14 | 18338.5  | 0.0097          | 0.0308           | 0.0409           | 0.0552            | 0.1095            | 0.1516            | 0.2577            |
    | 2021-10-13 | 18161.8  | 0.0094          | 0.0292           | 0.0254           | 0.0465            | 0.0988            | 0.1456            | 0.2521            |
    | 2021-10-12 | 17992    | 0.0026          | 0.0095           | 0.0137           | 0.0359            | 0.0995            | 0.1378            | 0.2404            |
    | 2021-10-11 | 17946    | 0.0028          | 0.0144           | 0.0051           | 0.0332            | 0.1022            | 0.1436            | 0.254             |
    | 2021-10-08 | 17895.2  | 0.0059          | 0.0207           | 0.0024           | 0.0312            | 0.102             | 0.1406            | 0.2063            |
    | 2021-10-07 | 17790.3  | 0.0082          | 0.0098           | -0.0018          | 0.0247            | 0.0956            | 0.1311            | 0.1961            |
    | 2021-10-06 | 17646    | -0.0099         | -0.0037          | 0.0057           | 0.0154            | 0.0867            | 0.1112            | 0.1908            |
    | 2021-10-05 | 17822.3  | 0.0074          | 0.0042           | 0.0148           | 0.0288            | 0.0938            | 0.1267            | 0.2138            |
    | 2021-10-04 | 17691.2  | 0.0091          | -0.0092          | 0.0169           | 0.0212            | 0.0881            | 0.1173            | 0.2086            |
    """

    if name is not None:
        print("Calculating returns for " + name)
    else:
        print("Calculating returns")

    if len(daily_data) == 0:
        print("Dataframe given is empty.")
        return

    df = daily_data
    if len(df) > 1200:
        raise ValueError("Size reduced to 1200 rows")

    df["Date"] = df.index
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df = df.rename({'Close Price': 'Close'}, axis='columns')

    actual_start_date = (df.iloc[0]["Date"]).strftime('%Y-%m-%d')
    actual_end_date = (df.iloc[-1]["Date"]).strftime('%Y-%m-%d')

    df = df.drop_duplicates()
    try:
        df = df.pivot(index="Date", columns="Close")
    except KeyError as e:
        print("Check data provided and index type", e)
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
    df = (df[actual_start_date:actual_end_date])
    df = df.asfreq(freq="1D")
    df["Date"] = pd.to_datetime(df["Date"])

    shift_by = [1, 7, 14, 30, 61, 91, 182, 273, 365, 730]
    time_periods = ['1 Day', '1 Week', '2 Week', '1 Month', '2 Month', '3 Month', '6 Month', '9 Month', '1 Year',
                    '2 Year']

    for i in range(len(shift_by)):

        if include_date is True:
            df[time_periods[i] + ' Date'] = (df.Date.shift(shift_by[i])).dt.date

        if include_price is True:
            df[time_periods[i] + ' Price'] = df["Close"].shift(shift_by[i])

        df[time_periods[i] + ' Returns'] = round((df["Close"] / df["Close"].shift(shift_by[i])) - 1, 4)

    ar = (np.where(df["1 Day Returns"] == 0))
    df.drop(df.index[ar], inplace=True)

    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df.index = df["Date"]

    try:
        df.drop(columns=["Date", 'Open', 'High', 'Low', 'Shares Traded', 'Turnover (Rs. Cr)'], inplace=True)
    except KeyError:
        df.drop(
            columns=['Date', 'Symbol', 'Series', 'Open Price', 'High Price', 'Low Price', 'Last Price', 'Average Price',
                     'Total Traded Quantity', 'Turnover', 'No. of Trades', 'Deliverable Qty', '% Dly Qt to Traded Qty'],
            inplace=True)

    df = df.iloc[::-1]
    df.fillna('-', inplace=True)

    if make_csv is True:

        if name is None:
            df.to_csv("data.csv", float_format='%.2f')
            print("File created : data.csv")
        else:
            df.to_csv("{}.csv".format(name), float_format='%.2f')
            print("File created : {}.csv".format(name))

    return df
