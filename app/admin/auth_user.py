#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, request, jsonify
from werkzeug.security import generate_password_hash
from app.libs.redprint import Redprint
from app.libs.role import role_required, logger
from app.models.auth_group import AuthGroup
from app.models.auth_user import AuthUser
from app.models.base import db

__author__ = 'justin.郑'

api = Redprint('auth_user')
mdb = globals()['AuthUser']
mdb_auth_group = globals()['AuthGroup']


@api.route('/index')
@role_required()
def auth_user_index():
    all = mdb.all()
    count = mdb.count()
    return render_template('admin/auth_user/index.html', list=all, count=count, menutitle='管理员管理', navtitle='列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
@logger('添加管理员')
def auth_user_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        group_list = mdb_auth_group.all()
        return render_template('admin/auth_user/add.html', group_list=group_list)


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def auth_user_edit():
    if request.method == 'GET':
        group_list = mdb_auth_group.all()
        id = request.args.get('id')
        find = mdb.by_id(id)
        return render_template('admin/auth_user/edit.html', find=find, group_list=group_list)

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        if request.form.get('_password'):
            data['_password'] = generate_password_hash(request.form.get('_password'))
        try:
             mdb.query.filter_by(id=id).update(data)
        except Exception as e:
            return jsonify({'status': 400, 'msg': e})
        return jsonify({'status': 200})


@api.route('/delete', methods=['POST'])
@role_required()
@logger('删除管理员')
def auth_user_delete():
    id = request.form.get('id')
    id_list = id.split(",")
    try:
        if len(id_list) > 1:
            for i in id_list:
                mdb.query.filter_by(id=i).delete()
        else:
            mdb.query.filter_by(id=id).delete()
    except Exception as e:
        return jsonify({'status': 400, 'msg': e})
    return jsonify({'status': 200})

