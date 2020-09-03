#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : token.py
# @Desc    : token令牌

import time
from flask import jsonify, current_app
from app.api import api
from app.libs.enums import MemberTypeEnum
from app.libs.error_code import AuthFailed
from app.models.member import Member
from app.validators.forms import MemberForm, TokenForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature


@api.route('/api/v1/get_token', methods=['POST'])
def get_token():
    """ 获取Token
    @@@
    #### 参数

    | 参数 | 是否必填 | 类型 | 备注 |
    |--------|--------|--------|--------|
    |    app_key    |    是    |    String   |        |
    |    app_secret    |    是    |    String   |       |

    #### 返回 json

    > { "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5OTEyNDA2MiwiZXhwIjoxNTk5MTMxMjYyfQ.eyJ1aWQiOjUsInNjb3BlIjoiTWVtYmVyU2NvcGUifQ.Y1DV9jRO7BajErkyqVws3vhXer-iEPclKNatn7b1UguYDjYsqmIbN0zZGVxXXjGBq5FiOdPF84A3XzMwezzKdg" }

    #### 备注
    - POST Raw JSON 方式提交
    - http://127.0.0.1:5000/api/v1/get_token
    @@@
    """
    form = MemberForm().validate_for_api()
    identity = Member.verify(form.app_key.data, form.app_secret.data)
    # 生成令牌
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], identity['scope'], expiration)
    return jsonify({"token": token.decode('ascii')}), 201


@api.route('/api/v1/get_token_info', methods=['POST'])
def get_token_info():
    """获取令牌信息
    @@@
    #### 参数

    | 参数 | 是否必填 | 类型 | 备注 |
    |--------|--------|--------|--------|
    |    token    |    是    |    String   |         |

    #### 返回 json

    > {
        "create_at": "2020-09-03 17:07:42",
        "expire_in": "2020-09-03 19:07:42",
        "scope": "MemberScope",
        "uid": 5
    }

    #### 备注
    - POST Raw JSON 方式提交
    - http://127.0.0.1:5000/api/v1/get_token_info
    @@@
    """
    form = TokenForm().validate_for_api()
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)

    return jsonify({
        'scope': data[0]['scope'],
        'create_at': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data[1]['iat'])),
        'expire_in': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data[1]['exp'])),
        'uid': data[0]['uid']
    })


def generate_auth_token(uid, scope=None, expiration=7200):
    """ 生成令牌 """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        "uid": uid,
        "scope": scope
    })
