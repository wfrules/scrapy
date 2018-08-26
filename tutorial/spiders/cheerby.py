# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import JavBuzItem

class CheerbySpider(scrapy.Spider):
    name = "cheerby"
    allowed_domains = ["javbuz.com/"]
    start_urls = ['http://javbuz.com/movie?sort=published&page=1']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # sites = response.css('.box a img::attr(src)').extract()
        items = []
        arrLinks = response.css('.video-item')
        for index, div in enumerate(arrLinks):
            item = JavBuzItem()
            item['title'] = div.css('h4 a::text').extract()
            sPic = div.css('img::attr(src)').extract()
            item['pic'] = sPic
            items.append(item)
        return items

