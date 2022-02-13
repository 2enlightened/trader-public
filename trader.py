from binance.client import Client

# init
api_key_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'
api_secret_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'

#api_key_Coinbase = '1qC6BQIj2zpN3Eou'
#api_secret_Coinbase = 'TJghP58m2smAYXim5G4miXCF3rG2pxms'

client = Client(api_key_Binance, api_secret_Binance)
t = TRUE
## main
while t:
    ## get lates data Binance
    btc_price = client.get_symbol_ticker(symbol='BTCUSDT')
    eth_price = client.get_symbol_ticker(symbol='ETHUSDT')
    btc = btc_price['price']
    eth = eth_price['price']
# print just the price
    print("BTC: ",btc, "ETH: ",eth)
