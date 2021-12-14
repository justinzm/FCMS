#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : auth_permission.py
# @Desc    : 分类管理

from flask import render_template, request, jsonify
from sqlalchemy import desc
from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.models.section import Section
from app.models.category import Category
from app.models.base import db

api = Redprint('category')
mdb = globals()['Category']
mdb_section = globals()['Section']


@api.route('/index')
@role_required()
def category_index():
    all = mdb.all()
    count = mdb.count()
    return render_template('admin/category/index.html', list=all, count=count, menutitle='分类管理', navtitle='分类列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
def category_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        section_list = mdb_section.query.filter_by(status=1).all()
        return render_template('admin/category/add.html', section_list=section_list)


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def category_edit():
    if request.method == 'GET':
        id = request.args.get('id')
        find = mdb.by_id(id)

        section_list = mdb_section.query.filter_by(status=1).all()
        return render_template('admin/category/edit.html', find=find, section_list=section_list)

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
def category_delete():
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


@api.route('/get_category_list')
def get_category_list():
    section_id = request.args.get('section_id')
    try:
        lists = mdb.query.filter_by(section_id=section_id).order_by(desc('sort')).all()
        result = []
        for list in lists:
            result.append(list.to_json())
    except Exception as e:
        return jsonify({'status': 400, 'msg': e})
    return jsonify({"status": 200, "list": result})


