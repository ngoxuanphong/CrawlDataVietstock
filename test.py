from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
import multiprocessing
import pandas as pd
import json
import time
import os
user = 'mfl26068@xcoxc.com'
password = 'xuanphong2002'

p = 'A:/DataLake/Volume/'
ps_finan = f'{p}Financial/'
ps_y = f'{ps_finan}Year/'
ps_q = f'{ps_finan}Quarter/'

ps_y_BS = f'{ps_y}BalanceSheet/'
ps_y_IS = f'{ps_y}IncomeStatement/'
ps_y_CF = f'{ps_y}CashFlow/'

ps_q_BS = f'{ps_q}BalanceSheet/'
ps_q_IS = f'{ps_q}IncomeStatement/'
ps_q_CF = f'{ps_q}CashFlow/'

p_Dividend = f'{p}Dividend/'
p_Volume = f'{p}Volume/'

p_DividendCash = f'{p}Dividend/DividendCash/'
p_DividendShares = f'{p}Dividend/DividendShares/'
p_TreasuryShares = f'{p}Volume/TreasuryShares/'
p_VolumeAdditionalEvents = f'{p}Volume/VolumeAdditionalEvents/'
p_VolumeNow = f'{p}Volume/VolumeNow.csv/'
p_DataUpDownExchange = f'{p}DataUpDownExchange/'
p_DataDownExchange = f'{p}DataUpDownExchange/DataDownExchange/'
p_BonusShare = f'{p}Dividend/BonusShare/'

# all_com = pd.read_excel('base/Phase1/List_Com_Phase4.xlsx')['Symbol']
all_com = pd.read_csv('base/Phase1/AllCompanyDone.csv')['Symbol']
all_com = list(all_com)
list_folder=[p, ps_finan, ps_y, ps_q, 
            ps_y_BS, ps_y_CF, ps_y_IS, 
            ps_q_BS, ps_q_CF, ps_q_IS,
            p_Dividend, p_Volume, p_BonusShare,
            p_DividendCash, p_DividendShares, p_TreasuryShares, p_VolumeAdditionalEvents, p_VolumeNow,
            p_DataUpDownExchange,p_DataDownExchange]
for folder in list_folder:
    if (os.path.exists(folder) == False) or (os.path.isdir(folder) == False):
        os.mkdir(folder)

# web = F.FinanStatement()
web = O.Other()
web.login(user,password)

def run1(symbol):
    # web.CashDividend(symbol).to_csv(f'{p_DividendCash}{symbol}.csv', index=False)
    # web.StockDividend(symbol).to_csv(f'{p_DividendShares}{symbol}.csv', index=False)
    web.AdditionalListing(symbol).to_csv(f'{p_VolumeAdditionalEvents}{symbol}.csv', index=False)
    web.TreasuryStockTransactions(symbol).to_csv(f'{p_TreasuryShares}{symbol}.csv', index=False)
    web.Company_delisting(symbol).to_csv(f'{p_DataDownExchange}{symbol}.csv', index=False)
    web.lst_infor(symbol).to_csv(f'{p_VolumeNow}{symbol}.csv', index=False)
    # web.BonusShare(symbol).to_csv(f'{p_BonusShare}{symbol}.csv', index=False)

def run3(symbol):
    web.BalanceSheet(symbol, 'NAM').to_csv(f'{ps_y_BS}{symbol}.csv', index = False)
    web.IncomStatement(symbol, 'NAM').to_csv(f'{ps_y_IS}{symbol}.csv', index = False)
    web.CashFlows(symbol, 'NAM').to_csv(f'{ps_y_CF}{symbol}.csv', index = False)

    web.BalanceSheet(symbol, 'QUY').to_csv(f'{ps_q_BS}{symbol}.csv', index = False)
    web.IncomStatement(symbol, 'QUY').to_csv(f'{ps_q_IS}{symbol}.csv', index = False)
    web.CashFlows(symbol, 'QUY').to_csv(f'{ps_q_CF}{symbol}.csv', index = False)

# run1('BCP')
def multip():
    pool = multiprocessing.Pool(processes=4)
    for symbol in all_com:
      pool.apply_async(run1,args=(symbol,))
    pool.close()
    pool.join()

if __name__ == '__main__':
    multip()