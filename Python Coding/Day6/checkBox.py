import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.common import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.maximize_window()

mywait = WebDriverWait(driver,10)


driver.get("https://testautomationpractice.blogspot.com/")


mywait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='active']")))






#To click one specific checkbox
# driver.find_element(By.CSS_SELECTOR,"#sunday").click()


#To select all the check box

# checkBox = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@value,'day')]")
# checkbox1=driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']/input[@type='checkbox']")
#
# print(len(checkbox1))
#
#
#
# for i in range(len(checkbox1)):
#     checkbox1[i].click()



# print(len(checkBox))
#
# # Approach 1
# for i in range(len(checkBox)):
#     checkBox[i].click()
#
# # Approach 2
# for i in checkBox:
#     i.click()


#To select by choice of checkbox----------


checkbox1=driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']/input[@type='checkbox']")
# labels=driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']/input[@type='checkbox']//following::label[@class='form-check-label']")
for i in checkbox1:
    if i.get_attribute('id')=='sunday' or i.get_attribute('id')=='thursday':
        i.click()





# checkBoxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@value,'day')]")
#
#
# print(len(checkBoxes))
# # print(checkBox.text)
#
# for i in checkBoxes:
#     # print(i.get_attribute('id'))
#     checkBox = i.get_attribute('id')
#     if checkBox == 'monday' or checkBox =='sunday':
#         i.click()

#Selecting last 2 checkboxes:

# checkBoxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@value,'day')]")
#
#
# print(len(checkBoxes))
# print(checkBox.text)

# for i in range(len(checkBoxes)-2,len(checkBoxes)):
#     checkBoxes[i].click()



# for i in range(len(checkBoxes)-5,len(checkBoxes)):
#     checkBoxes[i].click()


#Selecting first  2 checkboxes:
#
# checkBoxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@value,'day')]")
#
#
# print(len(checkBoxes))
#
# for i in range(len(checkBoxes)):
#     if i <2:
#         checkBoxes[i].click()


# Clearing all checkboxes:
#
# checkBoxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@value,'day')]")
#
# for i in checkBoxes:
#     # print(i.get_attribute('id'))
#     checkBox = i.get_attribute('id')
#     if checkBox == 'monday' or checkBox =='sunday':
#         i.click()
#
# time.sleep(3)
#
#
#
# for i in checkBoxes:
#     if i.is_selected():
#         i.click()
#
#



















time.sleep(10)












