#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024
# @Author  : justin.郑 3907721@qq.com
# @File    : enums.py
# @Desc    : 系统枚举

from enum import Enum


# 用户类型枚举
class MemberTypeEnum(Enum):
    MEMBER_EMAIL = 1
    MEMBER_MOBILE = 2
    MEMBER_WX = 3

