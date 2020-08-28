#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py
# @Desc    : 接口测试文件

from flask import request, jsonify, g
from app.api import api
from app.libs.token_auth import auth


@api.route('/api/v1/test', methods=['GET'])
@auth.login_required
def api_test():
    """ 测试接口
    @@@

    @@@
    """

    if request.method == 'GET':
        uid = g.member.uid
        return jsonify({"msg": "ok", "data": "测试", "count": 0, "code": 0})
 

