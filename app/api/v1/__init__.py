#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024-05-13 22:39
# @Author : justin.郑 3907721@qq.com
# @File : __init__.py.py
# @desc :

from flask import Blueprint

from app.api.v1 import user


def create_blueprint_api_v1():
    api_v1_blueprint = Blueprint('v1', __name__)

    user.api.register(api_v1_blueprint)

    return api_v1_blueprint