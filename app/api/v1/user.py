#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024-05-13 22:41
# @Author : justin.郑 3907721@qq.com
# @File : user.py
# @desc :

from flask import render_template, request, jsonify

from app.libs.error import APIException
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.libs.role import role_required

api = Redprint('user')
@api.route('/user_get')
def v1_get():
    return "api v1 user"

@api.route('/user_post', methods=['POST'])
def v1_post():
    data = request.form
    return Success()