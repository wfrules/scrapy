import json
from tutorial.db import gDb
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
class MySqlPipeline(object):
    def process_item(self, item, spider):
        sSql = "insert vods(title,pic,pageurl)values(%s,%s,%s)"
        gDb.nativeExec(sSql, (item['title'], item['pic'], item['pageurl']))
        gDb.commit()
        return item

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'w')#wb是按字节 w是写字符串

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item