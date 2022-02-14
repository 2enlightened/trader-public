from binance.client import Client
import pandas as pd
import btalib
import numpy as np


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
pair = 'BTCUSDT'
client = Client(api_key_Binance, api_secret_Binance)
df = getminutedata(pair,'1m','100')
print(df)
