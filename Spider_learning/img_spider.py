"""
    作者：刘硕
    时间：2020-04-01
    功能：本爬虫用于爬取 http://www.netbian.com/index.htm 网址的桌面壁纸
"""
import time
import requests
from lxml import etree
import urllib.request


class Spider(object):

    def __init__(self):
        self.start_url = "http://www.netbian.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
            "Referer": self.start_url
        }
        self.num = 0

    def get_response(self, url):
        while url:
            # ip = self.ip_list[self.num] proxies={'http': ip}
            html = requests.get(url, self.headers, timeout=3)
            time.sleep(1)
            code = html.status_code
            if code != 200:
                print("哎呀，状态码怎么变成{}了呀，那就先休息10秒吧~~".format(code))
                time.sleep(10)
                continue
            content = html.content.decode("utf-8", errors="ignore")
            return content

    def get_url_list(self, content):
        html = etree.HTML(content)
        url_list = html.xpath('//div[@class="list"]/ul//img/@src')
        return url_list

    def download_img(self, url_list):
        for url in url_list:
            img_name = url[-15:]
            urllib.request.urlretrieve(url, r"./images/" + img_name)
            self.num += 1
            print("成功保存第{}张图片：{}".format(self.num, img_name))

    def __get_next_url(self, content):
        html = etree.HTML(content)
        try:
            next_url = html.xpath('//div[@class="page"]/a[@class="prev"]/@href')
            next_url = self.start_url + next_url[0]
            return next_url
        except ValueError:
            return False

    def run(self):
        url = self.start_url
        while url:
            content = self.get_response(url)
            url_list = self.get_url_list(content)
            self.download_img(url_list)
            self.headers["Referer"] = url
            url = self.__get_next_url(content)


if __name__ == '__main__':
    img = Spider()
    img.run()
