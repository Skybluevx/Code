# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=r"E:\Anaconda\Pycharm.soure\爬虫学习\chromedriver_win32\chromedriver.exe")

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(2)
        try:
            while True:
                show_more = self.driver.find_element_by_class_name("H7E3vT")
                show_more.click()
                time.sleep(0.5)
                if not show_more:
                    break
        except:
            pass
        source = self.driver.page_source
        response = HtmlResponse(
            url=self.driver.current_url, body=source, request=request, encoding="utf-8")
        return response
