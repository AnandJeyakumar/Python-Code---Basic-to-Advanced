import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()


driver.implicitly_wait(7)



#drand Drop

sourceEle = driver.find_element(By.XPATH,"//div[@id='box3']")
dropEle = driver.find_element(By.XPATH,"//div[@id='box103']")


obj = ActionChains(driver)

obj.drag_and_drop(sourceEle,dropEle).perform()

time.sleep(5)


