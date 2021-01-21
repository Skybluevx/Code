# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    base_url = 'https://careers.tencent.com/search.html?index='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//a[@class='recruit-list-link']")
        for node in node_list:
            item = TencentItem()
            # 提取每个部分的信息，并且把转换为 utf-8 格式
            item["position_name"] = node.xpath("./h4/text()").extract()
            item["position_e_name"] = node.xpath("./p/span[1]/text()").extract()[0]
            item["work_location"] = node.xpath("./p/span[2]/text()").extract()[0]
            item["position_type"] = node.xpath("./p/span[3]/text()").extract()[0]
            item["publish_time"] = node.xpath("./p/span[4]/text()").extract()[0]
            item["position_other"] = node.xpath("./p/span[5]/text()").extract()[0]
            item["position_introduction"] = node.xpath("./p[2]/text()").extract()[0]
            for i in range(6):
                print(item[i])

            yield item

        # if self.offset < 10:
        #     self.offset += 1
        #     url = self.base_url + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)

        if len(response.xpath("最后下一页的xpath路径")) == 0:
            next_url = response.xpath("下一页的xpath路径").extract()[0]
            url = "前半部分的地址" + next_url
            yield scrapy.Request(url, callback=self.parse)


