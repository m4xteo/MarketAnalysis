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


api_key = ""
api_fullquote = "https://financialmodelingprep.com/api/v3/quote/AAPL?apikey="
api_otcquote = "https://financialmodelingprep.com/api/v3/otc/real-time-price/BATRB?apikey="


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
