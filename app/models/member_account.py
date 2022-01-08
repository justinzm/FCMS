#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 14:04
# @Author : justin.郑 3907721@qq.com
# @File : member_account.py
# @desc : 用户与微信账号关联表

from sqlalchemy import Column, Integer, Boolean
from app.models.base import Base


class MemberAccount(Base):
    __tablename__ = Base.prefix+'member_account'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    member_id = Column(Integer, comment="用户ID")
    account_id = Column(Integer, comment="微信账号ID")
    status = Column(Boolean, default=True, comment="是否启动")

    @classmethod
    def all(cls):
        return MemberAccount.query.filter_by().all()

    @classmethod
    def count(cls):
        return MemberAccount.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return MemberAccount.query.filter_by(id=id).first()



