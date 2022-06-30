from base import Login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import TimeoutException
class Other(Login.setup):
    def __init__(self) -> None:
        super().__init__()
    def CashDividend(self, symbol):
        link = f'https://finance.vietstock.vn/lich-su-kien.htm?page=1&tab=1&code={symbol}&group=13'
        data =self.getTable(link)
        return data
    def BonusShare(self, symbol):
        link = f'https://finance.vietstock.vn/lich-su-kien.htm?page=1&tab=1&code={symbol}&group=14'
        data = self.getTable(link)
        return data
    def StockDividend(self, symbol):
        link = f'https://finance.vietstock.vn/lich-su-kien.htm?page=1&tab=1&code={symbol}&group=15'
        data = self.getTable(link)
        return data
    def AdditionalListing(self, symbol):
        link = f'https://finance.vietstock.vn/lich-su-kien.htm?page=1&tab=2&code={symbol}&group=21#'
        data = self.getTable(link)
        return data
    def TreasuryStockTransactions(self, symbol):
        link = f'https://finance.vietstock.vn/giao-dich-noi-bo?page=1&tab=5&code={symbol}'
        data = self.getTable(link)
        return data
    def Company_delisting(self, symbol):
        link = f'https://finance.vietstock.vn/lich-su-kien.htm?page=1&tab=2&code={symbol}&group=18'
        data = self.getTable(link)
        return data
    def Listing(self):
        link = 'https://finance.vietstock.vn/doanh-nghiep-a-z?page=1'
        data = self.getTable(link)
        return data
    def Delisting(self):
        link = 'https://finance.vietstock.vn/doanh-nghiep-a-z/huy-niem-yet?page=1'
        data = self.getTable(link)
        return data
    def getlink(self, link):
        try:
            self.driver.set_page_load_timeout(10)
            self.driver.get(link)
        except:
            print('hi')
            # self.driver.refresh()
            self.getlink(link)
    def getTable(self, link):
        self.getlink(link)
        time.sleep(1)
        page_source = self.driver.page_source
        page = BeautifulSoup(page_source, 'html.parser')
        number_pages = self.getNumberPage(page)
        # print(number_pages)
        if number_pages > 1:
            data = self.getTableInfor(page)
            for number_page in range(2, number_pages+1):
                # if method == 'number_page'
                data_new = self.getNextTable(number_page, link)
                data= pd.concat([data, data_new])
            return data
        else: return self.getTableInfor(page)

    def getNextTable(self, number_page, link):
        # self.driver.get(link.replace('page=1', f'page={number_page}'))
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "btn-page-next"))
            ).click()
        finally: 
            time.sleep(1)
            pass
        page = BeautifulSoup(self.driver.page_source, 'html.parser')
        return self.getTableInfor(page)

    def getTableInfor(self, page):
        time.sleep(1)
        list_table = page.find_all('table', {'class':
        'table table-striped table-bordered table-hover table-middle pos-relative m-b'})
        try: return pd.read_html(str(list_table))[0]
        except: return pd.DataFrame(columns=[i.text for i in list_table])
            
    def getNumberPage(self, page):
        try:number_pages = int(page.find_all('span', {'class':'m-r-xs'})[1].find_all('span')[1].text)
        except: number_pages = 0
        return int(number_pages)
    # def getNumberPage(self):

    def lst_infor(self, symbol):
        link = f'https://finance.vietstock.vn/{symbol}/ho-so-doanh-nghiep.htm'
        self.getlink(link)
        data = self.getTableInforcom()
        return data
    def getTableInforcom(self):
        page_source = self.driver.page_source
        page = BeautifulSoup(page_source, 'html.parser')
        list_table = page.find_all('table', {'class':'table table-hover'})
        if len(list_table) == 0: 
            return pd.DataFrame({'Nothing':[]})
        return pd.read_html(str(list_table))[0]
