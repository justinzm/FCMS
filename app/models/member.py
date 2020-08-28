#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 0016
# @Author  : justin.郑 3907721@qq.com
# @File    : member.py
# @Desc    : 会员管理库

from sqlalchemy import Column, Integer, String, Boolean, SmallInteger
from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash


class Member(Base):
    __tablename__ = Base.prefix+'member'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    nickname = Column(String(30), comment="昵称")
    mobile = Column(String(20), comment="用户手机号")
    email = Column(String(50), comment="用户邮箱")
    openid = Column(String(30), comment="微信openid")
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
        if self.type == 1:
            return "手机号注册"
        elif self.type == 2:
            return "邮箱注册"
        elif self.type == 3:
            return "微信注册"

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @classmethod
    def all(cls):
        return Member.query.filter_by().all()

    @classmethod
    def count(cls):
        return Member.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Member.query.filter_by(id=id).first()
 
    @staticmethod
    def verify(email, password):
        find = Member.query.filter_by(email=email, status=1).first()
        if not find:
            raise NotFound(msg="member not found")
        if not find.check_password(password):
            raise AuthFailed()
        scope = "AdminScope" if find.auth == 2 else "MemberScope"
        return {"uid": find.id, "scope": scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
