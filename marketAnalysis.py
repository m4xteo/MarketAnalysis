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
stockTicker = "APPL"

# api links
api_fullquote = "https://financialmodelingprep.com/api/v3/quote/" + stockTicker + "?apikey="
api_otcquote = "https://financialmodelingprep.com/api/v3/otc/real-time-price/BATRB?apikey="
api_exsymbols = "https://financialmodelingprep.com/api/v3/symbol/"stockTicker + "?apikey="


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
	print(grabData(api_fullquote, api_key))

def grabData(apiLink, apiKey):
	parsedLink = apiLink + apiKey
	webResponse = requests.get(url=parsedLink)
	rawData = webResponse.json()

	return rawData

if __name__ == "__main__":
	main() 
