import time
import os
import pandas as pd
from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
import json
user = 'mfl26068@xcoxc.com'
password = 'xuanphong2002'

p = 'A:/DataLake/Phase3/'
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
p_DataUpDownExchange = f'{p}DataUpDownExchange/'
p_DataDownExchange = f'{p}DataUpDownExchange/DataDownExchange/'


all_com = pd.read_excel('base/Phase1/List_Com_Phase3.xlsx')['Symbol']
all_com = list(all_com)


# web = F.FinanStatement()
web = O.Other()
web.login(user,password)

def list_col(all_com, path, list_col, list_false):
    list_ = []
    for i in all_com:
        # if i not in list_com_nothing:
            # print(i, end='  ')
            try:
                data = pd.read_csv(path+i+'.csv')
                if len(data.index) == 0 and len(data.columns) == 1:
                    continue
                if len(data.index) not in list_col:
                    # print(len(data), end= '  ')
                    list_.append(i)
                else:
                    # print('hi')
                    if ('Year' in path) and ('/' in str(list(data.columns))):
                        list_.append(i)
                        # print('hihi')
                    elif ('Quarter' in path) and ('/' not in str(list(data.columns))):
                        # print(i)
                        list_.append(i)
                    elif len(data.columns) <=3:
                        list_.append(i)
            except:
                # print(i)
                list_.append(i)
                pass
    print(len(list_))
    list_false[str(path)] = list_
    return list_false

def run1():
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

def run2():
    data_false = json.load(open('false2.json'))
    # for symbol in data_false[p_DividendCash]:
    #     web.CashDividend(symbol).to_csv(f'{p_DividendCash}{symbol}.csv', index=False)
    # for symbol in data_false[p_DividendShares]:
    #     web.StockDividend(symbol).to_csv(f'{p_DividendShares}{symbol}.csv', index=False)
    # for symbol in data_false[p_TreasuryShares]:
    #     web.TreasuryStockTransactions(symbol).to_csv(f'{p_TreasuryShares}{symbol}.csv', index=False)
    for symbol in data_false[p_VolumeAdditionalEvents]:
        web.AdditionalListing(symbol).to_csv(f'{p_VolumeAdditionalEvents}{symbol}.csv', index=False)
    for symbol in data_false[p_VolumeNow]:
        web.lst_infor(symbol).to_csv(f'{p_VolumeNow}{symbol}.csv', index=False)
    for symbol in data_false[p_DataDownExchange]:
        web.Company_delisting(symbol).to_csv(f'{p_DataDownExchange}{symbol}.csv', index=False)

run2()