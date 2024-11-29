import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


driver.implicitly_wait(15)

#Double click


act=ActionChains(driver)
#
# driver.find_element(By.XPATH,"//input[@id='field1']").clear()
# driver.find_element(By.XPATH,"//input[@id='field1']").send_keys("Vinayakar!")
#
# doubleClickEle = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
#
# act.double_click(doubleClickEle).perform()
#

#Drad and Drop

#
# sourceElement=driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
# dropElement= driver.find_element(By.ID,'droppable')
#
#
# act.drag_and_drop(sourceElement,dropElement).perform()


#Slider
#
# sliderElement =driver.find_element(By.XPATH,"//div[@id='slider']/span")
# print("Before")
# print(sliderElement.location)
# act.drag_and_drop_by_offset(sliderElement,150,0).perform()
#
# print("After")
# after=driver.find_element(By.XPATH,"//div[@id='slider']/span")
# print(after.location)


#scroll
#By Pixels
# beforeValue=driver.execute_script("return window.pageYOffset;")
# print(beforeValue)
# driver.execute_script("window.scrollBy(0,2000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print(value)

# Scroll By element

# table = driver.find_element(By.XPATH,"//h2[normalize-space()='Web Table']")
# driver.execute_script("arguments[0].scrollIntoView()",table)
# value = driver.execute_script("return window.pageYOffset;")
# print(value)

# Scroll to the end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
value = driver.execute_script("return window.pageYOffset;")
print(value)

time.sleep(5)

# Scroll back to the top of the  page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
value = driver.execute_script("return window.pageYOffset;")
print(value)


time.sleep(5)
































