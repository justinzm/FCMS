#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 0022
# @Author  : justin.郑 3907721@qq.com
# @File    : wx_reply.py
# @Desc    : 微信公众号-关注回复表

from sqlalchemy import Column, Integer, Text
from app.models.base import Base


class WxReply(Base):
    __tablename__ = Base.prefix+'wx_reply'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    content = Column(Text, comment="回复内容")



