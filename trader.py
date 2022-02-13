from binance.client import Client

# init
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)
i = 0
## main
while i <= 10:
# get latest price from Binance API
    btc_price = client.get_symbol_ticker(symbol='BTCUSDT')
# print full output (dictionary)
    print(btc_price)
# print just the price
    print(btc_price['price'])
    i+=1
