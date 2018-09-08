# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

from scrapy_djangoitem import DjangoItem

from django_orm.app.models import Proxy

class ProxyItem(DjangoItem):
    django_model = Proxy

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class VodItem(Item):
    title = Field()
    pic = Field()
    pageurl = Field()
    vodurl = Field()
    image_urls = Field()
    images = Field()
    pic_path = Field()

class AuthorLinkItem(Item):
    id = Field()
    site_id = Field()
    author_id = Field()
    url = Field()

class TabItem(Item):
    id = Field()
    site_id = Field()
    song_id = Field()
    url = Field()
    ttype = Field()
    content = Field()