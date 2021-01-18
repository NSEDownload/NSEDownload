import pandas as pd
import datetime, timedelta
import requests
from bs4 import BeautifulSoup 
import os
import math

from NSEDownload.progress_bar import init_bar, print_bar, end_bar
from NSEDownload.static_data import values, arr, valuesTRI, arrTRI, headers

def scrape_givendate(x, y, indexName, first, types = 0, stockSymbol = None, symbolCount = None):

	result = pd.DataFrame()
	stage = 0
	total_stages = math.ceil((y-x).days/365)

	init_bar(total_stages)

	while(True):
		if((y-x).days < 365):
			try:

				fromdate = x.strftime("%d-%m-%Y")
				todate   = y.strftime("%d-%m-%Y")

				if(types==1):
					url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
				else:
					url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;

				try:
					response = requests.get(url, timeout = 20, headers = headers)
				except requests.exceptions.RequestException as e: 
					SystemExit(e)

				page_content = BeautifulSoup(response.content, "html.parser")

				a = page_content.find(id="csvContentDiv").get_text();
				a = a.replace(':',", \n")

				with open("data.csv", "w") as f:
					f.write(a)

				df = pd.read_csv("data.csv")
				df.set_index("Date",inplace=True)
				df = df[::-1]
				result = pd.concat([result,df])

				print_bar(stage, total_stages)
				stage = stage+1

				break;

			except AttributeError:
				break

		if ((y-x).days >= 365 ):
			try:

				todate= y.strftime("%d-%m-%Y")
				fromdate = ( y - datetime.timedelta(days=364) ).strftime("%d-%m-%Y")
				inter =  y - datetime.timedelta(days=364) 

				if(types==1):
					url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
				else:
					url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;

				try:
					response = requests.get(url, timeout = 20,headers = headers)
				except requests.exceptions.RequestException as e: 
					SystemExit(e)

				page_content = BeautifulSoup(response.content, "html.parser")

				a = page_content.find(id="csvContentDiv").get_text();
				a = a.replace(':',", \n")

				with open("data.csv", "w") as f:
					f.write(a)

				df = pd.read_csv("data.csv")
				df.set_index("Date",inplace=True)
				df = df[::-1]
				result = pd.concat([result,df])
				y = ( inter - datetime.timedelta(days=1) )

				print_bar(stage, total_stages)
				stage = stage+1

			except AttributeError:
				break;

	try:
		os.remove("data.csv")
	except(OSError):
		pass

	end_bar(total_stages)

	return result


def scrape_fulldata( indexName, first , types = 0, stockSymbol = None, symbolCount = None):

	result = pd.DataFrame()
	x = datetime.datetime.now()
	y = datetime.datetime.now() - datetime.timedelta(days=364)
	total_stages = math.ceil((y-x).days/365)

	total_stages = 30
	stage = 0
	init_bar(total_stages)

	while(True):
		try:

			todate   = x.strftime("%d-%m-%Y")
			fromdate = y.strftime("%d-%m-%Y")

			if(types==1):
				url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
			else:
				url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;

			try:
				response = requests.get(url, timeout = 20, headers = headers)
			except requests.exceptions.RequestException as e: 
				raise SystemExit(e)

			page_content = BeautifulSoup(response.content, "html.parser")

			a=page_content.find(id = "csvContentDiv").get_text();
			a = a.replace(':',", \n")

			with open("data.csv", "w") as f:
				f.write(a)

			df = pd.read_csv("data.csv")
			df.set_index("Date",inplace=True)
			df = df[::-1]
			result = pd.concat([result,df])

			x = y - datetime.timedelta(days=1)
			y = x - datetime.timedelta(days=364)

			print_bar(stage, total_stages)
			stage = stage+1
			
		except AttributeError:
			break;

	try:
		os.remove("data.csv")
	except(OSError):
		pass

	end_bar(total_stages)

	return result

