If you're looking for stable code, head over to the main branch. <br><br>
I'm testing a new feature in this one - **Adjusted stock prices** <br>
DISCLAIMER - This only works for data after 2010.

# Improvements #

So I'm scraping company events for bonuses and splits then find out date and ratio required. Then divide the prices before the record date with the ratio I found. <br>
This is slightly tricky. The company statements are in text and I need to figure out numbers from there and all of them aren't uniform. <br>

## Bug ##
More importantly, there's a bug that randomly causes the new dataframe to miss dates in between. If you can fix this, please make a pull request.

## Testing ##
I tried the stocks in Nifty 50 and the bug appeared a few times. But when I rerun the code, it seems to work fine. 


# Installation #

```
!git clone -b '3.1' https://github.com/NSEDownload/NSEDownload
!pip3 install NSEDownload/dist/NSEDownload-3.1.1.tar.gz 
```

# Usage #

This specific use case only for stocks. (If you're looking for other, go to the main branch)

To get historic data of stocks you'll have to provide the stock symbol, starting and ending data. You can also use parameter full_data = "Yes" to get complete data since its listing on the NSE.

```
from NSEDownload import stocks
df = stocks.get_data(stockSymbol="INFY", start_date = '1-1-2010', end_date = '2-2-2021')
df = stocks.get_adjusted_data("INFY", df)
```

To check you can plot the closing prices and if there is a vertical line somewhere, then the data is incorrect.

```
import matplotlib.pyplot as plt
df['Close Price'].plot()
plt.show()
```
