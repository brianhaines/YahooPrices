'''
This class will return price information from Finance.Yahoo.com
for any given equity ticker using BeautifulSoup4
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

class YahooPrice():
	"""Once initiated this class will reach out to yahoo finance and 
	request a quote page using the given ticker"""

	def __init__(self, tkr):
		url = 'http://finance.yahoo.com/q?s=%s' %tkr

		try:
			tickerPage = urlopen(url)
		except Exception, e:
			raise

		#Turn the page into soup
		soup = BeautifulSoup(tickerPage)

		#Find the Last Price value in the soup
		for y in soup.find_all("span", class_="time_rtq_ticker"):
			x = y.contents[0].contents
		self.LastPrice = x[0]