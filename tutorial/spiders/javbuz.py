# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from tutorial.items import JavBuzItem

class JavBuzSpider(scrapy.Spider):
    name = "javbuz"
    allowed_domains = ["javbuz.com"]
    start_urls = ['http://javbuz.com/movie?sort=published&page=1']

    def parse(self, response):
        iPage = int(re.findall('(?<=page=)\d', response.url)[0]) + 1
        hxs = HtmlXPathSelector(response)
        # sites = response.css('.box a img::attr(src)').extract()
        arrLinks = response.css('.video-item')
        if len(arrLinks) > 0:
            sNextUrl = 'http://javbuz.com/movie?sort=published&page=' + str(iPage)
            print(sNextUrl)
            yield Request(url=sNextUrl, callback=self.parse)
        for index, div in enumerate(arrLinks):
            item = JavBuzItem()
            item['title'] = div.css('h4 a::text').extract()[0]
            sPic = div.css('img::attr(src)').extract()[0]
            item['pic'] = 'http:' + sPic
            yield item

