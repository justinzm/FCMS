#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : index.py
# @Desc    : 首页管理

from flask import render_template, current_app
from flask_login import login_required, current_user
from sqlalchemy import desc
from app.libs.redprint import Redprint
from app.libs.tools import arrayTree
from app.models.auth_group import AuthGroup
from app.models.conf import Conf
from app.models.auth_permission import AuthPermission

api = Redprint('index')
db_conf = globals()['Conf']


@api.route('/')
@login_required
def index():
    group_id = current_user.group_id
    group_find = AuthGroup.query.filter_by(id=group_id).first()
    ids = list(map(int, group_find.permissions.split(",")))

    per_list = AuthPermission.query\
        .filter_by(status=1)\
        .order_by(desc('sort'), desc('id'))\
        .all()

    per_array = []
    for per in per_list:
        if per.id in ids:
            data = {
                'per_title': per.per_title,
                'per_name': per.per_name,
                'pid': per.pid,
                'id': per.id,
                'icon': per.icon
            }
            per_array.append(data)
    per_list = arrayTree(per_array)
    find = db_conf.query.filter_by(id=1).first()

    return render_template('admin/index.html', per_list=per_list, find=find, username=current_user.username, group_find=group_find, version=current_app.config['VERSION_ADMIN'])

