from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

class setup():
    def __init__(self):
        self.link = 'https://finance.vietstock.vn/'
        # self.reset_driver('C:\webdrive\Driver\chromedriver.exe')
        self.reset_driver('C:\webdrive\Driver\msedgedriver.exe')
    def reset_colab(self):
        from selenium import webdriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    def reset_driver(self, path = 'C:\webdrive\Driver\chromedriver.exe'):
        # self.driver = webdriver.Chrome(executable_path=path)
        self.driver = webdriver.ChromiumEdge(executable_path=path)
    def login(self, user, password):
        self.driver.get(self.link)
        self.driver.maximize_window() 
        try:       
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.ID, 'btn-request-call-login'))
            )[0].click()
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.ID, 'txtEmailLogin'))
            )
            element[0].send_keys(user)

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.ID, 'txtPassword'))
            )
            element[0].send_keys(password)

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.ID, 'btnLoginAccount'))
            )
            element[0].click()
        finally:
            time.sleep(1)
            pass
        
        
