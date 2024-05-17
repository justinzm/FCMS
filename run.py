#!/usr/bin/python
# -*- coding:utf-8 -*-
from http.client import HTTPException

from app import create_app

__author__ = 'justin.郑'

from app.libs.error import APIException
from app.libs.error_code import ServerException

app = create_app()

# 捕捉全局异常
@app.errorhandler(Exception)
def framework_error(e):
    # print(e)
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerException()
        else:
            raise e


if __name__ == '__main__':
    app.run()

