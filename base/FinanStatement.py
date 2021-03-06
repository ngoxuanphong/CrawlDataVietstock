from base import Login
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
class FinanStatement(Login.setup):
    def __init__(self) -> None:
        super().__init__()

    def BalanceSheet(self,symbol, PeriodType):
        link = f'https://finance.vietstock.vn/{symbol}/tai-chinh.htm?tab=CDKT'
        return self.table_lake(link, PeriodType)

    def IncomStatement(self, symbol,PeriodType):
        link = f'https://finance.vietstock.vn/{symbol}/tai-chinh.htm?tab=KQKD'
        return self.table_lake(link, PeriodType)

    def CashFlows(self, symbol, PeriodType):
        link = f'https://finance.vietstock.vn/{symbol}/tai-chinh.htm?tab=LC'
        return self.table_lake(link, PeriodType)
    
    def getlink(self, link):
        try:
            self.driver.set_page_load_timeout(10)
            self.driver.get(link)
        except:
            print('hi')
            # self.driver.refresh()
            self.getlink(link)
    def table_lake(self, link, PeriodType):
        self.getlink(link)
        if self.check_page() == True:
            self.click_to_all_year(PeriodType)
            time.sleep(1)
            data = self.getTable()
        else: data = pd.DataFrame({'Nothing':[]})
        return data

    def check_page(self):
        page_sourse = self.driver.page_source
        page = BeautifulSoup(page_sourse, "html.parser")
        check = page.find_all('div', {'class':'container m-b'})
        if len(check) == 0:
            return True
    def click_to_all_year(self, PeriodType):
        try:
            try:
                select = Select(self.driver.find_element_by_name('period'))
                select.select_by_value('-1')
                time.sleep(0.5)

                select = Select(self.driver.find_element_by_name('UnitDong'))
                select.select_by_value('1000')
                time.sleep(0.5)
                
                select = Select(self.driver.find_element_by_name('PeriodType'))
                select.select_by_value(PeriodType)
                time.sleep(2)
            except: pass
            try:
                element = WebDriverWait(self.driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="expand-overall-CDKT"]/i'))
                    )
                element.click()
                time.sleep(2)
                element.click()
                time.sleep(0.3)
            except: pass
        finally:
            # time.sleep()
            pass
    def getTable(self):
        page_sourse = self.driver.page_source
        page = BeautifulSoup(page_sourse, "html.parser")
        list_table = page.find_all(
            "table", {"class": "table table-hover"})
        try:
            data = pd.read_html(str(list_table))
            # print(len(data))
            # print(data[0], data[1])
            try:
                data = pd.concat([data[0], data[1]])
            except:
                data = data[0]
        except:
            data = pd.DataFrame({'Nothing':[]})
        return data