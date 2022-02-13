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
    price = data['lastPrice']
    avg_price = data['weightedAvgPrice']
    data = pd.DataFrame({'symbol': pair, 'price': data['lastPrice'], 'AVG': data['weightedAvgPrice'],'priceChange': data['priceChange'], '%': data['priceChangePercent'], 'LOW': data['lowPrice'], 'HIGH': data['highPrice'], 'VOLUME': data['volume'] }, index=[0])
    if price > avg_price:
        print("\033[32m {} \033[0m".format(data))
    else:
        print("\033[31m {} \033[40m".format(data))  
