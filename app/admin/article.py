#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : article.py
# @Desc    : 文章管理

from flask import render_template, request, jsonify
import time
from sqlalchemy import or_
from app.libs.redprint import Redprint
from app.libs.role import role_required, logger
from app.models.section import Section
from app.models.category import Category
from app.models.article import Article
from app.models.base import db

api = Redprint('article')
mdb = globals()['Article']
mdb_category = globals()['Category']
mdb_section = globals()['Section']


@api.route('/index', methods=['POST', 'GET'])
@role_required()
def article_index():
    if request.method == 'GET':
        return render_template('admin/article/index.html', menutitle='文章管理', navtitle='文章列表')
    else:
        offset = request.form.get('iDisplayStart')
        limit = request.form.get('iDisplayLength')
        search = request.form.get('sSearch')
        sEcho = request.form.get('sEcho')

        if search:
            alls = mdb.query.filter(Article.is_delete == 0) \
                .filter(or_(
                    mdb.title.like("%%%s%%" % search),
                    mdb.author.like("%%%s%%" % search))
                ) \
                .order_by(mdb.create_time.desc()) \
                .offset(offset).limit(limit) \
                .all()
            # 过滤后的记录
            recordsFiltered = mdb.query.filter(mdb.is_delete == 0) \
                .filter(or_(
                    mdb.title.like("%%%s%%" % search),
                    mdb.author.like("%%%s%%" % search))
                ) \
                .count()
        else:
            alls = mdb.query.filter(mdb.is_delete == 0) \
                .order_by(mdb.create_time.desc()) \
                .offset(offset).limit(limit) \
                .all()
            # 过滤后的记录
            recordsFiltered = mdb.count()

        # 未过滤记录数
        recordsTotal = mdb.count()
        res = []
        for find in alls:
            checkbox = '<input type="checkbox" name="did" value="%s">' % find.id
            istop = "未置顶" if find.istop == 0 else "置顶"
            status_checked = "checked" if find.status == 1 else ""
            status = '<input type="checkbox" class="js-switch" name="%s" %s />' % (find.id, status_checked)

            manage = '<span class="btn btn-info btn-xs" onclick="new_win(\'编辑文章\',\'edit?id=%s\',\'\',\'\')">编辑</span> <span class="btn btn-danger btn-xs" onclick="del(this, %s)">删除</span>' % (find.id, find.id)
            res.append([checkbox, find.id, find.title, find.section.title, find.category.title, find.author, istop,
                        find.sort, find.create_datetime, status, manage])
        res_data = {
            "draw": sEcho,
            "recordsTotal": recordsTotal,
            "recordsFiltered": recordsFiltered,
            "data": res
        }
        return jsonify(res_data)


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



