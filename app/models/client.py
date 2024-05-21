#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 0016
# @Author  : justin.郑 3907721@qq.com
# @File    : client.py
# @Desc    : 客户端库

import secrets
from sqlalchemy import Column, Integer, String, Boolean, SmallInteger
from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash


class Client(Base):
    __tablename__ = Base.prefix+'client'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    nickname = Column(String(30), comment="昵称")
    mobile = Column(String(20), comment="用户手机号")
    email = Column(String(50), comment="用户邮箱")
    openid = Column(String(30), comment="微信openid")
    _app_key = Column('app_key', String(128), nullable=False, comment="app_key")
    _app_secret = Column('app_secret', String(128), nullable=False, comment="app_secret")
    auth = Column(SmallInteger, default=1, comment="1普通用户，2管理员用户")
    _password = Column('password', String(128), nullable=False, comment="密码")
    type = Column(Integer, comment="类型1手机号 2邮箱 3微信")
    integral = Column(Integer, default=0, comment="积分")
    faceimg = Column(String(200), comment="头像")
    status = Column(Boolean, default=True, comment="是否发布")
    company = Column(String(100), comment="所属企业")
    profession = Column(String(50), comment="所属单位")

    @property
    def type_str(self):
        if self.type == 2:
            return "手机号注册"
        elif self.type == 1:
            return "邮箱注册"
        elif self.type == 3:
            return "微信注册"

    @property
    def password(self):
        return self._password

    @property
    def app_key(self):
        return self._app_key

    @property
    def app_secret(self):
        return self._app_secret

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
        self._app_key = str(secrets.token_hex(nbytes=16))
        self._app_secret = str(secrets.token_hex(nbytes=32))

    @classmethod
    def all(cls):
        return Client.query.filter_by().all()

    @classmethod
    def count(cls):
        return Client.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Client.query.filter_by(id=id).first()
 
    @staticmethod
    def verify_email(email, password):
        find = Client.query.filter_by(email=email, status=1).first()
        if not find:
            raise NotFound(msg="client not found")
        if not find.check_password(password):
            raise AuthFailed()
        scope = "AdminScope" if find.auth == 2 else "MemberScope"
        return {"uid": find.id, "scope": scope}

    @staticmethod
    def verify_mobile(mobile, password):
        find = Client.query.filter_by(mobile=mobile, status=1).first()
        if not find:
            raise NotFound(msg="client not found")
        if not find.check_password(password):
            raise AuthFailed()
        scope = "AdminScope" if find.auth == 2 else "MemberScope"
        return {"uid": find.id, "scope": scope}

    @staticmethod
    def verify(app_key, app_secret):
        find = Client.query.filter_by(_app_key=app_key, _app_secret=app_secret, status=1).first()
        if not find:
            raise NotFound(msg="client not found")
        scope = "AdminScope" if find.auth == 2 else "MemberScope"
        return {"uid": find.id, "scope": scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
