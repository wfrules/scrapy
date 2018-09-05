# -*- coding: utf-8 -*-

SECRET_KEY = '123'

import os
import json
objConfigFile = open(os.getcwd() + "/cliconfig.json", encoding='utf-8')  # 设置以utf - 8 解码模式读取文件，encoding参数必须设置
objSetting = json.load(objConfigFile)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': objSetting['db'],
        'USER': objSetting['user'],
        'PASSWORD': objSetting['passwd'],
        'HOST': objSetting['host'],
        'PORT': objSetting['port'],
        'OPTIONS': {'charset': 'utf8'}
    },
}