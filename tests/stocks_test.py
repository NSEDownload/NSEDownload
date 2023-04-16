import time
import NSEDownload.stocks as stocks
import unittest
import pandas as pd


class Test_stocks(unittest.TestCase):

    def test_get_data(self):
        for stock in ['RELIANCE', 'ITC', 'HDFC', 'HDFCBANK']:
            df = stocks.get_data(stock_symbol=stock, start_date='15-9-2021', end_date='1-10-2021')
            df_actual = pd.read_csv("./tests/stocks_data/{}.csv".format(stock), index_col='Date')
            assert (df == df_actual).all().all()
            time.sleep(10)

    # def test_get_data_check_name(self):
    #     df = stocks.get_data(stock_symbol='ANGELONE', start_date='01-01-2021',
    #                          end_date='01-02-2021')
    #     df_actual = pd.read_csv('./tests/stocks_data/ANGELONE.csv', index_col='Date')
    #     assert (df.to_string() == df_actual.to_string())
    #
    # def test_adjusted_data(self):
    #     df = stocks.get_data(
    #         stock_symbol='IOC', start_date='12-3-2018', end_date='12-4-2018')
    #     df = stocks.get_adjusted_data('IOC', df)
    #     df_actual = pd.read_csv('./tests/stocks_data/IOC.csv', index_col='Date')
    #     assert (df.to_string() == df_actual.to_string())
    #
    # def test_get_adjusted_stock(self):
    #     df = stocks.get_adjusted_stock(stock_symbol='HDFCBANK',
    #                                    start_date='12-1-2011',
    #                                    end_date='12-2-2011')
    #
    #     df_actual = pd.read_csv('./tests/stocks_data/HDFCBANK.csv',
    #                             index_col='Date', parse_dates=True,
    #                             infer_datetime_format=True)
    #
    #     df = df.round(1)
    #     df_actual = df_actual.round(1)
    #
    #     assert (df.to_string() == df_actual.to_string())
    #
    # def test_scrape_bonus_splits(self):
    #     val = stocks.scrape_bonus_splits("LAOPALA", "SPLIT")
    #     assert (str(val) == "[[5.0], ['24-Sep-2014']]")


if __name__ == '__main__':
    unittest.main()
