import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://www.speedtest.net/")
driver.maximize_window()


driver.implicitly_wait(7)


#Mouse Over

obj = ActionChains(driver)

appEle=driver.find_element(By.XPATH,"//a[contains(text(), 'Apps')][1]")


windowEle = driver.find_element(By.XPATH,"//ul[@class='sub-menu']//a[normalize-space()='Windows']")

obj.move_to_element(appEle).move_to_element(windowEle).click().perform()


time.sleep(7)











