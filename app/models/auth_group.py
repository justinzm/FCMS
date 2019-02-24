#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.auth_permission import AuthPermission
from app.models.base import Base

__author__ = 'justin.郑'


class AuthGroup(Base):
    # 角色权限表
    __tablename__ = Base.prefix+'auth_group'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="权限组ID")
    title = Column(String(100), comment="权限组名称")
    status = Column(Boolean, default=True, comment="是否发布")
    permissions = Column(Text, comment="规则列表")

    @classmethod
    def all(cls):
        return AuthGroup.query.filter_by().all()

    @classmethod
    def count(cls):
        return AuthGroup.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return AuthGroup.query.filter_by(id=id).first()

    @classmethod
    def get_auth_json(cls, group_id):
        list = []
        aplist = AuthPermission.query.filter_by().all()
        for v in aplist:
            data = {}
            data['id'] = v.id
            data['title'] = v.per_title
            data['pid'] = v.pid
            data['checked'] = cls._is_checked(group_id, v.id)
            list.append(data)
        return list

    def _is_checked(group_id, auth_id):
        agfind = AuthGroup.query.filter_by(id=group_id).first()
        if agfind.permissions:
            permissions = agfind.permissions.split(',')
            if str(auth_id) in permissions:
                return 1
            else:
                return 0
