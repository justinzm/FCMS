#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String
from app.models.base import Base

__author__ = 'justin.郑'


class Conf(Base):
    __tablename__ = Base.prefix+'config'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="配置表ID")
    sitename = Column(String(50), comment="站点名称")
    metakeys = Column(String(100), comment="站点关键词")
    metadesc = Column(String(300), comment="站点描述")
    company = Column(String(100), comment="公司名称")
    siteurl = Column(String(255), comment="站点网址")
    icp = Column(String(100), comment="备案信息")
    tel = Column(String(20), comment="联系电话")
    address = Column(String(300), comment="公司地址")
