import time

from selenium import webdriver
from selenium.webdriver.common.by import By






driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(3)

driver.maximize_window()


driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()


time.sleep(5)
driver.close()
# driver.quit()
time.sleep(5)






