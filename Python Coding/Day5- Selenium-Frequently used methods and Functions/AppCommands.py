import time

from selenium import webdriver
from selenium.webdriver.common.by import By






driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(3)

print(driver.title)   #OrangeHRM
print(driver.current_url)    #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)     









driver.close()