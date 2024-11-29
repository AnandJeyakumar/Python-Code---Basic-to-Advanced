import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()


driver.implicitly_wait(7)


#double CLick


obj = ActionChains(driver)

driver.switch_to.frame('iframeResult')

driver.find_element(By.XPATH,"//input[@id='field1']").clear()

driver.find_element(By.XPATH,"//input[@id='field1']").send_keys("I Will get a job this month")



doubleClickElement=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

obj.double_click(doubleClickElement).perform()





time.sleep(7)


