# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["et.mylo2o.net:55080"]
    start_urls = ['http://et.mylo2o.net:55080/api/sys/agent']

    def parse(self, response):
        print(response.text)
        pass
