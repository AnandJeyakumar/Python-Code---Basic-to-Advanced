from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()


driver.get("https://demo.nopcommerce.com/login")


driver.maximize_window()


time.sleep(10)

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))









time.sleep(10)