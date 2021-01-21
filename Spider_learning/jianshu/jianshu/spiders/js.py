# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        article_id = response.url.split("?")[0].split("/")[-1]
        content = response.xpath("//article[@class='_2rhmJa']//text()").getall()
        content = "".join(content).replace("\n", "")
        print(type(title), type(article_id), type(response.url), type(content))

        item = ArticleItem(title=title,
                           article_id=article_id,
                           origin_url=response.url,
                           content=content
                           )

        yield item

