#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

__author__ = 'justin.郑'


home = Blueprint('home', __name__)

from app.home import index