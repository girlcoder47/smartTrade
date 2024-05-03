import sys
import os
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
	parser.add_argument("--mkt",required=True, default=None)
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

sellFile = 'data/portfolio/trends/'+mkt+'/tradelist/sell_'+ind+'.csv'
cashFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_cash.csv'
portFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_portfolio.csv'
tranFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_transaction.csv'

# read mytrend_cash to know current cash balance for mytrend indicator
dfPortBal = pd.read_csv(cashFile) 
#print(dfPortBal)

# find cash available
cash = dfPortBal.loc[0]['Cash']
#print(cash)

# read portfolio to know existing stocks
dfPortfolio = pd.read_csv(portFile)
#print(dfPortfolio)

# read list of stocks to sell
dfSell = pd.read_csv(sellFile)
#print(dfSell) 

# iterate through portfoli, sell stock if in portfolio, update cash, create transaction record, write new current portfolio
temp_dfTran = []
temp_dfCash = []

tranType = 'SELL' # set transaction type to SELL

for i in dfPortfolio['Ticker']: # iterate through stocks in portfolio
	#print(i)

	#check if ticker exists in sell list
	if ( len(dfSell.loc[dfSell['Ticker'] == i]) > 0 ):

		# download data for this ticker and get open price 
		# create sell transaction in portfolio_transaction
		# delete from current_portfolio
		# update cash variable

		dfStock=yf.download(i, start=start, end=end)
		#print(dfStock)

		sellPrice = dfStock.iloc[0]['Open']
		#print(sellPrice)

		sellQty = dfPortfolio.loc[(dfPortfolio['Ticker'] == i),'Qty'].values[0] #getting quantity from portfolio
		#print(sellQty)

		sellTotal = sellPrice * sellQty
		#print('sell total:')
		#print(sellTotal)

		tran_rows={'Date':execDate, 'Ticker':i, 'Price':sellPrice, 'Qty':sellQty, 'Total':sellTotal, 'Type':tranType}
		#print(tran_rows)

		temp_dfTran.append(tran_rows)

		# delete sold stock from current portfolio
		dfPortfolio.drop(index=dfPortfolio[dfPortfolio['Ticker'] == i].index,inplace=True)

		# update available cash
		cash = cash + sellTotal

dfSellAll = pd.DataFrame.from_dict(temp_dfTran)
#print(dfSellAll)

# record sold stocks
if not os.path.isfile(tranFile):
	dfSellAll.to_csv(tranFile,mode='w',header=True, index=False)
else:
	dfSellAll.to_csv(tranFile,mode='a',header=False, index=False)

#write portfolio after removing sold stocks
dfPortfolio.to_csv(portFile,mode='w',header=True, index=False)

# record cash available 
cash_rows={'Cash':cash}
temp_dfCash.append(cash_rows)
dfCash = pd.DataFrame.from_dict(temp_dfCash)
dfCash.to_csv(cashFile,mode='w',header=True, index=False)
