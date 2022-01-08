#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 14:04
# @Author : justin.郑 3907721@qq.com
# @File : wx_group.py
# @desc : 微信群表

from sqlalchemy import Column, Integer, Boolean, String, SmallInteger
from app.models.base import Base


class WxGroup(Base):
    __tablename__ = Base.prefix+'wx_group'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    account_id = Column(Integer, comment="微信账号ID")
    group_name = Column(String(50), comment="微信群名称")
    status = Column(Boolean, default=True, comment="是否启动")

    @classmethod
    def all(cls):
        return WxGroup.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxGroup.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxGroup.query.filter_by(id=id).first()



