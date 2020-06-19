#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : __init__.py.py
# @Desc    : 

from flask import Blueprint


api = Blueprint('api', __name__)

from app.api import test


"""

接口地址
http://127.0.0.1/docs/api

"""

