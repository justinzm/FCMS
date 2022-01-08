#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 13:54
# @Author : justin.郑 3907721@qq.com
# @File : wx_account.py
# @desc : 微信账户管理

from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base


class WxAccount(Base):
    __tablename__ = Base.prefix+'wx_account'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    wx_name = Column(String(50), comment="微信账号名")
    member_id = Column(Integer, comment="用户ID")
    wx_sn = Column(String(50), comment="微信账号ID")
    status = Column(Boolean, default=True, comment="是否启动")

    @classmethod
    def all(cls):
        return WxAccount.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxAccount.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxAccount.query.filter_by(id=id).first()


