#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'justin.郑'

"""
机密信息 不上传git
"""

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:justin@localhost:3306/fcms'

# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'

# TABLE_PREFIX = 'sf_'
