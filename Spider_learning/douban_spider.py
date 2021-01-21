"""
    本爬虫功能实现为：采用手机 UA 进入豆瓣网页版然后对部分信息的爬取，并保存在 txt 文件中。
"""
import json
import requests


class DoubanSpider(object):

    # 初始化
    def __init__(self):

        # 基础 url 地址
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_" \
                   "american/items?os=android&for_mobile=1&start={}&count=18&loc" \
                   "_id=108288&_=1574086511372"
        self.count = 0
        self.total = 100

        # 用于爬虫的伪装， User-agent 为伪装成的目标浏览器
        self.headers = {"User-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 "
                                      "like Mac OS X) AppleWebKit/603.1.30 (KHTML, "
                                      "like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
                        "Referer": "https://m.douban.com/tv/american"
           }

    def response(self, url):
        """
        用于对目标网址发起请求
        :param url: 需要传入的 url 地址
        :return: 返回值为目标网址的源代码
        """
        # 向网页发起起请求，并加以伪装，限定超时时间为 5 秒。
        response = requests.get(url, headers=self.headers, timeout=5)
        return response.content.decode()

    def get_text(self, rep):
        """
        用于数据的提取
        :param rep: 传入一个 JSON 格式的参数
        :return: 返回提取的信息和所在网址标记信息
        """
        ret1 = json.loads(rep)
        ret2 = ret1["subject_collection_items"] 
        total = ret1["total"]
        return ret2, total

    def save(self, str):
        """
        用于文件的保存
        :param str: 传入需要保存的信息
        :return:
        """
        with open("douban2.txt", "a", encoding="utf-8") as f:  # 以 "a" （追加）的方式打开文件 douban.txt，编码方式为 utf-8
            for i in str:
                # f.write(json.dumps(i, ensure_ascii=False))
                f.write("片名：{}\n简介：{}\n演员：{}\n评论：{}\n".format(i["title"], i["card_subtitle"], i["actors"], i["recommend_comment"]))
                f.write("\n")
        print("保存成功")

    def run(self):  # 主要实现逻辑
        while self.count < self.total + 18:
            # 1.获取url地址
            url = self.url.format(self.count)
            # 2.发送请求，获取响应
            response = self.response(url)
            # 3.提取数据
            json_str, self.total = self.get_text(response)
            # 4.保存
            self.save(json_str)
            # 5.构造下一页url地址，并循环2~5步
            self.count += 18


if __name__ == '__main__':
    # 实例化类
    douban = DoubanSpider()

    # 运行实例
    douban.run()
