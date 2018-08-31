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
        iPage = int(re.findall('(?<=page=)\d*', response.url)[0]) + 1
        # sites = response.css('.box a img::attr(src)').extract()
        arrLinks = response.css('.video-item')
        for index, div in enumerate(arrLinks):
            item = JavBuzItem()
            item['title'] = div.css('h4 a::text').extract()[0]
            sPic = div.css('img::attr(src)').extract()[0]
            item['pic'] = 'http:' + sPic
            item['pageurl'] = 'http://' + self.allowed_domains[0] + '/' + div.css('a::attr(href)').extract()[0]
            item['image_urls'] = [item['pic']]
            yield Request(url=item['pageurl'], meta={'item': item}, callback=self.detail_parse)
        if len(arrLinks) > 0:
            sNextUrl = 'http://' + self.allowed_domains[0] + '/movie?sort=published&page=' + str(iPage)
            print(sNextUrl)
            yield Request(url=sNextUrl, callback=self.parse)
        else:
            print('抓取完毕')

    def detail_parse(self, response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        arrAs = response.css('.dropdown-menu li a')
        item['vodurl'] = ''
        if len(arrAs) > 0:
            objLs = arrAs[0]
            sVodUrl = objLs.css('::attr(href)').extract()[0]
            item['vodurl'] = sVodUrl

        #一级内页数据提取
        return item
