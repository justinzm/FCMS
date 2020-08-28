#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, request, jsonify
import time
from app.libs.redprint import Redprint
from app.libs.role import role_required, logger
from app.models.section import Section
from app.models.category import Category
from app.models.article import Article
from app.models.base import db

__author__ = 'justin.郑'

api = Redprint('article')
mdb = globals()['Article']
mdb_category = globals()['Category']
mdb_section = globals()['Section']


@api.route('/index')
@role_required()
def article_index():
    all = mdb.all()
    count = mdb.count()
    return render_template('admin/article/index.html', list=all, count=count, menutitle='文章管理', navtitle='列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
@logger('添加文章')
def article_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        section_list = mdb_section.query.filter_by(status=1).all()
        return render_template('admin/article/add.html', section_list=section_list, today=time.strftime("%Y-%m-%d"))


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def article_edit():
    if request.method == 'GET':
        id = request.args.get('id')
        find = mdb.by_id(id)
        section_list = mdb_section.query.filter_by(status=1).all()
        category_list = mdb_category.query.filter_by(status=1).all()
        return render_template('admin/article/edit.html', find=find, section_list=section_list, category_list=category_list)

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        try:
            mdb.query.filter_by(id=id).update(data)
            db.session.commit()
        except Exception as e:
            return jsonify({'status': 400, 'message': e})
        return jsonify({'status': 200})


@api.route('/delete', methods=['POST'])
@role_required()
@logger('删除文章')
def article_delete():
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



