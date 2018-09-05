# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["et.mylo2o.net:55080"]
    start_urls = ['http://et.mylo2o.net:55080/api/sys/agent']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'hello': 'world'})

    def parse(self, response):
        print(response.text)
        pass
