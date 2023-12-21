# **NSEDownload** #

[![Bump Up version](https://github.com/NSEDownload/NSEDownload/actions/workflows/Bump.yaml/badge.svg)](https://github.com/NSEDownload/NSEDownload/actions/workflows/Bump.yaml)

A Python Library to download publicly available data on the NSE website for stocks as pandas dataframe.
For a detailed usage : <a href="https://nsedownload.github.io/NSEDownload/">Documentation</a>

## **Installation** ##

```bash
git clone https://github.com/NSEDownload/NSEDownload
pip3 install NSEDownload/dist/*
```

## **Usage** ##

```python
from NSEDownload import stocks

# Gets data without adjustment for events
df = stocks.get_data(stock_symbol="RELIANCE", start_date='15-9-2021', end_date='1-10-2021')
```

Sample Output as a pandas dataframe :

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Date</th>
      <th>Symbol</th>
      <th>Series</th>
      <th>High Prices</th>
      <th>Low Prices</th>
      <th>Open Prices</th>
      <th>Close Prices</th>
      <th>Last Prices</th>
      <th>Prec Close Price</th>
      <th>Total Traded Quantity</th>
      <th>Total Traded Value</th>
      <th>52 Week High Price</th>
      <th>52 Week Low Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-08-11T18:30:00.000Z</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2675.25</td>
      <td>2646.6</td>
      <td>2656.6</td>
      <td>2668.75</td>
      <td>2666.0</td>
      <td>2658.5</td>
      <td>1702479</td>
      <td>4532596291.9</td>
      <td>2896</td>
      <td>1623</td>
    </tr>
    <tr>
      <th>2021-08-12T18:30:00.000Z</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2715.0</td>
      <td>2662.0</td>
      <td>2662.0</td>
      <td>2704.15</td>
      <td>2702.1</td>
      <td>2668.75</td>
      <td>3248615</td>
      <td>8774705017.55</td>
      <td>2896</td>
      <td>1623</td>
    </tr>
    <tr>
      <th>2021-08-15T18:30:00.000Z</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2734.45</td>
      <td>2693.8</td>
      <td>2696.8</td>
      <td>2731.15</td>
      <td>2732.7</td>
      <td>2704.15</td>
      <td>2465887</td>
      <td>6709996706.95</td>
      <td>2896</td>
      <td>1623</td>
    </tr>
    <tr>
      <th>2021-08-16T18:30:00.000Z</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2750.0</td>
      <td>2707.15</td>
      <td>2729.95</td>
      <td>2738.4</td>
      <td>2745.6</td>
      <td>2731.15</td>
      <td>2795510</td>
      <td>7620988084.3</td>
      <td>2896</td>
      <td>1623</td>
    </tr>
    <tr>
      <th>2021-08-17T18:30:00.000Z</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2770.3</td>
      <td>2698.0</td>
      <td>2750.0</td>
      <td>2710.75</td>
      <td>2710.0</td>
      <td>2738.4</td>
      <td>2501410</td>
      <td>6828940469.75</td>
      <td>2896</td>
      <td>1623</td>
    </tr>
  </tbody>
</table>

## **Tips & Tricks** ##
1. You might run into access issues due to requests per second exceeding the permissible threshold. Add a delay of 5-10 seconds between multiple symbols to resolve the issue. ([Discussion](https://github.com/NSEDownload/NSEDownload/issues#issuecomment-1699721241))

## **Change Log** ##

1. Removed indices, returns, and adjusted stocks.
2. Made changes to use the new NSE site and cookies.

## **Contributing** ##

Your feedback matters! If you come across any bugs or issues, don't hesitate to raise them. Feel free to share your ideas for exciting new features

## **Buy me a coffee** ##

If you've found my work helpful and appreciate the effort, consider supporting me with a coffee! Your contribution goes a long way!
<br>
<a href="https://www.buymeacoffee.com/jinit" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
