#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 0015
# @Author  : justin.郑 3907721@qq.com
# @File    : error.py
# @Desc    : 更改HTTPException为APIException

from flask import request, json
from werkzeug.exceptions import HTTPException

# code 状态码
# 200 查询成功
# 201 创建成功
# 204 删除成功
# 301 永久重定向
# 302 临时重定向
# 400 请求参数错误
# 401 未授权
# 403 禁止访问
# 404 未找到资源或页面
# 500 服务器未知错误


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake!'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        return json.dumps(body)

    def get_headers(self, environ=None, scope=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]



