#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base

__author__ = 'justin.郑'


class WxText(Base):
    """
    微信公众号-文本回复表
    """
    __tablename__ = Base.prefix+'wx_text'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    keyword = Column(String(50), comment="关键词")
    content = Column(Text, comment="回复内容")
    status = Column(Boolean, default=True, comment="是否发布")
    type = Column(Integer, default=1, comment="1完全2模糊匹配")

    @classmethod
    def all(cls):
        return WxText.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxText.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxText.query.filter_by(id=id).first()

