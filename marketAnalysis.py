import matplotlib.pyplot as plt
#import mplfinance as mpf
#import datetime as dt
import json
import urllib



'''
┳┳┓    ┓      ┏┓    ┓   • 
┃┃┃┏┓┏┓┃┏┏┓╋  ┣┫┏┓┏┓┃┓┏┏┓┏
┛ ┗┗┻┛ ┛┗┗ ┗  ┛┗┛┗┗┻┗┗┫┛┗┛
                      ┛   
Developed by Matt (m4xteo) and Karl (nok-si)

Pulls data from Financial Modeling Prep and others (future) and analyses stock market health.
'''

import requests
import numpy
import pandas



# init values
api_key = "TQ7srJMzwQvs5TU1eQiBWndnFCk8GwYF"
stockTicker ="AAPL"

# api links stocks
api_fullquote = "https://financialmodelingprep.com/api/v3/quote/" + stockTicker + "?apikey="
api_otcquote = "https://financialmodelingprep.com/api/v3/otc/real-time-price/BATRB?apikey="
api_exsymbols = "https://financialmodelingprep.com/api/v3/symbol/"+ stockTicker + "?apikey="
api_profile =  "https://financialmodelingprep.com/api/v3/profile/"+ stockTicker + "?apikey="

#https://docs.coincap.io/#61e708a8-8876-4fb2-a418-86f12f308978
#api links crypto
crypto_ticker = "bitcoin"
crpyto_interval = "d1" #day
crypto_api_historical = "https://api.coincap.io/v2/assets/" + crypto_ticker +"/history?interval=" + crpyto_interval


#functions
def printLogo():
	print("""┳┳┓    ┓      ┏┓    ┓   • 
┃┃┃┏┓┏┓┃┏┏┓╋  ┣┫┏┓┏┓┃┓┏┏┓┏
┛ ┗┗┻┛ ┛┗┗ ┗  ┛┗┛┗┗┻┗┗┫┛┗┛
                      ┛   
# Developed by Matt (m4xteo) and Karl (nok-si)
For crypto and stock markets.
 
""")

def main():
	printLogo()
	#print(grabData(api_exsymbols, api_key))
	#plt.plot(grabData(api_exsymbols, api_key))
	#plt.show()

	rawData = grabData(crypto_api_historical, "")
	#jsonObject = json.loads(rawData)
	#closingPrice = (jsonObject["price"])

	#price = rawData[0]["price"]
	#dayLow = rawData[0]["dayLow"]
	#print(rawData[0]["price"])



def showGraph(ticker, date, timestamp):
	
	return x

# Function to grab the data (raw)
def grabData(apiLink, apiKey): 
	parsedLink = apiLink + apiKey
	rawData = ""

	webResponse = requests.get(parsedLink).json()
	#rawData = json.loads(webResponse.content)
	#print(str(rawData))

	return webResponse


# Analyses Ticker with numerous methods
def analyseTicker(stock, avg, method):
	if method == "all":
		_RSI(stock, avg)
		_MCD(stock, avg)

def _RSI(stock, avg):
	return x

def _MCD_(stock, avg):
	return x 


if __name__ == "__main__":
	main()