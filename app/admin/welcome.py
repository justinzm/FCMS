#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : welcome.py
# @Desc    : 首页管理

from flask import render_template
from app.libs.role import role_required
from app.libs.redprint import Redprint

api = Redprint('welcome')


@api.route('/welcome')
@role_required()
def welcome():
    return render_template('admin/welcome/welcome.html', menutitle='首页', navtitle='首页信息')

