from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime


# class keyStats():
# 	'''This class will scape all data off of the 
# 	key stats page for a given ticker.'''

# 	def __init__(self, tkr):
tkr = "NFLX"
url = 'http://finance.yahoo.com/q/ks?s=%s+Key+Statistics' %tkr
ticker = tkr

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

#Pull data from price table
s = soup.find_all("td", class_="yfnc_tabledata1")


try:
	marketCap = s[0].contents[0].contents[0] #parse out the B
except AttributeError:
	marketCap = None

try:
	enterpriseValue = s[1].contents[0] #parse out the B
except AttributeError:
	enterpriseValue = None

try:
	trailPE = s[2].contents[0]
except AttributeError:
	trailPE = None

try:
	fwdPE = s[3].contents[0]
except AttributeError:
	fwdPE = None

try:
	peg = s[4].contents[0]	
except AttributeError:
	peg = None

try: 
	pSales = s[5].contents[0]
except AttributeError:
	pSales = None

try:
	pBook = s[6].contents[0]
except AttributeError:
	pBook = None

try: 
	EVrevenue = s[7].contents[0]
except AttributeError:
	EVrevenue = None

try: 
	EVebitda = s[8].contents[0]
except AttributeError:
	EVebitda = None

try: 
	EVebitda = s[8].contents[0]
 except AttributeError:
 	EVebitda = None

try:
	profitMarg = s[11].contents[0]
except AttributeError:
	profitMarg = None

try:
	operateMarg = s[12].contents[0]
except AttributeError:
	operateMarg = None

try:
	retAssets = s[13].contents[0]
except AttributeError:
	retAssets = None

 try:
	retEquity = s[14].contents[0]
except AttributeError:
	retEquity = None

 try:
	revenue = s[15].contents[0] #parse out the B
except AttributeError:
	revenue = None

 try:
	revenuePS = s[16].contents[0] 
except AttributeError:
	revenuePS = None

try:
	qRevGrowth = s[17].contents[0] #parse out the B
except AttributeError:
	qRevGrowth = None

try:
	grossProfit = s[18].contents[0] #parse out the B
except AttributeError:
	grossProfit = None

try:
	EBITDA = s[19].contents[0] #parse out the B
except AttributeError:
	EBITDA = None

try:
	netIncSH = s[20].contents[0] #parse out the B
except AttributeError:
	netIncSH = None

try:
	EPS = s[21].contents[0]
except AttributeError:
	EPS = None

try:
	qEarnGth = s[22].contents[0]
except AttributeError:
	qEarnGth = None

try:
	cash = s[23].contents[0]
except AttributeError:
	cash = None

try:
	cashPS = s[24].contents[0]
except AttributeError:
	cashPS = None

try:
	totDebt = s[25].contents[0]
except AttributeError:
	totDebt = None

try:
	totDebtEquity = s[26].contents[0]
except AttributeError:
	totDebtEquity = None

try:
	currRatio = s[27].contents[0]
except AttributeError:
	currRatio = None

try:
	bookValPS = s[28].contents[0]
except AttributeError:
	bookValPS = None

try:
	opCashFlow = s[29].contents[0]
except AttributeError:
	opCashFlow = None

try:
	beta = s[31].contents[0]
except AttributeError:
	beta = None

try:
	d52week = s[32].contents[0]
except AttributeError:
	d52week = None

try:
	sp52week = s[33].contents[0]
except AttributeError:
	sp52week = None

try:
	hi52week = s[34].contents[0]
except AttributeError:
	hi52week = None

try:
	lo52week = s[35].contents[0]
except AttributeError:
	lo52week = None

try:
	ma50day = s[36].contents[0]
except AttributeError:
	ma50day = None

try:
	ma200day = s[37].contents[0]
except AttributeError:
	ma200day = None

try:
	avgVol30d = s[38].contents[0]
except AttributeError:
	avgVol30d = None

try:
	avgVol10d = s[39].contents[0]
except AttributeError:
	avgVol10d = None

try:
	shrsShrt = s[44].contents[0]
except AttributeError:
	shrsShrt = None

try:
	shrsShrtNew = s[47].contents[0]
except AttributeError:
	shrsShrtNew = None

try:
	shortRatio = s[45].contents[0]
except AttributeError:
	shortRatio = None

try:
	floatShort  = s[46].contents[0]
except AttributeError:
	floatShort = None

try:
	fwdDivPS  = s[48].contents[0]
except AttributeError:
	fwdDivPS = None

try:
	fwdDivYld  = s[49].contents[0]
except AttributeError:
	fwdDivYld = None

try:
	avgDivYield  = s[52].contents[0]
except AttributeError:
	avgDivYield = None

try:
	payoutRatio  = s[53].contents[0]
except AttributeError:
	payoutRatio = None


#System time of the request
sysTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

		