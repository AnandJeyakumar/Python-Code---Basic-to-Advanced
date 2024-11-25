import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.common import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")
myWait = WebDriverWait(driver,10)   #Declaration

# myWait = WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
#                                                      ElementNotSelectableException,Exception]) #ingonred_Exception
#
# myWait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
#                                                      ElementNotSelectableException,Exception])  #withPoll

searchInput=driver.find_element(By.NAME,'q')
searchInput.send_keys("Selenium")
searchInput.submit()     # Enter click in submit

searchLink=myWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))   #Usage by format - delaration.until(ExpectedCondition.presence((byXpath))
searchLink.click()

time.sleep(5)