import time


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()


mywindow=driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()


# mywait = WebDriverWait(driver,10)
time.sleep(3)
# mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"")))

# windowID = driver.current_window_handle
# print(windowID)   #A82B3AA43165186B37738249CDE4538B   Next time on second run the ID is dynamicly changing - BE55C52C72C5C981C187A555A2129A70

# Aprroach when there is a tow or three
#
# driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# windowIdss = driver.window_handles
#
# parentWindowID = windowIdss[0]
# childWindowID = windowIdss[1]
#
# print(parentWindowID)
# print(childWindowID)
#
#
#
# driver.switch_to.window(childWindowID)
#
# titleOfChildBrowser = driver.title
# print("Child Title", titleOfChildBrowser)
#
#
#
# driver.switch_to.window(parentWindowID)
#
# print("Parent Title :" , driver.title)


# Approach 2


driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowID = driver.window_handles
for id in windowID:
    driver.switch_to.window(id)
    print(driver.title)

# To close a particular window or specific window
for id in windowID:
    driver.switch_to.window(id)
    title = driver.title
    if  title== "OrangeHRM":
        print("Inside closing one window loop")
        driver.close()
        time.sleep(2)
# driver.close()
time.sleep(3)











