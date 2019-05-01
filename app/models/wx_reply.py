#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, Text
from app.models.base import Base

__author__ = 'justin.郑'


class WxReply(Base):
    """
    微信公众号-关注回复表
    """
    __tablename__ = Base.prefix+'wx_reply'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    content = Column(Text, comment="回复内容")



