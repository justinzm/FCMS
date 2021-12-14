#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : auth_permission.py
# @Desc    : 菜单(权限)管理

from flask import render_template, request, jsonify
from app.libs.role import role_required
from app.libs.tools import ArrayLevel
from app.libs.redprint import Redprint
from app.models.auth_permission import AuthPermission
from app.models.base import db

api = Redprint('auth_permission')
mdb = globals()['AuthPermission']


@api.route('/index')
@role_required()
def auth_permission_index():
    arraylevel = ArrayLevel()
    arraylevel.array2level(mdb.all())
    all = arraylevel.get_list()
    count = mdb.count()
    return render_template('admin/auth_permission/index.html', list=all, count=count, menutitle='菜单(权限)管理', navtitle='菜单(权限)列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
def auth_permission_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        arraylevel = ArrayLevel()
        arraylevel.array2level(mdb.all())
        permission_list = arraylevel.get_list()
        if request.args.get('pid'):
            pid = int(request.args.get('pid'))
        else:
            pid = 0
        return render_template('admin/auth_permission/add.html', pid=pid, permission_list=permission_list)


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def auth_permission_edit():
    if request.method == 'GET':
        arraylevel = ArrayLevel()
        arraylevel.array2level(mdb.all())
        permission_list = arraylevel.get_list()
        id = request.args.get('id')
        find = mdb.by_id(id)
        return render_template('admin/auth_permission/edit.html', find=find, permission_list=permission_list)

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        try:
            mdb.query.filter_by(id=id).update(data)
            db.session.commit()
        except Exception as e:
            return jsonify({'status': 400, 'msg': e})
        return jsonify({'status': 200})


@api.route('/delete', methods=['POST'])
@role_required()
def auth_permission_delete():
    id = request.form.get('id')
    id_list = id.split(",")
    try:
        if len(id_list) > 1:
            for i in id_list:
                mdb.query.filter_by(id=i).delete()
        else:
            mdb.query.filter_by(id=id).delete()
        db.session.commit()
    except Exception as e:
        return jsonify({'status': 400, 'msg': e})
    return jsonify({'status': 200})

