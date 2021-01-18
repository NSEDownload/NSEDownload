Python Library to download publicly available data on NSE website for stocks and indices. Get the price history of stocks and NSE indices directly in pandas dataframe

# Libraries Required #

    * requests 
    * beautifulsoup
    * numpy
    * pandas
    * csv
    * datetime, timedelta 
    * time
    * os
    * fuzzywuzzy


# Installation #

```
git clone https://github.com/NSEDownload/NSEDownload
cd NSEDownload
pip3 install ./dist/NSEDownload-3.0.0.tar.gz 
```

# Usage #

## Stocks ##

1. To get historic data of stocks you'll have to provide the stock symbol, starting and ending data. You can also use parameter full_data = "Yes" to get complete data since its listing on the NSE.

```
from NSEDownload import stocks
df = stocks.get_data(stockSymbol="RELIANCE", start_date = '31-12-2018', end_date = '2-2-2021')
```

Output : 

```
RELIANCE
Downloading  [---] 100.00 % 
               Symbol Series  Prev Close  Open Price  ...  No. of Trades  Deliverable Qty  % Dly Qt to Traded Qty   
Date                                                  ...                                                           
18-Jan-2021  RELIANCE     EQ     1937.45     1949.10  ...         399642          6014603                   37.13   
15-Jan-2021  RELIANCE     EQ     1960.60     1960.60  ...         264152          3947767                   41.54   
14-Jan-2021  RELIANCE     EQ     1938.80     1945.00  ...         287671          5225648                   52.54   
13-Jan-2021  RELIANCE     EQ     1957.05     1963.55  ...         304901          4368602                   35.56   
12-Jan-2021  RELIANCE     EQ     1897.25     1903.00  ...         417387          8987850                   47.31   
...               ...    ...         ...         ...  ...            ...              ...                     ... ..
04-Jan-2019  RELIANCE     EQ     1092.75     1097.40  ...         189220          3496807                   41.31   
03-Jan-2019  RELIANCE     EQ     1106.40     1107.50  ...         231404          2883339                   38.72   
02-Jan-2019  RELIANCE     EQ     1121.00     1114.50  ...         147850          2543832                   35.60   
01-Jan-2019  RELIANCE     EQ     1121.25     1125.25  ...          76742          1306898                   29.33   
31-Dec-2018  RELIANCE     EQ     1125.55     1130.95  ...         155746          2448969                   33.91   

[510 rows x 15 columns]
```

2. To get a excel file of trailing returns at regular intervals from 1 day to 2 year.

```
from NSEDownload import returns
returns.calcualte_returns(df, "RELIANCE")

```

Output : 

```
Calculating returns for RELIANCE
File created : RELIANCE.xls

Date    Close   Symbol  1 Day Returns   1 Week Returns  2 Week Returns  1 Month Returns 2 Month Returns 3 Month Returns 6 Month Returns 9 Month Returns 1 Year Returns  2 Year Returns
2021-01-18  1983.95 RELIANCE    0.024   0.0457  -0.0035 -0.0038 -0.0016 -0.0883 0.0334  0.5951  0.2549  0.6751
2021-01-15  1937.45 RELIANCE    -0.0118 0.0019  -0.0252 -0.0198 -0.0324 -0.1095 0.0135  0.5829  0.2598  0.7057
2021-01-14  1960.6  RELIANCE    0.0112  0.0259  -0.0124 -0.007  -0.0208 -0.1114 0.0636  0.6785  0.2866  0.7356
2021-01-13  1938.8  RELIANCE    -0.0093 0.0128  -0.0284 -0.0264 -0.0289 -0.1524 0.0514  0.6861  0.2677  0.7677
2021-01-12  1957.05 RELIANCE    0.0315  -0.0046 -0.0166 -0.0243 -0.0116 -0.1419 0.0209  0.6458  0.2678  0.7823
2021-01-11  1897.25 RELIANCE    -0.0188 -0.047  -0.0529 -0.0541 -0.05   -0.1519 -0.0195 0.5955  0.2259  0.7278
2021-01-08  1933.7  RELIANCE    0.0118  -0.0271 -0.0303 -0.046  -0.047  -0.1342 0.0296  0.5851  0.2492  0.7409
2021-01-07  1911.15 RELIANCE    -0.0016 -0.0373 -0.0416 -0.0414 -0.0582 -0.1465 0.0476  0.5666  0.263   0.7301
2021-01-06  1914.25 RELIANCE    -0.0264 -0.0407 -0.0152 -0.0224 -0.0566 -0.152  0.0647  0.6057  0.2556  0.7327
2021-01-05  1966.1  RELIANCE    -0.0124 -0.012  0.0152  0.0099  0.0057  -0.1105 0.0782  0.6301  0.3094  0.7896
2021-01-04  1990.85 RELIANCE    0.0017  -0.0062 0.0264  0.0227  0.0406  -0.1001 0.0751  0.8477  0.2952  0.8121
2021-01-01  1987.5  RELIANCE    0.0011  -0.0033 -0.002  0.015   -0.0326 -0.1068 0.1116  0.8446  0.2945  0.7964
2020-12-31  1985.3  RELIANCE    -0.0051 -0.0044 -0.0002 0.0156  -0.0337 -0.1078 0.1278  0.8375  0.3151  0.771
2020-12-30  1995.5  RELIANCE    0.0027  0.0266  0.0096  0.034   -0.0287 -0.1069 0.1484  0.8469  0.318   0.7797

```

## Indices ##

1. To get historic data of indices you'll have to provide the index name, starting and ending data. You can also use parameter full_data = "Yes" to get complete data since its listing on the NSE.

```
from NSEDownload import indices
df = indices.get_data(indexName = "NIFTY Shariah 25",start_date="09-01-2017",end_date="14-08-2019")
```

Output : 

```
NIFTY SHARIAH 25
Downloading  [---] 100.00 % 
            Open High Low    Close Shares Traded Turnover (Rs. Cr)   
Date                                                                 
14-Aug-2019    -    -   -  3953.48      66282291           3432.26   
13-Aug-2019    -    -   -  3914.89     102320106           3963.02   
09-Aug-2019    -    -   -  3980.84     101887620           4350.84   
08-Aug-2019    -    -   -  3947.93      78407607           3800.53   
07-Aug-2019    -    -   -  3911.75      77638150           4232.25   
...          ...  ...  ..      ...           ...               ... ..
13-Jan-2017    -    -   -  3306.55             -                 -   
12-Jan-2017    -    -   -  3323.66             -                 -   
11-Jan-2017    -    -   -  3327.22             -                 -   
10-Jan-2017    -    -   -  3295.08             -                 -   
09-Jan-2017    -    -   -  3281.54             -                 -   
```

2. To get data for TRI indices use the indextype parameter.

```
from NSEDownload import indices
df = indices.get_data(indexName = "NIFTY 50",start_date="09-01-2017",end_date="14-08-2019", indextype = "TRI")
```

Output : 

```
NIFTY 50
Downloading  [---] 100.00 % 
             Total Returns Index   
Date                               
14-Aug-2019             15438.86   
13-Aug-2019             15289.35   
09-Aug-2019             15542.72   
08-Aug-2019             15434.73   
07-Aug-2019             15184.34   
...                          ... ..
13-Jan-2017             11329.78   
12-Jan-2017             11339.04   
11-Jan-2017             11303.19   
10-Jan-2017             11179.04   
09-Jan-2017             11108.20   

[643 rows x 2 columns]
```

3. To get a excel file of trailing returns at regular intervals from 1 day to 2 year. 

```
from NSEDownload import returns
returns.calcualte_returns(df, "Nifty 50")
```

Output : 

```
Calculating returns for NIFTY 50
File created : NIFTY 50.xls

Date    Close   1 Day Returns   1 Week Returns  2 Week Returns  1 Month Returns 2 Month Returns 3 Month Returns 6 Month Returns 9 Month Returns 1 Year Returns  2 Year Returns
2021-01-18  14281.3 -0.0106 -0.014  0.0105  0.0378  0.1038  0.2028  0.2957  0.5419  0.1562  0.3094
2021-01-15  14433.7 -0.0111 0.006   0.0296  0.0549  0.1294  0.2271  0.324   0.5576  0.1682  0.3254
2021-01-14  14595.6 0.0021  0.0324  0.0439  0.0757  0.142   0.2496  0.359   0.623   0.1825  0.3407
2021-01-13  14564.85    0.0001  0.0296  0.0417  0.0743  0.145   0.2167  0.3717  0.6319  0.1782  0.3564
2021-01-12  14563.45    0.0054  0.0256  0.0453  0.0777  0.1476  0.2203  0.373   0.6193  0.1812  0.3491
2021-01-11  14484.75    0.0096  0.0249  0.0441  0.0718  0.1361  0.214   0.3408  0.6105  0.1818  0.3418
2021-01-08  14347.25    0.0148  0.0235  0.0435  0.0605  0.1699  0.2042  0.3324  0.5746  0.1745  0.3217
2021-01-07  14137.35    -0.0006 0.0111  0.0282  0.0556  0.1528  0.1946  0.3074  0.5515  0.1756  0.3088
2021-01-06  14146.25    -0.0038 0.0118  0.0401  0.0592  0.1535  0.2051  0.3214  0.6169  0.1737  0.3133
2021-01-05  14199.5 0.0047  0.0192  0.0544  0.071   0.1715  0.2175  0.3148  0.615   0.184   0.3237
2021-01-04  14132.9 0.0082  0.0187  0.0604  0.0659  0.1868  0.2286  0.313   0.7483  0.1559  0.3175
2021-01-01  14018.5 0.0026  0.0196  0.0187  0.069   0.2041  0.2279  0.3216  0.7341  0.1414  0.2989
2020-12-30  13981.95    0.0035  0.028   0.0219  0.0781  0.201   0.2431  0.3405  0.694   0.149   0.2872

```
