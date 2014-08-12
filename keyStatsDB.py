import sqlite3
from KeyStatsScrape import keyStats
from datetime import datetime
import time
from sys import exc_info

def keyStatsFunc(tkrs):
	'''This function receives the list of tickers from streamerClient and loops over it
	until the key stats have all been retreived from yahoo and inserted into the database'''

	#Fire up an SQLite3 database
	db = None
	#create or open existing db
	db = sqlite3.connect('livePriceDBtest.db')
	# Get a cursor object
	cursor = db.cursor()
	#This is an SQL string to create a table in the database.
	cursor.execute('''CREATE TABLE IF NOT EXISTS keyStats(tickerDate TEXT unique PRIMARY KEY,
					avgDivYield REAL,avgVol10d INTEGER,avgVol30d INTEGER,beta REAL,bookValPS REAL,
					cash TEXT,cashPS REAL,companyName TEXT,currRatio REAL,d52week REAL,
					employees INTEGER,enterpriseValue INTEGER,floatShort REAL,fwdDivPS REAL,
					fwdDivYld REAL,fwdPE REAL,grossProfit INTEGER,hi52week REAL,indext TEXT,
					industry TEXT,lo52week REAL,ma200day REAL,ma50day REAL,marketCap REAL,
					netIncSH REAL,opCashFlow REAL,operateMarg REAL,payoutRatio REAL,peg REAL,
					profitMarg REAL,pSales REAL,qEarnGrth REAL,qRevGrowth REAL,retAssets REAL,
					retEquity REAL, revenue REAL,revenuePS REAL,sector TEXT,shortRatio REAL,
					shrsShrt REAL,shrsShrtNew REAL,sp52week REAL,ticker TEXT,totDebt REAL,
					totDebtEquity REAL,trailPE REAL)''')
	#db.commit

	for t in tkrs:
		try:
			ks = keyStats(t)
		except urllib.error.URLError as err:
			print("__URLError___:", err)
			time.sleep(3)
		except:
			print("___Unexpected___ error:", exc_info())
			time.sleep(3)

		#Set the variable values here
		#tickerDate first
		tickerDate = ks.ticker + '_' + ks.tDate
		cursor.execute('''INSERT OR IGNORE INTO keyStats(tickerDate,avgDivYield,avgVol10d,
						avgVol30d ,beta,bookValPS,cash,cashPS,companyName,currRatio,d52week,employees,
						enterpriseValue ,floatShort,fwdDivPS,fwdDivYld,fwdPE,grossProfit ,hi52week,indext,
						industry,lo52week,ma200day,ma50day,marketCap,netIncSH,opCashFlow,operateMarg,
						payoutRatio,peg,profitMarg,pSales,qEarnGrth,qRevGrowth,retAssets,retEquity, 
						revenue,revenuePS,sector,shortRatio,shrsShrt,shrsShrtNew,sp52week,ticker,totDebt,
						totDebtEquity,trailPE) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
						?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (tickerDate,ks.avgDivYield,ks.avgVol10d,
						ks.avgVol30d,ks.beta,ks.bookValPS,ks.cash,ks.cashPS,ks.companyName,ks.currRatio,
						ks.d52week,ks.employees,ks.enterpriseValue,ks.floatShort,ks.fwdDivPS,ks.fwdDivYld,
						ks.fwdPE,ks.grossProfit,ks.hi52week,ks.indext,ks.industry,ks.lo52week,ks.ma200day,
						ks.ma50day,ks.marketCap,ks.netIncSH,ks.opCashFlow,ks.operateMarg,ks.payoutRatio,
						ks.peg,ks.profitMarg,ks.pSales,ks.qEarnGrth,ks.qRevGrowth,ks.retAssets,ks.retEquity,
						ks.revenue,ks.revenuePS,ks.sector,ks.shortRatio,ks.shrsShrt,ks.shrsShrtNew,ks.sp52week,
						ks.ticker,ks.totDebt,ks.totDebtEquity,ks.trailPE))
		db.commit()
		db.close		

		print(ks.companyName)
		print(ks.pSales, ks.avgVol30d)

		db.commit()
		db.close
