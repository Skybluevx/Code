from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
from lxml import etree
import csv
import re


file = open("./key_url.csv", "w", encoding="utf-8", newline="")
header = ["key", "url"]
csv_file = csv.DictWriter(file, header)
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


with open("html_{}.txt", "r", encoding="utf-8") as f:
    response = f.read()
    get_infos(response)

file.close()

