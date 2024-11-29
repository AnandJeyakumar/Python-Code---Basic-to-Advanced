import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()

driver.get("https://jqueryui.com/slider/")
driver.maximize_window()


driver.implicitly_wait(15)


act=ActionChains(driver)
# sliderElement =driver.find_element(By.XPATH,"//div[@id='slider']/span")
# print("Before")
# print(sliderElement.location)
# act.drag_and_drop_by_offset(sliderElement,150,0).perform()
#
# print("After")
# after=driver.find_element(By.XPATH,"//div[@id='slider']/span")
# print(after.location)
