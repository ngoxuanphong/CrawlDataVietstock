import time
import os
import pandas as pd
from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
user = 'iyr60266@xcoxc.com'
password = 'xuanphong2002'

path = 'DataLake/'
p1 = f'{path}Phase1/'

p1_BalanceSheet = f'{p1}BalanceSheet/'
p1_IncomStatement =f'{p1}IncomStatement/'
p1_CashFlows = f'{p1}CashFlows/'

p1_AdditionalListing = f'{p1}AdditionalListing/'
p1_CashDividend =f'{p1}CashDividend/'
p1_StockDividend = f'{p1}StockDividend/'
p1_TreasuryStockTransactions =f'{p1}TreasuryStockTransactions/'
p1_Company_delisting = f'{p1}Company_delisting/'

p1_infor = f'{p1}InforCompany/'
all_com = list(pd.read_csv('DataLake/Phase1/List_Com_First (1_4) - Sheet1.csv')['Symbol'])
list_folder=[path, p1, p1_AdditionalListing,p1_BalanceSheet,p1_CashDividend,
            p1_CashFlows,p1_Company_delisting,p1_IncomStatement,p1_infor,
            p1_StockDividend,p1_TreasuryStockTransactions]
for folder in list_folder:
    if (os.path.exists(folder) == False) or (os.path.isdir(folder) == False):
        os.mkdir(folder)


# web = F.FinanStatement()
# web.login(user,password)
web_other = O.Other()
web_other.login(user,password)
# web_infor = LI.ListingInformation()
# web_infor.login(user,password)
# all_com = ['24H']
for symbol in all_com:
    print(symbol)
    # web.BalanceSheet(symbol).to_csv(f'{p1_BalanceSheet}{symbol}.csv', index = False)
    # web.IncomStatement(symbol).to_csv(f'{p1_IncomStatement}{symbol}.csv', index = False)
    # web.CashFlows(symbol).to_csv(f'{p1_CashFlows}{symbol}.csv', index = False)
    web_other.CashDividend(symbol).to_csv(f'{p1_CashDividend}{symbol}.csv', index=False)
    web_other.StockDividend(symbol).to_csv(f'{p1_StockDividend}{symbol}.csv', index=False)
    web_other.AdditionalListing(symbol).to_csv(f'{p1_AdditionalListing}{symbol}.csv', index=False)
    web_other.TreasuryStockTransactions(symbol).to_csv(f'{p1_TreasuryStockTransactions}{symbol}.csv', index=False)
    web_other.Company_delisting(symbol).to_csv(f'{p1_Company_delisting}{symbol}.csv', index=False)


# symbols = ['A32','AAM','AAA', 'VNM', 'VHM']
# symbols = ['VPH']
# for symbol in symbols:
# web_other.Listing().to_csv('Listing.csv', index = False)
# web_other.Delisting().to_csv('Delisting.csv', index = False)