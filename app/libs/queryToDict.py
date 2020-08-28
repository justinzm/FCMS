#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013
# @Author  : justin.郑 3907721@qq.com
# @File    : queryToDict.py
# @Desc    : 


from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from datetime import date, time
from flask_sqlalchemy import Model
from sqlalchemy import DateTime, Numeric, Date, Time  # 有时又是DateTime


def queryToDict(models, field=None):
    not_fields = ['is_delete', 'update_time', 'delete_time']
    if field != None:
        not_fields.extend(field)

    if (isinstance(models, list)):
        if (isinstance(models[0], Model)):
            lst = []
            for model in models:
                gen = model_to_dict(model)
                dit = {}
                for g in gen:
                    key, val = g[0], g[1]
                    if key not in not_fields:
                        dit[key] = val

                # dit = dict((g[0], g[1]) for g in gen)
                lst.append(dit)
            return lst
        else:
            res = result_to_dict(models)
            return res
    else:
        if (isinstance(models, Model)):
            gen = model_to_dict(models)
            dit = {}
            for g in gen:
                key, val = g[0], g[1]
                if key not in not_fields:
                    dit[key] = val

            # dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def model_to_dict(model):  # 这段来自于参考资源
    for col in model.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        yield (col.name, value)


def find_datetime(value):
    for v in value:
        if (isinstance(value[v], cdatetime)):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    if value:
        if (isinstance(value, (cdatetime, DateTime))):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif (isinstance(value, (date, Date))):
            return value.strftime("%Y-%m-%d")
        elif (isinstance(value, (Time, time))):
            return value.strftime("%H:%M:%S")
    else:
        return ""


