#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, request, jsonify
from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.models.wx_reply import WxReply

__author__ = 'justin.郑'

api = Redprint('wx_reply')
mdb = globals()['WxReply']


@api.route('/index', methods=['POST', 'GET'])
@role_required()
def reply_index():
    if request.method == 'GET':
        find = mdb.query.filter_by(id=1).first()
        return render_template('admin/wx_reply/index.html', find=find, menutitle='微信公众号', navtitle='关注回复')

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        # id = request.form.get('id')
        try:
            mdb.query.filter_by(id=1).update(data)
            return jsonify({'status': 200})
        except Exception as e:
            return jsonify({'status': 400, 'message': e})




