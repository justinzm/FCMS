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
    form = MemberForm().validate_for_api()
    promise = {
        MemberTypeEnum.MEMBER_EMAIL: Member.verify
    }
    identity = promise[MemberTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # 生成令牌
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)
    return jsonify({"token": token.decode('ascii')}), 201


@api.route('/api/v1/secret', methods=['POST'])
def get_token_info():
    """获取令牌信息"""
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


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """ 生成令牌 """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        "uid": uid,
        "ac_type": ac_type.value,
        "scope": scope
    })
