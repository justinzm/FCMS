#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = 'justin.郑'


class Category(Base):
    __tablename__ = Base.prefix+'category'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="分类ID")
    title = Column(String(50), nullable=False, comment="分类标题")
    alias = Column(String(50), comment="分类别名")
    intro = Column(String(300), comment="描述")
    status = Column(Boolean, default=True, comment="是否发布")
    sort = Column(Integer, default=0, comment="排序")

    section = relationship('Section', backref="section", uselist=False)
    section_id = Column(Integer, ForeignKey(Base.prefix + 'section.id'))

    @classmethod
    def all(cls):
        return Category.query.filter_by().all()

    @classmethod
    def count(cls):
        return Category.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return Category.query.filter_by(id=id).first()

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

