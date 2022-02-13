from binance.client import Client

# binance api
api_key_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'
api_secret_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'

#api_key_Coinbase = '1qC6BQIj2zpN3Eou'
#api_secret_Coinbase = 'TJghP58m2smAYXim5G4miXCF3rG2pxms'

client = Client(api_key_Binance, api_secret_Binance)
pair = input("Zadej pair napr BTCUSDT: ")
t = True
## main
while t:
    ##data Binance
    data = client.get_ticker(symbol=pair)
    #cena
    price = client.get_symbol_ticker(symbol=pair)
    price = price['price']
    #průměrná cena za 24h
    avg_price = client.get_avg_price(symbol=pair)
    avg_price = avg_price['price']
    #objem trhu
    volume = data['volume']
    #nejvyšší hodnota za 24 hodin
    high = data['highPrice']
    #nejnižší hodnota za 24 hodin
    low = data['lowPrice']
    #% změna 24h
    percent = data['priceChangePercent']
    #změna ceny 24h
    changePrice = data['priceChange']

    #tisk barveně podle vetší nebo menší než 24h průměr
    if price > avg_price:
        print("\033[32m {}: {} AVG: {} percent: {} changePrice: {} high: {} low: {} volume: {}\033[0m".format(pair,price,avg_price,percent,changePrice,high,low,volume))
    else:
        print("\033[31m {}: {} AVG: {} percent: {} changePrice: {} high: {} low: {} volume: {}\033[40m".format(pair,price,avg_price,percent,changePrice,high,low,volume))
    
