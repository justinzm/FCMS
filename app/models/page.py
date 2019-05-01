#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
from flask import request
from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base

__author__ = 'justin.郑'


class Page(Base):
    __tablename__ = Base.prefix+'page'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="单页ID")
    title = Column(String(50), nullable=False, comment="标题")
    img_url = Column(String(300), comment="封面图片URL")
    link_label = Column(String(60), comment="标识")
    intro = Column(String(300), comment="描述")
    status = Column(Boolean, default=True, comment="是否发布")
    sort = Column(Integer, default=0, comment="排序")
    content = Column(Text, comment="回复内容")
    readnum = Column(Integer, default=0, comment="阅读量")
    praise = Column(Integer, default=0, comment="点赞量")

    @property
    def create_time_date(self):
        timeArray = time.localtime(self.create_time)
        return time.strftime("%Y-%m-%d", timeArray)

    @property
    def url_img(self):
        return os.path.join(request.url_root, "static\\", self.img_url)

    @classmethod
    def all(cls):
        return Page.query.filter_by().all()

    @classmethod
    def count(cls):
        return Page.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Page.query.filter_by(id=id).first()

