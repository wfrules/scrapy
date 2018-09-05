# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tutorial.items import ProxyItem

class ProxySpider(scrapy.Spider):
    name = '66ip'
    allowed_domains = ['www.66ip.cn']
    start_urls = ['http://www.66ip.cn']

    def parse(self, response):
        arrLinks = response.css('.textlarge22 li a::attr(href)').extract()
        for index, aLink in enumerate(arrLinks):
            sLink = self.start_urls[0] + "/" + aLink
            yield Request(url=sLink, callback=self.area_parse)
    def area_parse(self, response):
        arrTrs = response.css('#footer tr')
        for index, aTr in enumerate(arrTrs):
            if index > 0:
                arrTds = aTr.css(" td")
                sIp = arrTds[0].css("::text").extract()[0]
                iPort = arrTds[1].css("::text").extract()[0]
                sArea = arrTds[2].css("::text").extract()[0]
                objItem = ProxyItem()
                objItem['ip'] = sIp
                objItem['port'] = iPort
                objItem['area'] = sArea
                yield objItem
