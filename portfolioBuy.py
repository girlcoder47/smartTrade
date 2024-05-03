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

buyFile = 'data/portfolio/trends/'+mkt+'/tradelist/buy_'+ind+'.csv'
cashFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_cash.csv'
portFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_portfolio.csv'
tranFile = 'data/portfolio/trades/'+mkt+'/'+ind+'_transaction.csv'

# read portfolio balance to know cash balance
dfPortBal = pd.read_csv(cashFile) 
#print(dfPortBal)

# find cash available
cash = dfPortBal.loc[0]['Cash']
#print(cash)

# read portfolio to know existing stocks
dfPortfolio = pd.read_csv(portFile)
#print(dfPortfolio)

# read list of stocks to buy
dfBuy = pd.read_csv(buyFile)

# iterate through buy list, buy stock if in portfolio, update cash, create transaction record, append to current portfolio

temp_dfTran = []
temp_dfPort = []
temp_dfCash = []

tranType = 'BUY' # set transaction type to BUY

for i in dfBuy['Ticker']: # iterate through stocks in buy list
	#print(i)

	if ( cash > 4999 ):

		# check if ticker alredy exists in portfolio
		if ( len(dfPortfolio.loc[dfPortfolio['Ticker'] == i]) == 0 ):

			#buy this ticker
			dfStock=yf.download(i, start=start, end=end)
			#print(dfStock)

			purchasePrice = dfStock.iloc[0]['Open']
			#print(purchasePrice)

			purchaseQty = 5000/purchasePrice

			purchaseTotal = purchasePrice * purchaseQty

			tran_rows={'Date':execDate, 'Ticker':i, 'Price':purchasePrice, 'Qty':purchaseQty, 'Total':purchaseTotal, 'Type':tranType}
			#print(tran_rows)

			temp_dfTran.append(tran_rows)

			port_rows={'Ticker':i, 'PurchaseDate':execDate, 'Qty':purchaseQty, 'PurchasePrice':purchasePrice, 'PurchaseTotal':purchaseTotal, 
					   'CurrentPrice':purchasePrice, 'CurrentTotal':purchaseTotal, 'ValueChange':0, 'PercentageChange':0}

			temp_dfPort.append(port_rows)

			# update available cash
			cash = cash - purchaseTotal

#print(tran_rows)
dfBuyAll = pd.DataFrame.from_dict(temp_dfTran)
#print(dfBuyAll)

# record sold stocks in transactions
dfBuyAll.to_csv(tranFile,mode='a',header=False, index=False)

#print(port_rows)
dfPortAdd = pd.DataFrame.from_dict(temp_dfPort)
#print(dfPortAdd)

#write bought stocks to current portfolio
dfPortAdd.to_csv(portFile,mode='a',header=False, index=False)

# record cash available 
cash_rows={'Cash':cash}
#print(cash_rows)
temp_dfCash.append(cash_rows)
dfCash = pd.DataFrame.from_dict(temp_dfCash)
dfCash.to_csv(cashFile,mode='w',header=True, index=False)
