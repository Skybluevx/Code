# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request


class BmwPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def process_item(self, item, spider):
        category = item["category"]
        urls = item["urls"]

        category_path = os.path.join(self.path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            filename = url.split("_")[-1]
            request.urlretrieve(url, os.path.join(category_path, filename))
        return item
