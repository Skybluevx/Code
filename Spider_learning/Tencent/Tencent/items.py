# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    position_name = scrapy.Field()
    position_e_name = scrapy.Field()
    work_location = scrapy.Field()
    position_type = scrapy.Field()
    publish_time = scrapy.Field()
    position_other = scrapy.Field()
    position_introduction = scrapy.Field()

