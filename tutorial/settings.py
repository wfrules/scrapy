import os
# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tutorial'
# BOT_VERSION = '1.0'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
# USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

LOG_ENABLED = True
LOG_LEVEL = 'ERROR'


IMAGES_STORE = os.getcwd() + '/../images'

# JsonWriterPipeline
ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
    'tutorial.pipelines.MySqlPipeline': 300
}

IPPOOL = [
    {"ipaddr": "119.27.172.241:80"}
]

UPPOOL = [
    "wf1 Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "wf2 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "wf3 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'tutorial.middlewares.IPPOOlS' : 125
}

import django
from django.conf import settings
import django_orm.djsettings as s

# settings.configure(DATABASES=s.DATABASES, INSTALLED_APPS=['django_orm.app'], DEBUG=True)
django.setup()