import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


driver.implicitly_wait(7)


#Mouse Over

obj = ActionChains(driver)


rightClickElement = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

obj.context_click(rightClickElement).perform()



time.sleep(3)

driver.find_element(By.XPATH,"//span[normalize-space()='Edit']").click()

driver._switch_to.alert.accept()

time.sleep(7)











