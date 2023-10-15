import time
import sys,os, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.action_chains import ActionChains
from time import gmtime, strftime
from datetime import datetime, timedelta, date
from lxml.html import fromstring
from selenium.webdriver.chrome.options import Options
from time import sleep
import xlrd
import re
import pyautogui
import keyboard

def junck(value):
    value = re.sub(r"\[","",str(value))
    value = re.sub(r"\]","",str(value))
    value = re.sub(r"\"","",str(value))
    value = re.sub(r"\'","",str(value))
    value = re.sub(r"\(","",str(value))
    value = re.sub(r"\)","",str(value))
    value = re.sub(r"&nbsp;","",str(value))
    # value = re.sub(r"\@","",str(value))
    value = re.sub(r"\   ","",str(value))
    return value
	
chrome_options = Options()    
chrome_options.add_extension('C:/Users/deepak/Desktop/chromedriver/Ultrasurf/Ultrasurf181-1.crx')
chrome_options.add_experimental_option("detach", True)	
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")    
driver = webdriver.Chrome(options=chrome_options, executable_path='C:/Users/deepak/Desktop/chromedriver/118/chromedriver1.exe')

f = open("Person_Data_Out.txt", "a")
f.write("Id"+"\t"+"Sku"+"\t"+"Link"+"\t"+"Name"+"\t"+"Locality_Age"+"\t"+"Address"+"\t"+"P_Phone"+"\t"+"Email"+"\n")
f.close()

excel_sheet = xlrd.open_workbook("Input.xlsx")
sheet1= excel_sheet.sheet_by_name('Sheet1')

for i in range(0, sheet1.nrows):        
    row = sheet1.row_slice(i)        
    Id = row[0].value 
    Sku = row[1].value    
    Link = row[2].value	
    print(Link)
    # time.sleep(3)
    response = driver.get("view-source:"+str(Link))
    content1=driver.page_source
    content = content1.encode('utf-8')
    driver.delete_all_cookies()
    print(driver.title)    
    content = content1.encode('utf-8')
    content = (content1,'utf-8')
    content=re.sub(r"\\n", "",str(content))
    content=re.sub(r"\\t", "",str(content))	
    content=re.sub(r'&amp;','&',str(content))
    content=re.sub(r"<[^<>]*?>","",str(content))
    content=re.sub(r"&lt;","<",str(content))
    content=re.sub(r"&gt;",">",str(content))
    content=re.sub(r"%40","@",str(content))		

    file_name=str(Id)+".html"
    print(file_name)
    time.sleep(2)
    # a =open(file_name,"w")
    # a.write(content)
    # a.close()
             
    Name=re.findall('<title\>\s*([^>]*?)\s*\<\/title\>', str(content), re.I)
    Name = junck(Name)
             
    Locality_Age=re.findall('>\s*([^>]*?)\s*\,\ age\s*([^>]*?)\s*\<\/small\>\<\/h1\>', str(content), re.I)
    Locality_Age = junck(Locality_Age)
	
    Address=re.findall('\"address\"\:\"\s*([^>]*?)\s*\"\}', str(content), re.I)
    Address = junck(Address)

    P_Phone=re.findall('<meta\ itemprop\=\"telephone\"\ content\=\"\s*([^>]*?)\s*\"\>\s*([^>]*?)\s*\<\/li\>', str(content), re.I)
    P_Phone = junck(P_Phone)

    Email=re.findall('<a\ href\=\"mailto\:\s*([^>]*?)\s*\"\>', str(content), re.I) 
    Email = junck(Email)
	
    f=open("Person_Data_Out.txt", 'a', encoding="utf-8")
    f.write(str(Id)+"\t"+str(Sku)+"\t"+str(Link)+"\t"+str(Name)+"\t"+str(Locality_Age)+"\t"+str(Address)+"\t"+str(P_Phone)+"\t"+str(Email)+"\n")
    f.close() 
    time.sleep(1)    
    # driver.close()
    		

     