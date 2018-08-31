# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class JavBuzItem(Item):
    title = Field()
    pic = Field()
    pageurl = Field()
    vodurl = Field()
    image_urls = Field()
    images = Field()
    pic_path = Field()
