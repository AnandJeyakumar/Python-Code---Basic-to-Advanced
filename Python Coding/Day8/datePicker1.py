import time


from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()




myWait = WebDriverWait(driver,10)




driver.switch_to.frame(0)


# driver.switch_to.default_content()

#By Send keys in data
# dateInput=myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='datepicker']")))
# dateInput.send_keys("07/04/2024")
# dateInput.send_keys(Keys.ENTER)

# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("07/04/2024")
#
#
#
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys(Keys.ESCAPE)



# #Selecting Month first
dateInput=myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='datepicker']")))
dateInput.click()
# myWait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='datepicker']"))).click()

date = '7'
month = "March"
year = "2025"



while True:
    yearText = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    monthText = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

    if yearText==year and   monthText==month:
        break
    elif int(yearText)>int(year):
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
        yearText = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        if yearText == year:
            while True:
                driver.find_element(By.XPATH, "//a[@title='Prev']").click()
                monthText = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
                if monthText==month:
                    break
    else:
        driver.find_element(By.XPATH,"//a[@title='Next']").click()

dateElement = driver.find_elements(By.XPATH,"//td[@data-handler='selectDay']")
for i in dateElement:
    if i.text==date:
        i.click()
        break

datevalue=dateInput.get_attribute('value')
print(datevalue)
if datevalue=='03/07/2025':
    print("Pass")
else:
    print("Fail")



# datevalue.equals('07/03/2023')

time.sleep(3)













# # Year and Month Selection
#
# while True:
#     m=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
#     y = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#
#     if m==month and y ==year :
#         break
#     else:
#         driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
#
#         # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
#
#
# # Date  Selection
#
#
#
# dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr//a")
#
#
# date =  '7'    # Dom Element in visible text is also a text not number if 7 is showing in don it is text -str
# for ele in dates:
#     if ele.text == date:
#         print("Date Matching")
#         ele.click()
#         break
#
#
#
#
#


time.sleep(5)






































time.sleep(5)
















































































