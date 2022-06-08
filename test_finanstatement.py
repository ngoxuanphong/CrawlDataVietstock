from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import warnings
warnings.filterwarnings('ignore')
wd = webdriver.Chrome(executable_path='C:\webdrive\Driver\chromedriver.exe')
# wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def click_to_all_year(wd):
    try:
        element = WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "form-control m-r m-b p1-2"))
        )
        element.click()
        element = WebDriverWait(wd, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[1]/option[12]'))
            )
        element.click()
    finally:
        time.sleep(2)
        pass

user = 'iyr60266@xcoxc.com'
password = 'xuanphong2002'
symbol = 'AAA'
wd.get('https://finance.vietstock.vn/')
wd.maximize_window()
try:
    WebDriverWait(wd, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'btn-request-call-login'))
    )[0].click()
    WebDriverWait(wd, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'txtEmailLogin'))
    )[0].send_keys(user)
    WebDriverWait(wd, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'txtPassword'))
    )[0].send_keys(password)
    WebDriverWait(wd, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'btnLoginAccount'))
    )[0].click()
finally:
    time.sleep(1)
    print('ngu')
    pass
wd.get(f'https://finance.vietstock.vn/{symbol}/tai-chinh.htm?tab=CDKT')
WebDriverWait(wd, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[1]'))
    ).click()
WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[1]/option[12]'))
    ).click()

time.sleep(0.5)
WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[3]'))
    ).click()
WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finance-content"]/div/div/div[2]/div/div[2]/div[1]/div[1]/select[3]/option[1]'))
    ).click()
time.sleep(5)
WebDriverWait(wd, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="expand-overall-CDKT"]/i'))
    ).click()
