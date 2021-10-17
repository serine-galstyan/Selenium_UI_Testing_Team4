# This test case was created by Hayk Poghosyan

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_user_options = Options()
chrome_user_options.add_argument("--start-maximized")
# chrome_user_options.add_argument("--headless")
chrome_user_options.add_argument("--log-level=3")
chrome_user_options.add_experimental_option("prefs", {"profile.default_content_settings_values.notifications": 2 })

# open browser
browser = webdriver.Chrome(chrome_options = chrome_user_options, executable_path=r"C:\Users\Hayk Poghosyan\Downloads\chromedriver.exe")
browser.get("https://www.saucedemo.com/")

# enter user name and password
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()

# click filter button
browser.find_element(By.XPATH, "//span[@class = 'select_container']").click()
time.sleep(3)
# choose "Price (low to high)" version
browser.find_element(By.XPATH, "//option[@value = 'lohi']").click()
time.sleep(3)

# to take the first price 
first_price = browser.find_element(By.XPATH, "//div[@class = 'inventory_item'][1]//div[@class = 'inventory_item_price']").text
first_price_int = first_price[1:]

# to take the middle price
middle_price = browser.find_element(By.XPATH, "//div[@class = 'inventory_item'][3]//div[@class = 'inventory_item_price']").text
middle_price_int = middle_price[1:]

# to take the last price
last_price = browser.find_element(By.XPATH, "//div[@class = 'inventory_item'][6]//div[@class = 'inventory_item_price']").text
last_price_int = last_price[1:]

if int(float(first_price_int)) < int(float(middle_price_int)) < int(float(last_price_int)):
    print("The test case Passed")
else:
    print("The test case Failed")
browser.close()