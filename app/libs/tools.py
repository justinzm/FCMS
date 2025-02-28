#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 0015
# @Author  : justin.郑 3907721@qq.com
# @File    : tools.py
# @Desc    : 自定义函数

from flask import request
from flask_login import current_user
from app.libs.logger import logger


class ArrayLevel:
    # 数组层级缩进转换
    def __init__(self):
        self.list = []

    def array2level(self, con, pid=0, level=1):
        for v in con:
            if v.pid == pid:
                v.level = level
                self.list.append(v)
                self.array2level(con, pid=v.id, level=level+1)

    def get_list(self):
        return self.list


def arrayTree(array, pid='pid', child_key_name='children'):
    """
    构建层级（树状）数组
    :param array:   要进行处理的一维数组，经过该函数处理后，该数组自动转为树状数组
    :param pid:     父级ID的字段名
    :param child_key_name:  子元素键名
    """
    list = []
    for con in array:
        if con['pid'] == 0:
            con['children'] = array_children(array, con['id'])
            list.append(con)

    return list


def array_children(array, pid):
    list = []
    for con in array:
        if con['pid'] == pid:
            list.append(con)
    return list


# 日志
def logger_info(message=None):
    tmps = 'admin_id：%s username：%s path：%s message：%s' % (current_user.id, current_user.username, request.path, message)
    logger.info(tmps)


def logger_error(message=None):
    tmps = 'admin_id：%s username：%s path：%s err：%s' % (current_user.id, current_user.username, request.path, message)
    logger.error(tmps)

