# -*- coding: utf8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Proxy(models.Model):
    id = models.IntegerField(primary_key=True, max_length=10)
    ip = models.CharField(max_length=50)
    port = models.IntegerField()
    request_at = models.DateTimeField(blank=True, null=True)
    response_at = models.DateTimeField(blank=True, null=True)
    area = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'proxy'

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'person'

class AppComment(models.Model):
    app_id = models.CharField(max_length=32)
    info_id = models.CharField(max_length=32)
    content = models.CharField(max_length=500)
    rating = models.FloatField(blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_comment'


class AppInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    app_id = models.CharField(max_length=32)
    app_name = models.CharField(max_length=100)
    app_name_more = models.CharField(max_length=200, blank=True, null=True)
    os = models.IntegerField()
    latest_version = models.CharField(max_length=50)
    update_time = models.DateTimeField()
    spider_time = models.DateTimeField()
    artist_name = models.CharField(max_length=200, blank=True, null=True)
    app_size = models.CharField(max_length=50)
    store_id = models.IntegerField()
    message_link = models.CharField(max_length=300)
    download_link = models.CharField(max_length=300)
    download_count = models.CharField(max_length=50, blank=True, null=True)
    lowest_os_version = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    update_msg = models.TextField(blank=True, null=True)
    classification = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    current_rating_count = models.IntegerField(blank=True, null=True)
    current_average_rating = models.FloatField(blank=True, null=True)
    good_rating = models.IntegerField(blank=True, null=True)
    medium_rating = models.IntegerField(blank=True, null=True)
    bad_rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_info'


class AppPicture(models.Model):
    info_id = models.CharField(max_length=32)
    link = models.CharField(max_length=300)
    path = models.CharField(max_length=300)
    type = models.IntegerField()
    version = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    md5 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_picture'


class AppReview(models.Model):
    app_id = models.CharField(primary_key=True, max_length=32)
    app_name = models.CharField(max_length=100)
    app_name_more = models.CharField(max_length=200, blank=True, null=True)
    os = models.IntegerField()
    latest_version = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    spider_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_review'


class AppSpider(models.Model):
    name = models.CharField(max_length=100)
    allowed_domains = models.CharField(max_length=300, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    store_name = models.CharField(max_length=100)
    enable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_spider'


class AppStartUrl(models.Model):
    app_id = models.CharField(max_length=32)
    app_name = models.CharField(max_length=100)
    spider_id = models.IntegerField()
    start_url = models.CharField(max_length=200)
    enable = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_start_url'


class AppStore(models.Model):
    store_name = models.CharField(max_length=100)
    search_link = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'app_store'


class WxAccount(models.Model):
    wx_id = models.CharField(max_length=100)
    wx_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    introduction = models.CharField(max_length=500, blank=True, null=True)
    type = models.IntegerField()
    add_time = models.DateTimeField()
    update_time = models.DateTimeField()
    total_follows = models.IntegerField()
    img_path = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'wx_account'


class WxArticle(models.Model):
    wx_account_id = models.IntegerField()
    title = models.CharField(max_length=500)
    abstract = models.CharField(max_length=1000)
    readings = models.IntegerField(blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField()
    img_path = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'wx_article'


# 新闻models

class NsInfo(models.Model):
    source = models.IntegerField()
    title = models.CharField(max_length=500)
    keyword = models.CharField(max_length=100)
    abstract = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=300, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ns_info'


class NsKeyword(models.Model):
    keyword = models.CharField(max_length=100)
    count = models.IntegerField()
    add_time = models.DateTimeField()
    spider_time = models.DateTimeField()
    enable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ns_keyword'


class NsSource(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=300)
    whole_url = models.CharField(max_length=300)
    search = models.CharField(max_length=300)
    enable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ns_source'
