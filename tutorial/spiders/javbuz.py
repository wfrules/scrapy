# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from tutorial.items import JavBuzItem

class JavBuzSpider(scrapy.Spider):
    name = "javbuz"
    allowed_domains = ["javbuz.com/"]
    start_urls = ['http://javbuz.com/movie?sort=published&page=1']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # sites = response.css('.box a img::attr(src)').extract()
        items = []
        arrLinks = response.css('.video-item')
        for index, div in enumerate(arrLinks):
            item = JavBuzItem()
            item['title'] = div.css('h4 a::text').extract()[0]
            sPic = div.css('img::attr(src)').extract()[0]
            item['pic'] = 'http:' + sPic
            items.append(item)
        return items

