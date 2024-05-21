#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/5/5 15:03
# @Author : justin.郑 3907721@qq.com
# @File : user.py
# @desc : 用户信息管理

import os
from flask import request
from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base


class User(Base):
    __tablename__ = Base.prefix + 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    name = Column(String(30), comment="真实姓名")
    nickname = Column(String(30), comment="昵称")
    mobile = Column(String(20), comment="用户手机号")
    openid = Column(String(30), comment="微信openid")
    faceimg = Column(String(200), comment="头像")
    status = Column(Boolean, default=True, comment="是否发布")

    @classmethod
    def all(cls):
        return User.query.filter_by().all()

    @classmethod
    def count(cls):
        return User.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return User.query.filter_by(id=id).first()


