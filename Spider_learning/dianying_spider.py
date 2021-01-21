"""
    功能：爬取阳光电影的最新电影的部分信息
    备注：由于 xpath 功能不知为何出现异常，所以暂时不能采用从当前网页获取下一页的网页地址来获取所有电影
         的列表，也正是因为这个原因，网页的页面数目采用固定值
"""
import json
import time
import csv
import requests
from lxml import etree




class Spider(object):
    def __init__(self):

        # 网页总页数（可根据网页的实际情况来修改）
        self.page_count = 165

        # 基本网页地址
        self.based_url = "https://www.ygdy8.com"

        # 起始网页地址
        self.start_url = "https://www.ygdy8.com/html/gndy/dyzz/list_23_{}.html"

        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "Referer": "https://www.ygdy8.com/html/gndy/dyzz/index.html"
            }

        # 保存计数器
        self.count = 1

        # 数据采集计数器
        self.count2 = 1

        # 文件名
        self.file_name = "电影清单2.csv"

        # 表头
        self.header = ["title", "海报地址", "电影截图", "迅雷下载地址", "译    名",
                       "片    名", "年    代", "产    地", "类    别", "语    言",
                       "字    幕", "上映日期", "豆瓣评分", "片    长", "导    演",
                       "编    剧", "主    演", "标    签", "简    介", "获奖情况"]

    def get_page_url_list(self):
        # 获取所有页面的 url 地址列表
        page_list = []
        for x in range(1, self.page_count + 1):
            url = self.start_url.format(x)
            page_list.append(url)
        # print(page_list)
        return page_list

    def get_url_list(self, start_url):
        # 获得当前页面电影的 url 地址列表
        url_list2 = []
        response_text = self.get_response_text(start_url)
        element = etree.HTML(response_text)
        url_list = element.xpath("//div[@class='co_content8']//@href")
        # print(url_list)
        for url in url_list:
            url = self.based_url + url
            # print(url)
            url_list2.append(url)
        return url_list2

    def get_response_text(self, url):
        response = requests.get(url, headers=self.headers)
        response_text = response.content
        # print(response_text)
        return response_text

    def __data_replace(self, op, data):
        data2 = data.replace(op, "").strip()
        return data2

    def get_data(self, response_text):
        movie = {}
        element = etree.HTML(response_text)
        data_list = element.xpath("//div[@id='Zoom']//p/text()")
        # print(data_list[0])
        try:
            movie["title"] = data_list[0]
        except IndexError:
            movie["title"] = ""

        # 获取海报地址
        img = element.xpath("//div[@id='Zoom']//p/img/@src")
        try:
            movie["海报地址"] = img[0]
            movie["电影截图"] = img[1]
        except IndexError:
            movie["海报地址"] = ""
            movie["电影截图"] = ""

        # 获取电影下载地址
        download_url = element.xpath("//td[@style='WORD-WRAP: break-word']//text()")
        # print(download_url)
        movie["迅雷下载地址"] = download_url

        # 获取电影的详细信息
        for index, data in enumerate(data_list):
            # print(data)
            # print(index)
            # print("*" * 30)
            if data.startswith("◎译　　名"):
                data = self.__data_replace("◎译　　名", data)
                movie["译    名"] = data
                # print(data)
            elif data.startswith("◎片　　名"):
                data = self.__data_replace("◎片　　名", data)
                movie["片    名"] = data
            elif data.startswith("◎年　　代"):
                data = self.__data_replace("◎年　　代", data)
                movie["年    代"] = data
            elif data.startswith("◎产　　地"):
                data = self.__data_replace("◎产　　地", data)
                movie["产    地"] = data
            elif data.startswith("◎类　　别"):
                data = self.__data_replace("◎类　　别", data)
                movie["类    别"] = data
            elif data.startswith("◎语　　言"):
                data = self.__data_replace("◎语　　言", data)
                movie["语    言"] = data
            elif data.startswith("◎字　　幕"):
                data = self.__data_replace("◎字　　幕", data)
                movie["字    幕"] = data
            elif data.startswith("◎上映日期"):
                data = self.__data_replace("◎上映日期", data)
                movie["上映日期"] = data
            elif data.startswith("◎豆瓣评分"):
                data = self.__data_replace("◎豆瓣评分", data)
                movie["豆瓣评分"] = data
            elif data.startswith("◎片　　长"):
                data = self.__data_replace("◎片　　长", data)
                movie["片    长"] = data
            elif data.startswith("◎导　　演"):
                data = self.__data_replace("◎导　　演", data)
                movie["导    演"] = data
            elif data.startswith("◎编　　剧"):
                data = self.__data_replace("◎编　　剧", data)
                movie["编    剧"] = data
            # 主演演员
            elif data.startswith("◎主　　演"):
                data = self.__data_replace("◎主　　演", data)
                # print(data)
                actors = [data]
                for x in range(index + 1, len(data_list)):
                    actor = data_list[x].strip()
                    if actor.startswith("◎"):
                        break
                    actors.append(actor)
                # print(actors)
                movie["主    演"] = actors
            elif data.startswith("◎标　　签"):
                data = self.__data_replace("◎标　　签", data)
                movie["标    签"] = data
            elif data.startswith("◎简　　介"):
                movie["简    介"] = data_list[index + 1].strip()
            elif data.startswith("◎获奖情况"):
                movie["获奖情况"] = data_list[index + 1].strip()
        # print(movie)
        return movie

    def saved_data(self, data):
        # 将数据保存为 json 文件
        # json_data = json.dumps(data, ensure_ascii=False, indent=2)
        # with open("电影清单.json", "a", encoding="utf8") as f:
        #     f.write(json_data + ", \n")
        #     print("保存成功+{}".format(self.count))
        #     self.count += 1
        #     time.sleep(0.5)

        """
            将数据保存为 csv 文件
            第一次：尝试失败，因为从网络爬取的数据慧存在部分数据缺失
            第二次：采用条件保存，当满足所有所有字典都存在的条件下才保存文件，
                并发现第一次尝试是成功的，因为第一次尝试有一点代码错误。。。
        """
        # print("数据采集+{}".format(self.count2))
        # self.count2 += 1
        # num = 0
        # for key in data.keys():
        #     num += 1
        # if num == 20:
        movie_list2 = []
        movie_list2.append(data)
        # print(type(data))
        # print(type(movie_list2))
        with open(self.file_name, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, self.header)
            writer.writerows(movie_list2)
            print("保存成功+{}".format(self.count))
            print("*" * 30)
            self.count += 1
            time.sleep(0.5)

    def __creat_file(self):
        # 创建文件，写入表头
        with open(self.file_name, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, self.header)
            writer.writeheader()
        print("文件创建成功！文件名称：" + self.file_name)

    def run(self):
        # 初始化文件
        self.__creat_file()

        # 获取所有的页面
        page_list = self.get_page_url_list()

        # 第二个循环，遍历所有的页面
        for page_url in page_list:
            url_list = self.get_url_list(page_url)

            # 第一个循环，遍历一页的所有电影
            for url in url_list:
                #     # url = url_list[0]
                # 请求网页，获取数据
                response_text = self.get_response_text(url)
                #
                # 提取数据
                data = self.get_data(response_text)
                #
                # 数据保存
                self.saved_data(data)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
