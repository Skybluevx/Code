# -*- coding: utf-8 -*-
import scrapy
from sc_test_v5.items import ScTestV5Item


class Test1Spider(scrapy.Spider):
    # 爬虫名称，启动爬虫时必须的参数
    name = "test_1"
    # 域名范围，允许爬虫在这个域名下爬取，可选参数
    allowed_domains = ["http://www.itcast.cn"]
    # 起始url列表，爬虫启动后第一批请求将从这个列表中获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        note_list = response.xpath("//div[@class='li_txt']")
        # 用来储存所有的 item 字段
        # items = []
        for note in note_list:

            # 创建 item 字段对象，用来存储信息
            item = ScTestV5Item()

            # extract() 将 xpath 对象转换为 Unicode 字符串
            name = note.xpath("./h3/text()").extract()
            title = note.xpath("./h4/text()").extract()
            info = note.xpath("./p/text()").extract()

            # 把信息存入 item（可以和字典无缝对接的字段） 字段中
            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]

            # 返回提取到的每个 item 数据，给管道文件处理，同时还会回来继续执行后面的代码
            yield item
            # items.append(item)

        # return items
