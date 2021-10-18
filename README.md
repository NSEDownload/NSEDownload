# **NSEDownload** #

A python Library to download publicly available data on NSE website for stocks and indices. Get the **price history**, **adjusted prices** and generate **trailing returns** of stocks and indices directly as a pandas dataframe.

For a detailed usage : <a href="https://nsedownload.github.io/NSEDownload/">Documentation</a>

## **Installation** ##

```python
git clone -b '3.1' https://github.com/NSEDownload/NSEDownload
pip3 install NSEDownload/dist/NSEDownload-3.1.6.1.tar.gz 
```

## **Usage** ##

```python
from NSEDownload import stocks
df = stocks.get_data(stockSymbol = 'RELIANCE', start_date = '15-9-2021', end_date = '1-10-2021')
```
Output as a pandas dataframe :

| Date                | Symbol   | Series   |   Prev Close |   Open Price |   High Price |   Low Price |   Last Price |   Close Price |   Average Price |   Total Traded Quantity |    Turnover |   No. of Trades |   Deliverable Qty |   % Dly Qt to Traded Qty |     |
|:--------------------|:---------|:---------|-------------:|-------------:|-------------:|------------:|-------------:|--------------:|----------------:|------------------------:|------------:|----------------:|------------------:|-------------------------:|:----|
| 2021-09-15 | RELIANCE | EQ       |      2368.45 |      2368.5  |      2395.75 |     2368.5  |      2379.4  |       2378.3  |         2380.39 |                 4186300 | 9.96505e+09 |          168130 |           2310144 |                    55.18 |     |
| 2021-09-16 | RELIANCE | EQ       |      2378.3  |      2381.55 |      2436.75 |     2367    |      2424    |       2428.2  |         2408.55 |                 6206657 | 1.49491e+10 |          214010 |           2473588 |                    39.85 |     |
| 2021-09-17 | RELIANCE | EQ       |      2428.2  |      2446    |      2455.85 |     2375.6  |      2387    |       2390.55 |         2410.13 |                16098099 | 3.87986e+10 |          278098 |           9460717 |                    58.77 |     |
| 2021-09-20 | RELIANCE | EQ       |      2390.55 |      2372.1  |      2418.35 |     2370    |      2391.85 |       2394.35 |         2398.57 |                 5436385 | 1.30396e+10 |          171011 |           3042705 |                    55.97 |     |
| 2021-09-21 | RELIANCE | EQ       |      2394.35 |      2405    |      2416.6  |     2384    |      2400    |       2404.7  |         2401.93 |                 4576111 | 1.09915e+10 |          149803 |           2365643 |                    51.7  |     |
| 2021-09-22 | RELIANCE | EQ       |      2404.7  |      2408    |      2442    |     2398.25 |      2430.8  |       2430.5  |         2426.47 |                 5074612 | 1.23134e+10 |          179090 |           2811116 |                    55.4  |     |

## **Contributing** ##
If you find any bugs or issue, please raise an issue for the same. You can also contribute by suggesting new features.