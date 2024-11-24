from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# # Example 1
# #
driver = webdriver.Chrome()

driver.maximize_window()
# driver.get("https://admin-demo.nopcommerce.com/login")
driver.get("https://opensource-demo.orangehrmlive.com/")
title = driver.title
print(title)
if "OrangeHRM" == title:
    print("Title Matched")
else:
    print("Title Doesn't match")

time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='username']").clear()

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")

driver.find_element(By.XPATH,"//input[@name='password']").clear()

driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')

driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(3)
title = driver.title
print(title)







driver.close()


