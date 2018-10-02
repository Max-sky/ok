import ccxt
huobipro=ccxt.huobipro()
exchange=huobipro.load_markets()
huobipro.symbols    #火币交易对

huobipro.fetch_order_book('ETH/BTC')
