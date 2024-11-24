from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(3)


# Absolute xpath
# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
#
# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
#


# Absolute xpath

#
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
#
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
#

# or and

#
# driver.find_element(By.XPATH,"//input[@name='username' or @class='oxd-in']").send_keys("Admin")
#
# driver.find_element(By.XPATH,"//input[@name='password' and @placeholder='Password']").send_keys("admin123")
#

# contains and startswith


# driver.find_element(By.XPATH,"//input[contains(@placeholder,'User')]").send_keys("Admin")
#
# driver.find_element(By.XPATH,"//input[contains(@placeholder,'Pass')]").send_keys("admin123")

# driver.find_element(By.XPATH,"//input[starts-with(@placeholder,'Username')]").send_keys("Admin")
#
# driver.find_element(By.XPATH,"//input[starts-with(@name,'pass')]").send_keys("admin123")

#Text




# driver.find_element(By.XPATH,"//label[text()='Username']").click()



















time.sleep(7)








