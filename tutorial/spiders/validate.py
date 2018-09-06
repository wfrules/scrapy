# -*- coding: utf-8 -*-
import scrapy
from django_orm.app.models import Proxy
from scrapy.http import Request
from tutorial.items import ProxyItem
import datetime


class ValidateSpider(scrapy.Spider):
    name = "validate"
    allowed_domains = ["www.baidu.com"]
    # start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        arrProxys = Proxy.objects.all()
        for index, aProxy in enumerate(arrProxys):
            aProxyItem = ProxyItem()
            aProxyItem['id'] = aProxy.id
            aProxyItem['ip'] = aProxy.ip
            aProxyItem['port'] = aProxy.port
            aProxyItem['request_at'] = datetime.datetime.now()
            aProxyItem['response_at'] = None
            aProxyItem['area'] = aProxy.area
            aProxyItem['remark'] = aProxy.remark
            yield aProxyItem
            yield Request(url='https://www.baidu.com',  meta={'item': aProxyItem}, callback=self.parse,  dont_filter=True)

    def parse(self, response):
        aProxyItem = response.meta['item']
        aProxyItem['response_at'] = datetime.datetime.now()
        yield aProxyItem
