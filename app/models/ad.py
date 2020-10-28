#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : ad.py
# @Desc    : 广告管理

import os
from flask import request
from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base


class Ad(Base):
    __tablename__ = Base.prefix+'ad'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="广告ID")
    title = Column(String(50), comment="广告标题")
    url = Column(String(300), comment="广告链接地址")
    img = Column(String(300), comment="广告图片")
    intro = Column(String(300), comment="描述")
    content = Column(Text, comment="广告代码")
    status = Column(Boolean, default=True, comment="是否发布")
    sort = Column(Integer, default=0, comment="排序")
    type = Column(String(50), comment="类型")
    hits = Column(Integer,  default=0, comment="点击量")

    @property
    def url_img(self):
        return os.path.join(request.url_root, "static\\", self.img)

    @classmethod
    def all(cls):
        return Ad.query.filter_by().all()

    @classmethod
    def count(cls):
        return Ad.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Ad.query.filter_by(id=id).first()

