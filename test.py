import time
import os
import pandas as pd
from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
import json
user = 'iyr60266@xcoxc.com'
password = 'xuanphong2002'
# 'D:\VIS\data_lake\test.py'
path = 'D:/VIS/DataLake/'
# path = '/content/drive/MyDrive/Vietstock/DataLake/'
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
all_com = pd.read_excel('base/Phase1/List_Com_First (1_4).xlsx')['Symbol']
all_com = list(all_com)
list_folder=[path, p1, p_summary, py, pq,p1_infor,
            p1q_BalanceSheet, p1q_IncomStatement, p1q_CashFlows,
            p1y_BalanceSheet, p1y_IncomStatement, p1y_CashFlows,
            p1_divident, p1_CashDividend, p1_StockDividend,
            p1_AdditionalListing, p1_TreasuryStockTransactions, p1_Company_delisting]
for folder in list_folder:
    if (os.path.exists(folder) == False) or (os.path.isdir(folder) == False):
        os.mkdir(folder)

# web = F.FinanStatement()
# web.login(user,password)
import multiprocessing
# web_infor = LI.ListingInformation()
# web_infor.login(user,password)

web_other = O.Other()
web_other.login(user,password)

def run1(symbol):
    web_other.CashDividend(symbol).to_csv(f'{p1_CashDividend}{symbol}.csv', index=False)
    web_other.StockDividend(symbol).to_csv(f'{p1_StockDividend}{symbol}.csv', index=False)
    web_other.AdditionalListing(symbol).to_csv(f'{p1_AdditionalListing}{symbol}.csv', index=False)
    web_other.TreasuryStockTransactions(symbol).to_csv(f'{p1_TreasuryStockTransactions}{symbol}.csv', index=False)
    web_other.Company_delisting(symbol).to_csv(f'{p1_Company_delisting}{symbol}.csv', index=False)

def run2(symbol):
    web_infor.lst_infor(symbol).to_csv(f'{p1_infor}{symbol}.csv', index=False)

# for i in range(489,len(all_com)):
#     symbol = all_com[i]
#     print(i, symbol)
#     web.BalanceSheet(symbol, 'NAM').to_csv(f'{p1y_BalanceSheet}{symbol}.csv', index = False)
#     web.IncomStatement(symbol, 'NAM').to_csv(f'{p1y_IncomStatement}{symbol}.csv', index = False)
    # web.CashFlows(symbol, 'NAM').to_csv(f'{p1y_CashFlows}{symbol}.csv', index = False)

    # web.BalanceSheet(symbol, 'QUY').to_csv(f'{p1q_BalanceSheet}{symbol}.csv', index = False)
    # web.IncomStatement(symbol, 'QUY').to_csv(f'{p1q_IncomStatement}{symbol}.csv', index = False)
    # web.CashFlows(symbol, 'QUY').to_csv(f'{p1q_CashFlows}{symbol}.csv', index = False)


# data_false = json.load(open('false.json'))
# for symbol in data_false[p1q_BalanceSheet]:
#     web.BalanceSheet(symbol, 'QUY').to_csv(f'{p1q_BalanceSheet}{symbol}.csv', index = False)
# for symbol in data_false[p1y_BalanceSheet]:
#     web.BalanceSheet(symbol, 'NAM').to_csv(f'{p1y_BalanceSheet}{symbol}.csv', index = False)
# for symbol in data_false[p1q_IncomStatement]:
#     web.IncomStatement(symbol, 'QUY').to_csv(f'{p1q_IncomStatement}{symbol}.csv', index = False)
# for symbol in data_false[p1y_IncomStatement]:
#     web.IncomStatement(symbol, 'NAM').to_csv(f'{p1y_IncomStatement}{symbol}.csv', index = False)
# for symbol in data_false[p1q_CashFlows]:
#     print(symbol)
#     web.CashFlows(symbol, 'QUY').to_csv(f'{p1q_CashFlows}{symbol}.csv', index = False)
# for symbol in data_false[p1y_CashFlows]:
#     print(symbol)
#     web.CashFlows(symbol, 'NAM').to_csv(f'{p1y_CashFlows}{symbol}.csv', index = False)

# web.CashFlows('AAM', 'QUY').to_csv(f'{p1q_CashFlows}AAM.csv', index = False)
# web.CashFlows('AAM', 'QUY').to_csv(f'{p1q_CashFlows}AAM.csv', index = False)
# web.CashFlows('AAM', 'QUY').to_csv(f'{p1q_CashFlows}AAM.csv', index = False)
data_false = json.load(open('false2.json'))
for symbol in data_false[p1_CashDividend]:
    web_other.CashDividend(symbol).to_csv(f'{p1_CashDividend}{symbol}.csv', index=False)
for symbol in data_false[p1_StockDividend]:
    web_other.StockDividend(symbol).to_csv(f'{p1_StockDividend}{symbol}.csv', index=False)
for symbol in data_false[p1_AdditionalListing]:
    web_other.AdditionalListing(symbol).to_csv(f'{p1_AdditionalListing}{symbol}.csv', index=False)
for symbol in data_false[p1_TreasuryStockTransactions]:
    web_other.TreasuryStockTransactions(symbol).to_csv(f'{p1_TreasuryStockTransactions}{symbol}.csv', index=False)
for symbol in data_false[p1_Company_delisting]:
    web_other.Company_delisting(symbol).to_csv(f'{p1_Company_delisting}{symbol}.csv', index=False)

# web.CashFlows('24H', 'QUY').to_csv(f'{p1q_CashFlows}24H.csv', index = False)

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
# list_bs_year_false = ['ACV', 'AME', 'AMV', 'APF', 'ATB', 'CLG', 'DNY']
list_bs_year_false = ['ABS', 'AUM', 'BAM', 'CLL', 'CTI']
# list_bs_year_false = ['AAA', 'AAT', 'AAV', 'ABC', 'ABS', 'ABT', 'ACC', 'ADC', 'ADP', 'ADS', 'AFX', 'AGC', 'AGF', 'ALC', 'ALP', 'ALT', 'ALV', 'AMS', 'AMV', 'APC', 'APH', 'API', 'ASG', 'AST', 'ATB', 'AUM', 'AVC', 'B82', 'BAM', 'BAS', 'BAX', 'BBL', 'BBM', 'BCG', 'BCI', 'BDB', 'BDC', 'BDG', 'BDP', 'BDT', 'BDW', 'BED', 'BEL', 'BFC', 'BGW', 'BHA', 'BKG', 'BLF', 'BMP', 'BMV', 'BNC', 'BNW', 'BPC', 'BRC', 'BTC', 'BTV', 'C69', 'CAD', 'CAG', 'CEC', 'CIG', 'CLL', 'CLM', 'CLX', 'CNG', 'CSM', 'CT6', 'CTI', 'CTT', 'DAE', 'DAT', 'DGL', 'DHC', 'DIH', 'DP1', 'DPC', 'DST', 'DTD', 'DTI']
list_bs_year_false_ic = ['ABR', 'ACG', 'AGP', 'AMS', 'ATA', 'BAM', 'BBL', 'BPC', 'BPW', 'BRR', 'BSQ', 'BTB', 'CAD', 'CEC', 'CTF', 'DBC', 'DDN', 'DGC', 'DHG', 'DHL', 'DLD', 'DLG', 'DPS', 'DRI']
list_bs_year_false_ic = ['CAD']
# for symbol in ['AAA', 'BHN', 'CCP']:
    # web.IncomStatement(symbol, 'NAM').to_csv(f'base/Phase1/false/{symbol}.csv', index = False)
    # web.CashFlows(symbol, 'QUY').to_csv(f'base/Phase1/false/{symbol}.csv', index = False)
    # web.BalanceSheet(symbol, 'NAM').to_csv(f'base/Phase1/false/{symbol}.csv', index = False)
list_infor_false = ['24H', 'ABG', 'AGB', 'AGE', 'ALC', 'ALS', 'ATC', 'ATP', 'AVG', 'BAV', 'BBL', 'BCH', 'BCO', 'BGT', 'BJC', 'BNC', 'BPT', 'BRM', 'BRV', 'BTA', 'BTJ', 'BTL', 'BVA', 'BVC', 'C42', 'CAF', 'CAR', 'CBV', 'CC7', 'CDV', 'CGC', 'CIE', 'CIV', 'CJV', 'CK8', 'CKI', 'CKM', 'CNS', 'CNX', 'CPT', 'CRV', 'CTE', 'CXC', 'DBV', 'DHQ', 'DKW', 'DLM', 'DLX', 'DMH', 'DNG', 'DNV', 'DO3', 'DTF', 'DTJ']


# for symbol in list_infor_false:
#      web_infor.lst_infor(symbol).to_csv(f'base/Phase1/false/{symbol}.csv', index = False)