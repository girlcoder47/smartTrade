import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt

# get input
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--ticker", required=True, default=None)
	parser.add_argument("--mkt", required=True, default=None)

	return parser.parse_args()

args = get_arguments()
ticker = args.ticker
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
mysmaValue=0
mysmaChange=0
mymacdValue=0
mymacdChange=0
myrsiValue=0
myrsiChange=0
myobvValue=0
myobvChange=0
mytrend1Value=0
mytrend1Change=0
mytrend2Value=0
mytrend2Change=0
mytrend3Value=0
mytrend3Change=0
priceStart=1
priceValue=0
priceChange=0

analysisFile = 'data/'+ticker+'/trade/'+mkt+'/'+ticker+'_'+'analysis.csv'
pltfile = 'data/plots/'+ticker+'_'+mkt+'.png'
djiFile = 'range/DJI/'+mkt+'.csv'
smaFile = 'data/'+ticker+'/trade/'+mkt+'/SMA_balance.csv'
macdFile = 'data/'+ticker+'/trade/'+mkt+'/MACD_balance.csv'
bolFile = 'data/'+ticker+'/trade/'+mkt+'/BOL_balance.csv'
rsiFile = 'data/'+ticker+'/trade/'+mkt+'/RSI_balance.csv'
obvFile = 'data/'+ticker+'/trade/'+mkt+'/OBV_balance.csv'
#mysmaFile = 'data/'+ticker+'/trade/'+mkt+'/MYSMA_balance.csv'
#mymacdFile = 'data/'+ticker+'/trade/'+mkt+'/MYMACD_balance.csv'
#myrsiFile = 'data/'+ticker+'/trade/'+mkt+'/MYRSI_balance.csv'
#myobvFile = 'data/'+ticker+'/trade/'+mkt+'/MYOBV_balance.csv'
mytrend1File = 'data/'+ticker+'/trade/'+mkt+'/MYTREND1_balance.csv'
mytrend2File = 'data/'+ticker+'/trade/'+mkt+'/MYTREND2_balance.csv'
mytrend3File = 'data/'+ticker+'/trade/'+mkt+'/MYTREND3_balance.csv'
priceFile = 'range/'+ticker+'/'+mkt+'.csv'

#print(djiFile)

dfDJI = pd.read_csv(djiFile)
dfSMA = pd.read_csv(smaFile) 
dfMACD = pd.read_csv(macdFile)
dfBOL = pd.read_csv(bolFile) 
dfRSI = pd.read_csv(rsiFile) 
dfOBV = pd.read_csv(obvFile) 
#dfmySMA = pd.read_csv(mysmaFile) 
#dfmyMACD = pd.read_csv(mymacdFile)
#dfmyRSI = pd.read_csv(myrsiFile) 
#dfmyOBV = pd.read_csv(myobvFile)
dfMYTREND1 = pd.read_csv(mytrend1File) 
dfMYTREND2 = pd.read_csv(mytrend2File) 
dfMYTREND3 = pd.read_csv(mytrend3File)
dfPrice = pd.read_csv(priceFile)

#print(dfSMA)

temp_df = []

for index, row in dfDJI.iterrows():

	if (index == 0):
		dateStart=row['Date']
		djiStart=row['Close']
		#print(row['Date'])
		priceStart=dfPrice.loc[(dfPrice['Date'] == row['Date']),'Close'].values[0]
		smaStart=dfSMA.loc[(dfSMA['Date'] == row['Date']),'PortfolioTotal'].values[0]
		macdStart=dfMACD.loc[(dfMACD['Date'] == row['Date']),'PortfolioTotal'].values[0]
		bolStart=dfBOL.loc[(dfBOL['Date'] == row['Date']),'PortfolioTotal'].values[0]
		rsiStart=dfRSI.loc[(dfRSI['Date'] == row['Date']),'PortfolioTotal'].values[0]
		obvStart=dfOBV.loc[(dfOBV['Date'] == row['Date']),'PortfolioTotal'].values[0]
		#mysmaStart=dfmySMA.loc[(dfmySMA['Date'] == row['Date']),'PortfolioTotal'].values[0]
		#mymacdStart=dfmyMACD.loc[(dfmyMACD['Date'] == row['Date']),'PortfolioTotal'].values[0]
		#myrsiStart=dfmyRSI.loc[(dfmyRSI['Date'] == row['Date']),'PortfolioTotal'].values[0]
		#myobvStart=dfmyOBV.loc[(dfmyOBV['Date'] == row['Date']),'PortfolioTotal'].values[0]
		mytrend1Start=dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date']),'PortfolioTotal'].values[0]
		mytrend2Start=dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date']),'PortfolioTotal'].values[0]
		mytrend3Start=dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date']),'PortfolioTotal'].values[0]


		compareRows = {'Date':row['Date'], 'DJIValue':djiStart,'DJIChange':djiChange,'PriceValue':priceStart,'PriceChange':priceChange,
					   'SMAValue':smaStart,'SMAChange':smaChange,'MACDValue':macdStart,'MACDChange':macdChange,'BOLValue':bolStart,'BOLChange':bolChange,
					   'RSIValue':rsiStart,'RSIChange':rsiChange,'OBVValue':obvStart,'OBVChange':obvChange,
					   #'MYSMAValue':mysmaStart,'MYSMAChange':mysmaChange,'MYMACDValue':mymacdStart,'MYMACDChange':mymacdChange,
					   #'MYRSIValue':myrsiStart,'MYRSIChange':myrsiChange,'MYOBVValue':myobvStart,'MYOBVChange':myobvChange,
					   'MYTREND1Value':mytrend1Start,'MYTREND1Change':mytrend1Change,'MYTREND2Value':mytrend2Start,'MYTREND2Change':mytrend2Change,
					   'MYTREND3Value':mytrend3Start,'MYTREND3Change':mytrend3Change}

		temp_df.append(compareRows)

	#elif (row['Date']<'2023-11-16'):
	else:
		djiClose = row['Close']
		djiChange = 100*((djiClose - djiStart)/djiStart)

		if (len(dfPrice.loc[(dfPrice['Date'] == row['Date'])])>0):
			priceValue=dfPrice.loc[(dfPrice['Date'] == row['Date']),'Close'].values[0]
			priceChange= 100*((priceValue - priceStart)/priceStart)
		else:
			priceValue = priceValue
			priceChange = priceChange

		if (len(dfSMA.loc[(dfSMA['Date'] == row['Date'])])>0):
			smaValue=dfSMA.loc[(dfSMA['Date'] == row['Date']),'PortfolioTotal'].values[0]
			smaChange=dfSMA.loc[(dfSMA['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			smaValue = smaValue
			smaChange = smaChange

		if (len(dfMACD.loc[(dfMACD['Date'] == row['Date'])])>0):
			macdValue=dfMACD.loc[(dfMACD['Date'] == row['Date']),'PortfolioTotal'].values[0]
			macdChange=dfMACD.loc[(dfMACD['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			macdValue = macdValue
			macdChange = macdChange

		if (len(dfBOL.loc[(dfBOL['Date'] == row['Date'])])>0):
			bolValue=dfBOL.loc[(dfBOL['Date'] == row['Date']),'PortfolioTotal'].values[0]
			bolChange=dfBOL.loc[(dfBOL['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			bolValue = bolValue
			bolChange = bolChange

		if (len(dfRSI.loc[(dfRSI['Date'] == row['Date'])])>0):
			rsiValue=dfRSI.loc[(dfRSI['Date'] == row['Date']),'PortfolioTotal'].values[0]
			rsiChange=dfRSI.loc[(dfRSI['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			rsiValue = rsiValue
			rsiChange = rsiChange

		if (len(dfOBV.loc[(dfOBV['Date'] == row['Date'])])>0):
			obvValue=dfOBV.loc[(dfOBV['Date'] == row['Date']),'PortfolioTotal'].values[0]
			obvChange=dfOBV.loc[(dfOBV['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			obvValue = obvValue
			obvChange = obvChange

		"""

		if (len(dfmySMA.loc[(dfmySMA['Date'] == row['Date'])])>0):
			mysmaValue=dfmySMA.loc[(dfmySMA['Date'] == row['Date']),'PortfolioTotal'].values[0]
			mysmaChange=dfmySMA.loc[(dfmySMA['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			mysmaValue = mysmaValue
			mysmaChange = mysmaChange

		if (len(dfmyMACD.loc[(dfmyMACD['Date'] == row['Date'])])>0):
			mymacdValue=dfmyMACD.loc[(dfmyMACD['Date'] == row['Date']),'PortfolioTotal'].values[0]
			mymacdChange=dfmyMACD.loc[(dfmyMACD['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			mymacdValue = mymacdValue
			mymacdChange = mymacdChange

		if (len(dfmyRSI.loc[(dfmyRSI['Date'] == row['Date'])])>0):
			myrsiValue=dfmyRSI.loc[(dfmyRSI['Date'] == row['Date']),'PortfolioTotal'].values[0]
			myrsiChange=dfmyRSI.loc[(dfmyRSI['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			myrsiValue = myrsiValue
			myrsiChange = myrsiChange

		if (len(dfmyOBV.loc[(dfmyOBV['Date'] == row['Date'])])>0):
			myobvValue=dfmyOBV.loc[(dfmyOBV['Date'] == row['Date']),'PortfolioTotal'].values[0]
			myobvChange=dfmyOBV.loc[(dfmyOBV['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			myobvValue = myobvValue
			myobvChange = myobvChange

		"""

		if (len(dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date'])])>0):
			mytrend1Value=dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date']),'PortfolioTotal'].values[0]
			mytrend1Change=dfMYTREND1.loc[(dfMYTREND1['Date'] == row['Date']),'PercentageChange'].values[0]		
		else:
			mytrend1Value = mytrend1Value
			mytrend1Change = mytrend1Change

		if (len(dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date'])])>0):
			mytrend2Value=dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date']),'PortfolioTotal'].values[0]
			mytrend2Change=dfMYTREND2.loc[(dfMYTREND2['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			mytrend2Value = mytrend2Value
			mytrend2Change = mytrend2Change

		if (len(dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date'])])>0):
			mytrend3Value=dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date']),'PortfolioTotal'].values[0]
			mytrend3Change=dfMYTREND3.loc[(dfMYTREND3['Date'] == row['Date']),'PercentageChange'].values[0]
		else:
			mytrend3Value = mytrend3Value
			mytrend3Change = mytrend3Change

		compareRows = {'Date':row['Date'], 'DJIValue':djiClose,'DJIChange':djiChange,'PriceValue':priceValue,'PriceChange':priceChange,
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
dfPlot[['PriceChange','DJIChange','SMAChange','MACDChange','RSIChange','OBVChange','MYTREND1Change','MYTREND2Change','MYTREND3Change']].plot(figsize=(12,6))
plt.grid()
plt.savefig(pltfile, bbox_inches='tight')
#plt.show()
