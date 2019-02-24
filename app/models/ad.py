#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base

__author__ = 'justin.郑'


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
    hits = Column(Integer, comment="点击量")