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


if __name__ == '__main__':
    unittest.main()
