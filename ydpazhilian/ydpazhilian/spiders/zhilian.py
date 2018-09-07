# -*- coding: utf-8 -*-
import scrapy
from ydpazhilian.items import YdpazhilianItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    # 增加一个域名范围的保护，防止抓到域名之外的网站数据
    allowed_domains = ['sou.zhaopin.com']
    # 可以在这一次性把所有要抓的URL全部放入start_urls，
    # 这样就不需要自己翻页了
    start_urls=[]
    for i in range(1,100):
        start_urls.append('https://sou.zhaopin.com/?p='+str(i)+'&pageSize=60&jl=489&kw=Python&kt=3')

    def parse(self, response):
        for i in range(1,61):
            a='//*[@id="listContent"]/div['+str(i)+']'
            for each in response.xpath(a):
                item = YdpazhilianItem()
                item['gongsi']=each.xpath('./div/div[1]/div/div[2]/a/text()').extract()[0]
                item['zhiwei']=each.xpath('./div/div[1]/div/div[1]/a/span[1]@title').extract()[0]
                item['daiyu']=each.xpath('./div/div[2]/div[1]/p/text()').extract()[0]
                item['xueli']=each.xpath('./div/div[2]/div[1]/ul/li/text()').extract()[0]
                yield item
