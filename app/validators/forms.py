#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024
# @Author  : justin.郑 3907721@qq.com
# @File    : forms.py
# @Desc    :

from wtforms import StringField, DateField, PasswordField, IntegerField
from wtforms.validators import DataRequired, length, ValidationError
from app.libs.enums import MemberTypeEnum
from app.validators.base_form import BaseForm


class StockForm(BaseForm):
    code = StringField(validators=[DataRequired(message="不许为空"), length(min=6, message="请填写正确股票代码")])
    date = StringField()

    def validate_date(self, field):
        if field.data != None:
            if len(field.data.replace("-", "")) != 8:
                raise ValidationError("请输入正确日期")
        else:
            return None


class MemberForm(BaseForm):
    account = StringField(validators=[DataRequired(message='不允许为空'), length(
        min=5, max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = MemberTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class ClientForm(BaseForm):
    app_key = StringField(validators=[DataRequired()])
    app_secret = StringField(validators=[DataRequired()])


class LoginForm(BaseForm):
    username = StringField(validators=[DataRequired(message='账号不能为空')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), length(6, 32)])


class AuthGroupForm(BaseForm):
    id = IntegerField(validators=[])
    status = IntegerField(validators=[])
    title = StringField(validators=[DataRequired(message='权限组名称不能为空')])


class TokenForm(BaseForm):
    token = StringField(validators=[DataRequired()])

