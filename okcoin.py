from OkcoinSpotAPI import OKCoinSpot

config=open('.config')
lines=config.readlines()
print(lines)

apikey = lines[0].strip()
secretkey lines[1].strip()

okcoinRESTURL = 'www.okcoin.cn'

okcoinSpot = OKCoinSpot(okcoinRESTURL，apikey,seretkey)

print(u'用户现货账户信息')
print(okcoinSpot.userinfo())
