#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.auth_group import AuthGroup
from app.models.auth_permission import AuthPermission
from app.models.base import Base
from app import login_manager

__author__ = 'justin.郑'


class AuthUser(UserMixin, Base):
    __tablename__ = Base.prefix+'auth_user'

    id = Column(Integer, primary_key=True, autoincrement=True, comment="管理员ID")
    username = Column(String(50), unique=True, comment="管理员账号")
    _password = Column('password', String(128), nullable=False, comment="密码")
    status = Column(Boolean, default=True, comment="是否发布")
    auth_group = relationship('AuthGroup', backref='auth_group', uselist=False)
    group_id = Column(Integer, ForeignKey(Base.prefix + 'auth_group.id'))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @classmethod
    def all(cls):
        return AuthUser.query.filter_by().all()

    @classmethod
    def count(cls):
        return AuthUser.query.filter_by().count()

    @classmethod
    def by_id(cls, id):
        return AuthUser.query.filter_by(id=id).first()

    def check_password(self, raw):
        return check_password_hash(self._password, raw)


@login_manager.user_loader
def get_user(uid):
    user = AuthUser.query.get(int(uid))
    user_group = AuthGroup.query.filter_by(id=user.group_id).first()

    per_codes = ['/admin/welcome/welcome']
    per_ids = user_group.permissions.split(",")
    for per_id in per_ids:
        per_find = AuthPermission.query.filter_by(id=per_id).first()
        if per_find:
            per_codes.append(per_find.per_name)
    per_codes = list(set(per_codes))
    user.permissions = per_codes
    return user

