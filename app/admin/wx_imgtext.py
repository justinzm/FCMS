#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, request, jsonify

from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.models.wx_imgtext import WxImgtext
from app.models.base import db

__author__ = 'justin.郑'

api = Redprint('wx_imgtext')
mdb = globals()['WxImgtext']


@api.route('/index')
@role_required()
def wx_imgtext_index():
    all = mdb.all()
    count = mdb.count()
    return render_template('admin/wx_imgtext/index.html', list=all, count=count, menutitle='微信图文回复管理', navtitle='列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
def wx_imgtext_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        return render_template('admin/wx_imgtext/add.html')


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def wx_imgtext_edit():
    if request.method == 'GET':
        id = request.args.get('id')
        find = mdb.by_id(id)
        return render_template('admin/wx_imgtext/edit.html', find=find)

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        try:
            mdb.query.filter_by(id=id).update(data)
        except Exception as e:
            return jsonify({'status': 400, 'message': e})
        return jsonify({'status': 200})


@api.route('/delete', methods=['POST'])
@role_required()
def wx_imgtext_delete():
    id = request.form.get('id')
    id_list = id.split(",")
    try:
        if len(id_list) > 1:
            for i in id_list:
                mdb.query.filter_by(id=i).delete()
        else:
            mdb.query.filter_by(id=id).delete()
    except Exception as e:
        return jsonify({'status': 400, 'message': e})
    return jsonify({'status': 200})



