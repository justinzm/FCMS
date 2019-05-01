#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

from flask import request
from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base

__author__ = 'justin.郑'


class WxImgtext(Base):
    """
    微信公众号-图文回复表
    """
    __tablename__ = Base.prefix+'wx_imgtext'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    keyword = Column(String(50), comment="关键词")
    title = Column(String(60), comment="图文标题")
    intro = Column(String(300), comment="图文简介")
    img_url = Column(String(300), comment="封面链接")
    url = Column(String(300), comment="链接正文")
    is_img = Column(Boolean, default=True, comment="是否显示封面")
    intro = Column(String(300), comment="图文简介")
    content = Column(Text, comment="回复内容")
    status = Column(Boolean, default=True, comment="是否发布")
    type = Column(Integer, default=1, comment="1完全2模糊匹配")
    readnum = Column(Integer, default=0, comment="阅读量")
    praise = Column(Integer, default=0, comment="点赞量")

    @property
    def url_img(self):
        return os.path.join(request.url_root, "static", self.img_url)

    @classmethod
    def all(cls):
        return WxImgtext.query.filter_by().all()

    @classmethod
    def count(cls):
        return WxImgtext.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return WxImgtext.query.filter_by(id=id).first()

