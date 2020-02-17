#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 11:08
# @Author  : justin.郑 3907721@qq.com
# @File    : company.py
# @Desc    : 企业管理

from flask import render_template, request, jsonify
from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.models.company import Company
from app.models.base import db

api = Redprint('company')
mdb = globals()['Company']


@api.route('/index')
@role_required()
def company_index():
    all = mdb.all()
    count = mdb.count()
    return render_template('admin/company/index.html', list=all, count=count, menutitle='企业管理', navtitle='列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
def company_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        return render_template('admin/company/add.html')


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def company_edit():
    if request.method == 'GET':
        id = request.args.get('id')
        find = mdb.by_id(id)
        return render_template('admin/company/edit.html', find=find)

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        data['is_vip'] = int(data['is_vip'])
        data['inte_vip'] = int(data['inte_vip'])
        try:
            mdb.query.filter_by(id=id).update(data)
            db.session.commit()
        except Exception as e:
            return jsonify({'status': 400, 'message': e})
        return jsonify({'status': 200})


@api.route('/delete', methods=['POST'])
@role_required()
def company_delete():
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



