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
	parser.add_argument("--ticker",help="pass AAPL/PFE etc.", required=True, default=None)
	parser.add_argument("--ind",help="pass SMA/MACD/BOL/RSI/OBV/MYTREND1/MYTREND2", required=True, default=None)
	parser.add_argument("--mkt",help="pass LOW/NEUTRAL/HIGH/FULL", required=True, default=None)

	return parser.parse_args()

# str to date
def convert_to_datetime(input_str, parserinfo=None):
	return parse(input_str, parserinfo=parserinfo)

args = get_arguments()
inputDate = args.date
ticker = args.ticker
ind = args.ind
mkt = args.mkt

execDate = convert_to_datetime(inputDate).date()

#print('printing execution date:')
#print(execDate)

end =  execDate + timedelta(days=1)
#print('printing end date:')
#print(end)

start = execDate
#print('printing start date:')
#print(start)

tmpTxnList=[]
tmpBalList=[]

trendFile = 'data/'+ticker+'/'+ticker+'_'+mkt+'_trends.csv'
balFile = 'data/'+ticker+'/trade/'+mkt+'/'+ind+'_balance.csv'
txnFile = 'data/'+ticker+'/trade/'+mkt+'/'+ind+'_txn.csv'

# read trends file for the stock
dfTrends = pd.read_csv(trendFile) 
latestTrend = dfTrends.iloc[-1]

# read balance file for exting quantity and cash
dfBal = pd.read_csv(balFile)
startBal = dfBal.iloc[0]['PortfolioTotal'] 

latestBal = dfBal.iloc[-1]
cash = latestBal['Cash']
qty = latestBal['Qty']
purPrice = latestBal['PurchasePrice']

# Download current open and close price
dfStock=yf.download(ticker, start=start, end=end)

if ( latestTrend[ind] == 'SELL'):
	
	if (qty>0):
		sellPrice = dfStock.iloc[-1]['Open']
		sellTotal = qty*sellPrice
		purPrice = 0

		newCash=cash+sellTotal
		newQty=0
		newPrice=dfStock.iloc[-1]['Close']
		newEquityTotal=0
		newBal = newCash+newEquityTotal
		changePCT = ((newBal - startBal)/startBal)*100

		txnRows={'Date':execDate, 'Ticker':ticker, 'Type':'SELL','Qty':qty,'Price':sellPrice,'Total':sellTotal}
		balRows={'date':execDate,'Cash':newCash,'Qty':0,'PurchasePrice':purPrice,'CurrentPrice':newPrice,'CurrentEquityTotal':newEquityTotal,
				 'PortfolioTotal':newBal,'PercentageChange':changePCT}

		tmpTxnList.append(txnRows)
		dfTxn =  pd.DataFrame.from_dict(tmpTxnList)

		if not os.path.isfile(txnFile):
			dfTxn.to_csv(txnFile,mode='w',header=True, index=False)
		else:
			dfTxn.to_csv(txnFile,mode='a',header=False, index=False)

		tmpBalList.append(balRows)
		dfBalNew =  pd.DataFrame.from_dict(tmpBalList)
		dfBalNew.to_csv(balFile,mode='a',header=False, index=False)
	else:
		# create balance record only
		purPrice=0
		newPrice=dfStock.iloc[-1]['Close']
		newEquityTotal=qty*newPrice
		newBal = cash+newEquityTotal
		changePCT = ((newBal - startBal)/startBal)*100

		balRows={'date':execDate,'Cash':cash,'Qty':qty,'PurchasePrice':purPrice,'CurrentPrice':newPrice,'CurrentEquityTotal':newEquityTotal,
				 'PortfolioTotal':newBal,'PercentageChange':changePCT}

		tmpBalList.append(balRows)
		dfBalNew =  pd.DataFrame.from_dict(tmpBalList)
		dfBalNew.to_csv(balFile,mode='a',header=False, index=False)

elif ( latestTrend[ind] == 'BUY'):
	#Check if cash balance is > 1000
	if ( cash > 1000 ):

		buyPrice = dfStock.iloc[-1]['Open']
		buyQty = cash/buyPrice
		buyTotal = buyQty*buyPrice
		newCash = cash - buyTotal
		newPrice = dfStock.iloc[-1]['Close']
		newEquityTotal=newPrice*buyQty
		newBal = newCash+newEquityTotal
		changePCT = ((newBal - startBal)/startBal)*100

		txnRows={'Date':execDate, 'Ticker':ticker, 'Type':'BUY','Qty':buyQty,'Price':buyPrice,'Total':buyTotal}
		balRows={'date':execDate,'Cash':newCash,'Qty':buyQty,'PurchasePrice':buyPrice,'CurrentPrice':newPrice,'CurrentEquityTotal':newEquityTotal,
				 'PortfolioTotal':newBal,'PercentageChange':changePCT}

		tmpTxnList.append(txnRows)
		dfTxn =  pd.DataFrame.from_dict(tmpTxnList)

		if not os.path.isfile(txnFile):
			dfTxn.to_csv(txnFile,mode='w',header=True, index=False)
		else:
			dfTxn.to_csv(txnFile,mode='a',header=False, index=False)

		tmpBalList.append(balRows)
		dfBalNew =  pd.DataFrame.from_dict(tmpBalList)
		dfBalNew.to_csv(balFile,mode='a',header=False, index=False)

	else:
		# create balance record only
		newPrice=dfStock.iloc[-1]['Close']
		newEquityTotal=qty*newPrice
		newBal = cash+newEquityTotal
		changePCT = ((newBal - startBal)/startBal)*100

		balRows={'date':execDate,'Cash':cash,'Qty':qty,'PurchasePrice':purPrice,'CurrentPrice':newPrice,'CurrentEquityTotal':newEquityTotal,
				 'PortfolioTotal':newBal,'PercentageChange':changePCT}

		tmpBalList.append(balRows)
		dfBalNew =  pd.DataFrame.from_dict(tmpBalList)
		dfBalNew.to_csv(balFile,mode='a',header=False, index=False)

else:
	newPrice=dfStock.iloc[-1]['Close']
	newEquityTotal=qty*newPrice
	newBal = cash+newEquityTotal
	changePCT = ((newBal - startBal)/startBal)*100
	if ( qty == 0 ):
		purPrice = 0

	balRows={'date':execDate,'Cash':cash,'Qty':qty,'PurchasePrice':purPrice,'CurrentPrice':newPrice,'CurrentEquityTotal':newEquityTotal,
			 'PortfolioTotal':newBal,'PercentageChange':changePCT}

	tmpBalList.append(balRows)
	dfBalNew =  pd.DataFrame.from_dict(tmpBalList)
	dfBalNew.to_csv(balFile,mode='a',header=False, index=False)
