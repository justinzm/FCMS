#!/usr/bin/python
# -*- coding:utf-8 -*-
from wtforms import Form, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length

__author__ = 'justin.郑'


class LoginForm(Form):
    username = StringField(validators=[DataRequired(message='账号不能为空')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])


class AuthGroupForm(Form):
    id = IntegerField(validators=[])
    status = IntegerField(validators=[])
    title = StringField(validators=[DataRequired(message='权限组名称不能为空')])