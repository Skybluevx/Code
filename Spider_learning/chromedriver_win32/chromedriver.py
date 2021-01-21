# coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.baidu.com"
url2 = "https://cnki.net/"
driver.get(url)

# 窗口最大化
driver.maximize_window()

# 打印网页的标题
print(driver.title)

input_sp = driver.find_element_by_id("kw")
input_sp.send_keys("CSDN")
search = driver.find_element_by_id("su")
search.click()
time.sleep(5)
driver.close()

