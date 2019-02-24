#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 0015
# @Author  : justin.郑 3907721@qq.com
# @File    : role.py
# @Desc    : 角色权限管理

import functools
from flask import request
from flask_login import current_user
from app.libs.error_code import AuthFailed
from app.libs.logger import CmsLogger


def role_required():
    # 角色权限管理
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if request.path not in current_user.permissions:
                return AuthFailed()
                # return '未授权 该功能没有使用权限'
            else:
                return func(*args, **kw)
        return wrapper
    return decorator


def logger(tmp=""):
    # 操作 日志记录
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if request.method == 'POST':
                tmps = '管理员ID：%s 账号：%s %s' % (current_user.id, current_user.username, tmp)
                CmsLogger('info').info(message=tmps)
            return func(*args, **kw)
        return wrapper
    return decorator
