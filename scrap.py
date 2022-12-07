from ast import Return
from itertools import product
from lib2to3.pgen2 import driver
from turtle import st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time
import pandas as pd
from openpyxl import Workbook,load_workbook
import xlsxwriter
import openpyxl

wb = Workbook()
ws =wb.active
ws.title = "suff"


PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
act = ActionChains(driver)


driver.get("https://www.sufisland.vercel.app")

print('')
print (driver.title)
print('')
 





for s in range(132):

        for i in range (1,31):

                xpath = '//*[@id="product-list-detail-content-sub-content"]/div/div['
                xpath += str(i)
                xpath += ']/div/div[2]/p[1]/a'

                urunlink=driver.find_element_by_xpath(xpath) 
                href = urunlink.get_attribute('href')
                print(href)
        
                driver.execute_script("window.open('');")
        
                driver.switch_to.window(driver.window_handles[1])
                driver.get(href)
        

                urunad= driver.find_element_by_class_name("product-header-right-head")
                urunozellik = driver.find_element_by_class_name("product-header-explain")
                urunaciklama = driver.find_element_by_class_name("product-long-text-explain")
                urunolcu = driver.find_element_by_class_name("product-specification-content")

                ws.append([urunad.text,urunozellik.text,urunaciklama.text,urunolcu.text])
                wb.save(r'C:\Users\yusuf\Desktop\DataScrap\suff.xlsx')
 
                print(urunolcu.text)
                print('----------------------------------------------------------------------------------------')
                
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        
        time.sleep(2)
        if s < 5:
                sayfa = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dpUrunSayfalama"]/a[7]').click()
        else :
                sayfa = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_dpUrunSayfalama"]/a[8]').click()
        print(s)
        print("SAYFA")
        time.sleep(2)
        