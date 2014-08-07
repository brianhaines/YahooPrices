import requests
'''This will open a connection to the yahoo streamerapi server and 
print the data dict to the terminal.'''

def stringGen(Chars,Char,numChars):
	'''Take in one character at a time and add it to the end of the string
	Chars while dropping the first character of the Chars string.
	eg: Chars='hart' Char='s' => 'arts'.'''

	charList = []
	newList=[]

	if numChars==8:
		if len(Chars)==8:
			charList = list(Chars)
			for i in range(numChars-1):
				newList.append(charList[i+1])
			newList.append(Char)
			return(''.join(newList))
		else:
			charList = list(Chars)
			charList.append(Char)
			return(''.join(charList))
	elif numChars==9:
		if len(Chars)==9:
			charList = list(Chars)
			for i in range(numChars-1):
				newList.append(charList[i+1])
			newList.append(Char)
			return(''.join(newList))
		else:
			charList = list(Chars)
			charList.append(Char)
		return(''.join(charList))

def main():
	r = requests.get('http://streamerapi.finance.yahoo.com/streamer/1.0?s=MSFT&k=l84&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb', stream=True)

	tagB = ''
	tagE = ''
	count =0
	beginQ = '<script>'
	endQ = '</script>'
	inState = False
	dataCollect = ''


	for char in r.iter_content():
		c = char.decode()
		tagB = stringGen(tagB,c,8)
		tagE = stringGen(tagE,c,9)
		
		print(tagB)
		print(tagE)

		if tagB == beginQ:
			print('___',tagB)
			inState = True
		if tagE == endQ:
			print(dataCollect[:len(dataCollect)-8])
			dataCollect = ''
			inState = False

		if inState == True:
			dataCollect = dataCollect + c		


if __name__ == '__main__':
	main()