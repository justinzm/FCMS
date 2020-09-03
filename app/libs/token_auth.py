#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : token_auth.py
# @Desc    : token验证装饰器

from collections import namedtuple
from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
Member = namedtuple("Member", ["uid", "scope"])


@auth.verify_password
def verify_password(token, password):
    member_info = verify_auth_token(token)
    if not member_info:
        return False
    else:
        g.member = member_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg="token is invalid", error_code=4002)
    except SignatureExpired:
        raise AuthFailed(msg="token is expired", error_code=4003)

    # request 视图函数
    allow = is_in_scope(data['scope'], request.endpoint)
    if not allow:
        raise Forbidden()
    return Member(data['uid'], data['scope'])


# @auth.verify_password
# def verify_password(account, password):
#     # HTTPBasicAuth 规则
#     # header  key:value  key=Authorization value=basic 账户:密码
#     # Authorization:basic base64(3907721@qq.com:123qwe)
#     pass





