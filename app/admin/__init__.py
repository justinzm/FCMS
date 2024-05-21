#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : __init__.py
# @Desc    :

from flask import Blueprint
from app.admin import auth_group, login, index, welcome, auth_permission, auth_user, conf, section, category, article, \
    upload, page, member, wx_diymenu, wx_imgtext, wx_reply, wx_text, param, ad, user, client


def create_blueprint_admin():
    admin_blueprint = Blueprint('admin', __name__)

    conf.api.register(admin_blueprint)
    auth_user.api.register(admin_blueprint)
    auth_permission.api.register(admin_blueprint)
    auth_group.api.register(admin_blueprint)
    login.api.register(admin_blueprint)
    welcome.api.register(admin_blueprint)
    index.api.register(admin_blueprint)
    section.api.register(admin_blueprint)
    category.api.register(admin_blueprint)
    article.api.register(admin_blueprint)
    upload.api.register(admin_blueprint)
    page.api.register(admin_blueprint)
    member.api.register(admin_blueprint)
    param.api.register(admin_blueprint)
    ad.api.register(admin_blueprint)
    wx_diymenu.api.register(admin_blueprint)
    wx_imgtext.api.register(admin_blueprint)
    wx_reply.api.register(admin_blueprint)
    wx_text.api.register(admin_blueprint)
    user.api.register(admin_blueprint)
    client.api.register(admin_blueprint)

    return admin_blueprint

# from app.admin import auth
# from app.admin import auth_group
# from app.admin import index
# from app.admin import welcome