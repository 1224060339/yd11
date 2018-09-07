# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YdpazhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gongsi = scrapy.Field()#公司
    zhiwei = scrapy.Field()#职位
    daiyu = scrapy.Field()#待遇
    xueli= scrapy.Field()#学历