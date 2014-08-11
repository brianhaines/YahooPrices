'''This will open a connection to the yahoo streamerapi server and 
print the data dict to the terminal.'''

import requests
from ast import literal_eval
from datetime import datetime
import sqlite3



def stringGen(Chars,Char,numChars):
	'''Take in one character at a time and add it to the end of the string
	Chars while dropping the first character of the Chars string.
	eg: Chars='hart' Char='s' numChars=4 => 'arts'.'''

	charList = []
	newList=[]

	if len(Chars)==numChars:
		charList = list(Chars)
		for i in range(numChars-1):
			newList.append(charList[i+1])
		newList.append(Char)
		return(''.join(newList))
	else:
		charList = list(Chars)
		charList.append(Char)
		return(''.join(charList))

def insertQuotes(strIn, field):
	'''Take an almost dict, find one of the keys, add single quotes around the key
	and return a dict using ast'''
	l=[]	
	for s in field:
		p = strIn.find(s)
		if  p > 0:
			l = list(strIn)
			l.insert(p,"'")
			l.insert(p+4,"'")
			strIn = ''.join(l)	
	d = literal_eval(strIn)
	return d

def assignVals(varDict):
	global LastPrice,bid,ask,bidSize,askSize 
	#Start with all names == None. Will assign values to those in the dict
	(LastPrice,bid,ask,bidSize,askSize) = (None,None,None,None,None)
	#LastPrice=l84,bid=b00,ask=a00,bidSize=b60,askSize=a50
	for dKey in varDict:
		if dKey == 'l84':
			LastPrice = varDict['l84']
		elif dKey == 'b00':
			bid = varDict['b00']
		elif dKey == 'a00':
			ask = varDict['a00']
		elif dKey == 'b60':
			bidSize = varDict['b60']
		elif dKey == 'a50':
			askSize = varDict['a50']

def main():
	#Initate connection to the Yahoo server
	tickers = ('GE','MSFT','BP','JPM','BAC','XOM','CVX','UTX','GOOG','C','NFLX','AMZN')
	fields = ('l84','a00','b00','a50','b60')
	fieldsStr = ','.join(fields)
	tickerStr = ','.join(tickers)
	url = 'http://streamerapi.finance.yahoo.com/streamer/1.0?s=%s&k=%s&r=0&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb' % (tickerStr,fieldsStr)
	r = requests.get(url, stream=True)

	tagB = '' #Recepticle for characters
	tagE = '' #Recepticle for characters
	beginQ = '<script>try{parent.yfs_u1f({' #Leading character tag
	endQ = ');}catch(e){}</script>' #Trailing character tag
	#<script>try{parent.yfs_u1f({"MSFT":{}});}catch(e){}</script>
	inState = False #Start the machin in the Not Recording state
	dataCollect = ''

	#Fire up an SQLite3 database
	db = None
	#create or open existing db
	db = sqlite3.connect('livePriceDB.db')
	# Get a cursor object
	cursor = db.cursor()
	#This is an SQL string to create a table in the database.
	cursor.execute('''CREATE TABLE IF NOT EXISTS livePrices(tickTime TEXT unique PRIMARY KEY, Ticker TEXT, qDate DATE, qTime TEXT, LastPrice REAL, bid REAL, ask REAL, bidSize INTEGER, askSize INTEGER)''')

	#Stoping time
	fourPMstop = datetime.now().replace(hour=16, minute=0, second=0,microsecond=50000)

	#This for loops continuously
	for char in r.iter_content():
		

		c = char.decode()
		tagB = stringGen(tagB,c,28)
		tagE = stringGen(tagE,c,22)

		if tagB == beginQ:
			#Transition current state to Recording
			inState = True
		if tagE == endQ:
			#Transition current state to Not Recording
			#Remove end tag from recorded string
			t = datetime.now()
			notRecTime = (t.date().isoformat(),t.time().isoformat())
			s = dataCollect[:len(dataCollect)-(len(endQ)-1)]
			#Sometimes an empty string is returned, this skips them
			if len(s)>0:
				retDict = insertQuotes(s,fields)
				retDict['timeStamp'] = notRecTime 
				#You now have dict with ticker:value and timestamp:(date,time)	
				#Insert those values into the DB
				for tkey in retDict.keys(): #can I call a 'any key but this one' operator to replace the loop?
					if tkey != 'timeStamp':
						ticker = tkey
				qTime = retDict['timeStamp'][1]		
				qDate = retDict['timeStamp'][0]
				tickTime = str.join('_',(ticker,qDate,qTime))
				
				#'assignVals' assigns vals to global variables depending on what is 
				# present in the returned dict (retDict)
				assignVals(retDict[ticker])
				print(ticker,qTime,LastPrice,bid,ask,bidSize,askSize)
				
				cursor.execute('''INSERT INTO livePrices(tickTime, Ticker, qDate, qTime, LastPrice, bid, ask, bidSize, askSize) VALUES(?,?,?,?,?,?,?,?,?)''', (tickTime, ticker, qDate, qTime, LastPrice, bid,ask,bidSize,askSize))
				db.commit()

			dataCollect = '' #Reset the collection
			inState = False #Not Recoding state
			
			#This ends the session at 4pm
			if datetime.now()>fourPMstop:
				print("Quitting time!")
				break	

		#When current state is Record, record all the characters that come in.
		if inState == True:
			dataCollect = dataCollect + c
	db.close

if __name__ == '__main__':
	main()