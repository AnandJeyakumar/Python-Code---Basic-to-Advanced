import time


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

mywait = WebDriverWait(driver,10)

time.sleep(5)
# countryDropdown=mywait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='country']")))
# selectElement = Select(mywait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='country']"))))
# selectElement.select_by_visible_text("Germany")
# time.sleep(10)

#Selecting option from dropdown

# selectElement=Select(driver.find_element(By.ID,"country"))
# selectElement.select_by_visible_text("India")
# selectElement.select_by_value("germany")
# selectElement.select_by_index(5)

#
#
# #Capturing all the options
#

selectElement=Select(driver.find_element(By.ID,"country"))
options= selectElement.options
print(len(options))


for countryName in options:
    print(countryName.text)



# Finding out the options without using the build in functions like Select or Options


#
# myOptions  = driver.find_elements(By.XPATH,"//select[@id='country']/option")
# print(len(myOptions))
#
# for countryName in myOptions:
#     CNN = countryName.text
#     if CNN == 'Germany':
#         print("Inside Germany selection")
#         countryName.click()
#         break
#




















































time.sleep(5)