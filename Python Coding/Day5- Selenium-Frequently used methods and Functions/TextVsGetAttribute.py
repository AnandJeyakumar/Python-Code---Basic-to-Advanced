import time

from selenium import webdriver
from selenium.webdriver.common.by import By




driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(3)



emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("Murugaaa")
print("The Text of Email input by text",emailbox.text)  #printed nothing
print("The Text of Email input by value",emailbox.get_attribute('value'))



button=driver.find_element(By.XPATH,"//button[@type='submit']")


print("The Text of Login by text",button.text)  #LOG IN
print("The Text of Login by value :",button.get_attribute('type'))   #printed nothing




time.sleep(3)















