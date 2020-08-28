#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : fake.py
# @Desc    : 创建初始数据或假数据

from app import create_app
from app.models.base import db
from app.models.ad import Ad

app = create_app()
with app.app_context():
    with db.auto_commit():
        ad = Ad()
        ad.title = "测试"
        db.session.add(ad)
 

