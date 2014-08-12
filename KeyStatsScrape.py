from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime


class keyStats():
	'''This class will scape all data off of the 
	key stats page for a given ticker.'''

	def __init__(self, tkr):
		url = 'http://finance.yahoo.com/q/ks?s=%s+Key+Statistics' %tkr
		urlProf = 'http://finance.yahoo.com/q/pr?s=%s+Profile' %tkr
		self.ticker = tkr

		try:
			count = 1
			ksPage = urlopen(url)
			profPage = urlopen(urlProf)
		except Exception:
			print("Problem with connection to Yahoo. Trying again")
			sleep(.25)
			ksPage = urlopen(url)
			profPage = urlopen(urlProf)
			if count > 4:
				print("No connection to the internet")
				raise SystemExit


		#Turn the page into soup
		soup = BeautifulSoup(ksPage)
		soupPro = BeautifulSoup(profPage)


		#Pull data from price table
		s = soup.find_all("td", class_="yfnc_tabledata1")
		Pro = soupPro.find_all("td", class_="yfnc_tabledata1")
		Pro2 = soupPro.find_all("div", class_="title")

		try:
			self.index = Pro[0].contents[0]
		except AttributeError:
			self.index = None

		try:
			self.sector = Pro[1].contents[0].contents[0]
		except AttributeError:
			self.sector = None

		try:
			self.industry = Pro[2].contents[0].contents[0]
		except AttributeError:
			self.industry = None

		try:
			self.employees = Pro[3].contents[0]
		except AttributeError:
			self.employees = None

		try:
			self.companyName = Pro2[0].contents[0].contents[0].split(' (')[0]
		except AttributeError:
			self.companyName = None

		try:
			self.marketCap = s[0].contents[0].contents[0] #parse out the B
		except AttributeError:
			self.marketCap = None

		try:
			self.enterpriseValue = s[1].contents[0] #parse out the B
		except AttributeError:
			self.enterpriseValue = None

		try:
			self.trailPE = s[2].contents[0]
		except AttributeError:
			self.trailPE = None

		try:
			self.fwdPE = s[3].contents[0]
		except AttributeError:
			self.fwdPE = None

		try:
			self.peg = s[4].contents[0]	
		except AttributeError:
			self.peg = None

		try: 
			self.pSales = s[5].contents[0]
		except AttributeError:
			self.pSales = None

		try:
			pBook = s[6].contents[0]
		except AttributeError:
			pBook = None

		try: 
			self.EVrevenue = s[7].contents[0]
		except AttributeError:
			self.EVrevenue = None

		try: 
			self.EVebitda = s[8].contents[0]
		except AttributeError:
			self.EVebitda = None

		try: 
			self.EVebitda = s[8].contents[0]
		except AttributeError:
			self.EVebitda = None

		try:
			self.profitMarg = s[11].contents[0]
		except AttributeError:
			self.profitMarg = None

		try:
			self.operateMarg = s[12].contents[0]
		except AttributeError:
			self.operateMarg = None

		try:
			self.retAssets = s[13].contents[0]
		except AttributeError:
			self.retAssets = None

		try:
			self.retEquity = s[14].contents[0]
		except AttributeError:
			self.retEquity = None

		try:
			self.revenue = s[15].contents[0] #parse out the B
		except AttributeError:
			self.revenue = None

		try:
			self.revenuePS = s[16].contents[0] 
		except AttributeError:
			self.revenuePS = None

		try:
			self.qRevGrowth = s[17].contents[0] #parse out the B
		except AttributeError:
			self.qRevGrowth = None

		try:
			self.grossProfit = s[18].contents[0] #parse out the B
		except AttributeError:
			self.grossProfit = None

		try:
			self.EBITDA = s[19].contents[0] #parse out the B
		except AttributeError:
			self.EBITDA = None

		try:
			self.netIncSH = s[20].contents[0] #parse out the B
		except AttributeError:
			self.netIncSH = None

		try:
			self.EPS = s[21].contents[0]
		except AttributeError:
			self.EPS = None

		try:
			self.qEarnGrth = s[22].contents[0]
		except AttributeError:
			self.qEarnGrth = None

		try:
			self.cash = s[23].contents[0]
		except AttributeError:
			self.cash = None

		try:
			self.cashPS = s[24].contents[0]
		except AttributeError:
			self.cashPS = None

		try:
			self.totDebt = s[25].contents[0]
		except AttributeError:
			self.totDebt = None

		try:
			self.totDebtEquity = s[26].contents[0]
		except AttributeError:
			self.totDebtEquity = None

		try:
			self.currRatio = s[27].contents[0]
		except AttributeError:
			self.currRatio = None

		try:
			self.bookValPS = s[28].contents[0]
		except AttributeError:
			self.bookValPS = None

		try:
			self.opCashFlow = s[29].contents[0]
		except AttributeError:
			self.opCashFlow = None

		try:
			self.beta = s[31].contents[0]
		except AttributeError:
			self.beta = None

		try:
			self.d52week = s[32].contents[0]
		except AttributeError:
			self.d52week = None

		try:
			self.sp52week = s[33].contents[0]
		except AttributeError:
			self.sp52week = None

		try:
			self.hi52week = s[34].contents[0]
		except AttributeError:
			self.hi52week = None

		try:
			self.lo52week = s[35].contents[0]
		except AttributeError:
			self.lo52week = None

		try:
			self.ma50day = s[36].contents[0]
		except AttributeError:
			self.ma50day = None

		try:
			self.ma200day = s[37].contents[0]
		except AttributeError:
			self.ma200day = None

		try:
			self.avgVol30d = s[38].contents[0]
		except AttributeError:
			self.avgVol30d = None

		try:
			self.avgVol10d = s[39].contents[0]
		except AttributeError:
			self.avgVol10d = None

		try:
			self.shrsShrt = s[44].contents[0]
		except AttributeError:
			self.shrsShrt = None

		try:
			self.shrsShrtNew = s[47].contents[0]
		except AttributeError:
			self.shrsShrtNew = None

		try:
			self.shortRatio = s[45].contents[0]
		except AttributeError:
			self.shortRatio = None

		try:
			self.floatShort  = s[46].contents[0]
		except AttributeError:
			self.floatShort = None

		try:
			self.fwdDivPS  = s[48].contents[0]
		except AttributeError:
			self.fwdDivPS = None

		try:
			self.fwdDivYld  = s[49].contents[0]
		except AttributeError:
			self.fwdDivYld = None

		try:
			self.avgDivYield  = s[52].contents[0]
		except AttributeError:
			self.avgDivYield = None

		try:
			self.payoutRatio  = s[53].contents[0]
		except AttributeError:
			self.payoutRatio = None


		#System time of the request
		t = datetime.now()
		tDate = t.strftime("%Y-%m-%d")
		tTime = t.strftime("-%H-%M-%S")

				