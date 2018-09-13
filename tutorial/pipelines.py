from tutorial.items import VodItem, AuthorLinkItem, TabItem, ProxyItem
import json
from tutorial.db import gDb
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
class MySqlPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, VodItem):
            item['pic_path'] = item['images'][0]['path']
            gDb.saveObj('vods', item)
            gDb.commit()
        if isinstance(item, AuthorLinkItem):
            gDb.saveUnique('author_link', item, 'url')
            gDb.commit()
        if isinstance(item, TabItem):
            gDb.saveUnique('tab', item, 'url')
            gDb.commit()
        if isinstance(item, ProxyItem):
            item.save()
        return item

class MongoPipeline(object):
    collection = 'proxy'
    def __init__(self, mongo_uri, mongo_db):
         self.mongo_uri = mongo_uri
         self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''scrapy为我们访问settings提供了这样的一个方法，这里，
        我们需要从settings.py文件中，取得数据库的URI和数据库名称'''
        return cls(
            mongo_uri = 'mongodb://localhost:27017',#crawler.settings.get('MONGO_URI'),
            mongo_db = 'crawler'  #crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):

       # 爬虫一旦开启，就会实现这个方法，连接到数据库
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        '''
        爬虫一旦关闭，就会实现这个方法，关闭数据库连接
        '''
        self.client.close()
    def process_item(self, item, spider):
        if isinstance(item, ProxyItem):
            data = {
                'ip': item['ip'],
                'remark': item['remark']
            }
            table = self.db[self.collection]
            table.insert_one(data)
        return item

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'w')#wb是按字节 w是写字符串

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item