import time
import os
import pandas as pd
from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
import json
user = 'iyr60266@xcoxc.com'
password = 'xuanphong2002'

p = 'D:/VIS/DataLake/Phase2/'
ps_finan = f'{p}Financial/'
ps_y = f'{ps_finan}Year/'
ps_q = f'{ps_finan}Quarter/'

ps_y_BS = f'{ps_y}BalanceSheet/'
ps_y_CF = f'{ps_y}CashFlow/'
ps_y_IS = f'{ps_y}IncomeStatement/'

ps_q_BS = f'{ps_q}BalanceSheet/'
ps_q_CF = f'{ps_q}CashFlow/'
ps_q_IS = f'{ps_q}IncomeStatement/'

p_Dividend = f'{p}Dividend/'
p_Volume = f'{p}Volume/'

p_DividendCash = f'{p}Dividend/DividendCash/'
p_DividendShares = f'{p}Dividend/DividendShares/'
p_TreasuryShares = f'{p}Volume/TreasuryShares/'
p_VolumeAdditionalEvents = f'{p}Volume/VolumeAdditionalEvents/'
p_VolumeNow = f'{p}Volume/VolumeNow.csv/'


all_com = pd.read_excel('base/Phase1/List_Com_Phase2.xlsx')['Symbol']
all_com = list(all_com)
list_folder=[p, ps_finan, ps_y, ps_q, 
            ps_y_BS, ps_y_CF, ps_y_IS, 
            ps_q_BS, ps_q_CF, ps_q_IS,
            p_Dividend, p_Volume, 
            p_DividendCash, p_DividendShares, p_TreasuryShares, p_VolumeAdditionalEvents, p_VolumeNow]
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


data_false = json.load(open('false.json'))
for symbol in data_false[ps_y_BS]:
    web.BalanceSheet(symbol, 'NAM').to_csv(f'{ps_y_BS}{symbol}.csv', index = False)
for symbol in data_false[ps_y_IS]:
    web.IncomStatement(symbol, 'NAM').to_csv(f'{ps_y_IS}{symbol}.csv', index = False)
for symbol in data_false[ps_y_CF]:
    web.CashFlows(symbol, 'NAM').to_csv(f'{ps_y_CF}{symbol}.csv', index = False)

for symbol in data_false[ps_q_BS]:
    web.BalanceSheet(symbol, 'QUY').to_csv(f'{ps_q_BS}{symbol}.csv', index = False)
for symbol in data_false[ps_q_IS]:
    web.IncomStatement(symbol, 'QUY').to_csv(f'{ps_q_IS}{symbol}.csv', index = False)
for symbol in data_false[ps_q_CF]:
    web.CashFlows(symbol, 'QUY').to_csv(f'{ps_q_CF}{symbol}.csv', index = False)

# web.CashFlows('AAM', 'QUY').to_csv(f'{p1q_CashFlows}AAM.csv', index = False)
# web.CashFlows('AAM', 'QUY').to_csv(f'{p1q_CashFlows}AAM.csv', index = False)
# web.CashFlows('AAM', 'QUY').to_csv(f'{p1q_CashFlows}AAM.csv', index = False)
# data_false = json.load(open('false2.json'))
# for symbol in data_false[p1_CashDividend]:
#     web_other.CashDividend(symbol).to_csv(f'{p1_CashDividend}{symbol}.csv', index=False)
# for symbol in data_false[p1_StockDividend]:
#     web_other.StockDividend(symbol).to_csv(f'{p1_StockDividend}{symbol}.csv', index=False)
# for symbol in data_false[p1_AdditionalListing]:
#     web_other.AdditionalListing(symbol).to_csv(f'{p1_AdditionalListing}{symbol}.csv', index=False)
# for symbol in data_false[p1_TreasuryStockTransactions]:
#     web_other.TreasuryStockTransactions(symbol).to_csv(f'{p1_TreasuryStockTransactions}{symbol}.csv', index=False)
# for symbol in data_false[p1_Company_delisting]:
#     web_other.Company_delisting(symbol).to_csv(f'{p1_Company_delisting}{symbol}.csv', index=False)

# web.CashFlows('24H', 'QUY').to_csv(f'{p1q_CashFlows}24H.csv', index = False)

# web_other.Listing().to_csv('Listing.csv', index = False)
# web_other.Delisting().to_csv('Delisting.csv', index = False)


# list_bs_year_false = ['ACV', 'AME', 'AMV', 'APF', 'ATB', 'CLG', 'DNY']
# list_bs_year_false = ['AC4', 'ATD', 'BBH', 'BTJ', 'BXT', 'CE1', 'CNA', 'DSS']
# for symbol in list_bs_year_false:
#     web.IncomStatement(symbol, 'NAM').to_csv(f'base/Phase1/false/{symbol}.csv', index = False)
    # web.CashFlows(symbol, 'QUY').to_csv(f'base/Phase1/false/{symbol}.csv', index = False)
    # web.BalanceSheet(symbol, 'NAM').to_csv(f'base/Phase1/false/{symbol}.csv', index = False)
# list_infor_false = ['24H', 'ABG', 'AGB', 'AGE', 'ALC', 'ALS', 'ATC', 'ATP', 'AVG', 'BAV', 'BBL', 'BCH', 'BCO', 'BGT', 'BJC', 'BNC', 'BPT', 'BRM', 'BRV', 'BTA', 'BTJ', 'BTL', 'BVA', 'BVC', 'C42', 'CAF', 'CAR', 'CBV', 'CC7', 'CDV', 'CGC', 'CIE', 'CIV', 'CJV', 'CK8', 'CKI', 'CKM', 'CNS', 'CNX', 'CPT', 'CRV', 'CTE', 'CXC', 'DBV', 'DHQ', 'DKW', 'DLM', 'DLX', 'DMH', 'DNG', 'DNV', 'DO3', 'DTF', 'DTJ']
