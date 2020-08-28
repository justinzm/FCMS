#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 0028
# @Author  : justin.郑 3907721@qq.com
# @File    : scope.py
# @Desc    : 接口权限类


class Scope:
    allow_api = []
    forbidden = []

    def __add__(self, other):
        # 运算符重载
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class AdminScope(Scope):
    allow_api = ["api.api_test"]


class MemberScope(Scope):
    allow_api = ["api.A"]


class SuperScope(Scope):
    allow_api = ["api.B"]

    def __init__(self):
        self + MemberScope() + AdminScope()
        print(self.allow_api)


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    else:
        return False

