import time


from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()




myWait = WebDriverWait(driver,10)


myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='dob']"))).click()

month= Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))

month.select_by_visible_text("Mar")

years= Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))

years.select_by_visible_text("1998")


date = '7'

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr//a")


for i in dates:
    if i.text ==date:
        i.click()
        break







time.sleep(5)