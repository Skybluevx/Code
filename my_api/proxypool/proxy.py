"""
    项目功能：爬取西刺上的代理 IP，并验证代理可用性。
"""
import time
import csv
import requests
from lxml import etree
import http.client


class Spider(object):

    def __init__(self):
        """
        爬虫执行时最先调用的内置函数，用于初始化数据
        """
        # 用于爬虫程序的伪装，伪装成浏览器
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

        # 最开始的网址
        self.start_url = "https://www.xicidaili.com/nn/"

        # 基础网址，用于构造其他的网址的
        self.base_url = "https://www.xicidaili.com"

        # 用于验证所爬取的 IP 地址可用性的网址
        self.check_url = "http://www.baidu.com/"

        # 爬取时停留的时间
        self.sleep_time = 1

        # 用于数据保存时候的表头
        self.header = ["country", "ip", "port", "is_anonymous", "types", "sur_time",
                       "check_time", "address", "speed", "connet_time"]

        # 保存数据的 CSV 文件名称
        self.file_name = "ip.csv"

        # 用于爬虫初始化时创建所需的文件，以防止文件不存在而引起报错
        # self.__creat_file()

    def __get_next_url(self, content):
        """
        用于获取当前网址的下一页网址的 url 地址
        :param content: 当前网址的源代码
        :return: 下一页网址
        """
        html = etree.HTML(content)
        try:
            # 尝试执行以下代码，为了防止达到最后一页时无法获取下一页的 url 而报错

            # 使用 xpath 获取下一页网址的 url 地址
            next_page_url = html.xpath('//div[@class="pagination"]/a[@class="next_page"]/@href')

            # 得到获取到的 url 地址的页码
            page_num = next_page_url[0][4:]

            # 构造下一页的能够使用的 url 地址
            next_page_url = self.base_url + next_page_url[0]
            # print(next_page_url)
            return next_page_url, page_num
        except ValueError:
            # 若无法获取下一页的 url 地址，即已经到了最后一页了，就输出以下
            print("已经是最后一页啦，后面没有啦！")
            return False

    def get_response(self, url, decode_code="utf-8", errors="", sleep_time=1):
        """
        获取目标网址的网页源代码
        :param url: 目标网址
        :param decode_code: 解码方式
        :param errors: 解码错误处理策略
        :param sleep_time: 睡眠时间
        :return: 源代码，网页状态码
        """
        # 对目标网址发起响应，并伪装程序
        response = requests.get(url, headers=self.headers)

        # 程序暂定指定时间，是为了防止程序访问目标网址速度太快而被识别为爬虫
        time.sleep(sleep_time)

        # 打印目标网址返回的状态码，200为正常，404为异常
        code = response.status_code
        # print(code)

        # 对所获得的响应进行编码
        content = response.content.decode(decode_code, errors)
        return content, code

    @staticmethod  # 这个意思是这个方法为静态方法
    def get_infos(content):
        """
        用于解析网页源代码，获取想要的数据
        :param content: 网页源代码
        :return: 目标信息列表
        """
        # 创建列表
        infos_list = []

        # 采用 xpath 方法时的固定用法
        html = etree.HTML(content)

        # 以下到达下一个注释之前都是用 xpath 方法解析网页源代码提取目标数据
        infos = html.xpath('//table[@id="ip_list"]//tr')
        for info in infos:
            infos_d = {}
            try:
                infos_d["country"] = info.xpath('./td[@class="country"]/img/@alt')[0]
            except IndexError:
                infos_d["country"] = "未知"
            some_info = info.xpath('./td/text()')
            if len(some_info) != 12:
                continue
            infos_d["ip"] = some_info[0]
            infos_d["port"] = some_info[1]
            infos_d["is_anonymous"] = some_info[4]
            infos_d["types"] = some_info[5]
            infos_d["sur_time"] = some_info[10]
            infos_d["check_time"] = some_info[11]
            try:
                infos_d["address"] = info.xpath('./td/a/text()')[0]
            except IndexError:
                infos_d["address"] = "未知"
            infos_d["speed"] = info.xpath('./td/div/@title')[0]
            infos_d["connet_time"] = info.xpath('./td/div/@title')[1]
            infos_list.append(infos_d)
        # print(infos_list)
        return infos_list

    def check_ip(self, ip, port):
        """
        用于验证单个 IP 地址的可用性，这个功能是抄别的项目的，以为可以用，
        但是好像并不行。这个问题还有待解决。
        :param ip: IP地址
        :param port: 端口号
        :return: 若可用，返回 True；若不可用，则返回 False。
        """
        try:
            conn = http.client.HTTPConnection(ip, port, timeout=5.0)
            conn.request(method="GET", url=self.check_url, headers=self.headers)
            return True
        except TimeoutError:
            return False

    def check_ip_list(self, infos_list):
        """
        用于检查传入的 ip 列表中的 ip 的可用性
        采用循环调用 self.check_ip 方法检验 IP 地址列表。
        :param infos_list: 传入的列表
        :return: 合格的 ip 列表
        """
        i = []
        for info in infos_list:
            ip = info["ip"]
            port = info["port"]
            result = self.check_ip(ip, port)
            if result:
                i.append(ip)
                print("代理 IP：{}， 端口号：{}，检验合格".format(ip["ip"], ip["port"]))
            else:
                print("代理 IP：{}， 端口号：{}，检验失败".format(ip["ip"], ip["port"]))
        return i

    def save_to_file(self, infos_list):
        """
        将数据保存到 CSV 文件。
        :param infos_list: 需要保存的信息列表
        :return:
        """
        # 采用 with open 方法打开文件，在此方法结束时会自动关闭文件。
        with open(self.file_name, "a", encoding="utf-8", newline="") as f:
            # 写入表头，创建操作对象
            wr = csv.DictWriter(f, self.header)

            # 将多行数据写入文件
            wr.writerows(infos_list)

    def __creat_file(self):
        # 创建文件，写入表头
        with open(self.file_name, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, self.header)
            writer.writeheader()
        print("文件创建成功！文件名称：" + self.file_name)

    def run(self):
        """
        当调用 run() 方法时，执行整个爬虫。
        :return:
        """
        # 创建一个 next_url，用于判定循环。
        next_url = True

        # 遍历所有网页的循环
        while next_url:
            # 第一步：向目标网址发起请求，并返回网页源代码
            content, code = self.get_response(self.start_url)
            if code != 200:
                print("网页不知道怎么了，状态码为{}，先休息十秒吧！".format(code))
                time.sleep(10)
                continue

            # 第二步：解析网页源代码，获取所需信息
            infos_list = self.get_infos(content)

            # 第三步：（可不要）检验获得的 IP 地址的可用性，并提取可用的 IP 地址的列表
            # infos_list = self.check_ip_list(infos_list)

            # 第四步：将获取的 IP 地址列表保存为 CSV 文件
            self.save_to_file(infos_list)

            # 第五步：获取下一页网页的 url 地址和下一页网页的页码，将 url 地址赋值给 self.start_url。
            self.start_url, page_num = self.__get_next_url(content)

            # 告诉你获取到第几页了
            print("成功获取第{}页信息".format(page_num))
        # print(content)

    def get_ip(self, num=10, speed=2, is_anonymous=True, types="HTTPS", connet_time=2):
        print("开始从西刺免费代理上获取代理")
        content, code = self.get_response(self.start_url)
        infos_list = self.get_infos(content)
        ips_list = []
        for infos in infos_list:
            if len(ips_list) > num:
                break
            if float(infos["speed"][:-2]) > float(speed):
                continue
            elif is_anonymous:
                if infos["is_anonymous"] == "高匿":
                    ips_list.append(infos)
                else:
                    continue
            elif infos["types"] != types:
                continue
            elif infos["connet_time"] > connet_time:
                continue
            else:
                ips_list.append(infos)

        ip_list = []
        for ips in ips_list:
            ip = ips["ip"] + ":" + ips["port"]
            ip_list.append(ip)

        print("代理获取完毕！本次获取代理数量为{}个！".format(num))
        return ip_list


if __name__ == '__main__':  # 这个是固定用法，用于整个程序的开始
    # 实例化爬虫对象
    spider = Spider()

    # 对爬虫对象进行操作：调用 run() 方法，整个爬虫开始运行。
    ip_pool = spider.get_ip()
    print(ip_pool)
