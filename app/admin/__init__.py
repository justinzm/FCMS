#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from app.admin import auth_group, login, index, welcome, auth_permission, auth_user, conf, section, category, article, \
    upload

__author__ = 'justin.郑'


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

    return admin_blueprint

# from app.admin import auth
# from app.admin import auth_group
# from app.admin import index
# from app.admin import welcome