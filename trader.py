import os

from binance.client import Client

# init
api_key = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'
api_secret = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'
client = Client(api_key, api_secret)

## main

# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol='BTCUSDT')
# print full output (dictionary)
print(btc_price)
# print just the price
print(btc_price['price'])