from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# مسیر دانلود وب درایور د 
webdriver_path = 'C:\webdrivers\chromedriver'

options.add_argument('--ignore-local-proxy-for-sockets')

driver = webdriver.Chrome(options=options)
# ایجاد یک نمونه از مرورگر Chrome
# باز کردن گوگل
driver.get('https://www.google.com')

search_box = driver.find_element_by_name('q')

# وارد کردن متن جستجو و ارسال آن
search_box.send_keys('پروژه سلنیوم')
search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

driver.quit()