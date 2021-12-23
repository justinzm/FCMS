#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : article.py
# @Desc    : 文章model

import os
import time
from flask import request
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Article(Base):
    __tablename__ = Base.prefix+'article'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="文章ID")
    title = Column(String(50), nullable=False, comment="文章标题")
    alias = Column(String(50), comment="文章别名")
    metakeys = Column(String(100), comment="SEO关键词")
    metadesc = Column(String(300), comment="SEO描述")
    intro = Column(String(300), comment="简介")
    img = Column(String(200), comment="文章图片")
    content = Column(Text, comment="正文")
    istop = Column(Boolean, default=False, comment="是否置顶")
    status = Column(Boolean, default=True, comment="是否发布")
    sort = Column(Integer, default=0, comment="排序")
    author = Column(String(50), comment="来源/作者")
    hits = Column(Integer, comment="点击量")
    praise = Column(Integer, comment="点赞量")

    start_time = Column(Integer, comment="开始时间")
    end_time = Column(Integer, comment="截止时间")

    section = relationship('Section', backref="sections", uselist=False)
    section_id = Column(Integer, ForeignKey(Base.prefix + 'section.id'))

    category = relationship('Category', backref="categorys", uselist=False)
    category_id = Column(Integer, ForeignKey(Base.prefix + 'category.id'))

    @property
    def start_time_date(self):
        timeArray = time.localtime(self.start_time)
        return time.strftime("%Y-%m-%d", timeArray)

    @property
    def url_img(self):
        if self.img:
            return os.path.join(request.url_root, "static\\", self.img)
        else:
            return ""

    @classmethod
    def all(cls):
        return Article.query.filter_by().all()

    @classmethod
    def count(cls):
        return Article.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Article.query.filter_by(id=id).first()

