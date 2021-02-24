import pandas as pd
import datetime, timedelta
import time
import requests
from bs4 import BeautifulSoup 
import os

from NSEDownload.static_data import values, arr, valuesTRI, arrTRI, headers, stocks_values
from NSEDownload.check import check_name
from NSEDownload.scraper import scrape_givendate, scrape_fulldata, scrape_bonus_splits


def get_data(stockSymbol, full_data = None, start_date = None, end_date = None):

	check_name(stocks_values, stocks_values, stockSymbol)

	first = 'https://www1.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp'
	urlpost = "https://www1.nseindia.com/marketinfo/sym_map/symbolCount.jsp?symbol="
	data = {"symbol":stockSymbol}

	try:
		response = requests.post(urlpost, data = data, headers = headers, timeout = 20)
	except requests.exceptions.RequestException as e: 
		raise SystemExit(e)

	page_content = BeautifulSoup(response.content, "html.parser")
	symbolCount = (str(page_content))

	if(full_data == None or full_data=="No"):

		x=datetime.datetime.strptime(start_date,"%d-%m-%Y")
		y=datetime.datetime.strptime(end_date,"%d-%m-%Y")

		if(x>y):
			raise ValueError("Starting date is greater than end date.")

		result = scrape_givendate(x, y, None, first, 1, stockSymbol, symbolCount)
	
	elif(full_data == "Yes" or full_data == "yes" or full_data == True or full_data == "Y"):
			result = scrape_fulldata(None, first, 1, stockSymbol, symbolCount)

	try:
		os.remove("data.csv")
	except(OSError):
		pass

	return result


def adjusted_price(stockSymbol, df):

	events = ['SPLIT', 'BONUS']
	arr = ['Open Price', 'High Price', 'Low Price' , 'Last Price', 'Close Price', 'Average Price']


	if(df.empty):
		print("Please check data. Dataframe is empty")
		return df

	for event in events:
		
		ratio, dates = scrape_bonus_splits(stockSymbol, event)
		for i in range(len(dates)):

			date = datetime.datetime.strptime(dates[i],'%d-%b-%Y')
			print(event," on : ", dates[i], " and ratio is : ", ratio[i])

			changed_data = df.loc[df.index < date]
			same_data    = df.loc[df.index >= date]

			for j in arr:
			  changed_data.loc[:, j] = changed_data.loc[:, j]/ratio[i]

			df = pd.concat([same_data, changed_data])

	return df