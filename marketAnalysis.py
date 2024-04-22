import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt



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


# init values
api_key = ""
stockTicker ="NASDAQ"

# api links
api_fullquote = "https://financialmodelingprep.com/api/v3/quote/" + stockTicker + "?apikey="
api_otcquote = "https://financialmodelingprep.com/api/v3/otc/real-time-price/BATRB?apikey="
api_exsymbols = "https://financialmodelingprep.com/api/v3/symbol/"+ stockTicker + "?apikey="
api_profile =  "https://financialmodelingprep.com/api/v3/profile/"+ stockTicker + "?apikey="


#functions
def printLogo():
	print("""┳┳┓    ┓      ┏┓    ┓   • 
┃┃┃┏┓┏┓┃┏┏┓╋  ┣┫┏┓┏┓┃┓┏┏┓┏
┛ ┗┗┻┛ ┛┗┗ ┗  ┛┗┛┗┗┻┗┗┫┛┗┛
                      ┛   
# Developed by Matt (m4xteo) and Karl (nok-si)
 
""")

def main():
	printLogo()
	#print(grabData(api_exsymbols, api_key))
	plt.plot(grabData(api_exsymbols, api_key))
	plt.show()

def grabData(apiLink, apiKey):
	main() 
	parsedLink = apiLink + apiKey
	webResponse = requests.get(url=parsedLink)
	rawData = webResponse.json()

	return rawData

if __name__ == "__main__":
