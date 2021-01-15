"""
    批量验证百度网盘链接是否失效
    数据文件为 csv 文件
"""
import re
import pandas as pd
import requests
import time


class Check(object):

    def __init__(self):
        self.data = pd.read_csv("data.csv")["代码地址"]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        }

    def check(self):
        # 检查 url 是否失效，失效的收集起来
        pan_urls = []
        for url in self.data:
            pan_url = self.to_url(url)
            result = self.int_check(pan_url)
            if result == 0:
                pan_urls.append(url)
        print(pan_urls)

    def int_check(self, pan_url):
        # 检查链接是否失效
        if pan_url.startswith("http"):
            time.sleep(1)
            html = requests.get(pan_url, self.headers, timeout=30)
            content = html.content.decode()
            # url = "https://pan.baidu.com/s/1ZM0mdr3aiIJLGKpcHnzhLA"
            ret = re.match('.*?(链接不存在).+?', content, re.S)
            if ret:
                ret2 = ret.group(1)
                if ret2 == "链接不存在":
                    print(pan_url + "该链接已失效")
                    return 0
            else:
                print(pan_url + "合格")


    def to_url(self, shuju):
        # 将字符串处理成为 url 链接
        try:
            url = shuju.split("：")[1]
        except IndexError:
            url = "1 "
        url2 = url.split(" ")[0]
        # print(url2)
        return url2

    def save(self):
        pass

    def run(self):
        # 读取数据，整理数据
        # 逐条验证，保存验证结果
        self.check()
        # 将失效链接储存
        # print(self.data)


if __name__ == '__main__':
    check = Check()
    check.run()

