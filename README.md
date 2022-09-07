# **NSEDownload** #

[![Bump Up version](https://github.com/NSEDownload/NSEDownload/actions/workflows/Bump.yaml/badge.svg)](https://github.com/NSEDownload/NSEDownload/actions/workflows/Bump.yaml)

A python Library to download publicly available data on NSE website for stocks and indices. Get the **price history**, **adjusted prices** and generate **trailing returns** of stocks and indices directly as a pandas dataframe.

For a detailed usage : <a href="https://nsedownload.github.io/NSEDownload/">Documentation</a>

## **Change Log** ##
1. Removed checking of name in stocks. `check_stockSymbol` is removed. Closest alternative suggestion is also removed. fuzzywuzzy package no longer required.
2. Code cleanup: variable nomenclature, static variables and multithreaded code in scraper
3. Change in requests: more resilient by adding backoff and retries.

## **Installation** ##

```python
git clone -b '4.0' https://github.com/NSEDownload/NSEDownload
pip3 install NSEDownload/dist/*
```

## **Usage** ##

```python
from NSEDownload import stocks

# Gets data without adjustment for events
df = stocks.get_data(symbol='RELIANCE', start_date='15-9-2021', end_date='1-10-2021')

# Adjusts the given stock data for events
df = stocks.get_adjusted_data('RELIANCE', df)

# Do above step in one line to get adjusted data
df = stocks.get_adjusted_stock(symbol='RELIANCE', start_date='15-9-2021', end_date='1-10-2021')
```

Output as a pandas dataframe :

| Date       | Symbol   | Series | Prev Close | Open Price | High Price | Low Price | Last Price | Close Price | Average Price | Total Traded Quantity |    Turnover | No. of Trades | Deliverable Qty | % Dly Qt to Traded Qty |
|:-----------|:---------|:-------|-----------:|-----------:|-----------:|----------:|-----------:|------------:|--------------:|----------------------:|------------:|--------------:|----------------:|-----------------------:|
| 2021-09-15 | RELIANCE | EQ     |    2368.45 |     2368.5 |    2395.75 |    2368.5 |     2379.4 |      2378.3 |       2380.39 |               4186300 | 9.96505e+09 |        168130 |         2310144 |                  55.18 |
| 2021-09-16 | RELIANCE | EQ     |     2378.3 |    2381.55 |    2436.75 |      2367 |       2424 |      2428.2 |       2408.55 |               6206657 | 1.49491e+10 |        214010 |         2473588 |                  39.85 |
| 2021-09-17 | RELIANCE | EQ     |     2428.2 |       2446 |    2455.85 |    2375.6 |       2387 |     2390.55 |       2410.13 |              16098099 | 3.87986e+10 |        278098 |         9460717 |                  58.77 |
| 2021-09-20 | RELIANCE | EQ     |    2390.55 |     2372.1 |    2418.35 |      2370 |    2391.85 |     2394.35 |       2398.57 |               5436385 | 1.30396e+10 |        171011 |         3042705 |                  55.97 |
| 2021-09-21 | RELIANCE | EQ     |    2394.35 |       2405 |     2416.6 |      2384 |       2400 |      2404.7 |       2401.93 |               4576111 | 1.09915e+10 |        149803 |         2365643 |                   51.7 |
| 2021-09-22 | RELIANCE | EQ     |     2404.7 |       2408 |       2442 |   2398.25 |     2430.8 |      2430.5 |       2426.47 |               5074612 | 1.23134e+10 |        179090 |         2811116 |                   55.4 |

```python
from NSEDownload import indices

# Getting historical data for index using date range
df = indices.get_data(index_name="NIFTY  50", start_date="09-01-2017", end_date="14-08-2019")

# Getting TRI data for index using date range
df = indices.get_data(index_name="NIFTY  50", start_date="09-01-2017", end_date="14-08-2019", indextype='TRI')
```

Output

| Date        |     Open |     High |      Low |    Close |   Shares Traded |   Turnover (Rs. Cr) |
|:------------|---------:|---------:|---------:|---------:|----------------:|--------------------:|
| 2017-01-09  |  8259.35 |  8263    |  8227.75 |  8236.05 |       102211190 |             5197.62 |
| 2017-01-10  |   8262.7 |  8293.8  |  8261    |  8288.6  |       147312927 |             6904.57 |
| 2017-01-11  |  8327.8  |  8389    |  8322.25 |  8380.65 |       192285417 |             8938.68 |
| 2017-01-12  |  8391.05 |  8417.2  |  8382.3  |  8407.2  |       177948383 |             7359.24 |
| 2017-01-13  |  8457.65 |  8461.05 |  8373.15 |  8400.35 |       190949616 |             9156.16 |
| 2017-01-16  |  8390.95 |  8426.7  |  8374.4  |  8412.8  |       127938836 |             6043.67 |
| 2017-01-17  |  8415.05 |  8440.9  |  8378.3  |  8398    |       125781216 |             6389.21 |
| 2017-01-18  |  8403.85 |  8460.3  |  8397.4  |  8417    |       168867039 |             7411.23 |
| 2017-01-19  |  8418.4  |  8445.15 |  8404.05 |  8435.1  |       170956149 |             7324.14 |

## **Contributing** ##
If you find any bugs or issue, please raise an issue for the same. You can also contribute by suggesting new features.

## **Buy me a coffee** ##
If my work has helped you in any way, you can buy me a coffee.  
<br>
<a href="https://www.buymeacoffee.com/jinit" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
