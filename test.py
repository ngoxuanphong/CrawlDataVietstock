import time
import os
import pandas as pd
from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
user = 'iyr60266@xcoxc.com'
password = 'xuanphong2002'
# 'D:\VIS\data_lake\test.py'
# path = 'D:/VIS/DataLake/'
path = '/content/drive/MyDrive/Vietstock/DataLake/'
p1 = f'{path}Phase1/'
p_summary = f'{p1}Summary/'
py = f'{p_summary}Year/'
pq = f'{p_summary}Quarter/'

p1y_BalanceSheet = f'{py}BalanceSheet/'
p1y_IncomStatement =f'{py}IncomStatement/'
p1y_CashFlows = f'{py}CashFlows/'

p1q_BalanceSheet = f'{pq}BalanceSheet/'
p1q_IncomStatement =f'{pq}IncomStatement/'
p1q_CashFlows = f'{pq}CashFlows/'

p1_AdditionalListing = f'{p1}AdditionalListing/'
p1_TreasuryStockTransactions =f'{p1}TreasuryStockTransactions/'
p1_Company_delisting = f'{p1}Company_delisting/'
p1_divident = f'{p1}Dividend/'
p1_CashDividend =f'{p1_divident}CashDividend/'
p1_StockDividend = f'{p1_divident}StockDividend/'

p1_infor = f'{p1}InforCompany/'
all_com = list(pd.read_csv('base/Phase1/List_Com_First (1_4) - Sheet1.csv')['Symbol'])
list_folder=[path, p1, p_summary, py, pq,p1_infor,
            p1q_BalanceSheet, p1q_IncomStatement, p1q_CashFlows,
            p1y_BalanceSheet, p1y_IncomStatement, p1y_CashFlows,
            p1_divident, p1_CashDividend, p1_StockDividend,
            p1_AdditionalListing, p1_TreasuryStockTransactions, p1_Company_delisting]
for folder in list_folder:
    if (os.path.exists(folder) == False) or (os.path.isdir(folder) == False):
        os.mkdir(folder)

web = F.FinanStatement()
web.login(user,password)
import multiprocessing
# web_infor = LI.ListingInformation()
# web_infor.login(user,password)

# web_other = O.Other()
# web_other.login(user,password)

def run1(symbol):
    web_other.CashDividend(symbol).to_csv(f'{p1_CashDividend}{symbol}.csv', index=False)
    web_other.StockDividend(symbol).to_csv(f'{p1_StockDividend}{symbol}.csv', index=False)
    web_other.AdditionalListing(symbol).to_csv(f'{p1_AdditionalListing}{symbol}.csv', index=False)
    web_other.TreasuryStockTransactions(symbol).to_csv(f'{p1_TreasuryStockTransactions}{symbol}.csv', index=False)
    web_other.Company_delisting(symbol).to_csv(f'{p1_Company_delisting}{symbol}.csv', index=False)

def run2(symbol):
    web_infor.lst_infor(symbol).to_csv(f'{p1_infor}{symbol}.csv', index=False)

for i in range(2,3):
    symbol = all_com[i]
    print(symbol)
    web.BalanceSheet(symbol, 'NAM').to_csv(f'{p1y_BalanceSheet}{symbol}.csv', index = False)
    web.IncomStatement(symbol, 'NAM').to_csv(f'{p1y_IncomStatement}{symbol}.csv', index = False)
    web.CashFlows(symbol, 'NAM').to_csv(f'{p1y_CashFlows}{symbol}.csv', index = False)

    # web.BalanceSheet(symbol, 'QUY').to_csv(f'{p1q_BalanceSheet}{symbol}.csv', index = False)
    # web.IncomStatement(symbol, 'QUY').to_csv(f'{p1q_IncomStatement}{symbol}.csv', index = False)
    # web.CashFlows(symbol, 'QUY').to_csv(f'{p1q_CashFlows}{symbol}.csv', index = False)


# web_other.Listing().to_csv('Listing.csv', index = False)
# web_other.Delisting().to_csv('Delisting.csv', index = False)

# def multip():
#     Symbol = all_com
#     pool = multiprocessing.Pool(processes=4)
#     for symbol in Symbol:
#       pool.apply_async(run1,args=(symbol,))
#     pool.close()
#     pool.join()

# if __name__ == '__main__':
#     multip()