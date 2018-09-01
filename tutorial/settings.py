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
    {"ipaddr": "221.230.72.165:80"},
    {"ipaddr": "175.154.50.162:8118"},
    {"ipaddr": "111.155.116.212:8123"}
]
