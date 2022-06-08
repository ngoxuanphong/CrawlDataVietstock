from base import Login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

class ListingInformation(Login.setup):
    def __init__(self) -> None:
        super().__init__()
    def lst_infor(self, symbol):
        link = f'https://finance.vietstock.vn/{symbol}/ho-so-doanh-nghiep.htm'
        self.getlink(link)
        data = self.getTableInfor()
        return data
    def getTableInfor(self):
        page_source = self.driver.page_source
        page = BeautifulSoup(page_source, 'html.parser')
        list_table = page.find_all('table', {'class':'table table-hover'})
        if len(list_table) == 0: 
            return pd.DataFrame()
        return pd.read_html(str(list_table))[0]
    def getlink(self, link):
        try:
            self.driver.implicitly_wait(10)
            self.driver.get(link)
        except:
            print('hi')
            self.driver.refresh()
            self.getlink(link)