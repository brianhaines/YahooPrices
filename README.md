YahooPrices
===========

This Python project takes advantage of the Yahoo server that streams "real-time" prices and other financial information to the finance.yahoo.com websites. A streaming connection to this server is established using python's requests package. Also, pertinent company information is scraped off of the Key Statistics pages for all of your stocks using BeautifulSoup4. 

All data that are captured are stored in an SQLite3 database for later retrieval.

Next steps include serving the data in a method condusive to statistical analysis.

Warning! This value of this information is non-existent in the context of making short term trading decisions. There are too many uncertainties as to when Yahoo decides to push price updates to the stream.

##Why I did this

The primary goal of this project is to acumulate a source of fine grained price updates for historical and 'real-time' analysis. The SQLite3 database provides the concurrency needed to make requests during the day while new information is being written.

##How to use it

All that is required is updating the list of stock tickers to reflect your interests and perhaps updating the file name and path for the DB.

Simply call the `streamerClient.py` from the command line and watch the updates scroll up your terminal!

This requires installation of the `requests` package.

##The Future

Current goals include:

1. Making eficiency improvements to the stringGen function which is called 2x for each byte that is parsed. While it works fine currently, I know I can do better. 

2. Add multiprocessing with the goal of maintaining multiple streams from the yahoo server. More streams will increase the bandwidth for receiving updates.

3. Improving the error handling around network errors so the client will continue in the case of an interuption.


