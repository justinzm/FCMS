#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/1/7 14:04
# @Author : justin.郑 3907721@qq.com
# @File : wx_push_data.py
# @desc : 微信信息推送表

from sqlalchemy import Column, Integer, Boolean, String, SmallInteger, Text
from app.models.base import Base


class WxPushData(Base):
    __tablename__ = Base.prefix+'wx_push_data'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    account_id = Column(Integer, comment="微信账号ID")
    group_id = Column(Integer, comment="微信群ID")
    group_name = Column(String(50), comment="微信群名称")
    push_data = Column(Text, comment="微信群推送信息")
    push_type = Column(SmallInteger, default=1, comment="1文本，2图片及文件")
    status = Column(Boolean, default=False, comment="0未推送，1已推送")

    @classmethod
    def all(cls):
        return WxPushData.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxPushData.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxPushData.query.filter_by(id=id).first()



