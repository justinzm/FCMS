#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 0016
# @Author  : justin.郑 3907721@qq.com
# @File    : template.py
# @Desc    : 模板表
import time

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base


class Template(Base):
    __tablename__ = Base.prefix+'template'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    template_name = Column(String(100), comment="模板名称")
    member_id = Column(Integer, comment="所属用户ID")
    project_id = Column(Integer, comment="所属项目ID")
    title = Column(String(200), comment="模板标题")
    intro = Column(String(500), comment="文章摘要")
    content = Column(Text, comment="文章正文")
    sort = Column(Integer, default=0, comment="排序")
    status = Column(Boolean, default=True, comment="是否发布")

    @property
    def create_time_date(self):
        timeArray = time.localtime(self.create_time)
        return time.strftime("%Y-%m-%d", timeArray)

    @classmethod
    def all(cls):
        return Template.query.filter_by().all()

    @classmethod
    def count(cls):
        return Template.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Template.query.filter_by(id=id).first()
 

