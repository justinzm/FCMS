#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, request, jsonify

from app.forms.auth import AuthGroupForm
from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.models.auth_group import AuthGroup
from app.models.base import db

__author__ = 'justin.郑'

api = Redprint('auth_group')
mdb = globals()['AuthGroup']

@api.route('/index')
@role_required()
def auth_group_index():
    all = mdb.all()
    count = mdb.count()
    return render_template('admin/auth_group/index.html', list=all, count=count, menutitle='权限组管理', navtitle='列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
def auth_group_add():
    form = AuthGroupForm(request.form)
    if request.method == 'POST':
        if form.validate():
            with db.auto_commit():
                res_add = mdb()
                res_add.set_attrs(form.data)
                db.session.add(res_add)
            return jsonify({'status': 200})
        else:
            return jsonify({'status': 400, 'msg': list(form.errors.values())[0]})
    else:
        return render_template('admin/auth_group/add.html')


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def auth_group_edit():
    if request.method == 'GET':
        id = request.args.get('id')
        find = mdb.by_id(id)
        return render_template('admin/auth_group/edit.html', find=find)

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        try:
            mdb.query.filter_by(id=id).update(data)
            db.session.commit()
        except Exception as e:
            return jsonify({'status': 400, 'message':e})
        return jsonify({'status': 200})


@api.route('/delete', methods=['POST'])
@role_required()
def auth_group_delete():
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
        return jsonify({'status': 400, 'message': e})
    return jsonify({'status': 200})


@api.route('/auth', methods=['POST', 'GET'])
@role_required()
def auth_group_auth():
    if request.method == 'GET':
        group_id = request.args.get('id')
        auth_list = mdb.get_auth_json(group_id)
        return render_template('admin/auth_group/auth.html', group_id=group_id, auth_list=auth_list)
    else:
        data = {}
        data['permissions'] = request.form.get('auth_permission_ids')
        id = request.form.get('id')
        try:
            mdb.query.filter_by(id=id).update(data)
            db.session.commit()
        except Exception as e:
            return jsonify({'status': 400, 'msg': e})
        return jsonify({'status': 200, 'msg': '设置权限成功'})

