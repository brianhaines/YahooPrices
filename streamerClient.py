import requests

#r = requests.get('http://streamerapi.finance.yahoo.com/streamer/1.0?s=TSLA,MSFT&k=l10&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb', stream=True)
r = requests.get('http://streamerapi.finance.yahoo.com/streamer/1.0?s=MSFT&k=l10,a00,a50,b00,b60,c63,g53,h53,j10,l84,p20,p43,t53,v53&j=c63,j10,l84,p20,p43,t53&r=0&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb', stream=True)
#curl -s -o - -N 'http://streamerapi.finance.yahoo.com/streamer/1.0?s=MSFT&k=l10,a00,a50,b00,b60,c63,g53,h53,j10,l84,p20,p43,t53,v53&j=c63,j10,l84,p20,p43,t53&r=0&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb'

tag = ''
count =0
for char in r.iter_content():
	tag = tag + char.decode()
	count += 1
	if count > 500:
		print(tag)
		tag = ''
		count = 0