import NSEDownload.indices as indices   # The code to test
import unittest   # The test framework
import pandas as pd


class Test_stocks(unittest.TestCase):

    def test_get_data(self):

        df = indices.get_data(indexName='NIFTY 50',
                              start_date='15-9-2005',
                              end_date='1-10-2005')

        df_actual = pd.read_csv('tests/indices_data/NIFTY_50.csv',
                                index_col='Date')

        assert(df.to_string() == (df_actual).to_string())

    def test_get_data_2(self):

        df = indices.get_data(indexName="NIFTY MidSmallcap 400",
                              start_date='1-9-2006',
                              end_date='7-10-2006')

        df_actual = pd.read_csv('tests/indices_data/NIFTY_MS_400.csv',
                                index_col='Date')

        assert(df.to_string() == (df_actual).to_string())

    def test_get_data_3(self):

        df = indices.get_data(indexName="NIFTY Shariah 25",
                              start_date="09-01-2017",
                              end_date="14-08-2017")

        df_actual = pd.read_csv('tests/indices_data/NIFTY_S_25.csv',
                                index_col='Date')

        assert(df.to_string() == (df_actual).to_string())

    def test_get_data_TRI(self):

        df = indices.get_data(indexName="NIFTY100 LIQUID 15",
                              start_date="09-01-2017",
                              end_date="14-08-2017",
                              indextype='TRI')

        df_actual = pd.read_csv('tests/indices_data/NIFTY_L_100_TRI.csv',
                                index_col='Date')

        assert(df.to_string() == (df_actual).to_string())


if __name__ == '__main__':
    unittest.main()
