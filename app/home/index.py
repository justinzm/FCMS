#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import url_for
from werkzeug.utils import redirect

__author__ = 'justin.郑'

from . import home


@home.route('/')
def index():
    # return 'home index'
    return redirect(url_for('admin.login'))