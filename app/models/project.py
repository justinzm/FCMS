#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 0022
# @Author  : justin.郑 3907721@qq.com
# @File    : project.py
# @Desc    : 项目表

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base
import time


class Project(Base):
    __tablename__ = Base.prefix + 'project'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    name = Column(String(50), comment="项目名称")
    intro = Column(String(500), comment="项目摘要")
    type = Column(String(30), comment="项目类型")
    sort = Column(Integer, default=0, comment="排序")
    status = Column(Boolean, default=True, comment="是否发布")

    @property
    def create_time_date(self):
        timeArray = time.localtime(self.create_time)
        return time.strftime("%Y-%m-%d", timeArray)

    @classmethod
    def all(cls):
        return Project.query.filter_by().all()

    @classmethod
    def count(cls):
        return Project.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Project.query.filter_by(id=id).first()

 

