from selenium import webdriver
from selenium.webdriver.common.by import By






driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
# # is enabled and is displayed
# firstNameInput=driver.find_element(By.XPATH,"//input[@id='FirstName']")
# print("The first is :",firstNameInput.is_enabled())
# print("The first is :",firstNameInput.is_displayed())
# is selected
genderMale=driver.find_element(By.XPATH,"//input[@id='gender-male']")
genderFemale = driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("The Default Value.........")

print("The Default of Male is :",genderMale.is_selected())
print("The Default of Female is :",genderFemale.is_selected())

genderMale.click()
print("After selecting Male.........")
if genderMale.is_selected():
    print("Inside IF logic")
print("The Default of Male is :",genderMale.is_selected())
print("The Default of Female is :",genderFemale.is_selected())

genderFemale.click()
print("After selecting Female.........")

print("The Default of Male is :",genderMale.is_selected())
print("The Default of Female is :",genderFemale.is_selected())

















