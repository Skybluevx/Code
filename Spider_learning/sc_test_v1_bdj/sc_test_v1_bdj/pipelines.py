# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
from scrapy.exporters import JsonLinesItemExporter


class ScTestV1BdjPipeline(object):
    def __init__(self):
        self.f = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=False, encoding="utf-8")

    def open_spider(self, spider):
        print("爬虫开始啦...")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        print("爬虫结束啦...")
