# This test case was created by Hayk Poghosyan

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
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

# click "ADD TO CART" button
browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# open burger menu
browser.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(3)
# click "RESET APP STATE" button in burger menu
browser.find_element(By.ID, "reset_sidebar_link").click()
time.sleep(3)

# checking the existence of the shopping cart badge
cart_badge = None
while not cart_badge:
    try:
        cart_badge = browser.find_element(By.XPATH, "//div[@class = 'shopping_cart_container']/a/span")
        print("The test case Failed")
    except NoSuchElementException:
        print("The test case Passed")
        break
browser.close()