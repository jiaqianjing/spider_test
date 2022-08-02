from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver_path = 'webdriver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

driver.get("http://jd.com/")

time.sleep(10)

# 首页商品 list
# page = driver.find_e lements(By.XPATH, '//div[@class="goods_img bg_stamp"]')
# print(len(page))

# 关键词搜索商品
driver.find_element(By.XPATH, '//input[@id="msKeyWord"]').send_keys("耳机")
driver.find_element(By.XPATH, '//a[@id="msSearchBtn"]/span').click()

time.sleep(10)