#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : base.py
# @Desc    : 基类

import time
from datetime import datetime
from contextlib import contextmanager
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, Boolean


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        # 查询软删除后数据
        if 'is_delete' not in kwargs.keys():
            kwargs['is_delete'] = 0
        return super(Query, self).filter_by(**kwargs)

    def update(self, values, synchronize_session="evaluate", update_args=None):
        # 修改编辑 添加修改时间
        if 'update_time' not in values.keys():
            values['update_time'] = int(datetime.now().timestamp())
        super(Query, self).update(values, synchronize_session=synchronize_session, update_args=update_args)

    def delete(self, synchronize_session="evaluate", is_delete=False):
        if is_delete == True:
            # 真删除
            super(Query, self).delete()
        else:
            # 软删除
            values = {'is_delete': 1, 'delete_time': int(datetime.now().timestamp())}
            super(Query, self).update(values, synchronize_session=synchronize_session, update_args=None)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    # 设置表名前缀
    prefix = 'cms_'

    is_delete = Column(Boolean, default=False, comment="是否删除 True为删除")
    create_time = Column(Integer, comment="创建时间")
    update_time = Column(Integer, comment="修改时间")
    delete_time = Column(Integer, comment="删除时间")

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_time:
            time = datetime.fromtimestamp(self.create_time)
            return str(time)[0:16]
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id' and value != '':
                if key in current_app.config['STR_TO_INT']:
                    setattr(self, key, int(value))
                elif key in current_app.config['DATE_TO_INT']:
                    timeArray = time.strptime(value, "%Y-%m-%d")
                    setattr(self, key, int(time.mktime(timeArray)))
                else:
                    setattr(self, key, value)

    def set_dicts(self, multi_dict):
        res = {}
        doc = dict(multi_dict)
        for key, value in doc.items():
            if value != '' and key != 'id':
                if key in current_app.config['STR_TO_INT']:
                    res[key] = int(value)
                elif key in current_app.config['DATE_TO_INT']:
                    timeArray = time.strptime(value, "%Y-%m-%d")
                    res[key] = int(time.mktime(timeArray))
                else:
                    res[key] = value
        return res


