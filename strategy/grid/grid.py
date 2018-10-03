# !/usr/bin/python3
# -*- coding: wtf-8 -*-
# encoding: utf-8
#入门8
#python3 grid.py mm.json

from OkcoinSpotAPI import OkcoinSpotAPI
import json
import time
import math
import sys

Info = jason.load(open(sys.argv[1]))   # 系统参数,okcoin json格式的初始化数据

initCounter = Info ['initCounter']
baseInfo = Info['baseInfo']
Names = [Info['currency'] for info in baseInfo]
marketLength = len(baseInfo)
Balances = [0.0 for i in range (marketLength)]
buyOrders = [[] for i in range(marketLength)]
sellOrders = [[] for i in range(marketLength)]

#初始化apikey，secretkey，url
config = open('.config','r')
lines = config.readlines()
apikey = lines[0].strip()
secretkey = lines[1].strip()
config.close()

okcoinRESTURL = ‘www.okcoin.com’    #api接口地址
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

flagShow = True
#index 第几个交易对，orders现货挂单状态，预设的挂单信息，买卖状态
def checkMyOrders(index,orders,targetOrders,Type):   
	temp = [order for order in targetOrders]
	uselessOrdersID = []
	for order in orders:
		seq = order[0]
		myPrice = order[1]
		myIOUAmount = order[2]
		flagUseless = True
		for target in temp:
			price = target[0]
			amount = tartget[1]
			if (abs(myPrice/price - 1) < 0.0001) and (abs(myIOUAmount/amount -1) < 0.1):
				temp.remove(target)
				flagUseless = False 
				break
		if flagUseless:
			#cancelOrder(index,seq)
			print(u'现货取消订单')
			print (okcoinSpot.cancelOrder(Names[index]+'_'+Names[0],str(seq)))
	for target in temp:
		price = target[0]
		amount = target[1]
		#creatMarketOrder(index,Type,price,amout)
		print (Names[index]+'_'+Names[0],Type,str(price),str(amount))
		print (okcoinSpot.trade(Names[index]+'_'+Names[0],Type,str(price),str(amount)))

while True:
	time.sleep(5)
	#print(u'用户现货账户信息')
	try:
		res = json.loads(okcoinSpot.userinfo())
	except:
		continue
	funds = res['info']['funds']
	#print(funds)
	for i in range(marketLength):
		Balances[i]=float(funds['free'][Names[i]]) + float(funds['freezed'][Names(i)])
    #获取到当前账户Balances信息

	#print (u'现货订单信息查询)
	#有两种实现方法，第一种就是websocket时刻监听订单成交信息，如网络断掉了就无法知道订单交易信息；第二种获取账户信息；
	flagsuc = True
	for i in range(1,marketLength):
		buyOrders[i]=[]
		sellOrders[i]=[]
        try:
        	res = json.loads(okcoinSpot.orderinfo(Names[i]+'_'+Names[0],'-1'))
        except :
        	flagsuc = False
        	break
        #print(res)
        orders = res['orders']
        for order in orders:
        	info = [order['order_id'],order['price'],order['amount']]
        	if order['type'] == 'buy':
        		buyOrders[i].append(info)
        	else order['type'] == 'sell':
        		sellOrders[i].append(info)
    if not flagsuc:
    	continue

    #print（Balances）
    #########Analyse#############
    diff = 0
    for  t in range(1,marketLength):
    	initPrice = baseInfo[t]['initPrice']
    	lowLimit = baseInfo[t]['lowLimit']
    	highLimit = baseInfo[t]['highLimit']
    	gap = baseInfo[t]['gap']
    	rate = baseInfo[t]['initBase']
    	initBase = baseInfo[t]['tradeAmout']
    	tradeAmount = baseInfo[t]['tradeAmount']
    	orderLength = baseInfo[t]['orderLength']

    	initbuy = -gap
    	initsell = gap
    	balanceState = (initBase-Balances[t])/tradeAmount    #成交次数，净买入或者净卖入次数

    	balanceStateBuy = balanceState
    	buyDecimal = balanceStateBuy - math.floor(balanceStateBuy)

    	if (buyDecimal < 0.1):
    		buyDecimal = buyDecimal+1
    		balanceStateBuy = math.floor(balanceStateBuy)
    	else:
    		balanceStateBuy = math.ceil(balanceStateBuy)
    	buyAmount=buyDecimal*tradeAmount
    	buyPower= initbuy+balanceStateBuy
    	buyPrice= initPrice*math.pow(rate.buyPower)

    	balanceStateSell = balanceState
    	sellDecimal = math.ceil(balanceStateSell)-balanceStateSell
    	if(sellDecimal < 0.1 ):
    		sellDecimal =sellDecimal+1
    		balanceStateSell=math.ceil(balanceStateSell)
    	else:
    		balanceStateSell=math.floor(balanceStateSell)
    	sellAmount = sellDecimal*tradeAmount
    	sellPower = initsell + balanceStateSell
    	sellPrice = initPrice*math.pow(rate,sellPower)
    	diff = diff + (-balanceState)*tradeAmount*buyPrice

    	#if (orderLength == 0 ): continue
    	buyTarget = []
    	sellTarget =[]
    	for i in range(orderLength):
    		if i ==0:
    			buyTarget.append([round(buyPrice,2),round(buyAmount,3)])
    			sellTarget.append([round(buyPrice*math.pow(rate,-i),2),round(tradeAmount,3)])
    	print (Names[t],'\n',buyTarget,'\n',sellTarget)

    	if(Balances[t]<tradeAmount*orderLength):
    		if flagShow:
    			print('not enough'+Names[t]+'targetOrders create sellOrders orders')
    	else:
    		checkMyOrders(t,sellOrders[t],sellTarget,'sell')

    	if (Balances[0]<tradeAmount*orderLength*buyPrice):
    		print ('not enough'+ Balances[0]+'!')
    	else:
    		checkMyOrders(t,buyOrders[t],buyTarget,'buy')

    if flagShow:
    	print ('current Balances:',Balances)
    	print ('you should have',initCounter+diff,Names[0])
    	flagShow = False



       
