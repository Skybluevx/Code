"""
    作者：刘硕
    时间：1/12/2019
    功能：采用多线程下载斗图啦网站最新表情内的表情包
    备注：2019年12月1日学习了多线程爬虫，特以此例作为尝试，过程稍有波折，
        但并无大碍，很荣幸，一次性成功，恭喜贺喜，再接再厉。
"""
import requests
import os
import threading
from queue import Queue
from lxml import etree
import re
from urllib import request


gLock = threading.Lock()
# 保存计数器
count = 1


class Spider(object):
    def __init__(self):
        self.base_url = "http://www.doutula.com/photo/list/?page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Referer": "http://www.doutula.com/article/list/",
            "Cookie": "__cfduid=d7a2ca7d663479a0d44f5447eb77568081575169297; UM_distinctid"
                      "=16ebf681026135-0793dbb962223-2393f61-100200-16ebf68102779; CNZZDATA"
                      "1256911977=682232657-1575168076-null%7C1575184287; XSRF-TOKEN=eyJpdi"
                      "I6ImZ2aThXZlhQTktrRkp3anZGR3ZQOXc9PSIsInZhbHVlIjoiV21MeFN3dHBpQVJ2WV"
                      "ZmdU9QUXlCeWZ5KzFHUVdlMHFSdnF3K202cTZLRTY2d3hcL0JRMHp2KzRCMDdcL3Q2YT"
                      "l0IiwibWFjIjoiNDczMWYxNzYwMjdhZWNhZTY0NWUyZTdhNjc3YTgwOWZmNDM2NGFlYW"
                      "U2MDc2MDg2ZWU3YzQ5Nzc5MGFmZTM0MSJ9; doutula_session=eyJpdiI6IkJielAw"
                      "MWljMVV6ZU5WYzRpb3ZMYmc9PSIsInZhbHVlIjoiRFJhd0lCa3BSNmhtQVwvN0U1bnN"
                      "JSm9QQmxqMEpzZDd1dHFCQ0VZNzNaYjNjbzZ6MG16YWw3OHFzYWVLbGRGMmYiLCJtYW"
                      "MiOiIwODAzNzNmNzNkNTk5YzNiN2JkZTRlNTNhNTNkZDRmMmJjMDA2MGQyYTdkNDYzM"
                      "GNkMGJmODRkODUyNTBhOWVjIn0%3D"
        }
        # 用于存储图片 url 地址的队列
        self.Img_Url_Queue = Queue(10000)
        # 用于存储页面 url 地址的队列
        self.Page_Queue = Queue(1000)

    def run(self):

        # 将所有网页的地址放到网页地址队列中
        for x in range(1, 101):
            url = self.base_url.format(x)
            # print(url)
            self.Page_Queue.put(url)

        # 启用5个线程用于生产图片的 url，并存入图片地址队列中
        for i in range(5):
            t = Producer(self.Page_Queue, self.Img_Url_Queue)
            t.start()

        # 启用五个线程用于下载图片并保存在文件中
        for z in range(5):
            a = Consumer(self.Img_Url_Queue, self.Page_Queue)
            a.start()


class Producer(threading.Thread):
    """
        生产者：用于生产每个图片的 url 和图片名称，并存入队列中。
        传入参数：每个页面的 url 队列, 图片 url 队列
    """
    def __init__(self, page_queue, img_url_queue):
        super().__init__()
        self.page_queue = page_queue
        self.img_url_queue = img_url_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get(block=True)
            response = requests.get(url, headers=Spider().headers)
            content = response.content.decode()
            # print(content)
            html = etree.HTML(content)
            img_infos = html.xpath('//div[@class="page-content text-center"]'
                                   '//img[@class!="gif"]')
            for img_info in img_infos:
                img_url = img_info.get("data-original")
                img_name = img_info.get("alt")
                # print(img_url, img_name)
                self.img_url_queue.put((img_url, img_name))
                # print(img_name, img_url)


class Consumer(threading.Thread):
    """
        消费者：用于下载队列中 url 地址的图片，并保存。
        传入参数：图片 url 队列
    """
    def __init__(self, img_url_queue, page_queue):
        super().__init__()
        self.img_url_queue = img_url_queue
        self.page_queue = page_queue

    def run(self):
        global count
        while True:
            if self.img_url_queue.empty() and self.page_queue.empty():
                break
            img_url, img_name = self.img_url_queue.get(block=True)
            # print(img_name, img_url)
            img_name = re.sub(r"[\\?？\.。*！!,，@%]", "", img_name)
            suffix = os.path.splitext(img_url)[1]
            # print(suffix)
            filename = img_name + suffix
            request.urlretrieve(img_url, "images/" + filename)
            print("保存成功+{}    ".format(count) + filename)
            gLock.acquire()
            count += 1
            gLock.release()


def main():
    spider = Spider()
    spider.run()


if __name__ == '__main__':
    main()
