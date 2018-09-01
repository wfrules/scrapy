# -*- coding: utf-8 -*-
# 导入随机模块
import random
# 导入settings文件中的IPPOOL
from .settings import IPPOOL
from .settings import UPPOOL
# 导入官方文档对应的HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOlS(HttpProxyMiddleware):
    # 初始化
    def __init__(self, ip=''):
        self.ip = ip

    # 请求处理
    def process_request(self, request, spider):
        # 先随机选择一个IP
        thisip = random.choice(IPPOOL)
        # print("当前使用IP是："+ thisip["ipaddr"])
        # request.meta["proxy"] = "http://"+thisip["ipaddr"]

        thisua = random.choice(UPPOOL)
        # print("当前使用User-Agent是："+thisua)
        request.headers.setdefault('User-Agent',thisua)