import time

from selenium import webdriver
from selenium.webdriver.common.by import By




driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")
time.sleep(3)

# FindElement-----------------
# Locator matching with single element

# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Allah")
# time.sleep(3)

# Locator  with Multiple  element

# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)
# time.sleep(3)    #Sitemap

# Locator  with Invalid  Xpath
#
# element=driver.find_element(By.LINK_TEXT,"Log").click()  # NoSuchElementException


# FindElements-----------------

# Locator matching with single element

# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print("THe length is " , len(elements))
# elements[0].send_keys("Om Namashivaya")
# time.sleep(3)


# Locator  with Multiple  element

# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print("THe length is " ,len(elements))
# for i in elements:
#     print(i.text)



 # Locator  with Invalid  Xpath
#
# elements=driver.find_elements(By.LINK_TEXT,"Log")
# print(len(elements))  # Here there will be no exeption










