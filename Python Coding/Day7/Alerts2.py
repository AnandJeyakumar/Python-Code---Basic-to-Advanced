import time


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#Site is not available


driver = webdriver.Chrome()
driver.get("https://the-internet-herokuapp.com/javascript-alerts")


driver.maximize_window()


time.sleep(5)


#Approach Without creating object directly doing flows in alert

driver.switch_to.alert.send_keys("Without creation of object")

alertText=print(driver.switch_to.alert.text)

driver.switch_to.alert.accept()  #Clicking on ok button

driver.switch_to.alert.dismiss()   #Clicking on no button



























