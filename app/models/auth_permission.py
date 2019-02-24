#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base

__author__ = 'justin.郑'


class AuthPermission(Base):
    # 权限表
    __tablename__ = Base.prefix+'auth_permission'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="权限规则ID")
    _per_name = Column('per_name', String(50), comment="规则名称（控制器）")
    per_title = Column(String(50), comment="菜单名称")
    status = Column(Boolean, default=True, comment="是否发布")
    icon = Column(String(30), comment="图标")
    pid = Column(Integer, comment="父级ID")
    sort = Column(Integer, default=0, comment="排序")

    @property
    def per_name(self):
        return self._per_name

    @per_name.setter
    def per_name(self, value):
        if value:
            self._per_name = '/admin/' + value
        else:
            self._per_name = ''

    @classmethod
    def all(cls):
        return AuthPermission.query.filter_by().order_by(cls.sort.desc()).all()

    @classmethod
    def count(cls):
        return AuthPermission.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return AuthPermission.query.filter_by(id=id).first()

