A python Library to download publicly available data on NSE website for stocks and indices. Get the **price history**, **adjusted prices** and generate **trailing returns** of stocks and indices directly as a pandas dataframe.

## **Installation** ##

```python
git clone -b '4.0' https://github.com/NSEDownload/NSEDownload
pip3 install NSEDownload/dist/*
```

## **Usage** ##

### Stocks ###

```python
from NSEDownload import stocks

# Gets data without adjustment for events
df = stocks.get_data(stockSymbol = 'RELIANCE', start_date = '15-9-2021', end_date = '1-10-2021')

# Adjusts the given stock data for events
df = stocks.get_adjusted_data('RELIANCE', df)

# Do above steps in one line to get adjusted data
df = stocks.get_adjusted_stock(stockSymbol = 'RELIANCE', start_date = '15-9-2021', end_date = '1-10-2021')

# Download all Series
df = stocks.get_adjusted_stock(stockSymbol = 'RELIANCE', start_date = '15-9-2021', end_date = '1-10-2021', series='ALL')
```

### Indices ###

```python
from NSEDownload import indices
# Getting historical data for index using date range
df = indices.get_data(indexName = "NIFTY  50",start_date="09-01-2017",end_date="14-08-2019")
```
## **Contributing** ##
If you find any bugs or issue, please raise an issue for the same. You can also contribute by suggesting new features.

## **Buy me a coffee** ##
If my work has helped you in anyway, you can buy me a coffee.  
<br>
<a href="https://www.buymeacoffee.com/jinit" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
