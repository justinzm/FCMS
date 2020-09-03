#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py
# @Desc    : 接口测试文件

from flask import request, jsonify, g
from app.api import api
from app.libs.token_auth import auth


@api.route('/api/v1/auth', methods=['GET'])
def api_auth():
    """ API鉴权机制
    @@@
    本文档主要针对HTTP API调用者，调用API时必须在请求头中带上token参数，获取token的流程如下：

    #### STEP1：获取用户app_key和app_secret

    由管理员创建用户或自建用户，每个用户都会分配一组唯一的app_key和app_secret，如：

    app_key = a4a3713c6f664c46f95a4c91dda28fd1

    app_secret = 0d73a528bfea588f402333cbe5e5f65fe72893ac25b7342ffedb55135ca603f4

    #### STEP2：生成token

    * 将app_key和app_secret 拼接为JSON格式。如：
    ```
    {"app_key":"a4a3713c6f664c46f95a4c91dda28fd1", "app_secret":"0d73a528bfea588f402333cbe5e5f65fe72893ac25b7342ffedb55135ca603f4"}
    ```
    * 以POST方式raw类型 JSON提交到 http://127.0.0.1/api/v1/get_token 地址上获取token
    http://127.0.0.1 地址 根据具体项目来定

    * token有效期为7200秒

    #### STEP3：生成请求头参数

    + 把token后面加入“:”
    + 用base64_encode对加入“:”号的token进行加密，获得加密后的值，并在该值前面加“basic ”作为Authorization的参数值

    如：Authorization: basic ZXlKaGJHY2lPaUpJVX……

    那么请求头中的参数名为Authorization，参数值就是字符串basic ZXlKaGJHY2lPaUpJVX……

    至此，所有的准备工作都做完了，下面就可以发起接口调用了,比如：
    http://127.0.0.1:5000/api/v1/test

    重要提醒：请求头中要加上token参数，否则验证不通过，视为无效请求。
    @@@
    """
    pass


@api.route('/api/v1/test', methods=['GET'])
@auth.login_required
def api_test():
    """ 测试接口
    @@@

    @@@
    """

    if request.method == 'GET':
        uid = g.member.uid
        return jsonify({"msg": "ok", "data": "测试", "member_id": uid, "code": 0})
 

