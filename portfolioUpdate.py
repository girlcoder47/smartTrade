import sys
import argparse
from dateutil.parser import parse
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date
from datetime import datetime
from datetime import timedelta

# get input date
def get_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--date",help="pass date in yyyy-mm-dd format", required=True, default=None)
	parser.add_argument("--mkt", required=True, default=None)
	parser.add_argument("--ind",help="pass mytrend/mav/macd/bol/rsi/obv", required=True, default=None)

	return parser.parse_args()

# str to date
def convert_to_datetime(input_str, parserinfo=None):
	return parse(input_str, parserinfo=parserinfo)

args = get_arguments()
inputDate = args.date
mkt = args.mkt
ind = args.ind

execDate = convert_to_datetime(inputDate).date()

end =  execDate + timedelta(days=1)

start = execDate

cashFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_cash.csv'
portFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_portfolio.csv'
trackFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_tracking.csv'

# read portfolio balance to know cash balance
dfPortBal = pd.read_csv(cashFile) 
#print(dfPortBal)

# find cash available
cash = dfPortBal.loc[0]['Cash']
#print(cash)

# read current portfolio
dfPortfolio = pd.read_csv(portFile)

# read current tracking file
dfTracking = pd.read_csv(trackFile)


# iterate through portfolio, update current price in portfolio, calculate current equity value

temp_dfPort = []
temp_dfTrack = []
equityTotal = 0

for index,row in dfPortfolio.iterrows(): # iterate through portfolio
	#print(row['ticker'])

	#download current stock price
	dfStock=yf.download(row['Ticker'], start=start, end=end)
	#print(dfStock.iloc[0]['Close'])

	port_rows = {'Ticker':row['Ticker'], 'PurchaseDate':row['PurchaseDate'], 'Qty':row['Qty'], 'PurchasePrice':row['PurchasePrice'],
				 'PurchaseTotal':row['PurchaseTotal'], 'CurrentPrice':dfStock.iloc[0]['Close'],
				 'CurrentTotal':row['Qty']*dfStock.iloc[0]['Close'],
				 'ValueChange':row['Qty']*dfStock.iloc[0]['Close']-row['PurchaseTotal'],
				 'PercentageChange':(100*(row['Qty']*dfStock.iloc[0]['Close']-row['PurchaseTotal'])/row['PurchaseTotal'])}

	# calculate equity total
	equityTotal = equityTotal + row['Qty']*dfStock.iloc[0]['Close']
	#print(equityTotal)

	temp_dfPort.append(port_rows)

dfPortNew = pd.DataFrame.from_dict(temp_dfPort)
#print(dfPortNew)

if ( len(dfTracking)>0 ):
	firstTrack = dfTracking.iloc[0]
	currentTotal = firstTrack['Total']

	track_row={'Date':execDate, 'Cash':cash, 'Equity':equityTotal, 'Total':cash+equityTotal, 
           'Change':((cash+equityTotal)-currentTotal), 'PercentageChange':(100*((cash+equityTotal)-currentTotal)/currentTotal)}

else:
	track_row={'Date':execDate, 'Cash':cash, 'Equity':equityTotal, 'Total':cash+equityTotal, 
           'Change':0, 'PercentageChange':0}

#print(track_row)

temp_dfTrack.append(track_row)
dfTrack = pd.DataFrame.from_dict(temp_dfTrack)

#write to current portfolio
if len(dfPortNew)>0:
	dfPortNew.to_csv(portFile,mode='w',header=True, index=False)

#create a row in portfolio tracking
dfTrack.to_csv(trackFile,mode='a',header=False, index=False)
