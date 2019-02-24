#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template
from app.libs.role import role_required
from app.libs.redprint import Redprint

__author__ = 'justin.郑'

api = Redprint('welcome')


@api.route('/welcome')
@role_required()
def welcome():
    return render_template('admin/welcome/welcome.html')

