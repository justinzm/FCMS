#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 0022
# @Author  : justin.郑 3907721@qq.com
# @File    : section.py
# @Desc    : 单元表

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base


class Section(Base):
    __tablename__ = Base.prefix+'section'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="单元ID")
    title = Column(String(50), nullable=False, comment="单元标题")
    alias = Column(String(50), comment="单元别名")
    intro = Column(String(300), comment="描述")
    status = Column(Boolean, default=True, comment="是否发布")
    sort = Column(Integer, default=0, comment="排序")

    @classmethod
    def all(cls):
        return Section.query.filter_by().all()

    @classmethod
    def count(cls):
        return Section.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Section.query.filter_by(id=id).first()

