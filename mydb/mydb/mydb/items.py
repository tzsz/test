# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MydbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy,Field()
    actor = scrapy.Field()
    xi_lie = scrapy.Field()
    zhi_zao_shang = scrapy.Field()
    dao_yan = scrapy.Field()
    shijian = scrapy.Field()
    fan_hao = scrapy.Field()
    pass
