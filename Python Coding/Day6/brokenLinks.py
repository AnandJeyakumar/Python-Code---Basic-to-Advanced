import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests import request




driver=webdriver.Chrome()

# mywait = WebDriverWait(driver,10)


driver.get("http://www.deadlinkcity.com/")


driver.maximize_window()
time.sleep(4)

allLinks = driver.find_elements(By.TAG_NAME,'a')
print(len(allLinks))

count=0

for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print("This is a Broke Link")
        count+=1

print("The Total Count is ",count)