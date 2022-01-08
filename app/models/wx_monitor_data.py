#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 14:04
# @Author : justin.郑 3907721@qq.com
# @File : wx_monitor_data.py
# @desc : 微信群监控信息表

from sqlalchemy import Column, Integer, Boolean, String, SmallInteger, Text
from app.models.base import Base


class WxMonitorData(Base):
    __tablename__ = Base.prefix+'wx_monitor_data'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    group_id = Column(Integer, comment="微信群ID")
    group_name = Column(String(50), comment="微信群名称")
    data = Column(Text, comment="微信群信息")
    md5 = Column(String(50), comment="MD5")
    remark = Column(Text, comment="备注信息")
    status = Column(Boolean, default=True, comment="是否启动")

    @classmethod
    def all(cls):
        return WxMonitorData.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxMonitorData.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxMonitorData.query.filter_by(id=id).first()



