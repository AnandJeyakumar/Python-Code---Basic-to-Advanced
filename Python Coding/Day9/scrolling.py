
import time


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()


driver.implicitly_wait(15)


#Scrolling by Pixels


# beforeValue = driver.execute_script("return window.pageYOffset;")
# print("Detault Value of Pixel is:",beforeValue)
#
#
# driver.execute_script("window.scrollBy(0,3000)","")
# afterValue= driver.execute_script("return window.pageYOffset;")
# print("After  Value of Pixel is:",afterValue)


#Scroll by element

flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")


driver.execute_script("arguments[0].scrollIntoView();",flag)
v= driver.execute_script("return window.pageYOffset")

time.sleep(3)
print('vvvvvvvvvvv;',v)



# scroll to the last end


driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")



time.sleep(3)


driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(3)











































