import pandas as pd
from bs4 import BeautifulSoup 
import datetime, timedelta, requests, os, re, math

from NSEDownload.progress_bar import init_bar, print_bar, end_bar
from NSEDownload.static_data import values, arr, valuesTRI, arrTRI, headers, headers_adjusted

attempt = 0
def scrape_givendate(x, y, indexName, first, types = 0, stockSymbol = None, symbolCount = None):

	original_x = x
	original_y = y

	result = pd.DataFrame()
	stage = 0
	total_stages = math.ceil((y-x).days/365)
	response = []

	init_bar(total_stages)

	while(True):
		if((y-x).days < 365):

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
			except Exception as e:
				SystemExit(e)

			if(response.status_code == requests.codes.ok):

				page_content = BeautifulSoup(response.content, "html.parser")

				try:
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

				except AttributeError:
					# if(total_stages <= 1):
						# print("No data available from " + str(fromdate) + " to " + str(todate))
					break;

			else:
				response.raise_for_status()

			break;

		if ((y-x).days >= 365 ):

			todate   = y.strftime("%d-%m-%Y")
			fromdate = ( y - datetime.timedelta(days=364) ).strftime("%d-%m-%Y")
			inter    =  y - datetime.timedelta(days=364) 

			if(types==1):
				url = first + '?symbol='+(stockSymbol)+ '&segmentLink=3&symbolCount'+ symbolCount+ "&series=EQ&dateRange=+&fromDate="+fromdate+"&toDate="+todate+"&dataType=PRICEVOLUMEDELIVERABLE"			
			else:
				url = first + '?indexType='+(indexName)+ '&fromDate='+ fromdate + '&toDate='+ todate;

			try:
				response = requests.get(url, timeout = 20, headers = headers)
			except requests.exceptions.RequestException as e: 
				SystemExit(e)
			except Exception as e:
				SystemExit(e)

			if(response.status_code == requests.codes.ok):

				page_content = BeautifulSoup(response.content, "html.parser")
				y = ( inter - datetime.timedelta(days=1) )

				try:
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

				except AttributeError:
					pass
					# print("No data available from " + str(fromdate) + " to " + str(todate))


			else:
				response.raise_for_status()

	try:
		os.remove("data.csv")
	except(OSError):
		pass


	global attempt

	if(len(result) == 0 and attempt == 0):
		attempt = attempt + 1
		print("Unsuccessful attempt. Trying again.")
		scrape_givendate(original_x, original_y, indexName, first, types, stockSymbol, symbolCount)

	elif(len(result) == 0 and attempt == 1):
		print("Error : Empty dataframe. Please try Again.")
		return result

	if(attempt == 1):
		attempt = 0

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
		except Exception as e:
				SystemExit(e)

		if(response.status_code == requests.codes.ok):

			page_content = BeautifulSoup(response.content, "html.parser")

			try:
				a = page_content.find(id = "csvContentDiv").get_text();
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
				# print("No data available from " + str(fromdate) + " to " + str(todate))
				break;

			
		else:
			response.raise_for_status()

	try:
		os.remove("data.csv")
	except(OSError):
		pass

	global attempt

	if(len(result) == 0 and attempt == 0):
		attempt = attempt + 1
		print("Unsuccessful attempt. Trying again.")
		scrape_fulldata( indexName, first , types, stockSymbol, symbolCount)
		

	elif(len(result) == 0 and attempt == 1):
		print("Error : Empty dataframe. Please try Again.")
		return result

	if(attempt == 1):
		attempt = 0

	end_bar(total_stages)

	return result


def scrape_bonus_splits(stockSymbol, event_type):

	dates = [];	ratio = []

	if(not (event_type == "SPLIT" or event_type == "BONUS")):
		print("Event type not understood")
		return [ratio, dates]

	url = "https://www1.nseindia.com/corporates/corpInfo/equities/getCorpActions.jsp?symbol=" + stockSymbol + "&Industry=&ExDt=More%20than%2024%20Months&exDt=More%20than%2024%20Months&recordDt=&bcstartDt=&industry=&CAType=" + event_type
	response = requests.get(url, timeout = 60, headers = headers_adjusted)

	page_content = BeautifulSoup(response.content, "html.parser")
	page_content = page_content.text.replace('\n','')
	page_content = page_content.replace('\t','')

	date_start = page_content.find('exDt:"')
	date_end = page_content.find(',', date_start)

	while(date_start != -1):

		sub_start = page_content.find('Spl')
		if(event_type == "BONUS"):
		  sub_start = page_content.find('Bonus')

		sub_end = page_content.find(',', sub_start)

		num = re.findall('\d+',page_content[sub_start:sub_end])

		if(event_type == "BONUS"):
			ratio.append((int(num[0])+int(num[1]))/int(num[1]))
		else:
			ratio.append(int(num[0])/int(num[1]))

		dates.append(page_content[date_start+6:date_end-1])
		page_content = page_content[date_end:-1]

		date_start = page_content.find('exDt:"')
		date_end = page_content.find(',', date_start)

	return [ratio, dates]

