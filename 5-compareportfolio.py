import numpy as np
import pandas as pd
import yfinance as yf
from dateutil.parser import parse
from datetime import timedelta

# str to date
def convert_to_datetime(input_str, parserinfo=None):
	return parse(input_str, parserinfo=parserinfo)

rowList = []

ind = ['SMA','MACD','BOL','RSI','OBV','MYTREND1','MYTREND2','MYTREND3']

outputFile = 'data/dataAnalysisPortfolio.csv'

lowMkt = 'range/DJI/LOW.csv'
dfLow = pd.read_csv(lowMkt)
lowStDate = dfLow.iloc[0]['Date']
lowEnDate = dfLow.iloc[-1]['Date']
lowMktChgPct = 100*(( dfLow.iloc[-1]['Close'] - dfLow.iloc[0]['Close'] )/dfLow.iloc[0]['Close'])

#SPY data
lowStSPY=yf.download('SPY', start=lowStDate, end=convert_to_datetime(lowStDate).date()+timedelta(days=1))
lowEnSPY=yf.download('SPY', start=lowEnDate, end=convert_to_datetime(lowEnDate).date()+timedelta(days=1))
lowSPYChgPct = 100*(( lowEnSPY.iloc[0]['Close'] - lowStSPY.iloc[0]['Close'] )/lowStSPY.iloc[0]['Close'])

neutralMkt = 'range/DJI/NEUTRAL.csv'
dfNeutral = pd.read_csv(neutralMkt)
neutralStDate = dfNeutral.iloc[0]['Date']
neutralEnDate = dfNeutral.iloc[-1]['Date']
neutralMktChgPct = 100*(( dfNeutral.iloc[-1]['Close'] - dfNeutral.iloc[0]['Close'] )/dfNeutral.iloc[0]['Close'])

#SPY data
neutralStSPY=yf.download('SPY', start=neutralStDate, end=convert_to_datetime(neutralStDate).date()+timedelta(days=1))
neutralEnSPY=yf.download('SPY', start=neutralEnDate, end=convert_to_datetime(neutralEnDate).date()+timedelta(days=1))
neutralSPYChgPct = 100*(( neutralEnSPY.iloc[0]['Close'] - neutralStSPY.iloc[0]['Close'] )/neutralStSPY.iloc[0]['Close'])

highMkt = 'range/DJI/HIGH.csv'
dfHigh = pd.read_csv(highMkt)
highStDate = dfHigh.iloc[0]['Date']
highEnDate = dfHigh.iloc[-1]['Date']
highMktChgPct = 100*(( dfHigh.iloc[-1]['Close'] - dfHigh.iloc[0]['Close'] )/dfHigh.iloc[0]['Close'])

#SPY data
highStSPY=yf.download('SPY', start=highStDate, end=convert_to_datetime(highStDate).date()+timedelta(days=1))
highEnSPY=yf.download('SPY', start=highEnDate, end=convert_to_datetime(highEnDate).date()+timedelta(days=1))
highSPYChgPct = 100*(( highEnSPY.iloc[0]['Close'] - highStSPY.iloc[0]['Close'] )/highStSPY.iloc[0]['Close'])

fullMkt = 'range/DJI/FULL.csv'
dfFull = pd.read_csv(fullMkt)
fullStDate = dfFull.iloc[0]['Date']
fullEnDate = dfFull.iloc[-1]['Date']
fullMktChgPct = 100*(( dfFull.iloc[-1]['Close'] - dfFull.iloc[0]['Close'] )/dfFull.iloc[0]['Close'])

#SPY data
fullStSPY=yf.download('SPY', start=fullStDate, end=convert_to_datetime(fullStDate).date()+timedelta(days=1))
fullEnSPY=yf.download('SPY', start=fullEnDate, end=convert_to_datetime(fullEnDate).date()+timedelta(days=1))
fullSPYChgPct = 100*(( fullEnSPY.iloc[0]['Close'] - fullStSPY.iloc[0]['Close'] )/fullStSPY.iloc[0]['Close'])

#print(fullSPYChgPct)

row = {'Ticker':'Portfolio', 'Indicator':'MARKET', 'Low Value':'', 'Low Change':lowMktChgPct,
	   'Neutral Value':'', 'Neutral Change':neutralMktChgPct,
	   'High Value':'', 'High Change':highMktChgPct,
	   'Full Value':'', 'Full Change':fullMktChgPct}
rowList.append(row)

row = {'Ticker':'Portfolio', 'Indicator':'SPY', 'Low Value':'', 'Low Change':lowSPYChgPct,
	   'Neutral Value':'', 'Neutral Change':neutralSPYChgPct,
	   'High Value':'', 'High Change':highSPYChgPct,
	   'Full Value':'', 'Full Change':fullSPYChgPct}
rowList.append(row)

for i in ind:

	lowFile = 'data/portfolio/trades/LOW/' + i + '_tracking.csv'
	neutralFile = 'data/portfolio/trades/NEUTRAL/' + i + '_tracking.csv'
	highFile = 'data/portfolio/trades/HIGH/' + i + '_tracking.csv'
	fullFile = 'data/portfolio/trades/FULL/' + i + '_tracking.csv'

	dfIndLOW = pd.read_csv(lowFile)
	dfIndNEUTRAL = pd.read_csv(neutralFile)
	dfIndHIGH = pd.read_csv(highFile)
	dfIndFULL = pd.read_csv(fullFile)

	lowValue = dfIndLOW.iloc[-1]['Total']
	lowChgPct = dfIndLOW.iloc[-1]['PercentageChange']

	neutralValue = dfIndNEUTRAL.iloc[-1]['Total']
	neutralChgPct = dfIndNEUTRAL.iloc[-1]['PercentageChange']

	highValue = dfIndHIGH.iloc[-1]['Total']
	highChgPct = dfIndHIGH.iloc[-1]['PercentageChange']

	fullValue = dfIndFULL.iloc[-1]['Total']
	fullChgPct = dfIndFULL.iloc[-1]['PercentageChange']

	row = {'Ticker':'Portfolio', 'Indicator':i, 'Low Value':lowValue, 'Low Change':lowChgPct,
	   'Neutral Value':neutralValue, 'Neutral Change':neutralChgPct,
	   'High Value':highValue, 'High Change':highChgPct,
	   'Full Value':fullValue, 'Full Change':fullChgPct}
	rowList.append(row)

dfRow =  pd.DataFrame.from_dict(rowList)
#print(dfRow)
dfRow.to_csv(outputFile,mode='w',header=True, index=False)
