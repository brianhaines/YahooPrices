'''
Run a loop that calls YahooPrice on a list of tickers
'''

from yahooPrice import YahooPrice
from datetime import datetime
import time
import sqlite3
import sys

tList = ['msft','tsla','ge','f','bp']

stop = time.time()+600
fourPMstop = datetime.now().replace(hour=16, minute=00, second=0,microsecond=5000)


while datetime.now() < fourPMstop:
	for t in tList:
		#Call the price getter for each ticker, 
		#report but pass any errors
		try:
			p = YahooPrice(t)
			print("Ticker: ", t, " At:", p.sysTime[6:],"  ", p.LastPrice)
			
			dbKey = str.join('_',(p.ticker,p.sysTime))
			db = None
			#create or open existing db
			db = sqlite3.connect('priceDB.db')
			# Get a cursor object
			cursor = db.cursor()
			#This is an SQL string to create a table in the database.
			cursor.execute('''CREATE TABLE IF NOT EXISTS prices(tickTime TEXT unique PRIMARY KEY, Ticker TEXT, Time TEXT, LastPrice REAL, bid REAL, ask REAL)''')

			#'OR IGNORE' allows the INSERT command to ignore any rows where the 'unique' constraint is violated. This occurs
			#when an attempt is made to INSERT an already existing day 
			cursor.execute('''INSERT OR IGNORE INTO prices(tickTime, Ticker, Time, LastPrice, bid, ask) VALUES(?,?,?,?,?,?)''', (dbKey,p.ticker,p.sysTime,p.LastPrice,p.bid,p.ask))
			db.commit()
			db.close
		except urllib.error.URLError as err:
			print("__URLError___:", err)
			time.sleep(3)
		except:
			print("___Unexpected___ error:", sys.exc_info())
			time.sleep(3)
	time.sleep(2)