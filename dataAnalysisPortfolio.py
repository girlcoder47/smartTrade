import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt

# get input
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--mkt", required=True, default=None)

	return parser.parse_args()

args = get_arguments()
mkt = args.mkt

djiChange=0
smaValue=0
smaChange=0
macdValue=0
macdChange=0
bolValue=0
bolChange=0
rsiValue=0
rsiChange=0
obvValue=0
obvChange=0
mytrend1Value=0
mytrend1Change=0
mytrend2Value=0
mytrend2Change=0
mytrend3Value=0
mytrend3Change=0
priceStart=1
spyValue=0
spyChange=0

analysisFile = 'data/portfolio/trades/'+mkt+'/portfolio_analysis.csv'
pltfile = 'data/plots/portfoliovalue_'+mkt+'.png'
djiFile = 'range/DJI/'+mkt+'.csv'
spyFile = 'range/SPY/'+mkt+'.csv'
smaFile = 'data/portfolio/trades/'+mkt+'/SMA_tracking.csv'
macdFile = 'data/portfolio/trades/'+mkt+'/MACD_tracking.csv'
bolFile = 'data/portfolio/trades/'+mkt+'/BOL_tracking.csv'
rsiFile = 'data/portfolio/trades/'+mkt+'/RSI_tracking.csv'
obvFile = 'data/portfolio/trades/'+mkt+'/OBV_tracking.csv'
mytrend1File = 'data/portfolio/trades/'+mkt+'/MYTREND1_tracking.csv'
mytrend2File = 'data/portfolio/trades/'+mkt+'/MYTREND2_tracking.csv'
mytrend3File = 'data/portfolio/trades/'+mkt+'/MYTREND3_tracking.csv'

#print(djiFile)

dfDJI = pd.read_csv(djiFile)
dfSPY = pd.read_csv(spyFile)
dfSMA = pd.read_csv(smaFile) 
dfMACD = pd.read_csv(macdFile)
dfBOL = pd.read_csv(bolFile) 
dfRSI = pd.read_csv(rsiFile) 
dfOBV = pd.read_csv(obvFile) 
dfMYTREND1 = pd.read_csv(mytrend1File) 
dfMYTREND2 = pd.read_csv(mytrend2File) 
dfMYTREND3 = pd.read_csv(mytrend3File)

#print(dfSMA)

temp_df = []

for index, row in dfDJI.iterrows():

	if (index == 0):
		dateStart=row['Date']
		djiStart=row['Close']
		spyStart=dfSPY.loc[(dfSPY['Date'] == row['Date']),'Close'].values[0]
		smaStart=dfSMA.loc[(dfSMA['Date'] == row['Date']),'Total'].values[0]
		macdStart=dfMACD.loc[(dfMACD['Date'] == row['Date']),'Total'].values[0]
		bolStart=dfBOL.loc[(dfBOL['Date'] == row['Date']),'Total'].values[0]
		rsiStart=dfRSI.loc[(dfRSI['Date'] == row['Date']),'Total'].values[0]
		obvStart=dfOBV.loc[(dfOBV['Date'] == row['Date']),'Total'].values[0]
		mytrend1Start=dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date']),'Total'].values[0]
		mytrend2Start=dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date']),'Total'].values[0]
		mytrend3Start=dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date']),'Total'].values[0]


		compareRows = {'Date':row['Date'], 'DJIValue':djiStart,'DJIChange':djiChange,'SPYValue':spyStart,'SPYChange':spyChange,
					   'SMAValue':smaStart,'SMAChange':smaChange,'MACDValue':macdStart,'MACDChange':macdChange,'BOLValue':bolStart,'BOLChange':bolChange,
					   'RSIValue':rsiStart,'RSIChange':rsiChange,'OBVValue':obvStart,'OBVChange':obvChange,
					   'MYTREND1Value':mytrend1Start,'MYTREND1Change':mytrend1Change,'MYTREND2Value':mytrend2Start,'MYTREND2Change':mytrend2Change,
					   'MYTREND3Value':mytrend3Start,'MYTREND3Change':mytrend3Change}

		temp_df.append(compareRows)

	#elif (row['Date']<'2023-11-16'):
	else:
		djiClose = row['Close']
		djiChange = 100*((djiClose - djiStart)/djiStart)

		if (len(dfSPY.loc[(dfSPY['Date'] == row['Date'])])>0):
			spyValue=dfSPY.loc[(dfSPY['Date'] == row['Date']),'Close'].values[0]
			spyChange= 100*((spyValue - spyStart)/spyStart)
		else:
			spyValue = spyValue
			spyChange = spyChange

		if (len(dfSMA.loc[(dfSMA['Date'] == row['Date'])])>0):
			smaValue=dfSMA.loc[(dfSMA['Date'] == row['Date']),'Total'].values[0]
			smaChange=dfSMA.loc[(dfSMA['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			smaValue = smaValue
			smaChange = smaChange

		if (len(dfMACD.loc[(dfMACD['Date'] == row['Date'])])>0):
			macdValue=dfMACD.loc[(dfMACD['Date'] == row['Date']),'Total'].values[0]
			macdChange=dfMACD.loc[(dfMACD['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			macdValue = macdValue
			macdChange = macdChange

		if (len(dfBOL.loc[(dfBOL['Date'] == row['Date'])])>0):
			bolValue=dfBOL.loc[(dfBOL['Date'] == row['Date']),'Total'].values[0]
			bolChange=dfBOL.loc[(dfBOL['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			bolValue = bolValue
			bolChange = bolChange

		if (len(dfRSI.loc[(dfRSI['Date'] == row['Date'])])>0):
			rsiValue=dfRSI.loc[(dfRSI['Date'] == row['Date']),'Total'].values[0]
			rsiChange=dfRSI.loc[(dfRSI['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			rsiValue = rsiValue
			rsiChange = rsiChange

		if (len(dfOBV.loc[(dfOBV['Date'] == row['Date'])])>0):
			obvValue=dfOBV.loc[(dfOBV['Date'] == row['Date']),'Total'].values[0]
			obvChange=dfOBV.loc[(dfOBV['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			obvValue = obvValue
			obvChange = obvChange

		if (len(dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date'])])>0):
			mytrend1Value=dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date']),'Total'].values[0]
			mytrend1Change=dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date']),'PercentageChange'].values[0]		
		else:
			mytrend1Value = mytrend1Value
			mytrend1Change = mytrend1Change

		if (len(dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date'])])>0):
			mytrend2Value=dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date']),'Total'].values[0]
			mytrend2Change=dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			mytrend2Value = mytrend2Value
			mytrend2Change = mytrend2Change

		if (len(dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date'])])>0):
			mytrend3Value=dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date']),'Total'].values[0]
			mytrend3Change=dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			mytrend3Value = mytrend3Value
			mytrend3Change = mytrend3Change

		compareRows = {'Date':row['Date'], 'DJIValue':djiClose,'DJIChange':djiChange,'SPYValue':spyValue,'SPYChange':spyChange,
		'SMAValue':smaValue,'SMAChange':smaChange,'MACDValue':macdValue,'MACDChange':macdChange,
		'BOLValue':bolValue,'BOLChange':bolChange,'RSIValue':rsiValue,'RSIChange':rsiChange,'OBVValue':obvValue,'OBVChange':obvChange,
		'MYTREND1Value':mytrend1Value,'MYTREND1Change':mytrend1Change,'MYTREND2Value':mytrend2Value,'MYTREND2Change':mytrend2Change, 
		'MYTREND3Value':mytrend3Value,'MYTREND3Change':mytrend3Change}

		temp_df.append(compareRows)

dfCompare = pd.DataFrame.from_dict(temp_df)
#print(dfCompare)

#create a row in data analysis file
dfCompare.to_csv(analysisFile,mode='w',header=True, index=False)

#plot graph
dfPlot = pd.read_csv(analysisFile)
#dfPlot[['djiChange','SPYChange','SMAChange','MACDChange','RSIChange','OBVChange','MYTREND1Change','MYTREND2Change','MYTREND3Change']].plot(figsize=(12,6))
dfPlot[['SMAValue','MACDValue','RSIValue','OBVValue','MYTREND1Value','MYTREND2Value','MYTREND3Value']].plot(figsize=(12,6))
plt.grid()
plt.savefig(pltfile, bbox_inches='tight')
#plt.show()
