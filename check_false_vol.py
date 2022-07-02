import time
import os
import pandas as pd
from base import Login as L,FinanStatement as F, ListingInformation as LI, Other as O
import json
user = 'mfl26068@xcoxc.com'
password = 'xuanphong2002'

p = 'A:/DataLake/Volume/'
p_Volume = f'{p}Volume/'

p_TreasuryShares = f'{p}Volume/3c.Vietstock_CoPhieuQuy/'
p_VolumeAdditionalEvents = f'{p}Volume/3b.Vietstock_NiemYet/'
p_VolumeNow = f'{p}Volume/3a.Vietstock_InforCompany.csv/'
p_DataUpDownExchange = f'{p}DataUpDownExchange/'
p_DataDownExchange = f'{p}DataUpDownExchange/DataDownExchange/'
all_com = pd.read_csv('base/Phase1/AllCompanyDone.csv')['Symbol']

web = O.Other()
web.login(user,password)

def run2():
    data_false = json.load(open('false2.json'))

    for symbol in data_false[p_VolumeAdditionalEvents]:
        web.AdditionalListing(symbol).to_csv(f'{p_VolumeAdditionalEvents}{symbol}.csv', index=False)
    for symbol in data_false[p_TreasuryShares]:
        web.TreasuryStockTransactions(symbol).to_csv(f'{p_TreasuryShares}{symbol}.csv', index=False)
    for symbol in data_false[p_DataDownExchange]:
        web.Company_delisting(symbol).to_csv(f'{p_DataDownExchange}{symbol}.csv', index=False)
    for symbol in data_false[p_VolumeNow]:
        web.lst_infor(symbol).to_csv(f'{p_VolumeNow}{symbol}.csv', index=False)
run2()