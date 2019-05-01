#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base

__author__ = 'justin.郑'


class WxDiymenu(Base):
    """
    微信公众号-自定义菜单表
    """
    __tablename__ = Base.prefix+'wx_diymenu'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    pid = Column(Integer, comment="父ID")
    keyword = Column(String(50), comment="关键词")
    name = Column(String(20), comment="菜单标题")
    type = Column(String(20), comment="类型")
    sort = Column(Integer, comment="排序")
    url = Column(Text, comment="链接地址")
    status = Column(Boolean, default=True, comment="是否发布")

    @classmethod
    def all(cls):
        return WxDiymenu.query.filter_by().order_by(WxDiymenu.sort.desc()).all()

    @classmethod
    def count(cls):
        return WxDiymenu.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxDiymenu.query.filter_by(id=id).first()

