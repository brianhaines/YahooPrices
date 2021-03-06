'''
This class will return price information from Finance.Yahoo.com
for any given equity ticker using BeautifulSoup4
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime


class YahooPrice():
	"""Once initiated this class will reach out to yahoo finance and 
	request a quote page using the given ticker"""

	def __init__(self, tkr):
		url = 'http://finance.yahoo.com/q?s=%s' %tkr
		self.ticker = tkr


		try:
			count = 1
			tickerPage = urlopen(url)
		except Exception:
			print("Problem with connection to Yahoo. Trying again")
			sleep(.25)
			tickerPage = urlopen(url)
			if count > 4:
				print("No connection to the internet")
				raise SystemExit


		#Turn the page into soup
		soup = BeautifulSoup(tickerPage)

		#Find the real-time Last Price value in the soup
		for y in soup.find_all("span", class_="time_rtq_ticker"):
			x = y.contents[0].contents
		self.LastPrice = x[0]

		#And the time of the rtq
		for y in soup.find_all("span", class_="time_rtq"):
			t = y.contents[1].contents[0].contents
		self.qTime = t[0]

		#Pull data from price table
		s = soup.find_all("td", class_="yfnc_tabledata1")

		#System time of the request
		self.sysTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

		try:
			self.prevClose = s[0].contents[0]
		except AttributeError:
			self.prevClose = 'N/A'

		try:
			self.tOpen = s[1].contents[0]
		except AttributeError:
			self.tOpen = 'N/A'

		try:
			self.bid = s[2].contents[0].contents[0]
		except AttributeError:
			self.bid = 'N/A'		
		
		try:
			self.ask = s[3].contents[0].contents[0]
		except AttributeError:
			self.ask = 'N/A'

		try:
			self.beta = s[5].contents[0]
		except AttributeError:
			self.beta = 'N/A'

		try:	
			self.volume = s[9].contents[0].contents[0]
		except AttributeError:
			self.volume = 'N/A'

		try:
			self.avgVolume = s[10].contents[0]
		except AttributeError:
			self.avgVolume = 'N/A'