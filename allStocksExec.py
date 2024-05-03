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

dateFile='range/DJI/'+mkt+'.csv'
dfDates = pd.read_csv(dateFile) 

ticker=pd.read_csv('all/SnP100.csv')

for ticker_index, ticker_row in ticker.iterrows():

	for index, row in dfDates.iterrows():

		filename01 = 'python3 allStockTrends.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --mkt '+mkt

		filename02 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --ind SMA --mkt '+mkt
		filename03 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --ind MACD --mkt '+mkt
		filename04 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --ind BOL --mkt '+mkt
		filename05 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --ind RSI --mkt '+mkt
		filename06 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --ind OBV --mkt '+mkt
		filename07 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol']  + ' --ind MYTREND1 --mkt '+mkt
		filename08 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol']  + ' --ind MYTREND2 --mkt '+mkt
		filename09 = 'python3 allStockTrades.py --date '+row['Date']+' --ticker '+ ticker_row['Symbol'] + ' --ind MYTREND3 --mkt '+mkt
	
		if (index==0):
			os.system(filename01)
			os.system(filename02)
			os.system(filename03)
			os.system(filename04)
			os.system(filename05)
			os.system(filename06)
			os.system(filename07)
			os.system(filename08)
			os.system(filename09)
		else:
			os.system(filename02)
			os.system(filename03)
			os.system(filename04)
			os.system(filename05)
			os.system(filename06)
			os.system(filename07)
			os.system(filename08)
			os.system(filename09)
			os.system(filename01)
