from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# Self
# elementText = driver.find_element(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/self::a").text
# print(elementText)


#Parent
# elementText = driver.find_element(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/parent::td").text
# print(elementText)  #Hitachi Energy India
#

#Child

# childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/ancestor::tr/child::td")
# print(len(childs))  #5

#ancestor
#
# msg = driver.find_element(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/ancestor::tr").text
# print(msg)  # Hitachi Energy India A 6,879.10 7,155.80 + 4.02

#Descented

# Descented = driver.find_elements(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/ancestor::tr/descendant::*")
# print("The Number of Descented nodes is",len(Descented))

#Following

time.sleep(3)
# following = driver.find_elements(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/following::tr")
# print("The Number of following nodes is",len(following))   #372

#Following Sibling

# time.sleep(3)
# followingSib = driver.find_elements(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/ancestor::tr/following-sibling::tr")
# print("The Number of following nodes is",len(followingSib))   #370


#Preceeding
# following = driver.find_elements(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/preceding::tr")
# print("The Number of following nodes is",len(following))   #23

#Following Sibling

# time.sleep(3)
followingSib = driver.find_elements(By.XPATH,"//a[contains(text(),'Hitachi Energy India')]/ancestor::tr/preceding-sibling::tr")
print("The Number of following nodes is",len(followingSib))   #22










time.sleep(5)