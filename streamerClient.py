'''This will open a connection to the yahoo streamerapi server and 
print the data dict to the terminal.'''

import requests
from ast import literal_eval


def stringGen(Chars,Char,numChars):
	'''Take in one character at a time and add it to the end of the string
	Chars while dropping the first character of the Chars string.
	eg: Chars='hart' Char='s' => 'arts'.'''

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
		l = list(strIn)
		l.insert(p,"'")
		l.insert(p+4,"'")
		strIn = ''.join(l)	
	d = literal_eval(strIn)
	return d


def main():
	#Initate connection to the Yahoo server
	tickers = ('GE','MSFT','BP','OPEN','JPM','BAC')
	fields = ('l84','a00','b00')
	fieldsStr = ','.join(fields)
	tickerStr = ','.join(tickers)
	url = 'http://streamerapi.finance.yahoo.com/streamer/1.0?s=%s&k=%s&r=0&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb' % (tickerStr,fieldsStr)
	r = requests.get(url, stream=True)

	tagB = '' #Receptical for characters
	tagE = '' #Receptical for characters
	beginQ = '<script>try{parent.yfs_u1f({' #Leading character tag
	endQ = ');}catch(e){}</script>' #Trailing character tag
	inState = False #Start the machin in the Not Recording state
	dataCollect = ''

	#<script>try{parent.yfs_u1f({"MSFT":{}});}catch(e){}</script>

	for char in r.iter_content():
		c = char.decode()
		tagB = stringGen(tagB,c,28)
		tagE = stringGen(tagE,c,22)

		if tagB == beginQ:
			#Transition current state to Recording
			inState = True
		if tagE == endQ:
			#Transition current state to Not Recording
			s = dataCollect[:len(dataCollect)-(len(endQ)-1)]
			retDict = insertQuotes(s,fields)	
			# retDict = insertQuotes(insertQuotes(s,'a00'),'l84')
			for key in retDict.keys():
				print("key: %s , value: %s" % (key, retDict[key]))


			dataCollect = '' #Reset the collection
			inState = False #Not Recoding state
		#When current state is Record, record all the characters that come in.
		if inState == True:
			dataCollect = dataCollect + c		
	
if __name__ == '__main__':
	main()