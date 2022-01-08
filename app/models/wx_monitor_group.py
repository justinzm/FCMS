#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 14:04
# @Author : justin.郑 3907721@qq.com
# @File : wx_monitor_group.py
# @desc : 微信监控群表

from sqlalchemy import Column, Integer, Boolean, String, SmallInteger
from app.models.base import Base


class WxMonitorGroup(Base):
    __tablename__ = Base.prefix+'wx_monitor_group'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    account_id = Column(Integer, comment="微信账号ID")
    group_id = Column(Integer, comment="微信群ID")
    type = Column(SmallInteger, default=1, comment="1全量监控，2快速监控")
    status = Column(Boolean, default=True, comment="是否启动")

    @classmethod
    def all(cls):
        return WxMonitorGroup.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxMonitorGroup.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxMonitorGroup.query.filter_by(id=id).first()



