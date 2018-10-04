import ccxt
import pprint import pprint
import time
from numpy import  NaN

baseCurrency = 'BTC'
counterPart  'ETH'
pair = counterPart+'/' + baseCurrency
limit = 3
highLimit = 0.2
lowLimit = 0.001
Exchanges=[]   #存交易所信息
Names = []     #存交易所名字

#快速调试
length = 0
lengthLimit = 10
#调试

# print (ccxt.exchanges)

for i in ccx.exchanges:
	exchange = getattr(ccxt,i)
	try :                             #  当ccxt无法获得交易所数据做异常处理
		exchanges.fetch_order_book(pair,limit)
        Exchanges.append(exchange)
        Names.append(str(i))
        
        #快速调试
        length++
        if  length  > lengthLimit:
        	break
		# 快速测试
	except:
		 pass

gatewaysLength = len(Exchanges)
 
MES = [{} for i in Exchanges]    #交易所信息
bids = [NaN for i in Exchanges]
bidsVolum = [NaN for i in Exchanges]
asks = [NaN for i in Exchanges]
asksVolum = [NaN for i in Exchanges]

for i in  range(gatewaysLength)
     try :
     	mes = Exchanges[i].fetch_order_book(pair,limit)
     	MES[i] = mes
     	bidPrice = mes['bids'][0][0]       #[价格]【数量】
     	askPrice = mes['asks'][0][0]
     	if bidPrice < highLimit and bidPrice >lowLimit:   #处理ask和bid的数据异常
     	     bids[i] = bidPrice
     	     bidsVolum[i] = mes['bids'][0][1]
     	          	     
        else: 
             bids[i] = NaN
     	     bidsVolum[i] = NaN
     	     
        if askPrice <highLimit and askPrice >lowLimit:
             asks[i] = askPrice
             asksVolum[i] = mes['asks'][0][1]
        else:
        	 asks[i] = NaN
     	     asksVolum[i] = NaN

     except:
     	MES[i] = NaN
     	bids[i] = NaN
     	asks[i] = NaN
     	print (Names[i] + ' has a error')

print (bids)
print (asks)

higestBid = max(bids)
lowestAsk = min(asks)
sellIndex = bids.index(higestBid)       #最高的卖单
buyIndex = asks.index(lowestAsk)       #最低的买单
profit = higestBid/lowestAsk - 1.
tradeVolum = min([bidsVolum[sellIndex],[asksVolum[buyIndex]]])


print ('there are' + str(gatewaysLength) + 'exchanges')
print ('buy at ' + Names[buyIndex] + 'sell at ' + Names[sellIndex])
print ('profit: ' + str(profit) +'  volume :'+str(tradeVolum))

