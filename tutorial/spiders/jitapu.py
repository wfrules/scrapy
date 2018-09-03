# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tutorial.items import AuthorLinkItem
from tutorial.db import gDb
import re

class JitapuSpider(scrapy.Spider):
    name = 'jitapu'
    allowed_domains = ['www.jitapu.com']
    start_urls = ['http://www.jitapu.com']
    site_id = 1
    def parse(self, response):
        arrLinks = response.css('.linkLetter a::attr(href)').extract()
        for index, aLink in enumerate(arrLinks):
            sLink = self.start_urls[0] + "/" + aLink
            yield Request(url=sLink, callback=self.index_parse)
        pass

    def index_parse(self, response):
        # 接收索引数据
        arrLinks = response.css('#dlListArtist a')
        for index, aLink in enumerate(arrLinks):
            objData = {'aname': aLink.css('::text').extract()[0].strip(), 'id': 0}
            objRet = gDb.saveUnique('author', objData, 'aname')
            gDb.commit()
            objItem = AuthorLinkItem()
            objItem['site_id'] = self.site_id
            objItem['author_id'] = objRet['id']
            sLink = self.start_urls[0] + "/" + aLink.css('::attr(href)').extract()[0].strip()
            objItem['url'] = sLink
            yield objItem
            yield Request(url=sLink, callback=self.tablist_parse)
    def tablist_parse(self, response):
            arrLinks = response.css("#dgListSong tr")
            for index, tr in enumerate(arrLinks):
                if index > 0:#排除表头行
                    sLink = self.start_urls[0] + "/" + tr.css('td a::attr(href)').extract()[0].strip()
                    print(tr.css('td:nth-child(4)::text').extract()[0].strip())
                    # yield Request(url=sLink, callback=self.tabdetail_parse)
    def tabdetail_parse(self, response):
            print(response.url)