from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

#Tag & ID
#CSS Selector
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Hello")
# driver.find_element(By.CSS_SELECTOR,"#email").clear()
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("Facebook")
# time.sleep(5)

#Tag & Class
#CSS Selector
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").clear()
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("By Tag and class")
# driver.find_element(By.CSS_SELECTOR,".inputtext").clear()


#Tag & Attribute
#CSS Selector
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("Hello@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").clear()
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("Facebook@gmail.com")
#

#Tag class and attribute
#CSS Selector
#
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email").send_keys("TagClassAttribute")
#
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass").send_keys("TagClassAttribute")
#
# driver.find_element(By.CSS_SELECTOR,"div._9lsa").click()
# # driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email").clear()
# # driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass").clear()



time.sleep(10)