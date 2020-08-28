#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 0016
# @Author  : justin.郑 3907721@qq.com
# @File    : fixed_field.py
# @Desc    : 固定字段表

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base


class FixedField(Base):
    __tablename__ = Base.prefix+'fixed_field'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID")
    var_name = Column(String(50), comment="变量名称")
    var_example = Column(String(100), comment="变量示例")
    var_format = Column(String(50), comment="变量格式")
    var_key = Column(String(50), comment="变量名")
    var_type = Column(String(50), comment="变量类型")
    sort = Column(Integer, default=0, comment="排序")
    remark = Column(String(100), comment="备注")
    status = Column(Boolean, default=True, comment="是否发布")

    @classmethod
    def all(cls):
        return FixedField.query.filter_by().all()

    @classmethod
    def count(cls):
        return FixedField.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return FixedField.query.filter_by(id=id).first()
 

