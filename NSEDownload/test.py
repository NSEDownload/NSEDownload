import pandas
import requests
import json
import pandas as pd

def get_adjusted_headers():
    return {
        'Host': 'www.nseindia.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
    }


session = requests.Session()
response = session.get('https://www.nseindia.com/', timeout=15, headers=get_adjusted_headers())
print(session.cookies.get_dict())

# session.get('https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE',
#             headers=get_adjusted_headers(),
#             timeout=15,
#             cookies=session.cookies.get_dict())
# print(session.cookies.get_dict())

# response3 = session.get(
#     'https://www.nseindia.com/api/historical/cm/equity?symbol=RELIANCE&series=[%22EQ%22]&from=15-04-2022&to=15-04-2023',
#     headers=get_adjusted_headers(),
#     timeout=15,
#     cookies=session.cookies.get_dict())
#
# print(response3.content)
# final_dictionary = json.loads(response3.content)
#
# print(len(final_dictionary['data']))
# print(final_dictionary['data'][0])
# print(final_dictionary['data'][-1])

response2 = session.get(
    'https://www.nseindia.com/api/historical/cm/equity?symbol=RELIANCE&series=[%22EQ%22]&from=15-07-2022&to=15-04-2023',
    headers=get_adjusted_headers(),
    timeout=15,
    cookies=session.cookies.get_dict())

print(response2.cookies)
print(response2.status_code)
print(response2.content)

if response2.status_code == 200:
    final_dictionary = json.loads(response2.content)
    print(len(final_dictionary['data']))
    print(final_dictionary['data'][0])
    print(final_dictionary['data'][-1])
    df = pd.DataFrame.from_dict(final_dictionary['data'])
    print(df.columns)
    print(df)

# Date,Symbol,Series,Open Price,High Price,Low Price,Last Price,Close Price,Average Price,Total Traded Quantity,Turnover,No. of Trades,Deliverable Qty,% Dly Qt to Traded Qty,
# TIMESTAMP,_id,CH_SYMBOL,CH_SERIES,CH_MARKET_TYPE,CH_TRADE_HIGH_PRICE,CH_TRADE_LOW_PRICE,CH_OPENING_PRICE,CH_CLOSING_PRICE,CH_LAST_TRADED_PRICE,CH_PREVIOUS_CLS_PRICE,CH_TOT_TRADED_QTY,CH_TOT_TRADED_VAL,CH_52WEEK_HIGH_PRICE,CH_52WEEK_LOW_PRICE,CH_TOTAL_TRADES,CH_ISIN,CH_TIMESTAMP,createdAt,updatedAt,__v,SLBMH_TOT_VAL,VWAP,mTIMESTAMP,CA

