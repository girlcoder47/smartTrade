import sys
import os
import argparse
from dateutil.parser import parse
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
from datetime import timedelta

# Variables

tmpTrendList = []
latestDataList = []
currMarketList = []

# get input date
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--date",help="pass date in yyyy-mm-dd format", required=True, default=None)
	parser.add_argument("--ticker", required=True, default=None)
	parser.add_argument("--mkt", required=True, default=None)

	return parser.parse_args()

# str to date
def convert_to_datetime(input_str, parserinfo=None):
	return parse(input_str, parserinfo=parserinfo)

args = get_arguments()
inputDate = args.date
ticker = args.ticker
mkt = args.mkt

execDate = convert_to_datetime(inputDate).date()

end =  execDate + timedelta(days=1)
start = end - timedelta(days=365)

#dataFile = 'all/'+mkt+'/'+ticker+'_'+inputDate+'.csv'
latestDataFile = 'all/'+mkt+'/'+ticker+'_latest_data.csv'
trendFile = 'all/'+mkt+'/'+ticker+'_trends.csv'

################ determine market trend ##########################################

dfMarket=yf.download('^DJI', start=start, end=end)

dfMarket['MKT_EMA50'] = dfMarket['Close'].ewm(span=50, adjust=False).mean()
dfMarket['MKT_EMA200'] = dfMarket['Close'].ewm(span=200, adjust=False).mean()
dfMarket['MKT_CHGPCT'] = 100*((dfMarket['MKT_EMA50']-dfMarket['MKT_EMA200'])/dfMarket['MKT_EMA200'])

currMarket = dfMarket.iloc[-1]

mktTrend='NEUTRAL' # initialize market trend

if ( currMarket['MKT_CHGPCT'] > 5 ):
	mktTrend='UP'
elif ( currMarket['MKT_CHGPCT'] < -5 ):
	mktTrend='DOWN'
else: 
	mktTrend='NEUTRAL'

###################################################################################

dfStock=yf.download(ticker, start=start, end=end)

#Simple Moving Average Indicator Calculations
dfStock['SMA50'] = dfStock['Close'].rolling(50).mean()
dfStock['SMA200'] = dfStock['Close'].rolling(200).mean()

#dfStock['SMA100'] = dfStock['Close'].rolling(100).mean()
#dfStock['SMA250'] = dfStock['Close'].rolling(250).mean()

#Moving Average Convergence Divergence Indicator Calculations
dfStock['EMA12'] = dfStock['Close'].ewm(span=12, adjust=False).mean()
dfStock['EMA26'] = dfStock['Close'].ewm(span=26, adjust=False).mean()

dfStock['MACDLine'] = dfStock['EMA12'] - dfStock['EMA26']
dfStock['MACDSignal'] = dfStock['MACDLine'].ewm(span=9, adjust=False).mean()
dfStock['MACDHist'] = dfStock['MACDLine'] - dfStock['MACDSignal'] # >0 if up trend

#Bollinger Band Indicator Caluculation
dfStock['TP'] = (dfStock['High'] + dfStock['Low'] + dfStock['Close'])/3
std = dfStock['TP'].rolling(20).std()
dfStock['TP20'] = dfStock['TP'].rolling(20).mean()
dfStock['middleBand'] = dfStock['TP20']
dfStock['upperBand'] = dfStock['middleBand'] + std*2
dfStock['lowerBand'] = dfStock['middleBand'] - std*2

#Relative Strength Indicator Calculations
change = dfStock["Close"].diff()
change_up = change.copy()
change_down = change.copy()

change_up[change_up<0]=0
change_down[change_down>0]=0

avg_up = change_up.ewm(span=14, adjust=False).mean()
avg_down = change_down.ewm(span=14, adjust=False).mean().abs()

dfStock['RSI'] = 100 * avg_up/(avg_up+avg_down)

#On Balance Volume Indicator Calculations
dfStock['EMA5'] = dfStock['Close'].ewm(span=5, adjust=False).mean()
dfStock['EMA20'] = dfStock['Close'].ewm(span=20, adjust=False).mean()

OBVCalc = []
OBVCalc.append(0)
for j in range(1,len(dfStock.Close)):
	if ( dfStock.iloc[j]['Close'] > dfStock.iloc[j-1]['Close'] ):
		OBVCalc.append(OBVCalc[-1] + dfStock.iloc[j]['Volume'])

	elif ( dfStock.iloc[j]['Close'] < dfStock.iloc[j-1]['Close'] ):
		OBVCalc.append(OBVCalc[-1] - dfStock.iloc[j]['Volume'])

	else:
		OBVCalc.append(OBVCalc[-1])

dfStock['OBV'] = OBVCalc
dfStock['OBV_EMA3'] = dfStock['OBV'].ewm(span=3, adjust=False).mean()
dfStock['OBV_EMA20'] = dfStock['OBV'].ewm(span=20, adjust=False).mean()

#Find Current Data Record
latestData = dfStock.iloc[-1]

#Simple Moving Average Indicator Trend

if ( latestData['SMA50'] > latestData['SMA200'] ):
	sma = 'BUY'
elif ( latestData['SMA50'] < latestData['SMA200'] ):
	sma = 'SELL'
else:
	sma = 'HOLD'

#Moving Average Convergence Divergence Indicator Trend

if ( latestData['MACDHist'] > 0 ): 
	macd = 'BUY'
elif ( latestData['MACDHist'] < 0 ):
	macd = 'SELL'
else:
	macd = 'HOLD'

# Bollinger Band Indicator Trend

if ( latestData['Close'] < latestData['lowerBand'] ):
	bol = 'BUY'
elif ( latestData['Close'] > latestData['upperBand'] ):
	bol = 'SELL'
else:
	bol = 'HOLD'

# Relative Strength Indicator Trend

if ( latestData['RSI'] > 70 ):
	rsi = 'SELL'
elif ( latestData['RSI'] < 30 ):
	rsi = 'BUY'
else:
	rsi = 'HOLD'

# On Balance Volume Indicator Trend
if ( latestData['EMA5'] > latestData['EMA20'] ):
	if ( latestData['OBV_EMA3'] > latestData['OBV_EMA20']):
		obv = 'BUY'
	else:
		obv = 'HOLD'
elif ( latestData['EMA5'] < latestData['EMA20'] ):
	if ( latestData['OBV_EMA3'] < latestData['OBV_EMA20']):
		obv = 'SELL'
	else:
		obv = 'HOLD'
else:
	obv = 'HOLD'

#Mytrend1 Indicator Trend
myTrend1 = 'HOLD'

if ( mktTrend == 'DOWN'):

	myTrend1 = macd #if market trend is down then use MACD (original)

elif ( mktTrend == 'NEUTRAL'):

	myTrend1 = macd #if market trend is neutral then use MACD (original)

elif ( mktTrend == 'UP'):

	myTrend1 = bol #if market trend is up then use BOL

#Mytrend2 Indicator Trend
myTrend2 = 'HOLD' #initialize

if ( mktTrend == 'DOWN'):

	myTrend2 = macd #if market trend is down then use MACD (original)

elif ( mktTrend == 'NEUTRAL'):

	myTrend2 = macd

elif ( mktTrend == 'UP'): #if market trend is up then use RSI

	myTrend2 = rsi

#Mytrend3 Indicator Trend
myTrend3 = 'HOLD' #initialize

if ( mktTrend == 'DOWN'):

	myTrend3 = macd #if market trend is down then use MACD (original)

elif ( mktTrend == 'NEUTRAL'):

	myTrend3 = macd #if market trend is neutral then use OBV

elif ( mktTrend == 'UP'):

	myTrend3 = obv #if market trend is up then use OBV

latestDataList.append(latestData)
dfLatestData =  pd.DataFrame.from_dict(latestDataList)
dfLatestData.reset_index(names=['Date'],inplace=True)
#print(dfLatestData)

#Wrire only latest data record to file

if not os.path.isfile(latestDataFile):
	dfLatestData.to_csv(latestDataFile,mode='w',header=True, index=False)
	
else:
	dfLatestData.to_csv(latestDataFile,mode='a',header=False, index=False)

trendRows={'Date':execDate, 'Ticker':ticker, 'MKTTREND':mktTrend,
		   'SMA':sma, 'MACD':macd, 'BOL':bol, 'RSI':rsi, 'OBV':obv, 
		   'MYTREND1':myTrend1, 'MYTREND2':myTrend2, 'MYTREND3':myTrend3}
#print(trendRows)

tmpTrendList.append(trendRows)
dfTrend =  pd.DataFrame.from_dict(tmpTrendList)

if not os.path.isfile(trendFile):
	dfTrend.to_csv(trendFile,mode='w',header=True, index=False)
else:
	dfTrend.to_csv(trendFile,mode='a',header=False, index=False)
