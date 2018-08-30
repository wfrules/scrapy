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

ITEM_PIPELINES = {
    'tutorial.pipelines.MySqlPipeline': 300
}