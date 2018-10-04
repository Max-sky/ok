import ccxt
import pprint import pprint
import time

huobipro = ccxt.huobipro();
okex = ccxt.okex();
pair = 'ETH/BTC'
# exchange = huobipro.load_markets();
#print huobipro.symbols
# print huobipro.fetch_order_book(pair)
# print okex.fetch_order_book(pair)

limit = 3

while True:
	
      DATA = [huobipro.fetch_order_book(pair,limit),okex.fetch_order_book(pair,limit)]
      bids=[]
      asks=[]
      for data in DATA:
	      bids.append(data['bids'][0])
	      asks.append(data['asks'][0])

      # print bids,asks
      print 'sell in huobipro and buy in okex',(1.*bids[0][0]/asks[1][0]-1.)*100,"%"
      time.sleep(1)
