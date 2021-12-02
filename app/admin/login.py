#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, request, redirect, url_for, jsonify, current_app
from flask_login import login_user, logout_user, current_user

from app.libs.logger import CmsLogger
from app.libs.redprint import Redprint
from app.models.auth_user import AuthUser
from app.models.conf import Conf

__author__ = 'justin.郑'

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
            return jsonify({"status": 200})
        else:
            return jsonify({"status": 401, "msg": "账号或密码错误,请重新输入"})

    if request.method == 'GET':
        find = db_conf.query.filter_by(id=1).first()
        return render_template('admin/login/login.html', find=find)


@api.route('/logout')
def logout():
    CmsLogger('info').info('ID：%s 账号：%s 退出系统' % (current_user.id, current_user.username))
    logout_user()
    return redirect(url_for('admin.index'))


@api.route('/test')
def test():
    CmsLogger('info').info('测试logger')
    return 'abc'

