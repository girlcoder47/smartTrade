import numpy as np
import pandas as pd

rowList = []

ticker = ['AAPL','AMT','BAC','CAT','COST','CVX','DIS','MMM','PFE','SO','TSLA','WMT']

for i in ticker:

	lowFile = 'data/'+i+'/trade/LOW/'+i+'_analysis.csv'
	neutralFile = 'data/'+i+'/trade/NEUTRAL/'+i+'_analysis.csv'
	highFile = 'data/'+i+'/trade/HIGH/'+i+'_analysis.csv'
	fullFile = 'data/'+i+'/trade/FULL/'+i+'_analysis.csv'

	outputFile = 'data/dataAnalysisStock.csv'

	dfLOW = pd.read_csv(lowFile)
	dfNEUTRAL = pd.read_csv(neutralFile)
	dfHIGH = pd.read_csv(highFile)
	dfFULL = pd.read_csv(fullFile)

	lowRow = dfLOW.iloc[-1]
	neutralRow = dfNEUTRAL.iloc[-1]
	highRow = dfHIGH.iloc[-1]
	fullRow = dfFULL.iloc[-1]

	if ( i == 'AAPL' ):
		row = {'Ticker':'', 'Indicator':'Market', 'Low Value':'', 'Low Change':lowRow['DJIChange'],
			   'Neutral Value':'', 'Neutral Change':neutralRow['DJIChange'],
			   'High Value':'', 'High Change':highRow['DJIChange'],
			   'Full Value':'', 'Full Change':fullRow['DJIChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'Price', 'Low Value':'', 'Low Change':lowRow['PriceChange'],
			   'Neutral Value':'', 'Neutral Change':neutralRow['PriceChange'],
			   'High Value':'', 'High Change':highRow['PriceChange'],
			   'Full Value':'', 'Full Change':fullRow['PriceChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'SMA', 'Low Value':lowRow['SMAValue'], 'Low Change':lowRow['SMAChange'],
			   'Neutral Value':neutralRow['SMAValue'], 'Neutral Change':neutralRow['SMAChange'],
			   'High Value':highRow['SMAValue'], 'High Change':highRow['SMAChange'],
			   'Full Value':fullRow['SMAValue'], 'Full Change':fullRow['SMAChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MACD', 'Low Value':lowRow['MACDValue'], 'Low Change':lowRow['MACDChange'],
			   'Neutral Value':neutralRow['MACDValue'], 'Neutral Change':neutralRow['MACDChange'],
			   'High Value':highRow['MACDValue'], 'High Change':highRow['MACDChange'],
			   'Full Value':fullRow['MACDValue'], 'Full Change':fullRow['MACDChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'BOL', 'Low Value':lowRow['BOLValue'], 'Low Change':lowRow['BOLChange'],
			   'Neutral Value':neutralRow['BOLValue'], 'Neutral Change':neutralRow['BOLChange'],
			   'High Value':highRow['BOLValue'], 'High Change':highRow['BOLChange'],
			   'Full Value':fullRow['BOLValue'], 'Full Change':fullRow['BOLChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'RSI', 'Low Value':lowRow['RSIValue'], 'Low Change':lowRow['RSIChange'],
			   'Neutral Value':neutralRow['RSIValue'], 'Neutral Change':neutralRow['RSIChange'],
			   'High Value':highRow['RSIValue'], 'High Change':highRow['RSIChange'],
			   'Full Value':fullRow['RSIValue'], 'Full Change':fullRow['RSIChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'OBV', 'Low Value':lowRow['OBVValue'], 'Low Change':lowRow['OBVChange'],
			   'Neutral Value':neutralRow['OBVValue'], 'Neutral Change':neutralRow['OBVChange'],
			   'High Value':highRow['OBVValue'], 'High Change':highRow['OBVChange'],
			   'Full Value':fullRow['OBVValue'], 'Full Change':fullRow['OBVChange']}
		rowList.append(row)

		"""

		row = {'Ticker':i, 'Indicator':'MYSMA', 'Low Value':lowRow['MYSMAValue'], 'Low Change':lowRow['MYSMAChange'],
			   'Neutral Value':neutralRow['MYSMAValue'], 'Neutral Change':neutralRow['MYSMAChange'],
			   'High Value':highRow['MYSMAValue'], 'High Change':highRow['MYSMAChange'],
			   'Full Value':fullRow['MYSMAValue'], 'Full Change':fullRow['MYSMAChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYMACD', 'Low Value':lowRow['MYMACDValue'], 'Low Change':lowRow['MYMACDChange'],
			   'Neutral Value':neutralRow['MYMACDValue'], 'Neutral Change':neutralRow['MYMACDChange'],
			   'High Value':highRow['MYMACDValue'], 'High Change':highRow['MYMACDChange'],
			   'Full Value':fullRow['MYMACDValue'], 'Full Change':fullRow['MYMACDChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYRSI', 'Low Value':lowRow['MYRSIValue'], 'Low Change':lowRow['MYRSIChange'],
			   'Neutral Value':neutralRow['MYRSIValue'], 'Neutral Change':neutralRow['MYRSIChange'],
			   'High Value':highRow['MYRSIValue'], 'High Change':highRow['MYRSIChange'],
			   'Full Value':fullRow['MYRSIValue'], 'Full Change':fullRow['MYRSIChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYOBV', 'Low Value':lowRow['MYOBVValue'], 'Low Change':lowRow['MYOBVChange'],
			   'Neutral Value':neutralRow['MYOBVValue'], 'Neutral Change':neutralRow['MYOBVChange'],
			   'High Value':highRow['MYOBVValue'], 'High Change':highRow['MYOBVChange'],
			   'Full Value':fullRow['MYOBVValue'], 'Full Change':fullRow['MYOBVChange']}
		rowList.append(row)
		"""

		row = {'Ticker':i, 'Indicator':'MYTREND1', 'Low Value':lowRow['MYTREND1Value'], 'Low Change':lowRow['MYTREND1Change'],
			   'Neutral Value':neutralRow['MYTREND1Value'], 'Neutral Change':neutralRow['MYTREND1Change'],
			   'High Value':highRow['MYTREND1Value'], 'High Change':highRow['MYTREND1Change'],
			   'Full Value':fullRow['MYTREND1Value'], 'Full Change':fullRow['MYTREND1Change']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYTREND2', 'Low Value':lowRow['MYTREND2Value'], 'Low Change':lowRow['MYTREND2Change'],
			   'Neutral Value':neutralRow['MYTREND2Value'], 'Neutral Change':neutralRow['MYTREND2Change'],
			   'High Value':highRow['MYTREND2Value'], 'High Change':highRow['MYTREND2Change'],
			   'Full Value':fullRow['MYTREND2Value'], 'Full Change':fullRow['MYTREND2Change']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYTREND3', 'Low Value':lowRow['MYTREND3Value'], 'Low Change':lowRow['MYTREND3Change'],
			   'Neutral Value':neutralRow['MYTREND3Value'], 'Neutral Change':neutralRow['MYTREND3Change'],
			   'High Value':highRow['MYTREND3Value'], 'High Change':highRow['MYTREND3Change'],
			   'Full Value':fullRow['MYTREND3Value'], 'Full Change':fullRow['MYTREND3Change']}
		rowList.append(row)
	
	else:
		row = {'Ticker':i, 'Indicator':'Price', 'Low Value':'', 'Low Change':lowRow['PriceChange'],
			   'Neutral Value':'', 'Neutral Change':neutralRow['PriceChange'],
			   'High Value':'', 'High Change':highRow['PriceChange'],
			   'Full Value':'', 'Full Change':fullRow['PriceChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'SMA', 'Low Value':lowRow['SMAValue'], 'Low Change':lowRow['SMAChange'],
			   'Neutral Value':neutralRow['SMAValue'], 'Neutral Change':neutralRow['SMAChange'],
			   'High Value':highRow['SMAValue'], 'High Change':highRow['SMAChange'],
			   'Full Value':fullRow['SMAValue'], 'Full Change':fullRow['SMAChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MACD', 'Low Value':lowRow['MACDValue'], 'Low Change':lowRow['MACDChange'],
			   'Neutral Value':neutralRow['MACDValue'], 'Neutral Change':neutralRow['MACDChange'],
			   'High Value':highRow['MACDValue'], 'High Change':highRow['MACDChange'],
			   'Full Value':fullRow['MACDValue'], 'Full Change':fullRow['MACDChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'BOL', 'Low Value':lowRow['BOLValue'], 'Low Change':lowRow['BOLChange'],
			   'Neutral Value':neutralRow['BOLValue'], 'Neutral Change':neutralRow['BOLChange'],
			   'High Value':highRow['BOLValue'], 'High Change':highRow['BOLChange'],
			   'Full Value':fullRow['BOLValue'], 'Full Change':fullRow['BOLChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'RSI', 'Low Value':lowRow['RSIValue'], 'Low Change':lowRow['RSIChange'],
			   'Neutral Value':neutralRow['RSIValue'], 'Neutral Change':neutralRow['RSIChange'],
			   'High Value':highRow['RSIValue'], 'High Change':highRow['RSIChange'],
			   'Full Value':fullRow['RSIValue'], 'Full Change':fullRow['RSIChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'OBV', 'Low Value':lowRow['OBVValue'], 'Low Change':lowRow['OBVChange'],
			   'Neutral Value':neutralRow['OBVValue'], 'Neutral Change':neutralRow['OBVChange'],
			   'High Value':highRow['OBVValue'], 'High Change':highRow['OBVChange'],
			   'Full Value':fullRow['OBVValue'], 'Full Change':fullRow['OBVChange']}
		rowList.append(row)

		"""

		row = {'Ticker':i, 'Indicator':'MYSMA', 'Low Value':lowRow['MYSMAValue'], 'Low Change':lowRow['MYSMAChange'],
			   'Neutral Value':neutralRow['MYSMAValue'], 'Neutral Change':neutralRow['MYSMAChange'],
			   'High Value':highRow['MYSMAValue'], 'High Change':highRow['MYSMAChange'],
			   'Full Value':fullRow['MYSMAValue'], 'Full Change':fullRow['MYSMAChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYMACD', 'Low Value':lowRow['MYMACDValue'], 'Low Change':lowRow['MYMACDChange'],
			   'Neutral Value':neutralRow['MYMACDValue'], 'Neutral Change':neutralRow['MYMACDChange'],
			   'High Value':highRow['MYMACDValue'], 'High Change':highRow['MYMACDChange'],
			   'Full Value':fullRow['MYMACDValue'], 'Full Change':fullRow['MYMACDChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYRSI', 'Low Value':lowRow['MYRSIValue'], 'Low Change':lowRow['MYRSIChange'],
			   'Neutral Value':neutralRow['MYRSIValue'], 'Neutral Change':neutralRow['MYRSIChange'],
			   'High Value':highRow['MYRSIValue'], 'High Change':highRow['MYRSIChange'],
			   'Full Value':fullRow['MYRSIValue'], 'Full Change':fullRow['MYRSIChange']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYOBV', 'Low Value':lowRow['MYOBVValue'], 'Low Change':lowRow['MYOBVChange'],
			   'Neutral Value':neutralRow['MYOBVValue'], 'Neutral Change':neutralRow['MYOBVChange'],
			   'High Value':highRow['MYOBVValue'], 'High Change':highRow['MYOBVChange'],
			   'Full Value':fullRow['MYOBVValue'], 'Full Change':fullRow['MYOBVChange']}
		rowList.append(row)

		"""

		row = {'Ticker':i, 'Indicator':'MYTREND1', 'Low Value':lowRow['MYTREND1Value'], 'Low Change':lowRow['MYTREND1Change'],
			   'Neutral Value':neutralRow['MYTREND1Value'], 'Neutral Change':neutralRow['MYTREND1Change'],
			   'High Value':highRow['MYTREND1Value'], 'High Change':highRow['MYTREND1Change'],
			   'Full Value':fullRow['MYTREND1Value'], 'Full Change':fullRow['MYTREND1Change']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYTREND2', 'Low Value':lowRow['MYTREND2Value'], 'Low Change':lowRow['MYTREND2Change'],
			   'Neutral Value':neutralRow['MYTREND2Value'], 'Neutral Change':neutralRow['MYTREND2Change'],
			   'High Value':highRow['MYTREND2Value'], 'High Change':highRow['MYTREND2Change'],
			   'Full Value':fullRow['MYTREND2Value'], 'Full Change':fullRow['MYTREND2Change']}
		rowList.append(row)

		row = {'Ticker':i, 'Indicator':'MYTREND3', 'Low Value':lowRow['MYTREND3Value'], 'Low Change':lowRow['MYTREND3Change'],
			   'Neutral Value':neutralRow['MYTREND3Value'], 'Neutral Change':neutralRow['MYTREND3Change'],
			   'High Value':highRow['MYTREND3Value'], 'High Change':highRow['MYTREND3Change'],
			   'Full Value':fullRow['MYTREND3Value'], 'Full Change':fullRow['MYTREND3Change']}
		rowList.append(row)

dfRow =  pd.DataFrame.from_dict(rowList)

dfRow.to_csv(outputFile,mode='w',header=True, index=False)



