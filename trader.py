from binance.client import Client
import pandas as pd
import btalib
import numpy as np
import time

def getminutedata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Opent','High','Low','Close','Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit="ms")
    frame = frame.astype(float)
    return frame


# binance api
api_key_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'
api_secret_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'

#api_key_Coinbase = '1qC6BQIj2zpN3Eou'
#api_secret_Coinbase = 'TJghP58m2smAYXim5G4miXCF3rG2pxms'

client = Client(api_key_Binance, api_secret_Binance)
print('\x1bc')
pair = input("Zadej pair napr BTCUSDT: ")

t = True
## main
while t:
    ##data Binance
    data = client.get_ticker(symbol=pair)
    price = data['lastPrice']
    avg_price = data['weightedAvgPrice']
    percent = float(data['priceChangePercent'])
    df = getminutedata(pair,'1m','100')
    rsi = btalib.rsi(df, period=14)
    df = df.join([rsi.df])
    RSI = rsi.df.rsi[-1]
    data = pd.DataFrame({'symbol': pair, 'price': data['lastPrice'], 'AVG': data['weightedAvgPrice'],'priceChange': data['priceChange'], '%': percent, 'RSI': RSI}, index=[0])
    
    if percent >= 0:
        print("\033[32m {} \033[0m".format(data))
    else:
        print("\033[31m {} \033[40m".format(data))  
