# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from tutorial.items import AuthorLinkItem,TabItem
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
            yield Request(url=sLink, meta={'author_id': objRet['id']}, callback=self.tablist_parse)
    def tablist_parse(self, response):
            arrLinks = response.css("#dgListSong tr")
            for index, tr in enumerate(arrLinks):
                if index > 0:#排除表头行
                    sLink = self.start_urls[0] + "/" + tr.css('td a::attr(href)').extract()[0].strip()
                    sSong = tr.css('td a::text').extract()[0].strip()
                    objItem = TabItem()
                    sSql = "select id from song where author_id=%s and sname=%s"
                    arrRet = gDb.nativeQry(sSql, [response.meta['author_id'], sSong])
                    if len(arrRet) == 0:
                        iSongId = gDb.saveObj('song ', {'author_id': response.meta['author_id'],'sname': sSong})
                        gDb.commit()
                    else:
                       iSongId = arrRet[0]['id']
                    objItem['song_id'] = iSongId
                    sType = tr.css('td:nth-child(4)::text').extract()[0].strip()
                    iType = 0
                    if sType == 'TXT':
                        iType = 1
                    elif sType == 'IMG':
                        iType = 2
                    elif sType == 'GTP':
                        iType = 3
                    objItem['site_id'] = self.site_id
                    objItem['url'] = sLink
                    objItem['ttype'] = iType
                    yield Request(url=sLink, meta={'item': objItem}, callback=self.tabdetail_parse)
    def tabdetail_parse(self, response):
            objItem = response.meta['item']
            if objItem['ttype'] == 1:
                objItem['content'] = response.css('#txt pre::text').extract()[0]
            elif  objItem['ttype'] == 2:
                objItem['content'] = self.start_urls[0] + "/" + response.css('#imgTab img::attr(src)').extract()[0]
            elif  objItem['ttype'] == 3:
                objItem['content'] = self.start_urls[0] + "/" + response.css('#gtp form::attr(action)').extract()[0]
            return objItem