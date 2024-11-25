import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

mywait =WebDriverWait(driver,10)


# linkElement=mywait.until(EC.presence_of_element_located((By.LINK_TEXT,'Digital downloads')))

linkElement=mywait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'Digital')))

linkElement.click()


# To find the number of link text present in the page
linkElements = driver.find_elements(By.TAG_NAME,'a')
print(len(linkElements))

for text in linkElements:
    print(text.text)









time.sleep(10)

