import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup 
import bs4
import csv
import datetime, timedelta
import time
import os
from fuzzywuzzy import fuzz

class data:

	# def __init__(indexName,full_data=None,start_date=None,end_date=None,indextype=None):
	# 	self.indexName = indexName
	# 	self.full_data = full_data
	# 	self.start_date = start_date
	# 	self.end_date = end_date
	# 	self.indextype = in


	def returns(self,indexName,full_data=None,start_date=None,end_date=None,indextype=None):
		self.indexName = indexName
		self.indextype = indextype

		##Setting by default to be historical	

		result=[];
		if(full_data ==None or full_data=="No"):
			x=datetime.datetime.strptime(start_date,"%d-%m-%Y")
			y=datetime.datetime.strptime(end_date,"%d-%m-%Y")

			if(x>y):
				raise ValueError("Starting date is greater than end date.")

			# Checking for proper IndexName and suggesting closest alternative.
			flag=0;
			for i in range(len(arr)):
				if(arr[i]==indexName or values[i]==indexName):
					indexName = arr[i]
					print(indexName)
					flag=1

			maxi = 0
			maxVal = values[0];
			for compare in values:
				str1 = indexName
				str2 = compare

				Ratio = fuzz.ratio(str1.lower(),str2.lower())
				if(Ratio>maxi):
					maxVal = compare
					maxi = Ratio


			indexName = indexName.replace(" ","%20")
			# print("HAAA")
			#Downloading Data
			result = pd.DataFrame()
			while(True):
					if((y-x).days<365):
						try:
							# print(1)
							fromdate= x.strftime("%d-%m-%Y")
							# print(fromdate)
							todate=y.strftime("%d-%m-%Y")
							url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;			
							headers = {
								"Host": "www1.nseindia.com",
								"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
								"Accept": "*/*",
								"Accept-Language": "en-US,en;q=0.5",
								"Accept-Encoding": "gzip, deflate, br",
								"X-Requested-With": "XMLHttpRequest",
								"Referer": "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm",
								"Access-Control-Allow-Origin" : "*",
								"Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
								"Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
								'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
							}
							response = requests.get(url, timeout=240,headers=headers)
							page_content = BeautifulSoup(response.content, "html.parser")

							a=page_content.find(id="csvContentDiv").get_text();
							a = a.replace(':',", \n")


							with open("data.csv", "w") as f:
								f.write(a)

							df = pd.read_csv("data.csv")
							df.set_index("Date",inplace=True)
							df = df[::-1]
							result = pd.concat([result,df])
							break;

						except AttributeError:
							break

					if ((y-x).days > 365 ):
						try:
							# print(0)
							todate= y.strftime("%d-%m-%Y")
							fromdate = ( y - datetime.timedelta(days=364) ).strftime("%d-%m-%Y")
							inter =  y - datetime.timedelta(days=364) 
							# print(todate)
							url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;			
							headers = {
								"Host": "www1.nseindia.com",
								"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
								"Accept": "*/*",
								"Accept-Language": "en-US,en;q=0.5",
								"Accept-Encoding": "gzip, deflate, br",
								"X-Requested-With": "XMLHttpRequest",
								"Referer": "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm",
								"Access-Control-Allow-Origin" : "*",
								"Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
								"Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
								'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
							}

							response = requests.get(url, timeout=10,headers=headers)
							page_content = BeautifulSoup(response.content, "html.parser")

							a=page_content.find(id="csvContentDiv").get_text();
							a = a.replace(':',", \n")
							# print(a)


							with open("data.csv", "w") as f:
								f.write(a)

							df = pd.read_csv("data.csv")
							df.set_index("Date",inplace=True)
							df = df[::-1]
							result = pd.concat([result,df])
							y = ( inter - datetime.timedelta(days=1) )

						except AttributeError:
							break;

			
		elif(full_data =="Yes" or full_data=="yes"):
			
				# Checking for proper IndexName and suggesting closest alternative.
				flag=0;
				for i in range(len(arr)):
					if(arr[i]==indexName or values[i]==indexName):
						indexName = arr[i]
						print(indexName)
						flag=1

				maxi = 0
				maxVal = values[0];
				for compare in values:
					str1 = indexName
					str2 = compare

					Ratio = fuzz.ratio(str1.lower(),str2.lower())
					if(Ratio>maxi):
						maxVal = compare
						maxi = Ratio

				if(flag==0):
					raise ValueError("Check Index name. Try {} as index name".format(maxVal))

				x=datetime.datetime.now()
				y=datetime.datetime.now() - datetime.timedelta(days=364)

				result = pd.DataFrame()
				i=0;
				while(True):
					try:
						print("Stage ",i)
						todate=x.strftime("%d-%m-%Y")
						fromdate= y.strftime("%d-%m-%Y")

						url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;			
						headers = {
								"Host": "www1.nseindia.com",
								"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
								"Accept": "*/*",
								"Accept-Language": "en-US,en;q=0.5",
								"Accept-Encoding": "gzip, deflate, br",
								"X-Requested-With": "XMLHttpRequest",
								"Referer": "https://www1.nseindia.com/products/content/equities/equities/eq_security.htm",
								"Access-Control-Allow-Origin" : "*",
								"Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
								"Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
								'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
						}
						response = requests.get(url, timeout=10,headers=headers)
						page_content = BeautifulSoup(response.content, "html.parser")

						a=page_content.find(id="csvContentDiv").get_text();
						a = a.replace(':',", \n")

						with open("data.csv", "w") as f:
							f.write(a)

						df = pd.read_csv("data.csv")
						df.set_index("Date",inplace=True)
						df = df[::-1]
						result = pd.concat([result,df])

						x = y - datetime.timedelta(days=1)
						y = x - datetime.timedelta(days=364)
						i=i+1
					except AttributeError:
						# print("YES")
						break;
		try:
			os.remove("data.csv")
		except(OSError):
			pass


		return result;

	def returnsToCSV(self,data,link=None):
		try:
			if(link==None):
				data.to_csv(self.indexName+".csv")
				print("Data stored as csv in the name {}.csv".format(self.indexName))
			else:
				data.to_csv(link+"/{}.csv".format(self.indexName))
				print("Data stored as csv in the name {}.csv".format(self.indexName))

		except (AttributeError):
			print("Check data")


	def returnsToCSVStocks(self,data,link=None):
		if(link==None):
			data.to_csv(self.stockSymbol+".csv")
			print("Data stored as csv in the name {}.csv".format(self.stockSymbol))

		else:
			data.to_csv(link+"/{}.csv".format(self.stockSymbol))
			print("Data stored as csv in the name {}.csv".format(self.stockSymbol))


