# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class XmfishSpider(scrapy.Spider):
    name = "xmfish"
    allowed_domains = ["bbs.xmfish.com"]
    start_urls = ['http://bbs.xmfish.com']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'24a79_winduser': 'C1VWW1VoUAhRXlMFUwMMAAAOAVQBAlMHBAZUW1ECUARZAQZeD1ZqahEIWEBZXQZQFUUxFAQ',\
                                        '24a79_user_id_flag': '5673Ge5gugpMl3RXDwjcUQ4IPcf0gQBDEmhmAhOa18u8cQ'},  dont_filter=True, \
                                meta={'cookiejar': 1})

    def parse(self, response):
        print(response.css('#header .fr .nav-link-account::text').extract_first())
        # print(response.text)
        pass
