#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'justin.郑'

from . import home


@home.route('/')
def index():
    return 'home index'