import NSEDownload.stocks as stocks   # The code to test
import unittest   # The test framework
import pandas as pd


class Test_stocks(unittest.TestCase):

    def test_get_data(self):

        df = stocks.get_data(stockSymbol='RELIANCE',
                             start_date='15-9-2021', end_date='1-10-2021')
        df_actual = pd.read_csv(
            'tests/stocks_data/RELIANCE.csv', index_col='Date')
        assert(df.equals(df_actual))

    def test_get_data_check_name(self):

        df = stocks.get_data(stockSymbol='ANGELONE', start_date='01-01-2021',
                             end_date='01-02-2021', check_stockSymbol=False)
        df_actual = pd.read_csv(
            'tests/stocks_data/ANGELONE.csv', index_col='Date')
        assert(df.equals(df_actual))

    def test_adjusted_data(self):

        df = stocks.get_data(
            stockSymbol='IOC', start_date='12-3-2018', end_date='12-4-2018')
        df = stocks.get_adjusted_data('IOC', df)
        df_actual = pd.read_csv('tests/stocks_data/IOC.csv', index_col='Date')
        assert(df.equals(df_actual))

    def test_get_adjusted_stock(self):

        df = stocks.get_adjusted_stock(stockSymbol='HDFCBANK',
                                       start_date='12-1-2011',
                                       end_date='12-2-2011')

        df_actual = pd.read_csv('tests/stocks_data/HDFCBANK.csv',
                                index_col='Date', parse_dates=True,
                                infer_datetime_format=True)

        df = df.round(1)
        df_actual = df_actual.round(1)

        assert(df.equals(df_actual))


if __name__ == '__main__':
    unittest.main()
