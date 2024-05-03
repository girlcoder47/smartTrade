import sys
import argparse
from dateutil.parser import parse
import numpy as np
import pandas as pd
#import talib as ta
import yfinance as yf
import matplotlib.pyplot as plt
#import seaborn as sns
from datetime import date
from datetime import datetime
from datetime import timedelta

filename='data/AAPL/AAPL_HIGH_latest_data.csv'

dfStock = pd.read_csv(filename)
dfStock.dropna(inplace=True)

#dfStock['MACDHist_EMA5'] = dfStock['MACDHist'].ewm(span=5, adjust=False).mean()
#dfStock['EMA_Change'] = 100 * ((dfStock['EMA12'] - dfStock ['EMA26'])/dfStock['EMA12'])

#dfStock[['MACDLine','MACDSignal','MACDHist','MACDHist_EMA9' ]].plot(figsize=(12,6))

dfStock[['MACDHist','MACDHist_EMA9']].plot(figsize=(10,5))

plt.title('MACD')
#plt.xlabel('X')
#plt.ylabel('Y')
plt.grid()
plt.show()