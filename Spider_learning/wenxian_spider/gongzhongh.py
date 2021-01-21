from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
from lxml import etree
import re
import csv


file = open("./text.txt", "w", encoding="utf-8")
num = 0
file_2 = open("./key_url.csv", "w", encoding="utf-8", newline="")
header = ["key", "url"]
csv_file = csv.DictWriter(file_2, header)
csv_file.writeheader()


def get_infos(response):
    key_url_list = []
    infos_list = re.findall(r'"content": "(.*?)"', response, re.S)
    for line in range(0, len(infos_list), 2):
        key_url = {}
        key_url["key"] = infos_list[line]
        key_url["url"] = infos_list[line + 1]
        # print(infos_list[line], infos_list[line + 1])
        # print("*" * 10)
        key_url_list.append(key_url)
    # print(key_url_list)
    csv_file.writerows(key_url_list)
    return True


def get_html(response):
    global num
    with open("./html_{}.txt".format(num), "w", encoding="utf-8") as f:
        num += 1
        f.write(response)
    return True


Driver_path = "./chromedriver.exe"
base_url = "https://mp.weixin.qq.com/"

driver = webdriver.Chrome(executable_path=Driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
})

driver.maximize_window()
driver.get(base_url)
wait = WebDriverWait(driver, 200)
account = wait.until(
    expected_conditions.presence_of_element_located(
        (By.XPATH,
         '//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input')))
password = wait.until(
    expected_conditions.presence_of_element_located(
        (By.XPATH,
         '//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input')))
account.send_keys("2738847334@qq.com")
time.sleep(1)
password.send_keys("python314aihaoze")
login = wait.until(
    expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, "btn_login")))
login.click()

huifu = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//*[@id="menuBar"]/li[2]/ul/li[1]/a/span/span')))
huifu.click()

key_huifu = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/div[2]/div[2]/ul/li[1]/a')))
key_huifu.click()

yanzhengci = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[1]/div[1]/div')))


to_next_page = wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[3]/span[1]/a')))
response = driver.page_source
result = get_infos(response)

to_next_page.click()

while result:
    try:
        to_next_page = wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[3]/span[1]/a[2]')))
        response = driver.page_source
        result = get_infos(response)

        to_next_page.click()
    except BaseException:
        result = False

file.close()
file_2.close()
driver.close()
