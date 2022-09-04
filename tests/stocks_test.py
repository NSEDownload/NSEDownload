import NSEDownload.stocks as stocks   # The code to test
import unittest   # The test framework
import pandas as pd

class Test_stocks(unittest.TestCase):

    def test_get_data(self):

        df = stocks.get_data(symbol='RELIANCE',
                             start_date='15-9-2021', end_date='1-10-2021')
        df_actual = pd.read_csv(
            'tests/stocks_data/RELIANCE.csv', index_col='Date')
        self.assertTrue(df.to_string() == (df_actual).to_string())

        df = stocks.get_data(symbol='ANGELONE', start_date='01-01-2021',
                             end_date='01-02-2021')
        df_actual = pd.read_csv(
            'tests/stocks_data/ANGELONE.csv', index_col='Date')
        self.assertTrue(df.to_string() == (df_actual).to_string())

    def test_scrape_bonus_splits(self):
        val = stocks.scrape_bonus_splits("LAOPALA", "SPLIT")
        self.assertTrue(str(val) == "[[5.0], ['24-Sep-2014']]")

    def test_data(self):
        df = stocks.get_data(symbol='JSWENERGY', full_data=True, series="ALL")
        self.assertFalse(df.empty)

        df = stocks.get_data(symbol='RELIANCE', full_data=True, series="ALL")
        self.assertFalse(df.empty)

        df = stocks.get_data(symbol='ITC', full_data=True, series="ALL")
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
