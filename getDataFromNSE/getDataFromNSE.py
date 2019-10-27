import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup 
import bs4
import csv
import datetime, timedelta
import time
import os


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

		values = ["NIFTY 50", "NIFTY Next 50", "NIFTY Midcap Liquid 15", "NIFTY 100", "NIFTY 200", "NIFTY 500", "NIFTY Midcap 150", "NIFTY Midcap 50", "NIFTY Full Midcap 100", "NIFTY Midcap 100", "NIFTY Smallcap 250", "NIFTY Smallcap 50", "NIFTY Full Smallcap 100", "NIFTY Smallcap 100", "NIFTY LargeMidcap 250", "NIFTY MidSmallcap 400", "NIFTY Auto", "NIFTY Bank", "NIFTY Financial Services", "NIFTY FMCG", "NIFTY IT", "NIFTY Media", "NIFTY Metal", "NIFTY Pharma", "NIFTY Private Bank", "NIFTY PSU Bank", "NIFTY Realty", "NIFTY Commodities", "NIFTY India Consumption", "NIFTY CPSE", "NIFTY Energy", "NIFTY100 ESG", "NIFTY100 Enhanced ESG", "NIFTY Infra", "NIFTY MNC", "NIFTY PSE", "NIFTY SME EMERGE", "NIFTY Services Sector", "NIFTY Shariah 25", "NIFTY50 Shariah", "NIFTY500 Shariah", "NIFTY Aditya Birla Group", "NIFTY Mahindra Group", "NIFTY Tata Group", "NIFTY Tata Group 25% Cap", "NIFTY100 LIQ 15", "NIFTY Midcap Liquid 15", "NIFTY500 Value 50", "NIFTY Alpha Low-Volatility 30", "NIFTY Quality Low-Volatility 30", "NIFTY Alpha Quality Low-Volatility 30", "NIFTY Alpha Quality Value Low-Volatility 30", "NIFTY50 Equal Weight", "NIFTY100 Equal Weight", "NIFTY100 Low Volatility 30", "NIFTY50 USD", "NIFTY50 Dividend Points", "NIFTY Dividend Opportunities 50", "NIFTY100 Alpha 30", "NIFTY Alpha 50", "NIFTY 50 Arbitrage", "NIFTY 50 Futures Index", "NIFTY 50 Futures TR Index", "NIFTY High Beta 50", "NIFTY Low Volatility 50", "NIFTY200 Quality 30", "NIFTY100 Quality 30", "NIFTY50 Value 20", "NIFTY Growth Sectors 15", "NIFTY50 TR 2X Leverage", "NIFTY50 PR 2X Leverage", "NIFTY50 TR 1X Inverse", "NIFTY50 PR 1X Inverse", "NIFTY Composite G-sec Index", "NIFTY 4-8 yr G-Sec Index", "NIFTY 8-13 yr G-Sec", "NIFTY 10 yr Benchmark G-Sec", "NIFTY 10 yr Benchmark G-Sec (Clean Price)", "NIFTY 11-15 yr G-Sec Index", "NIFTY 15 yr and above G-Sec Index", "NIFTY 10 Year SDL Index", "NIFTY AAA Corporate Bond", "NIFTY AAA Ultra Short-Term Corporate Bond", "NIFTY AAA Short-Term Corporate Bond", "NIFTY AAA Medium-Term Corporate Bond", "NIFTY AAA Long-Term Corporate Bond", "NIFTY AAA Ultra Long-Term Corporate Bond", "Nifty 1D Rate Index"]
		arr =    ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY MID LIQ 15', 'NIFTY 100', 'NIFTY 200', 'NIFTY 500', 'NIFTY MIDCAP 150', 'NIFTY MIDCAP 50', 'NIFTY FULL MIDCAP 100', 'NIFTY MIDCAP 100', 'NIFTY SMALLCAP 250', 'NIFTY SMALLCAP 50', 'NIFTY FULL SMALLCAP 100', 'NIFTY SMLCAP 100', 'NIFTY LargeMidcap 250', 'NIFTY MIDSMALLCAP 400', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY FIN SERVICE', 'NIFTY FMCG', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PVT BANK', 'NIFTY PSU BANK', 'NIFTY REALTY', 'NIFTY COMMODITIES', 'NIFTY CONSUMPTION', 'NIFTY CPSE', 'NIFTY ENERGY', 'NIFTY100 ESG', 'NIFTY100 Enhanced ESG', 'NIFTY INFRA', 'NIFTY MNC', 'NIFTY PSE', 'NIFTY SME EMERGE', 'NIFTY SERV SECTOR', 'NIFTY SHARIAH 25', 'NIFTY50 SHARIAH', 'NIFTY500 SHARIAH', 'NIFTY ADITYA BIRLA GROUP', 'NIFTY MAHINDRA GROUP', 'NIFTY TATA GROUP', 'NIFTY TATA GROUP 25% CAP', 'NIFTY100 LIQ 15', 'NIFTY MID LIQ 15', 'NIFTY500 VALUE 50', 'NIFTY ALPHA LOW-VOLATILITY 30', 'NIFTY QUALITY LOW-VOLATILITY 30', 'NIFTY ALPHA QUALITY LOW-VOLATILITY 30', 'NIFTY ALPHA QUALITY VALUE LOW-VOLATILITY 30', 'NIFTY50 EQL WGT', 'NIFTY100 EQL WGT', 'NIFTY100 LOWVOL30', 'NIFTY50 USD', 'NIFTY50 DIV POINT', 'NIFTY DIV OPPS 50', 'NIFTY100 ALPHA 30', 'NIFTY ALPHA 50', 'NIFTY 50 ARBITRAGE', 'NIFTY 50 FUTURES INDEX', 'NIFTY 50 FUTURES TR INDEX', 'NIFTY HIGH BETA 50', 'NIFTY LOW VOLATILITY 50', 'NIFTY200 QUALITY 30', 'NIFTY100 Quality 30', 'NIFTY50 VALUE 20', 'NIFTY GROWSECT 15', 'NIFTY50 TR 2X LEV', 'NIFTY50 PR 2X LEV', 'NIFTY50 TR 1X INV', 'NIFTY50 PR 1X INV', 'NIFTY GS COMPSITE', 'NIFTY GS 4 8YR', 'NIFTY GS 8 13YR', 'NIFTY GS 10YR', 'NIFTY GS 10YR CLN', 'NIFTY GS 11 15YR', 'NIFTY GS 15YRPLUS', 'NIFTY 10 YEAR SDL INDEX', 'NIFTY AAA CORPORATE BOND', 'NIFTY AAA ULTRA SHORT-TERM CORPORATE BOND', 'NIFTY AAA SHORT-TERM CORPORATE BOND', 'NIFTY AAA MEDIUM-TERM CORPORATE BOND', 'NIFTY AAA LONG-TERM CORPORATE BOND', 'NIFTY AAA ULTRA LONG-TERM CORPORATE BOND', 'Nifty 1D Rate Index']
		valuesTRI = ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY 100', 'NIFTY 200', 'NIFTY 500', 'NIFTY MIDCAP 150', 'NIFTY MIDCAP 50', 'NIFTY FULL MIDCAP 100', 'NIFTY MIDCAP 100', 'NIFTY SMALLCAP 250', 'NIFTY SMALLCAP 50', 'NIFTY FULL SMALLCAP 100', 'NIFTY SMALLCAP 100', 'NIFTY LARGEMIDCAP 250', 'NIFTY MIDSMALLCAP 400', 'NIFTY AUTO', 'NIFTY BANK', 'NIFTY FINANCIAL SERVICES', 'NIFTY FMCG', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PRIVATE BANK', 'NIFTY PSU BANK', 'NIFTY REALTY', 'NIFTY COMMODITIES', 'NIFTY CPSE', 'NIFTY ENERGY', 'NIFTY100 ESG', 'NIFTY100 ENHANCED ESG', 'NIFTY INDIA CONSUMPTION', 'NIFTY INFRASTRUCTURE', 'NIFTY MIDCAP LIQUID 15', 'NIFTY MNC', 'NIFTY PSE', 'NIFTY SME EMERGE', 'NIFTY SERVICES SECTOR', 'NIFTY SHARIAH 25', 'NIFTY100 LIQUID 15', 'NIFTY50 SHARIAH', 'NIFTY500 SHARIAH', 'NIFTY ADITYA BIRLA GROUP', 'NIFTY MAHINDRA GROUP', 'NIFTY TATA GROUP', 'NIFTY TATA GROUP 25% CAP', 'NIFTY500 VALUE 50', 'NIFTY ALPHA LOW-VOLATILITY 30', 'NIFTY QUALITY LOW-VOLATILITY 30', 'NIFTY ALPHA QUALITY LOW-VOLATILITY 30', 'NIFTY ALPHA QUALITY VALUE LOW-VOLATILITY 30', 'NIFTY50 EQUAL WEIGHT', 'NIFTY100 EQUAL WEIGHT', 'NIFTY100 LOW VOLATILITY 30', 'NIFTY DIVIDEND OPPORTUNITIES 50', 'NIFTY100 ALPHA 30', 'NIFTY ALPHA 50', 'NIFTY HIGH BETA 50', 'NIFTY LOW VOLATILITY 50', 'NIFTY200 QUALITY 30', 'NIFTY100 QUALITY 30', 'NIFTY50 VALUE 20', 'NIFTY GROWTH SECTORS 15']
		arrTRI = ['NIFTY 50', 'NIFTY Next 50', 'NIFTY 100', 'NIFTY 200', 'NIFTY 500', 'NIFTY Midcap 150', 'NIFTY Midcap 50', 'NIFTY Full Midcap 100', 'NIFTY Midcap 100', 'NIFTY Smallcap 250', 'NIFTY Smallcap 50', 'NIFTY Full Smallcap 100', 'NIFTY Smallcap 100', 'NIFTY LargeMidcap 250', 'NIFTY MidSmallcap 400','NIFTY Auto', 'NIFTY Bank', 'NIFTY Financial Services', 'NIFTY FMCG', 'NIFTY IT', 'NIFTY Media', 'NIFTY Metal', 'NIFTY Pharma', 'NIFTY Private Bank', 'NIFTY PSU Bank', 'NIFTY Realty','NIFTY Commodities', 'NIFTY CPSE', 'NIFTY Energy', 'NIFTY100 ESG', 'NIFTY100 Enhanced ESG', 'NIFTY India Consumption', 'NIFTY Infrastructure', 'NIFTY Midcap Liquid 15', 'NIFTY MNC', 'NIFTY PSE', 'NIFTY SME EMERGE', 'NIFTY Services Sector', 'NIFTY Shariah 25', 'NIFTY100 Liquid 15', 'NIFTY50 Shariah', 'NIFTY500 Shariah', 'NIFTY Aditya Birla Group', 'NIFTY Mahindra Group', 'NIFTY Tata Group', 'NIFTY Tata Group 25% Cap','NIFTY500 Value 50', 'NIFTY Alpha Low-Volatility 30', 'NIFTY Quality Low-Volatility 30', 'NIFTY Alpha Quality Low-Volatility 30', 'NIFTY Alpha Quality Value Low-Volatility 30', 'NIFTY50 Equal Weight', 'NIFTY100 Equal Weight','NIFTY100 Low Volatility 30', 'NIFTY Dividend Opportunities 50','NIFTY100 Alpha 30','NIFTY Alpha 50', 'NIFTY High Beta 50', 'NIFTY Low Volatility 50', 'NIFTY200 Quality 30', 'NIFTY100 Quality 30', 'NIFTY50 Value 20', 'NIFTY Growth Sectors 15']
	
		if(indextype=="Historical" or indextype=="historical")	:	
			first = 'https://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp'
		elif(indextype=="TRI" or indextype=="tri"):
			first =  "https://www.nseindia.com/products/dynaContent/equities/indices/total_returnindices.jsp"
			values=valuesTRI
			arr = arrTRI
		else:
			first = 'https://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp'

		##Setting by default to be historical	

		result=[];
		if(full_data ==None or full_data=="No"):
			x=datetime.datetime.strptime(start_date,"%d-%m-%Y")
			y=datetime.datetime.strptime(end_date,"%d-%m-%Y")

			# if(y<x):
			# 	print("Error!Please check the start and end date")
			# try:
			# 	raise MyError.MyError.verifyDate(x,y);
			# except (TypeError):
			# 	pass
			if(x>y):
				raise ValueError("Starting date is greater than end date.")


			flag=0;
			for i in xrange(len(arr)):
				if(arr[i]==indexName or values[i]==indexName):
					indexName = arr[i]
					# print(indexName)
					flag=1

			if(flag==0):
				raise ValueError("Check Index name.")

			# if(flag==0):
			# 	print("ERROR check Index name.")

			# else:
			indexName = indexName.replace(" ","%20")

			result = pd.DataFrame()
			while(True):
					if((y-x).days<365):
						try:
							# print(1)
							fromdate= x.strftime("%d-%m-%Y")
							# print(fromdate)
							todate=y.strftime("%d-%m-%Y")
							url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;			
							
							response = requests.get(url, timeout=240)
							page_content = BeautifulSoup(response.content, "html.parser")

							a=page_content.find(id="csvContentDiv").get_text();
							a = a.replace(':',", \n")


							with open("data.csv", "wb") as f:
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
							
							response = requests.get(url, timeout=240)
							page_content = BeautifulSoup(response.content, "html.parser")

							a=page_content.find(id="csvContentDiv").get_text();
							a = a.replace(':',", \n")


							with open("data.csv", "wb") as f:
								f.write(a)

							df = pd.read_csv("data.csv")
							df.set_index("Date",inplace=True)
							df = df[::-1]
							result = pd.concat([result,df])
							y = ( inter - datetime.timedelta(days=1) )

						except AttributeError:
							break;

			
		elif(full_data =="Yes" or full_data=="yes"):


			try:
				raise IndexError.IndexError.verifyIndex(indexName,values)
			except (TypeError):
				pass

				# for i in xrange(len(arr)):
				# 	if(arr[i]==indexName or values[i]==indexName):
				# 		indexName = values[i]
				# 		print(indexName)
				# 		flag=1

				# if(flag==0):
				# 	print("ERROR check Index name.")
				# print("YES")
				x=datetime.datetime.now()
				y=datetime.datetime.now() - datetime.timedelta(days=364)

				# print(x,y)
				result = pd.DataFrame()
				while(True):
					try:
						todate=x.strftime("%d-%m-%Y")
						fromdate= y.strftime("%d-%m-%Y")

						url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;			

						response = requests.get(url, timeout=240)
						page_content = BeautifulSoup(response.content, "html.parser")

						a=page_content.find(id="csvContentDiv").get_text();
						a = a.replace(':',", \n")

						with open("data.csv", "wb") as f:
							f.write(a)

						df = pd.read_csv("data.csv")
						df.set_index("Date",inplace=True)
						df = df[::-1]
						result = pd.concat([result,df])

						x = y - datetime.timedelta(days=1)
						y = x - datetime.timedelta(days=364)

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
			else:
				data.to_csv(link+"/{}.csv".format(self.indexName))
		except (AttributeError):
			print("Check data")

	def returnsToCSVStocks(self,data,link=None):
		try:
			if(link==None):
				data.to_csv(self.stockSymbol+".csv")
			else:
				data.to_csv(link+"/{}.csv".format(self.stockSymbol))
		except (AttributeError):
			print("Check data")


	def returnsForStocks(self,stockSymbol,full_data=None,start_date=None,end_date=None):
		values = ['20MICRONS', '21STCENMGM', '3IINFOTECH', '3MINDIA', '3PLAND', '5PAISA', '63MOONS', '8KMILES', 'A2ZINFRA', 'AARTIDRUGS', 'AARTIIND', 'AARVEEDEN', 'AAVAS', 'ABAN', 'ABB', 'ABBOTINDIA', 'ABCAPITAL', 'ABFRL', 'ABMINTLTD', 'ACC', 'ACCELYA', 'ACE', 'ADANIENT', 'ADANIGAS', 'ADANIGREEN', 'ADANIPORTS', 'ADANIPOWER', 'ADANITRANS', 'ADFFOODS', 'ADHUNIK', 'ADHUNIKIND', 'ADLABS', 'ADORWELD', 'ADROITINFO', 'ADSL', 'ADVANIHOTR', 'ADVENZYMES', 'AEGISCHEM', 'AFFLE', 'AGARIND', 'AGCNET', 'AGRITECH', 'AGROPHOS', 'AHLEAST', 'AHLUCONT', 'AHLWEST', 'AIAENG', 'AIONJSW', 'AIRAN', 'AJANTPHARM', 'AJMERA', 'AKASH', 'AKSHARCHEM', 'AKSHOPTFBR', 'AKZOINDIA', 'ALANKIT', 'ALBERTDAVD', 'ALBK', 'ALCHEM', 'ALEMBICLTD', 'ALICON', 'ALKALI', 'ALKEM', 'ALKYLAMINE', 'ALLCARGO', 'ALLSEC', 'ALMONDZ', 'ALOKTEXT', 'ALPA', 'ALPHAGEO', 'ALPSINDUS', 'AMARAJABAT', 'AMBER', 'AMBIKCO', 'AMBUJACEM', 'AMDIND', 'AMJLAND', 'AMRUTANJAN', 'ANANTRAJ', 'ANDHRABANK', 'ANDHRACEMT', 'ANDHRSUGAR', 'ANIKINDS', 'ANKITMETAL', 'ANSALAPI', 'ANSALHSG', 'ANTGRAPHIC', 'ANUP', 'APARINDS', 'APCL', 'APCOTEXIND', 'APEX', 'APLAPOLLO', 'APLLTD', 'APOLLO', 'APOLLOHOSP', 'APOLLOTYRE', 'APOLSINHOT', 'APTECHT', 'ARCHIDPLY', 'ARCHIES', 'ARCOTECH', 'ARENTERP', 'ARIES', 'ARIHANT', 'ARIHANTSUP', 'ARMANFIN', 'AROGRANITE', 'ARROWGREEN', 'ARROWTEX', 'ARSHIYA', 'ARSSINFRA', 'ARVIND', 'ARVINDFASN', 'ARVSMART', 'ASAHIINDIA', 'ASAHISONG', 'ASAL', 'ASHAPURMIN', 'ASHIANA', 'ASHIMASYN', 'ASHOKA', 'ASHOKLEY', 'ASIANHOTNR', 'ASIANPAINT', 'ASIANTILES', 'ASPINWALL', 'ASSAMCO', 'ASTEC', 'ASTERDM', 'ASTRAL', 'ASTRAMICRO', 'ASTRAZEN', 'ASTRON', 'ATFL', 'ATLANTA', 'ATLASCYCLE', 'ATUL', 'ATULAUTO', 'AUBANK', 'AURIONPRO', 'AUROPHARMA', 'AUSOMENT', 'AUTOAXLES', 'AUTOIND', 'AUTOLITIND', 'AVADHSUGAR', 'AVANTIFEED', 'AVTNPL', 'AXISBANK', 'AXISCADES', 'AYMSYNTEX', 'BAGFILMS', 'BAJAJ-AUTO', 'BAJAJCON', 'BAJAJELEC', 'BAJAJFINSV', 'BAJAJHIND', 'BAJAJHLDNG', 'BAJFINANCE', 'BALAJITELE', 'BALAMINES', 'BALAXI', 'BALKRISHNA', 'BALKRISIND', 'BALLARPUR', 'BALMLAWRIE', 'BALPHARMA', 'BALRAMCHIN', 'BANARBEADS', 'BANARISUG', 'BANCOINDIA', 'BANDHANBNK', 'BANG', 'BANKBARODA', 'BANKINDIA', 'BANSWRAS', 'BARTRONICS', 'BASF', 'BASML', 'BATAINDIA', 'BAYERCROP', 'BBL', 'BBTC', 'BCG', 'BCP', 'BDL', 'BEARDSELL', 'BEDMUTHA', 'BEL', 'BEML', 'BEPL', 'BERGEPAINT', 'BFINVEST', 'BFUTILITIE', 'BGLOBAL', 'BGRENERGY', 'BHAGERIA', 'BHAGYANGR', 'BHAGYAPROP', 'BHANDARI', 'BHARATFORG', 'BHARATGEAR', 'BHARATRAS', 'BHARATWIRE', 'BHARTIARTL', 'BHEL', 'BIGBLOC', 'BIL', 'BILENERGY', 'BINANIIND', 'BINDALAGRO', 'BIOCON', 'BIOFILCHEM', 'BIRLACABLE', 'BIRLACORPN', 'BIRLAMONEY', 'BKMINDST', 'BLBLIMITED', 'BLISSGVS', 'BLKASHYAP', 'BLS', 'BLUEBLENDS', 'BLUECOAST', 'BLUEDART', 'BLUESTARCO', 'BODALCHEM', 'BOMDYEING', 'BOROSIL', 'BOSCHLTD', 'BPCL', 'BPL', 'BRFL', 'BRIGADE', 'BRITANNIA', 'BRNL', 'BROOKS', 'BSE', 'BSELINFRA', 'BSL', 'BSOFT', 'BURNPUR', 'BUTTERFLY', 'BVCL', 'BYKE', 'CADILAHC', 'CALSOFT', 'CAMLINFINE', 'CANBK', 'CANDC', 'CANFINHOME', 'CANTABIL', 'CAPACITE', 'CAPLIPOINT', 'CAPTRUST', 'CARBORUNIV', 'CAREERP', 'CARERATING', 'CASTEXTECH', 'CASTROLIND', 'CCHHL', 'CCL', 'CDSL', 'CEATLTD', 'CEBBCO', 'CELEBRITY', 'CELESTIAL', 'CENTENKA', 'CENTEXT', 'CENTRALBK', 'CENTRUM', 'CENTUM', 'CENTURYPLY', 'CENTURYTEX', 'CERA', 'CEREBRAINT', 'CESC', 'CESCVENT', 'CGCL', 'CGPOWER', 'CHALET', 'CHAMBLFERT', 'CHEMFAB', 'CHENNPETRO', 'CHOLAFIN', 'CHOLAHLDNG', 'CHROMATIC', 'CIGNITITEC', 'CIMMCO', 'CINELINE', 'CINEVISTA', 'CIPLA', 'CKFSL', 'CLEDUCATE', 'CLNINDIA', 'CMICABLES', 'CNOVAPETRO', 'COALINDIA', 'COCHINSHIP', 'COFFEEDAY', 'COLPAL', 'COMPINFO', 'COMPUSOFT', 'CONCOR', 'CONFIPET', 'CONSOFINVT', 'CONTROLPR', 'CORALFINAC', 'CORDSCABLE', 'COROMANDEL', 'CORPBANK', 'COSMOFILMS', 'COUNCODOS', 'COX&KINGS', 'CREATIVE', 'CREATIVEYE', 'CREDITACC', 'CREST', 'CRISIL', 'CROMPTON', 'CTE', 'CUB', 'CUBEXTUB', 'CUMMINSIND', 'CUPID', 'CURATECH', 'CYBERMEDIA', 'CYBERTECH', 'CYIENT', 'DAAWAT', 'DABUR', 'DALBHARAT', 'DALMIASUG', 'DAMODARIND', 'DATAMATICS', 'DBCORP', 'DBL', 'DBREALTY', 'DBSTOCKBRO', 'DCAL', 'DCBBANK', 'DCM', 'DCMFINSERV', 'DCMNVL', 'DCMSHRIRAM', 'DCW', 'DECCANCE', 'DEEPAKFERT', 'DEEPAKNTR', 'DEEPIND', 'DELTACORP', 'DELTAMAGNT', 'DEN', 'DENORA', 'DFMFOODS', 'DGCONTENT', 'DHAMPURSUG', 'DHANBANK', 'DHANUKA', 'DHARSUGAR', 'DHFL', 'DHUNINV', 'DIAMONDYD', 'DIAPOWER', 'DICIND', 'DIGISPICE', 'DIGJAMLTD', 'DISHTV', 'DIVISLAB', 'DIXON', 'DLF', 'DLINKINDIA', 'DMART', 'DNAMEDIA', 'DOLAT', 'DOLLAR', 'DOLPHINOFF', 'DONEAR', 'DPSCLTD', 'DQE', 'DREDGECORP', 'DRREDDY', 'DSSL', 'DTIL', 'DUCON', 'DVL', 'DWARKESH', 'DYNAMATECH', 'DYNPRO', 'EASTSILK', 'EASUNREYRL', 'ECLERX', 'EDELWEISS', 'EDL', 'EDUCOMP', 'EICHERMOT', 'EIDPARRY', 'EIHAHOTELS', 'EIHOTEL', 'EIMCOELECO', 'EKC', 'ELECON', 'ELECTCAST', 'ELECTHERM', 'ELGIEQUIP', 'ELGIRUBCO', 'EMAMILTD', 'EMAMIPAP', 'EMAMIREAL', 'EMCO', 'EMKAY', 'EMMBI', 'ENDURANCE', 'ENERGYDEV', 'ENGINERSIN', 'ENIL', 'EON', 'EQUITAS', 'ERIS', 'EROSMEDIA', 'ESABINDIA', 'ESCORTS', 'ESSARSHPNG', 'ESSELPACK', 'ESTER', 'EUROCERA', 'EUROMULTI', 'EUROTEXIND', 'EVEREADY', 'EVERESTIND', 'EXCEL', 'EXCELINDUS', 'EXIDEIND', 'EXPLEOSOL', 'FACT', 'FAIRCHEM', 'FCL', 'FCONSUMER', 'FCSSOFT', 'FDC', 'FEDERALBNK', 'FEL', 'FELDVR', 'FIEMIND', 'FILATEX', 'FINCABLES', 'FINEORG', 'FINPIPE', 'FLEXITUFF', 'FLFL', 'FLUOROCHEM', 'FMGOETZE', 'FMNL', 'FORCEMOT', 'FORTIS', 'FOSECOIND', 'FRETAIL', 'FSC', 'FSL', 'GABRIEL', 'GAEL', 'GAIL', 'GAL', 'GALAXYSURF', 'GALLANTT', 'GALLISPAT', 'GAMMNINFRA', 'GANDHITUBE', 'GANECOS', 'GANESHHOUC', 'GANGESSECU', 'GANGOTRI', 'GARDENSILK', 'GARFIBRES', 'GATI', 'GAYAHWS', 'GAYAPROJ', 'GDL', 'GEECEE', 'GENESYS', 'GENUSPAPER', 'GENUSPOWER', 'GEOJITFSL', 'GEPIL', 'GESHIP', 'GET&D', 'GFLLIMITED', 'GFSTEELS', 'GHCL', 'GICHSGFIN', 'GICRE', 'GILLANDERS', 'GILLETTE', 'GINNIFILA', 'GIPCL', 'GISOLUTION', 'GKWLIMITED', 'GLAXO', 'GLENMARK', 'GLFL', 'GLOBALVECT', 'GLOBOFFS', 'GLOBUSSPR', 'GMBREW', 'GMDCLTD', 'GMMPFAUDLR', 'GMRINFRA', 'GNA', 'GNFC', 'GOACARBON', 'GOCLCORP', 'GODFRYPHLP', 'GODREJAGRO', 'GODREJCP', 'GODREJIND', 'GODREJPROP', 'GOENKA', 'GOKEX', 'GOKUL', 'GOKULAGRO', 'GOLDENTOBC', 'GOLDIAM', 'GOLDTECH', 'GOODLUCK', 'GPIL', 'GPPL', 'GPTINFRA', 'GRANULES', 'GRAPHITE', 'GRASIM', 'GRAVITA', 'GREAVESCOT', 'GREENLAM', 'GREENPANEL', 'GREENPLY', 'GREENPOWER', 'GRINDWELL', 'GROBTEA', 'GRPLTD', 'GRSE', 'GSCLCEMENT', 'GSFC', 'GSKCONS', 'GSPL', 'GSS', 'GTL', 'GTLINFRA', 'GTNIND', 'GTNTEX', 'GTPL', 'GUFICBIO', 'GUJALKALI', 'GUJAPOLLO', 'GUJGASLTD', 'GUJRAFFIA', 'GULFOILLUB', 'GULFPETRO', 'GULPOLY', 'GVKPIL', 'HAL', 'HARITASEAT', 'HARRMALAYA', 'HATHWAY', 'HATSUN', 'HAVELLS', 'HAVISHA', 'HBLPOWER', 'HBSL', 'HCC', 'HCG', 'HCL-INSYS', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HDIL', 'HEG', 'HEIDELBERG', 'HERCULES', 'HERITGFOOD', 'HEROMOTOCO', 'HESTERBIO', 'HEXATRADEX', 'HEXAWARE', 'HFCL', 'HGINFRA', 'HGS', 'HIGHGROUND', 'HIKAL', 'HIL', 'HILTON', 'HIMATSEIDE', 'HINDALCO', 'HINDCOMPOS', 'HINDCOPPER', 'HINDMOTORS', 'HINDNATGLS', 'HINDOILEXP', 'HINDPETRO', 'HINDSYNTEX', 'HINDUJAVEN', 'HINDUNILVR', 'HINDZINC', 'HIRECT', 'HISARMETAL', 'HITECH', 'HITECHCORP', 'HITECHGEAR', 'HMT', 'HMVL', 'HNDFDS', 'HONAUT', 'HONDAPOWER', 'HOTELEELA', 'HOTELRUGBY', 'HOVS', 'HPL', 'HSCL', 'HSIL', 'HTMEDIA', 'HUBTOWN', 'HUDCO', 'IBREALEST', 'IBULHSGFIN', 'IBULISL', 'IBVENTURES', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ICIL', 'ICRA', 'IDBI', 'IDEA', 'IDFC', 'IDFCFIRSTB', 'IEX', 'IFBAGRO', 'IFBIND', 'IFCI', 'IFGLEXPOR', 'IGARASHI', 'IGL', 'IGPL', 'IIFL', 'IIFLSEC', 'IIFLWAM', 'IITL', 'IL&FSENGG', 'IL&FSTRANS', 'IMFA', 'IMPAL', 'IMPEXFERRO', 'INDBANK', 'INDHOTEL', 'INDIACEM', 'INDIAGLYCO', 'INDIAMART', 'INDIANB', 'INDIANCARD', 'INDIANHUME', 'INDIGO', 'INDLMETER', 'INDNIPPON', 'INDOCO', 'INDORAMA', 'INDOSOLAR', 'INDOSTAR', 'INDOTECH', 'INDOTHAI', 'INDOWIND', 'INDRAMEDCO', 'INDSWFTLAB', 'INDSWFTLTD', 'INDTERRAIN', 'INDUSINDBK', 'INEOSSTYRO', 'INFIBEAM', 'INFOBEAN', 'INFRATEL', 'INFY', 'INGERRAND', 'INOXLEISUR', 'INOXWIND', 'INSECTICID', 'INSPIRISYS', 'INTEGRA', 'INTELLECT', 'INTENTECH', 'INVENTURE', 'IOB', 'IOC', 'IOLCP', 'IPAPPM', 'IPCALAB', 'IRB', 'IRCON', 'IRCTC', 'ISEC', 'ISFT', 'ISMTLTD', 'ITC', 'ITDC', 'ITDCEM', 'ITI', 'IVC', 'IVP', 'IVRCLINFRA', 'IZMO', 'J&KBANK', 'JAGRAN', 'JAGSNPHARM', 'JAIBALAJI', 'JAICORPLTD', 'JAIHINDPRO', 'JAINSTUDIO', 'JAMNAAUTO', 'JAYAGROGN', 'JAYBARMARU', 'JAYNECOIND', 'JAYSREETEA', 'JBCHEPHARM', 'JBFIND', 'JBMA', 'JCHAC', 'JETAIRWAYS', 'JHS', 'JIKIND', 'JINDALPHOT', 'JINDALPOLY', 'JINDALSAW', 'JINDALSTEL', 'JINDCOT', 'JINDRILL', 'JINDWORLD', 'JISLDVREQS', 'JISLJALEQS', 'JITFINFRA', 'JIYAECO', 'JKCEMENT', 'JKIL', 'JKLAKSHMI', 'JKPAPER', 'JKTYRE', 'JMA', 'JMCPROJECT', 'JMFINANCIL', 'JMTAUTOLTD', 'JOCIL', 'JPASSOCIAT', 'JPINFRATEC', 'JPOLYINVST', 'JPPOWER', 'JSL', 'JSLHISAR', 'JSWENERGY', 'JSWHL', 'JSWSTEEL', 'JTEKTINDIA', 'JUBILANT', 'JUBLFOOD', 'JUBLINDS', 'JUMPNET', 'JUSTDIAL', 'JVLAGRO', 'JYOTHYLAB', 'KABRAEXTRU', 'KAJARIACER', 'KAKATCEM', 'KALPATPOWR', 'KALYANI', 'KALYANIFRG', 'KAMATHOTEL', 'KAMDHENU', 'KANANIIND', 'KANORICHEM', 'KANSAINER', 'KARDA', 'KARMAENG', 'KARURVYSYA', 'KAUSHALYA', 'KAVVERITEL', 'KAYA', 'KCP', 'KCPSUGIND', 'KDDL', 'KEC', 'KECL', 'KEI', 'KELLTONTEC', 'KENNAMET', 'KERNEX', 'KESARENT', 'KESORAMIND', 'KEYFINSERV', 'KGL', 'KHADIM', 'KHAITANLTD', 'KHANDSE', 'KICL', 'KILITCH', 'KINGFA', 'KIOCL', 'KIRIINDUS', 'KIRLOSBROS', 'KIRLOSENG', 'KIRLOSIND', 'KITEX', 'KKCL', 'KMSUGAR', 'KNRCON', 'KOHINOOR', 'KOKUYOCMLN', 'KOLTEPATIL', 'KOPRAN', 'KOTAKBANK', 'KOTARISUG', 'KOTHARIPET', 'KOTHARIPRO', 'KPITTECH', 'KPRMILL', 'KRBL', 'KREBSBIO', 'KRIDHANINF', 'KRISHANA', 'KSB', 'KSCL', 'KSERASERA', 'KSK', 'KSL', 'KTIL', 'KTKBANK', 'KUANTUM', 'KWALITY', 'L&TFH', 'LAKPRE', 'LAKSHVILAS', 'LALPATHLAB', 'LAMBODHARA', 'LAOPALA', 'LASA', 'LAURUSLABS', 'LAXMIMACH', 'LEMONTREE', 'LFIC', 'LGBBROSLTD', 'LGBFORGE', 'LIBAS', 'LIBAS', 'LIBERTSHOE', 'LICHSGFIN', 'LINCOLN', 'LINCPEN', 'LINDEINDIA', 'LOKESHMACH', 'LOTUSEYE', 'LOVABLE', 'LPDC', 'LSIL', 'LT', 'LTI', 'LTTS', 'LUMAXIND', 'LUMAXTECH', 'LUPIN', 'LUXIND', 'LYKALABS', 'LYPSAGEMS', 'M&M', 'M&MFIN', 'MAANALU', 'MADHAV', 'MADHUCON', 'MADRASFERT', 'MAGADSUGAR', 'MAGMA', 'MAGNUM', 'MAHABANK', 'MAHAPEXLTD', 'MAHASTEEL', 'MAHESHWARI', 'MAHINDCIE', 'MAHLIFE', 'MAHLOG', 'MAHSCOOTER', 'MAHSEAMLES', 'MAITHANALL', 'MAJESCO', 'MALUPAPER', 'MANAKALUCO', 'MANAKCOAT', 'MANAKSIA', 'MANAKSTEEL', 'MANALIPETC', 'MANAPPURAM', 'MANGALAM', 'MANGCHEFER', 'MANGLMCEM', 'MANGTIMBER', 'MANINDS', 'MANINFRA', 'MANPASAND', 'MANUGRAPH', 'MARALOVER', 'MARATHON', 'MARICO', 'MARKSANS', 'MARUTI', 'MASFIN', 'MASKINVEST', 'MASTEK', 'MATRIMONY', 'MAWANASUG', 'MAXINDIA', 'MAXVIL', 'MAYURUNIQ', 'MAZDA', 'MBAPL', 'MBECL', 'MBLINFRA', 'MCDHOLDING', 'MCDOWELL-N', 'MCLEODRUSS', 'MCX', 'MEGASOFT', 'MEGH', 'MELSTAR', 'MENONBE', 'MEP', 'MERCATOR', 'METALFORGE', 'METKORE', 'METROPOLIS', 'MFSL', 'MGL', 'MHRIL', 'MIC', 'MIDHANI', 'MINDACORP', 'MINDAIND', 'MINDTECK', 'MINDTREE', 'MIRCELECTR', 'MIRZAINT', 'MMFL', 'MMTC', 'MODIRUBBER', 'MOHITIND', 'MOHOTAIND', 'MOIL', 'MOLDTECH', 'MOLDTKPAC', 'MONTECARLO', 'MORARJEE', 'MOREPENLAB', 'MOTHERSUMI', 'MOTILALOFS', 'MOTOGENFIN', 'MPHASIS', 'MPSLTD', 'MRF', 'MRO-TEK', 'MRPL', 'MSPL', 'MSTCLTD', 'MTEDUCARE', 'MTNL', 'MUKANDENGG', 'MUKANDLTD', 'MUKTAARTS', 'MUNJALAU', 'MUNJALSHOW', 'MURUDCERA', 'MUTHOOTCAP', 'MUTHOOTFIN', 'MVL', 'NACLIND', 'NAGAFERT', 'NAGAROIL', 'NAGREEKCAP', 'NAGREEKEXP', 'NAHARCAP', 'NAHARINDUS', 'NAHARPOLY', 'NAHARSPING', 'NATCOPHARM', 'NATHBIOGEN', 'NATIONALUM', 'NATNLSTEEL', 'NAUKRI', 'NAVINFLUOR', 'NAVKARCORP', 'NAVNETEDUL', 'NBCC', 'NBIFIN', 'NBVENTURES', 'NCC', 'NCLIND', 'NDGL', 'NDL', 'NDTV', 'NECCLTD', 'NECLIFE', 'NELCAST', 'NELCO', 'NEOGEN', 'NESCO', 'NESTLEIND', 'NETWORK18', 'NEULANDLAB', 'NEWGEN', 'NEXTMEDIA', 'NFL', 'NH', 'NHPC', 'NIACL', 'NIBL', 'NIITLTD', 'NIITTECH', 'NILAINFRA', 'NILASPACES', 'NILKAMAL', 'NIPPOBATRY', 'NIRAJISPAT', 'NITCO', 'NITESHEST', 'NITINFIRE', 'NITINSPIN', 'NKIND', 'NLCINDIA', 'NMDC', 'NOCIL', 'NOIDATOLL', 'NORBTEAEXP', 'NRAIL', 'NRBBEARING', 'NSIL', 'NTL', 'NTPC', 'NUCLEUS', 'OAL', 'OBEROIRLTY', 'OCCL', 'OFSS', 'OIL', 'OILCOUNTUB', 'OISL', 'OLECTRA', 'OMAXAUTO', 'OMAXE', 'OMKARCHEM', 'OMMETALS', 'ONELIFECAP', 'ONEPOINT', 'ONGC', 'ONMOBILE', 'ONWARDTEC', 'OPTIEMUS', 'OPTOCIRCUI', 'ORBTEXP', 'ORICONENT', 'ORIENTABRA', 'ORIENTALTL', 'ORIENTBANK', 'ORIENTBELL', 'ORIENTCEM', 'ORIENTELEC', 'ORIENTHOT', 'ORIENTLTD', 'ORIENTPPR', 'ORIENTREF', 'ORISSAMINE', 'ORTEL', 'ORTINLABSS', 'OSWALAGRO', 'PAEL', 'PAGEIND', 'PAISALO', 'PALASHSECU', 'PALREDTEC', 'PANACEABIO', 'PANAMAPET', 'PAPERPROD', 'PARABDRUGS', 'PARACABLES', 'PARAGMILK', 'PARSVNATH', 'PATELENG', 'PATINTLOG', 'PATSPINLTD', 'PCJEWELLER', 'PDMJEPAPER', 'PDPL', 'PDSMFL', 'PEARLPOLY', 'PEL', 'PENIND', 'PENINLAND', 'PERSISTENT', 'PETRONENGG', 'PETRONET', 'PFC', 'PFIZER', 'PFOCUS', 'PFS', 'PGEL', 'PGHH', 'PGHL', 'PGIL', 'PHILIPCARB', 'PHOENIXLTD', 'PIDILITIND', 'PIIND', 'PILANIINVS', 'PILITA', 'PIONDIST', 'PIONEEREMB', 'PIRPHYTO', 'PITTIENG', 'PKTEA', 'PLASTIBLEN', 'PNB', 'PNBGILTS', 'PNBHOUSING', 'PNC', 'PNCINFRA', 'PODDARHOUS', 'PODDARMENT', 'POKARNA', 'POLYCAB', 'POLYMED', 'POLYPLEX', 'PONNIERODE', 'POWERGRID', 'POWERMECH', 'PPAP', 'PPL', 'PRABHAT', 'PRADIP', 'PRAENG', 'PRAJIND', 'PRAKASH', 'PRAKASHSTL', 'PRAXIS', 'PRECAM', 'PRECOT', 'PRECWIRE', 'PREMEXPLN', 'PREMIER', 'PREMIERPOL', 'PRESSMN', 'PRESTIGE', 'PRICOLLTD', 'PRIMESECU', 'PROSEED', 'PROVOGE', 'PROZONINTU', 'PRSMJOHNSN', 'PSB', 'PSL', 'PSPPROJECT', 'PTC', 'PTL', 'PUNJABCHEM', 'PUNJLLOYD', 'PURVA', 'PVR', 'QUESS', 'QUICKHEAL', 'RADAAN', 'RADICO', 'RADIOCITY', 'RAIN', 'RAJESHEXPO', 'RAJRAYON', 'RAJSREESUG', 'RAJTV', 'RAJVIR', 'RALLIS', 'RAMANEWS', 'RAMASTEEL', 'RAMCOCEM', 'RAMCOIND', 'RAMCOSYS', 'RAMKY', 'RANASUG', 'RANEENGINE', 'RANEHOLDIN', 'RATNAMANI', 'RAYMOND', 'RBL', 'RBLBANK', 'RCF', 'RCOM', 'RECLTD', 'REDINGTON', 'REFEX', 'REGENCERAM', 'RELAXO', 'RELCAPITAL', 'RELIANCE', 'RELIGARE', 'RELINFRA', 'REMSONSIND', 'RENUKA', 'REPCOHOME', 'REPRO', 'RESPONIND', 'REVATHI', 'RGL', 'RHFL', 'RICOAUTO', 'RIIL', 'RITES', 'RKDL', 'RKFORGE', 'RMCL', 'RML', 'RNAM', 'RNAVAL', 'ROHITFERRO', 'ROHLTD', 'ROLLT', 'ROLTA', 'ROSSELLIND', 'RPGLIFE', 'RPOWER', 'RPPINFRA', 'RSSOFTWARE', 'RSWM', 'RSYSTEMS', 'RTNINFRA', 'RTNPOWER', 'RUBYMILLS', 'RUCHINFRA', 'RUCHIRA', 'RUCHISOYA', 'RUPA', 'RUSHIL', 'RVNL', 'SABEVENTS', 'SABTN', 'SADBHAV', 'SADBHIN', 'SAFARI', 'SAGARDEEP', 'SAGCEM', 'SAIL', 'SAKAR', 'SAKHTISUG', 'SAKSOFT', 'SAKUMA', 'SALASAR', 'SALONA', 'SALSTEEL', 'SALZERELEC', 'SAMBHAAV', 'SANCO', 'SANDESH', 'SANDHAR', 'SANGAMIND', 'SANGHIIND', 'SANGHVIFOR', 'SANGHVIMOV', 'SANGINITA', 'SANOFI', 'SANWARIA', 'SARDAEN', 'SAREGAMA', 'SARLAPOLY', 'SASKEN', 'SASTASUNDR', 'SATHAISPAT', 'SATIA', 'SATIN', 'SBILIFE', 'SBIN', 'SCAPDVR', 'SCHAEFFLER', 'SCHAND', 'SCHNEIDER', 'SCI', 'SDBL', 'SEAMECLTD', 'SELAN', 'SELMCL', 'SEPOWER', 'SEQUENT', 'SESHAPAPER', 'SETCO', 'SETUINFRA', 'SEYAIND', 'SFL', 'SGL', 'SHAHALLOYS', 'SHAKTIPUMP', 'SHALBY', 'SHALPAINTS', 'SHANKARA', 'SHANTIGEAR', 'SHARDACROP', 'SHARDAMOTR', 'SHEMAROO', 'SHILPAMED', 'SHIRPUR-G', 'SHIVAMAUTO', 'SHIVAMILLS', 'SHIVATEX', 'SHK', 'SHOPERSTOP', 'SHREDIGCEM', 'SHREECEM', 'SHREEPUSHK', 'SHREERAMA', 'SHRENIK', 'SHREYANIND', 'SHREYAS', 'SHRIPISTON', 'SHRIRAMCIT', 'SHRIRAMEPC', 'SHYAMCENT', 'SHYAMTEL', 'SICAGEN', 'SICAL', 'SIEMENS', 'SIGIND', 'SIL', 'SILINV', 'SIMBHALS', 'SIMPLEXINF', 'SINTEX', 'SIRCA', 'SIS', 'SITINET', 'SIYSIL', 'SJVN', 'SKFINDIA', 'SKIL', 'SKIPPER', 'SKMEGGPROD', 'SMARTLINK', 'SMLISUZU', 'SMPL', 'SMSLIFE', 'SMSPHARMA', 'SNOWMAN', 'SOBHA', 'SOLARA', 'SOLARINDS', 'SOMANYCERA', 'SOMATEX', 'SOMICONVEY', 'SONATSOFTW', 'SORILINFRA', 'SOTL', 'SOUTHBANK', 'SOUTHWEST', 'SPAL', 'SPANDANA', 'SPARC', 'SPCENET', 'SPECIALITY', 'SPENCERS', 'SPENTEX', 'SPIC', 'SPICEJET', 'SPLIL', 'SPMLINFRA', 'SPTL', 'SPYL', 'SREEL', 'SREINFRA', 'SRF', 'SRHHYPOLTD', 'SRIPIPES', 'SRSLTD', 'SRTRANSFIN', 'SSWL', 'STAMPEDE', 'STAR', 'STARCEMENT', 'STARPAPER', 'STCINDIA', 'STEELCITY', 'STEELXIND', 'STEL', 'STERTOOLS', 'STINDIA', 'STRTECH', 'SUBCAPCITY', 'SUBEX', 'SUBROS', 'SUDARSCHEM', 'SUJANAUNI', 'SUMEETINDS', 'SUMIT', 'SUMMITSEC', 'SUNCLAYLTD', 'SUNDARAM', 'SUNDARMFIN', 'SUNDARMHLD', 'SUNDRMBRAK', 'SUNDRMFAST', 'SUNFLAG', 'SUNPHARMA', 'SUNTECK', 'SUNTV', 'SUPERHOUSE', 'SUPERSPIN', 'SUPPETRO', 'SUPRAJIT', 'SUPREMEIND', 'SUPREMEINF', 'SURANASOL', 'SURANAT&P', 'SURYALAXMI', 'SURYAROSNI', 'SUTLEJTEX', 'SUVEN', 'SUZLON', 'SWANENERGY', 'SWARAJENG', 'SWELECTES', 'SWSOLAR', 'SYMPHONY', 'SYNCOM', 'SYNDIBANK', 'SYNGENE', 'TAINWALCHM', 'TAJGVK', 'TAKE', 'TALBROAUTO', 'TALWALKARS', 'TALWGYM', 'TANLA', 'TANTIACONS', 'TARAPUR', 'TARMAT', 'TASTYBITE', 'TATACHEM', 'TATACOFFEE', 'TATACOMM', 'TATAELXSI', 'TATAGLOBAL', 'TATAINVEST', 'TATAMETALI', 'TATAMOTORS', 'TATAMTRDVR', 'TATAPOWER', 'TATASTEEL', 'TATASTLBSL', 'TATASTLLP', 'TBZ', 'TCI', 'TCIDEVELOP', 'TCIEXP', 'TCIFINANCE', 'TCNSBRANDS', 'TCPLPACK', 'TCS', 'TDPOWERSYS', 'TEAMLEASE', 'TECHIN', 'TECHM', 'TECHNOE', 'TECHNOFAB', 'TEJASNET', 'TERASOFT', 'TEXINFRA', 'TEXMOPIPES', 'TEXRAIL', 'TEXRAIL', 'TFCILTD', 'TFL', 'TGBHOTELS', 'TGBHOTELS', 'THANGAMAYL', 'THEINVEST', 'THEMISMED', 'THERMAX', 'THIRUSUGAR', 'THOMASCOOK', 'THOMASCOTT', 'THYROCARE', 'TI', 'TIDEWATER', 'TIIL', 'TIINDIA', 'TIJARIA', 'TIL', 'TIMESGTY', 'TIMETECHNO', 'TIMKEN', 'TINPLATE', 'TIPSINDLTD', 'TIRUMALCHM', 'TITAN', 'TMRVL', 'TNPETRO', 'TNPL', 'TNTELE', 'TOKYOPLAST', 'TORNTPHARM', 'TORNTPOWER', 'TPLPLASTEH', 'TREEHOUSE', 'TREJHARA', 'TRENT', 'TRF', 'TRIDENT', 'TRIGYN', 'TRIL', 'TRITURBINE', 'TRIVENI', 'TTKHLTCARE', 'TTKPRESTIG', 'TTL', 'TTML', 'TV18BRDCST', 'TVSELECT', 'TVSMOTOR', 'TVSSRICHAK', 'TVTODAY', 'TVVISION', 'TWL', 'UBL', 'UCALFUEL', 'UCOBANK', 'UFLEX', 'UFO', 'UGARSUGAR', 'UJAAS', 'UJJIVAN', 'ULTRACEMCO', 'UMANGDAIRY', 'UMESLTD', 'UNICHEMLAB', 'UNIENTER', 'UNIONBANK', 'UNIPLY', 'UNITECH', 'UNITEDBNK', 'UNITEDTEA', 'UNITY', 'UNIVCABLES', 'UPL', 'URJA', 'USHAMART', 'UTTAMSTL', 'UTTAMSUGAR', 'UVSL', 'V2RETAIL', 'VADILALIND', 'VAIBHAVGBL', 'VAKRANGEE', 'VARDHACRLC', 'VARDMNPOLY', 'VARROC', 'VASCONEQ', 'VASWANI', 'VBL', 'VEDL', 'VENKEYS', 'VENUSREM', 'VESUVIUS', 'VETO', 'VGUARD', 'VHL', 'VICEROY', 'VIDEOIND', 'VIDHIING', 'VIJIFIN', 'VIKASECO', 'VIKASMCORP', 'VIKASPROP', 'VIKASWSP', 'VIMALOIL', 'VIMTALABS', 'VINATIORGA', 'VINDHYATEL', 'VINYLINDIA', 'VIPCLOTHNG', 'VIPIND', 'VIPULLTD', 'VISAKAIND', 'VISASTEEL', 'VISESHINFO', 'VISHAL', 'VISHNU', 'VISHWARAJ', 'VIVIDHA', 'VIVIMEDLAB', 'VLSFINANCE', 'VMART', 'VOLTAMP', 'VOLTAS', 'VRLLOG', 'VSSL', 'VSTIND', 'VSTTILLERS', 'VTL', 'WABAG', 'WABCOINDIA', 'WALCHANNAG', 'WANBURY', 'WATERBASE', 'WEBELSOLAR', 'WEIZFOREX', 'WEIZMANIND', 'WELCORP', 'WELENT', 'WELINV', 'WELSPUNIND', 'WENDT', 'WESTLIFE', 'WHEELS', 'WHIRLPOOL', 'WILLAMAGOR', 'WINDMACHIN', 'WINSOME', 'WIPL', 'WIPRO', 'WOCKPHARMA', 'WONDERLA', 'WSI', 'WSTCSTPAPR', 'XCHANGING', 'XELPMOC', 'XLENERGY', 'XPROINDIA', 'YESBANK', 'ZEEL', 'ZEELEARN', 'ZEEMEDIA', 'ZENITHBIR', 'ZENITHEXPO', 'ZENSARTECH', 'ZENTEC', 'ZICOM', 'ZODIACLOTH', 'ZODJRDMKJ', 'ZOTA', 'ZUARI', 'ZUARIGLOB', 'ZYDUSWELL']

		self.stockSymbol = stockSymbol;

		headers = {
		"Host": "www.nseindia.com",
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate, br",
		"X-Requested-With": "XMLHttpRequest",
		"Referer": "https://www.nseindia.com/products/content/equities/equities/eq_security.htm",
		"Access-Control-Allow-Origin" : "*",
		"Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
		"Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
		'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}

		first = 'https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp'
		result=[];
		session = requests.Session()
		urlpost = "https://www.nseindia.com/marketinfo/sym_map/symbolCount.jsp?symbol="
		data = {"symbol":stockSymbol}
		response = session.post(urlpost,data=data)
		page_content = BeautifulSoup(response.content, "html.parser")
		symbolCount = (str(page_content))

		print(stockSymbol)
		if(full_data ==None or full_data=="No"):

				x=datetime.datetime.strptime(start_date,"%d-%m-%Y")
				y=datetime.datetime.strptime(end_date,"%d-%m-%Y")

				if(x>y):
					raise ValueError("Starting date is greater than end date.")
			# try:
			# 	raise IndexError.IndexError.verifyIndex(stockSymbol,values)
			# except (TypeError):
			# 	pass			
				if stockSymbol not in values:
					raise ValueError("Check the Stock symbol.")

				result = pd.DataFrame()
				while(True):
					if((y-x).days<365):
						try:
							# print(1)
							fromdate= x.strftime("%d-%m-%Y")
							# print(fromdate)
							todate=y.strftime("%d-%m-%Y")

							url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
							
							response = requests.get(url, timeout=240,headers=headers)
							page_content = BeautifulSoup(response.content, "html.parser")
							# print(page_content)
							a=page_content.find(id="csvContentDiv").get_text();
							a = a.replace(':',", \n")


							with open("data.csv", "wb") as f:
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
							url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
												
							response = requests.get(url, timeout=240,headers=headers)
							page_content = BeautifulSoup(response.content, "html.parser")
							# print(page_content)

							a=page_content.find(id="csvContentDiv").get_text();
							# print(a)
							a = a.replace(':',", \n")


							with open("data.csv", "wb") as f:
								f.write(a)

							df = pd.read_csv("data.csv")
							df.set_index("Date",inplace=True)
							df = df[::-1]
							result = pd.concat([result,df])
							y = ( inter - datetime.timedelta(days=1) )

						except AttributeError:
							break;

			
		elif(full_data =="Yes" or full_data=="yes"):
				# print("YES")
				x=datetime.datetime.now()
				y=datetime.datetime.now() - datetime.timedelta(days=364)

				if stockSymbol not in values:
					raise ValueError("Check the Stock symbol.")
				result = pd.DataFrame()
				while(True):
					try:
						todate=x.strftime("%d-%m-%Y")
						fromdate= y.strftime("%d-%m-%Y")

						url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
								

						response = requests.get(url, timeout=240,headers=headers)
						page_content = BeautifulSoup(response.content, "html.parser")
						a=page_content.find(id="csvContentDiv").get_text();
						a = a.replace(':',", \n")

						with open("data.csv", "wb") as f:
							f.write(a)

						df = pd.read_csv("data.csv")
						df.set_index("Date",inplace=True)
						df = df[::-1]
						result = pd.concat([result,df])

						x = y - datetime.timedelta(days=1)
						y = x - datetime.timedelta(days=364)

					except AttributeError:

						break;
		try:
			os.remove("data.csv")
		except(OSError):
			pass


		return result;




	def calculateReturns(self,data,link=None):
		# print(data)
		df = data
		df["Date"] = df.index
		df["Date"] = pd.to_datetime(df["Date"]).dt.date

		endActual = (df.iloc[0]["Date"]).strftime('%Y-%m-%d')
		startActual = (df.iloc[-1]["Date"]).strftime('%Y-%m-%d')


		df = df.pivot(index = "Date",columns = "Close")
		start_date = df.index.min() - pd.DateOffset(day=1)
		end_date = df.index.max() + pd.DateOffset(day=31)
		dates = pd.date_range(start_date, end_date, freq='D')
		dates.name = 'Date'
		df = df.reindex(dates, method='ffill')
		df = df.stack('Close')
		df = df.sort_index(level=0)
		df = df.reset_index()

		df.index = df["Date"]
		df = (df[startActual:endActual])
		df = df.asfreq(freq="1D")
		df["Date"] = pd.to_datetime(df["Date"])


		df["1 Day Date"] = (df.Date.shift(1)).dt.date
		df["1 Day Price"] = ( df["Close Price"].shift(1) )
		df["1 Day Returns"] = ( df["Close Price"]/df["Close Price"].shift(1) ) -1

		df["1 Week Date"] = (df.Date.shift(7)).dt.date
		df["1 Week Price"] = ( df["Close Price"].shift(7) )
		df["1 Week Returns"] = ( df["Close Price"]/df["Close Price"].shift(7) ) -1

		df["2 Week Date"] = (df.Date.shift(14)).dt.date
		df["2 Week Price"] = ( df["Close Price"].shift(14) )
		df["2 Week Returns"] = ( df["Close Price"]/df["Close Price"].shift(14) ) -1

		df["1 Month Date"] = (df.Date.shift(30)).dt.date
		df["1 Month Price"] = ( df["Close Price"].shift(30) )
		df["1 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(30) ) -1

		df["2 Month Date"] = (df.Date.shift(61)).dt.date
		df["2 Month Price"] = ( df["Close Price"].shift(61) )
		df["2 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(61) ) -1


		df["3 Month Date"] = (df.Date.shift(91)).dt.date
		df["3 Month Price"] = ( df["Close Price"].shift(91) )
		df["3 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(91) ) -1

		df["6 Month Date"] = (df.Date.shift(182)).dt.date
		df["6 Month Price"] = ( df["Close Price"].shift(182) )
		df["6 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(182) ) -1

		df["9 Month Date"] = (df.Date.shift(273)).dt.date
		df["9 Month Price"] = ( df["Close Price"].shift(273) )
		df["9 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(273) ) -1

		df["1 Year Date"] = (df.Date.shift(365)).dt.date
		df["1 Year Price"] = ( df["Close Price"].shift(365) )
		df["1 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(365) ) -1

		df["2 Year Date"] = (df.Date.shift(730)).dt.date
		df["2 Year Price"] = ( df["Close Price"].shift(730) )
		df["2 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(730) ) -1

		# df["5 Year Date"] = (df.Date.shift(1826)).dt.date
		# df["5 Year Price"] = ( df["Close Price"].shift(1826) )
		# df["5 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(1826) ) -1

		ar = (np.where(df["1 Day Returns"]==0))
		df.drop(df.index[ar],inplace=True)

		df["Date"] = pd.to_datetime(df["Date"]).dt.date
		df.index = df["Date"]
		df.drop(columns="Date",inplace=True)
		if(link==None):
			df.to_excel("{}.xls".format(self.indexName))
		else:
			df.to_excel(link+"/{}.xls".format(self.indexName))


	def calculateReturnsForStocks(self,data,link=None):
		# print(data)
		df = data
		df["Date"] = df.index
		df["Date"] = pd.to_datetime(df["Date"]).dt.date

		endActual = (df.iloc[0]["Date"]).strftime('%Y-%m-%d')
		startActual = (df.iloc[-1]["Date"]).strftime('%Y-%m-%d')

		print(df)
		df = df.drop_duplicates()
		df = df.pivot(index = "Date",columns = "Close Price")
		start_date = df.index.min() - pd.DateOffset(day=1)
		end_date = df.index.max() + pd.DateOffset(day=31)
		dates = pd.date_range(start_date, end_date, freq='D')
		dates.name = 'Date'
		df = df.reindex(dates, method='ffill')
		df = df.stack('Close Price')
		df = df.sort_index(level=0)
		df = df.reset_index()

		df.index = df["Date"]
		df = (df[startActual:endActual])
		df = df.asfreq(freq="1D")
		df["Date"] = pd.to_datetime(df["Date"])


		df["1 Day Date"] = (df.Date.shift(1)).dt.date
		df["1 Day Price"] = ( df["Close Price"].shift(1) )
		df["1 Day Returns"] = ( df["Close Price"]/df["Close Price"].shift(1) ) -1

		df["1 Week Date"] = (df.Date.shift(7)).dt.date
		df["1 Week Price"] = ( df["Close Price"].shift(7) )
		df["1 Week Returns"] = ( df["Close Price"]/df["Close Price"].shift(7) ) -1

		df["2 Week Date"] = (df.Date.shift(14)).dt.date
		df["2 Week Price"] = ( df["Close Price"].shift(14) )
		df["2 Week Returns"] = ( df["Close Price"]/df["Close Price"].shift(14) ) -1

		df["1 Month Date"] = (df.Date.shift(30)).dt.date
		df["1 Month Price"] = ( df["Close Price"].shift(30) )
		df["1 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(30) ) -1

		df["2 Month Date"] = (df.Date.shift(61)).dt.date
		df["2 Month Price"] = ( df["Close Price"].shift(61) )
		df["2 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(61) ) -1


		df["3 Month Date"] = (df.Date.shift(91)).dt.date
		df["3 Month Price"] = ( df["Close Price"].shift(91) )
		df["3 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(91) ) -1

		df["6 Month Date"] = (df.Date.shift(182)).dt.date
		df["6 Month Price"] = ( df["Close Price"].shift(182) )
		df["6 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(182) ) -1

		df["9 Month Date"] = (df.Date.shift(273)).dt.date
		df["9 Month Price"] = ( df["Close Price"].shift(273) )
		df["9 Month Returns"] = ( df["Close Price"]/df["Close Price"].shift(273) ) -1

		df["1 Year Date"] = (df.Date.shift(365)).dt.date
		df["1 Year Price"] = ( df["Close Price"].shift(365) )
		df["1 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(365) ) -1

		df["2 Year Date"] = (df.Date.shift(730)).dt.date
		df["2 Year Price"] = ( df["Close Price"].shift(730) )
		df["2 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(730) ) -1

		# df["5 Year Date"] = (df.Date.shift(1826)).dt.date
		# df["5 Year Price"] = ( df["Close Price"].shift(1826) )
		# df["5 Year Returns"] = ( df["Close Price"]/df["Close Price"].shift(1826) ) -1

		ar = (np.where(df["1 Day Returns"]==0))
		df.drop(df.index[ar],inplace=True)

		df["Date"] = pd.to_datetime(df["Date"]).dt.date
		df.index = df["Date"]
		df.drop(columns="Date",inplace=True)
		if(link==None):
			df.to_excel("{}.xls".format(self.stockSymbol))
		else:
			df.to_excel(link+"/{}.xls".format(self.stockSymbol))
