import time
import sys,os, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import gmtime, strftime
from datetime import datetime, timedelta, date
from six.moves.html_parser import HTMLParser
from lxml.html import fromstring
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import xlrd
import re

global driver;

chromedriver = 'chromedriver.exe';
# Ultrasurf = 'Ultrasurf.crx';
time.sleep(5)

def junck(value):
    value = re.sub(r"\[","",str(value))
    value = re.sub(r"\]","",str(value))
    value = re.sub(r"\"","",str(value))
    value = re.sub(r"\'","",str(value))
    value = re.sub(r"\(","",str(value))
    value = re.sub(r"\)","",str(value))
    # value = re.sub(r"\\\\","",str(value))
    # value = re.sub(r"\@","",str(value))
    value = re.sub(r"\   ","",str(value))

    return value
	
excel_sheet = xlrd.open_workbook("Input.xlsx")
sheet1= excel_sheet.sheet_by_name('Sheet1')

def func1(Id,Sku,content1):
    try:
        
        content = content1.encode('utf-8')
        content = re.sub(r"\\n", "",str(content))
        content = re.sub(r"\\t", "",str(content))
        content=re.sub(r'&amp;','&',str(content))
        

        rest_Url=re.findall('<a\ href\=\"\/fips\/\s*([^>]*?)\s*\/\"\>', str(content), re.I)


        for i in rest_Url:
            link=i
            # print(link)
            
            f=open("Localities_Out.txt", 'a', encoding="utf-8")
            f.write(str(Id)+"\t"+str(Sku)+"\t"+str('https://clustrmaps.com/fips/')+str(link)+"\n")
            f.close()
            # time.sleep(5)			

    
    except Exception as e: 
        print(e)
                
        f=open("No_result.txt", 'a', encoding="utf-8")
        f.write(str(Id)+"\t"+str(Sku)+"\n")
        f.close() 


def func(driver,Id,Sku,Link):
    try:           
        response = driver.get("view-source:"+str(Link))
        time.sleep(5)
        
        # wait = WebDriverWait(driver, 10)

        # men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/nav')))
       
        content1 = driver.page_source
        
        content1 = re.sub(r"<[^<>]*?>","",str(content1))
        content1 = re.sub(r"&lt;","<",str(content1))
        content1 = re.sub(r"&gt;",">",str(content1))
        
        driver.delete_all_cookies()	
         	
        # if urls_processed >= urls_per_session:
            # driver.close()
            # driver.quit()
            # chrome_options = Options()
            # chrome_options.add_extension(Ultrasurf)
            # driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
            # driver.delete_all_cookies()
            # time.sleep(1)
            # urls_processed = 0    

        file_name=str(Id)+".html"
        print(file_name)
        time.sleep(2)
        
        # a =open(file_name,"wb")
        # a.write(content1)
        # a.close()
        
        check=re.findall('<h1>Access Denied<\/h1>', str(content1), re.I)
        if(check):
            
            driver.close()
            driver.quit()
            chrome_options = Options()
            # chrome_options.add_extension(Ultrasurf)
            driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
            driver.delete_all_cookies()
            time.sleep(1)
            urls_processed = 0    
        
            func(driver,Id,Sku,Link)
        
        else:
            func1(Id,Sku,content1)
        
        
        
      
    except Exception as e: 
        print(e)
        
        driver.close()
        driver.quit()
        chrome_options = Options()
        # chrome_options.add_extension(Ultrasurf)
        driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
        driver.delete_all_cookies()
        time.sleep(2)
        urls_processed = 0    
    
        func(driver,Id,Sku,Link)


chrome_options = Options()
# chrome_options.add_extension(Ultrasurf)
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-browser-side-navigation')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
driver.delete_all_cookies()
time.sleep(1)

for i in range(0, sheet1.nrows):        
    row = sheet1.row_slice(i)        
    Id = row[0].value 
    Sku = row[1].value    
    Link = row[2].value
    print(Sku)
    
    func(driver,Id,Sku,Link)
    
