#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_caching import Cache
from flask_docs import ApiDoc
from flask_migrate import Migrate
from app.models.base import db
from flask_login import LoginManager
from flask_cors import *

__author__ = 'justin.郑'

"""
创建应用程序，并注册相关蓝图
"""

login_manager = LoginManager()
cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # 系统设置常量
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    # # 需要显示文档的 Api
    # app.config['API_DOC_MEMBER'] = ['api']
    # # 需要排除的 RESTful Api 文档
    # app.config['RESTFUL_API_DOC_EXCLUDE'] = []
    # ApiDoc(app)

    # 注册蓝图
    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'
    login_manager.login_message = '请先登录或注册'

    # 注册SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    # 设置注册缓存
    cache.init_app(app)

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.admin import create_blueprint_admin
    from app.api import api
    from app.home import home
    from app.wechat import wechat

    app.register_blueprint(create_blueprint_admin(), url_prefix="/admin")
    app.register_blueprint(home)
    app.register_blueprint(wechat)
    app.register_blueprint(api)

