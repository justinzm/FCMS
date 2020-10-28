#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : param.py
# @Desc    : 参数管理

from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base


class Param(Base):
    __tablename__ = Base.prefix+'param'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    title = Column(String(200), comment="参数名称")
    type = Column(String(100), comment="参数类型")
    type_name = Column(String(100), comment="参数类型名称")
    sort = Column(Integer, default=0, comment="排序")
    status = Column(Boolean, default=True, comment="是否发布")

    @classmethod
    def all(cls):
        return Param.query.filter_by().all()

    @classmethod
    def count(cls):
        return Param.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Param.query.filter_by(id=id).first()


 

