#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/5/20 下午3:29
# @Author : justin.郑 3907721@qq.com
# @File : llm.py
# @desc :

from flask import url_for, current_app
from werkzeug.utils import redirect
from app.api import api
from app.validators.forms import StockForm


@api.route('/api/tmp')
def apiindex():
    # form = StockForm().validate_for_api()
    return 'api index'