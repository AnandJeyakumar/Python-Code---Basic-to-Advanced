import time


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


#Site is not available

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()


time.sleep(5)


driver.find_element(By.ID,"promptBtn").click()  # fOr clicking the element to get alert popup
myAlert = driver.switch_to.alert
myAlert.send_keys("Shiva")
print(myAlert.text)   # Will get text from the alert popup

# myAlert.send_keys("Welcome")        # We can also send keys in the alert popup
time.sleep(3)

myAlert.accept()   # Clicking on Ok button in the alert popup


# myAlert.dismiss()     # Clicking on no in the alert popup

time.sleep(3)

#Approach 2


# driver.switch_to.alert.send_keys("Without Object Creation")   # We can also directly use by not defining an object also

# driver.switch_to.alert.accept()   # We can also directly use by not defining an object also

# driver.switch_to.alert.dismiss()     # We can also directly use by not defining an object also
































