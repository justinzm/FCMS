#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 0015
# @Author  : justin.郑 3907721@qq.com
# @File    : error_code.py
# @Desc    :
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = '成功'
    error_code = 0


class DeleteSuccess(APIException):
    code = 202
    msg = '删除成功'
    error_code = 1


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 4000


class ServerException(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class AuthFailed(APIException):
    code = 401
    error_code = 4005
    msg = 'authorization failed'


class LoginFailed(APIException):
    code = 401
    error_code = 4006
    msg = 'Unauthorized'


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 4001


class Forbidden(APIException):
    code = 403
    error_code = 4004
    msg = 'forbidden, not in scope'


