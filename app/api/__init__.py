#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : __init__.py.py
# @Desc    :

from flask import Blueprint, current_app
from werkzeug.exceptions import HTTPException
from app.libs.error import APIException
from app.libs.error_code import ServerException

api = Blueprint('api', __name__)

from app.api import test
from app.api import stock
from app.api import token


# 捕捉全局异常
@api.errorhandler(Exception)
def framework_error(e):
    # print(e)
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 4007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not current_app.config['DEBUG']:
            return ServerException()
        else:
            raise e

"""

接口地址
http://127.0.0.1:5000/docs/api

"""

