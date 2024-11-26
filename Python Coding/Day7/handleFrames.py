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

# Frame 1
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.CSS_SELECTOR,"#RESULT_TextField-0").send_keys("Om Namashivaya")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Hellow")
time.sleep(3)







