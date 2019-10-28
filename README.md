Python Library to get publicly available data on NSE website ie. stock quotes, historical data, live indices.

# Libraries Required #

    * requests 
    * beautifulsoup
    * numpy
    * scipy
    * pandas
    * csv
    * datetime, timedelta 
    * time
    * os


# Installation #

$pip install -i https://test.pypi.org/simple/ NSEDownload==0.1.2

# Usage #

Get the price history of stocks and NSE indices directly in pandas dataframe

```
from getDataFromNSE import getDataFromNSE

// Data For Stocks
df = a.returnsForStocks(stockSymbol="RELIANCE",full_data="Yes")

               Symbol Series  ...  % Dly Qt to Traded Qty   
Date                          ...                           
17-Sep-2019  RELIANCE     EQ  ...                   44.61   
16-Aug-2019  RELIANCE     EQ  ...                   53.58   
14-Aug-2019  RELIANCE     EQ  ...                   36.86   
13-Aug-2019  RELIANCE     EQ  ...                   37.01   
09-Aug-2019  RELIANCE     EQ  ...                   39.58   
...               ...    ...  ...                     ... ..
05-Jan-1996  RELIANCE     EQ  ...                       -   
04-Jan-1996  RELIANCE     EQ  ...                       -   
03-Jan-1996  RELIANCE     EQ  ...                       -   
02-Jan-1996  RELIANCE     EQ  ...                       -   
01-Jan-1996  RELIANCE     EQ  ...                       -   



df = a.returnsForStocks(stockSymbol = "AMBUJACEM",start_date="09-08-2018",end_date="14-08-2019")


                Symbol Series  ...  % Dly Qt to Traded Qty   
Date                           ...                           
14-Aug-2019  AMBUJACEM     EQ  ...                   56.73   
13-Aug-2019  AMBUJACEM     EQ  ...                   72.61   
09-Aug-2019  AMBUJACEM     EQ  ...                   53.36   
08-Aug-2019  AMBUJACEM     EQ  ...                   46.25   
07-Aug-2019  AMBUJACEM     EQ  ...                   59.19     
...                ...    ...  ...                     ... ..
14-Aug-2018  AMBUJACEM     EQ  ...                   39.63   
13-Aug-2018  AMBUJACEM     EQ  ...                   35.40   
10-Aug-2018  AMBUJACEM     EQ  ...                   33.45   
09-Aug-2018  AMBUJACEM     EQ  ...                   26.36   


// Calculating Returns for Historical Index
// This calculates trailing returns from 1 day to upto 2 Years. It stores the output in an Excel File.
a.calculateReturnsForStocks(df,link)


// For Data of an Index from a particular start date to particular end date 
a = getDataFromNSE.data()
df= a.returns(indexName = "NIFTY Shariah 25",start_date="09-01-2017",end_date="14-08-2019")
a.returnsToCSV(df,link)

            Open High Low    Close Shares Traded Turnover (Rs. Cr)   
Date                                                                 
14-Aug-2019    -    -   -  3953.48      66282291           3432.26   
13-Aug-2019    -    -   -  3914.89     102320106           3963.02   
09-Aug-2019    -    -   -  3980.84     101887620           4350.84   
08-Aug-2019    -    -   -  3947.93      78407607           3800.53   
07-Aug-2019    -    -   -  3911.75      77638150           4232.25   
 ...          ...  ...  ..      ...           ...               ... ..
11-Jan-2017    -    -   -  3327.22             -                 -   
10-Jan-2017    -    -   -  3295.08             -                 -   
09-Jan-2017    -    -   -  3281.54             -                 - 


// For Complete Data for Index 
df = a.returns(indexName = "NIFTY 50",full_data="Yes")

Date                                       ...                                    
17-Sep-2019  11000.10  11000.10  10796.50  ...      482013044           17721.9   
16-Sep-2019  10994.85  11052.70  10968.20  ...      434449776           15786.2   
13-Sep-2019  10986.80  11084.45  10945.75  ...      624305151           18012.8   
12-Sep-2019  11058.30  11081.75  10964.95  ...      551436050           17510.2   
11-Sep-2019  11028.50  11054.80  11011.65  ...      687140326           19550.6   
09-Sep-2019  10936.70  11028.85  10889.80  ...      412471067           14762.1   
...               ...       ...       ...  ...            ...               ... ..

12-Jul-1990      0.00      0.00      0.00  ...              -                 -   
11-Jul-1990      0.00      0.00      0.00  ...              -                 -   
10-Jul-1990      0.00      0.00      0.00  ...              -                 -   
09-Jul-1990      0.00      0.00      0.00  ...              -                 -   
06-Jul-1990      0.00      0.00      0.00  ...              -                 -   
05-Jul-1990      0.00      0.00      0.00  ...              -                 -   
03-Jul-1990      0.00      0.00      0.00  ...              -                 -   


// Data for Total Return index 
df = a.returns(indexName = "NIFTY 50",full_data="Yes",indexType="TRI")
df  = a.returns(indexName = "NIFTY AUTO",start_date="09-08-2010",end_date="14-08-2019",indexType="TRI")

// Calculating Returns for Historical Index
// This calculates trailing returns from 1 day to upto 2 Years. It stores the output in an Excel File
a.calculateReturns(df,link)


```# NSEDownload
