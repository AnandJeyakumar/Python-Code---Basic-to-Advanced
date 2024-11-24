from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login")

driver.maximize_window()

# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop ")

driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop ")

time.sleep(10)

# By link and Partial link test

# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
time.sleep(10)


