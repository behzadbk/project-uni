from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver_path = r"C:\webdrivers\chromedriver.exe"


topic_search = input("Enter the Topic : ")


options = webdriver.ChromeOptions()

options.use_chromium = True

options.add_argument('--disable-extensions')

options.add_argument('--disable-cookies')

options.add_argument('--disable-gpu')

options.add_argument('--no-sandbox')

options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/search?q=" + topic_search + "&start")

time.sleep(4)

driver.quit()
