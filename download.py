import numpy as np
import pandas as pd
import argparse
import yfinance as yf
from datetime import date
from datetime import datetime
from datetime import timedelta


# get input
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--mkt", required=True, default=None)

	return parser.parse_args()

args = get_arguments()
mkt = args.mkt

#ticker = ['AAPL','AMT','PFE','BAC','COST','CAT','DIS','CVX','SO','MMM','TSLA','WMT']
ticker = ['SPY']
#print(ticker)

if ( mkt == 'LOW' ):

	start = datetime(2020,1,3)
	end = datetime(2020,5,2)

elif ( mkt == 'NEUTRAL'):

	start = datetime(2021,4,30)
	end = datetime(2022,3,5)

elif ( mkt == 'HIGH'):

	start = datetime(2020,5,1)
	end = datetime(2021,5,1)

elif ( mkt == 'FULL'):

	start = datetime(2020,1,3)
	end = datetime(2024,1,6)

for i in ticker:
	#print(i)

	dataFile='range/'+i+'/'+mkt+'.csv'
	#print(dataFile)

	dfStock=yf.download(i, start=start, end=end)

	dfStock.to_csv(dataFile,mode='w',header=True, index=True)