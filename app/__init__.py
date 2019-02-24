#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_migrate import Migrate

from app.models.base import db
from flask_login import LoginManager

__author__ = 'justin.郑'

"""
创建应用程序，并注册相关蓝图
"""

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # 系统设置常量
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'
    login_manager.login_message = '请先登录或注册'

    # 注册SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.admin import create_blueprint_admin
    from app.home import home

    app.register_blueprint(create_blueprint_admin(), url_prefix="/admin")
    app.register_blueprint(home)

