import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(10)     #seconds   #implicitwait


searchInput=driver.find_element(By.NAME,'q')
searchInput.send_keys("Selenium")
searchInput.submit()     # Enter click in submit

searchLink=driver.find_element(By.XPATH,"//h3[text()='Selenium']")
searchLink.click()

time.sleep(5)