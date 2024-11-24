import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

time.sleep(3)
driver.maximize_window()

driver.get("https://www.snapdeal.com")
time.sleep(3)
driver.get("https://www.amazon.com")
time.sleep(3)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(3)











