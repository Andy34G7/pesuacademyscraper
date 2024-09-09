#Required libraries: Selenium
#This is a simple scraper for pesuacademy!

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import time
x=open("Data.csv","w",newline='')
y=csv.writer(x)
y.writerow([])
service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.pesuacademy.com/")
kcbt=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"knowClsSection")))
kcbt.click()
time.sleep(2)
number=1
campus=1
year=2024
while True:
    if number>0:
        prn=f"PES{campus}{year}0000{number}"
    if number>9:
        prn=f"PES{campus}{year}000{number}"
    if number>99:
        prn=f"PES{campus}{year}00{number}"
    if number>999:
        prn=f"PES{campus}{year}0{number}"
    kcsb=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"knowClsSectionModalLoginId")))
    #kcsb=driver.find_element(By.ID,"knowClsSectionModalLoginId")
    kcsb.clear()
    kcsb.send_keys(prn+Keys.ENTER)
    number+=1
    time.sleep(0.1)
    try: 
        #tbdy=driver.find_element(By.XPATH,'//*[@id="knowClsSectionModalTableDate"]')
        tbdy=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="knowClsSectionModalTableDate"]')))
        for tr in tbdy.find_elements(By.XPATH,'//tr'):
            row=[item.text for item in tr.find_elements(By.XPATH,'.//td')]
            if any(row):
                y.writerow(row)
    except:
        print("Data not found for",prn)
time.sleep(5)
x.close()
