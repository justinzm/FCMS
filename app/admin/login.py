#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : login.py
# @Desc    : 登录管理

from flask import render_template, request, redirect, url_for, jsonify, current_app
from flask_login import login_user, logout_user, current_user
from app.libs.logger import CmsLogger
from app.libs.redprint import Redprint
from app.libs.tools import logger_info
from app.models.auth_user import AuthUser
from app.models.conf import Conf

api = Redprint('login')
mdb = globals()['AuthUser']
db_conf = globals()['Conf']


@api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        user_find = AuthUser.query.filter_by(username=username).first()
        if user_find and user_find.check_password(request.form.get('password')):
            # remember=True 记住我 功能
            login_user(user_find)
            # next = request.args.get('next')
            # if not next or not next.startswith('/'):
            #     next = url_for('admin.index')
            # return redirect(next)
            # CmsLogger('info').info('ID：%s 账号：%s 登录系统' % (user_find.id, user_find.username))
            logger_info("登录系统")
            return jsonify({"status": 200})
        else:
            return jsonify({"status": 401, "msg": "账号或密码错误,请重新输入"})

    if request.method == 'GET':
        find = db_conf.query.filter_by(id=1).first()
        return render_template('admin/login/login.html', find=find)


@api.route('/logout')
def logout():
    logger_info("退出系统")
    logout_user()
    return redirect(url_for('admin.index'))


@api.route('/test')
def test():
    # CmsLogger('info').info('测试logger')
    logger_info("测试logger")
    return 'abc'

