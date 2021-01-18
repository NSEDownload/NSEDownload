import pandas as pd
import datetime, timedelta, time

from NSEDownload.static_data import values, arr, valuesTRI, arrTRI
from NSEDownload.check import check_name
from NSEDownload.scraper import scrape_givendate, scrape_fulldata

def get_data(indexName, full_data = None, start_date = None, end_date = None, indextype = None):

	Array = arr
	Values = values

	if(indextype=="Historical" or indextype=="historical" or indextype=="H" or indextype=="h")	:	
		first = 'https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp'
	elif(indextype=="TRI" or indextype=="tri" or indextype=="T" or indextype=='t'):
		first  =  "https://www1.nseindia.com/products/dynaContent/equities/indices/total_returnindices.jsp"
		Values =  valuesTRI
		Array  =  arrTRI
	else:
		first = 'https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp'

	check_name(Array, Values, indexName)

	if(full_data == None or full_data=="No"):

		x = datetime.datetime.strptime(start_date,"%d-%m-%Y")
		y = datetime.datetime.strptime(end_date,"%d-%m-%Y")

		if(x>y):
			raise ValueError("Starting date is greater than end date.")
		
		result = scrape_givendate(x, y, indexName, first)

	elif(full_data =="Yes" or full_data=="yes" or full_data==True or full_data=="Y"):
		result = scrape_fulldata(indexName, first)

	return result
