import sys
import os
import argparse
import pandas as pd

# get input
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--mkt", required=True, default=None)

	return parser.parse_args()

args = get_arguments()
mkt = args.mkt

ind = ['SMA', 'MACD', 'BOL', 'RSI', 'OBV', 'MYTREND1', 'MYTREND2', 'MYTREND3']

dateFile='range/DJI/'+mkt+'.csv'

# read dates
dfDates = pd.read_csv(dateFile) 
#print(dfDates['Date'])

for index, row in dfDates.iterrows():

	#first day execute trend only
	#second day onwards execute sell, buy, tracking update, trend

	if ( index == 0 ):
		#print('executing first indicator recommendations ....')
		trendExec = 'python3 portfolioTrends.py --date ' + row['Date'] + ' --mkt ' + mkt
		os.system(trendExec)

		for i in ind:

			#print('executing tracking updates ....')
			updateExec = 'python3 portfolioUpdate.py --date ' + row['Date'] + ' --mkt ' + mkt + ' --ind ' + i
			os.system(updateExec)
	else:

		for i in ind:

			#print('executing sell trades ....')
			sellExec = 'python3 portfolioSell.py --date ' + row['Date'] + ' --mkt ' + mkt + ' --ind ' + i
			os.system(sellExec)

			#print('executing buy trades ....')
			buyExec = 'python3 portfolioBuy.py --date ' + row['Date'] + ' --mkt ' + mkt + ' --ind ' + i
			os.system(buyExec)

			#print('executing tracking updates ....')
			updateExec = 'python3 portfolioUpdate.py --date ' + row['Date'] + ' --mkt ' + mkt + ' --ind ' + i
			os.system(updateExec)

		#print('executing indicator recommendations for the next day ....')
		trendExec = 'python3 portfolioTrends.py --date ' + row['Date'] + ' --mkt '+mkt
		os.system(trendExec)
