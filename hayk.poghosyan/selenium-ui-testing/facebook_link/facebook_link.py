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

# click Facebook button
browser.find_element(By.XPATH, "//li[@class = 'social_facebook']/a").click()

# switch to second opened tab
window1= browser.window_handles[1]
browser.switch_to_window(window1)

# check that the Facebook page is opened
if "Facebook" in browser.title:
    print("The test case Passed")
else:
    print("The test case Failed")
time.sleep(3)
browser.close()