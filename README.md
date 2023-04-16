# **NSEDownload** #

[![Bump Up version](https://github.com/NSEDownload/NSEDownload/actions/workflows/Bump.yaml/badge.svg)](https://github.com/NSEDownload/NSEDownload/actions/workflows/Bump.yaml)

A python Library to download publicly available data on NSE website for stocks and indices. Get the **price history**, **adjusted prices** and generate **trailing returns** of stocks and indices directly as a pandas dataframe.

For a detailed usage : <a href="https://nsedownload.github.io/NSEDownload/">Documentation</a>

## **Change Log** ##
1. Removed checking of name in stocks. `check_stockSymbol` is removed. Closest alternative suggestion is also removed. fuzzywuzzy package no longer required.
2. Code cleanup: variable nomenclature, static variables and multithreaded code in scraper
3. Change in requests: more resilient by adding backoff and retries.
4. Specify Series as argument like 'ALL', 'BE' and 'EQ'. (By default set to 'EQ')

## **Installation** ##

```python
git clone -b 'jshah-fix-nse-url' https://github.com/NSEDownload/NSEDownload
pip3 install NSEDownload/dist/*
```

## **Usage** ##

```python
from NSEDownload import stocks

# Gets data without adjustment for events
df = stocks.get_data(stock_symbol="RELIANCE", start_date='15-9-2021', end_date='1-10-2021')
```

Sample Output as a pandas dataframe :
| Date                     | Symbol | Series | High Price | Low Price | Open Price | Close Price | Last Price | Prev Close Price | Total Traded Quantity | Total Traded Value | 52 Week High Price | 52 Week Low Price |
|--------------------------|--------|--------|------------|-----------|------------|-------------|------------|------------------|-----------------------|--------------------|--------------------|-------------------|
| 2021-08-11T18:30:00.000Z | HDFC   | EQ     | 2675.25    | 2646.6    | 2656.6     | 2668.75     | 2666.0     | 2658.5           | 1702479               | 4532596291.9       | 2896               | 1623              |
| 2021-08-12T18:30:00.000Z | HDFC   | EQ     | 2715.0     | 2662.0    | 2662.0     | 2704.15     | 2702.1     | 2668.75          | 3248615               | 8774705017.55      | 2896               | 1623              |
| 2021-08-15T18:30:00.000Z | HDFC   | EQ     | 2734.45    | 2693.8    | 2696.8     | 2731.15     | 2732.7     | 2704.15          | 2465887               | 6709996706.95      | 2896               | 1623              |
| 2021-08-16T18:30:00.000Z | HDFC   | EQ     | 2750.0     | 2707.15   | 2729.95    | 2738.4      | 2745.6     | 2731.15          | 2795510               | 7620988084.3       | 2896               | 1623              |
| 2021-08-17T18:30:00.000Z | HDFC   | EQ     | 2770.3     | 2698.0    | 2750.0     | 2710.75     | 2710.0     | 2738.4           | 2501410               | 6828940469.75      | 2896               | 1623              |

## **Contributing** ##
If you find any bugs or issue, please raise an issue for the same. You can also contribute by suggesting new features.

## **Buy me a coffee** ##
If my work has helped you in any way, you can buy me a coffee.  
<br>
<a href="https://www.buymeacoffee.com/jinit" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
