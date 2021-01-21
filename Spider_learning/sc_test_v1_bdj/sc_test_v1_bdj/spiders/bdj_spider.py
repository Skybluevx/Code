# -*- coding: utf-8 -*-
import scrapy
from sc_test_v1_bdj.items import ScTestV1BdjItem


class BdjSpiderSpider(scrapy.Spider):
    name = "bdj_spider"
    allowed_domains = ["www.budejie.com"]
    start_urls = ['http://www.budejie.com/']

    def parse(self, response):
        budejie_divs = response.xpath('//div[@class="j-r-list"]')
        for div in budejie_divs:
            text = div.xpath('.//div[@class="j-r-list-c-desc"]//text()').getall()
            text = "".join(text).strip()
            item = ScTestV1BdjItem(content=text)
            yield item

        next_url = response.xpath("//a[@class='pagenxt']/@href").get()
        url = self.start_urls[0] + str(next_url)
        if not next_url:
            return
        else:
            yield scrapy.Request(url, callback=self.parse)
