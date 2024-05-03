import sys
import os
import argparse
import pandas as pd

# get input
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--ticker", required=True, default=None)
	parser.add_argument("--mkt", required=True, default=None)

	return parser.parse_args()

args = get_arguments()
ticker = args.ticker
mkt = args.mkt

dateFile='range/'+ticker+'/'+mkt+'.csv'

# read dates
dfDates = pd.read_csv(dateFile) 
#print(dfDates['Date'])

for index, row in dfDates.iterrows():

	#print(row['Date'])

	filename01 = 'python3 stockTrends.py --date '+row['Date']+' --ticker '+ ticker + ' --mkt '+mkt

	filename02 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind SMA --mkt '+mkt
	filename03 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MACD --mkt '+mkt
	filename04 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind BOL --mkt '+mkt
	filename05 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind RSI --mkt '+mkt
	filename06 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind OBV --mkt '+mkt

	#filename07 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYSMA --mkt '+mkt
	#filename08 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYMACD --mkt '+mkt
	#filename09 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYRSI --mkt '+mkt
	#filename10 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYOBV --mkt '+mkt

	filename11 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYTREND1 --mkt '+mkt
	filename12 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYTREND2 --mkt '+mkt
	filename13 = 'python3 stockTrades.py --date '+row['Date']+' --ticker '+ ticker + ' --ind MYTREND3 --mkt '+mkt
	
	
	if (index==0):
		os.system(filename01)
	else:
		os.system(filename02)
		os.system(filename03)
		os.system(filename04)
		os.system(filename05)
		os.system(filename06)
		#os.system(filename07)
		#os.system(filename08)
		#os.system(filename09)
		#os.system(filename10)
		os.system(filename11)
		os.system(filename12)
		os.system(filename13)
		os.system(filename01)