# This test case was created by Hayk Poghosyan

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_user_options = Options()
chrome_user_options.add_argument("--start-maximized")
chrome_user_options.add_argument("--headless")
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

time.sleep(3)
# click cart container
browser.find_element(By.ID, "shopping_cart_container").click()

# click "CHECKOUT" button
browser.find_element(By.ID, "checkout").click()

# enter first name
browser.find_element(By.ID, "first-name").send_keys("Hayk")

# enter last name
browser.find_element(By.ID, "last-name").send_keys("Poghosyan")

# enter postal code
browser.find_element(By.ID, "postal-code").send_keys("12345")

# click continue button
browser.find_element(By.ID, "continue").click()

# check calculate function
item_total_price = browser.find_element(By.CLASS_NAME, "summary_subtotal_label").text
item_total_int = item_total_price[13:]

tax_price = browser.find_element(By.CLASS_NAME, "summary_tax_label").text
tax_int = tax_price[6:]

total_price = browser.find_element(By.CLASS_NAME, "summary_total_label").text
total_int = total_price[8:]

if float(item_total_int) + float(tax_int) == float(total_int):
    print("The test case Passed")
else:
    print("The test case Failed")

# click finish button
browser.find_element(By.ID, "finish").click()
time.sleep(2)

finish_text = "THANK YOU FOR YOUR ORDER"

complete_header = browser.find_element(By.XPATH, "//div[@id = 'checkout_complete_container']/h2").text

if finish_text == complete_header:
    print("The test case Passed")
else:
    print("The test case Failed")
browser.close()