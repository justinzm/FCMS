#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Blueprint

__author__ = 'justin.郑'


wechat = Blueprint('wechat', __name__)

from app.wechat import api

