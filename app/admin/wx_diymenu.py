#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, request, jsonify, current_app
from wechatpy import WeChatClient

from app.libs.logger import CmsLogger
from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.libs.tools import ArrayLevel
from app.models.wx_diymenu import WxDiymenu
from app.models.base import db

__author__ = 'justin.郑'

api = Redprint('wx_diymenu')
mdb = globals()['WxDiymenu']


@api.route('/index')
@role_required()
def wx_diymenu_index():
    arraylevel = ArrayLevel()
    arraylevel.array2level(mdb.all())
    all = arraylevel.get_list()

    count = mdb.count()
    return render_template('admin/wx_diymenu/index.html', list=all, count=count, menutitle='微信自定义菜单', navtitle='列表')


@api.route('/add', methods=['POST', 'GET'])
@role_required()
def wx_diymenu_add():
    if request.method == 'POST':
        with db.auto_commit():
            res_add = mdb()
            res_add.set_attrs(request.form)
            db.session.add(res_add)
        return jsonify({'status': 200})
    else:
        diymenu_list = mdb.query.filter_by(pid=0).all()

        return render_template('admin/wx_diymenu/add.html', diymenu_list=diymenu_list)


@api.route('/edit', methods=['POST', 'GET'])
@role_required()
def wx_diymenu_edit():
    if request.method == 'GET':
        id = request.args.get('id')
        find = mdb.by_id(id)
        diymenu_list = mdb.query.filter_by(pid=0).order_by(mdb.sort.desc()).all()

        return render_template('admin/wx_diymenu/edit.html', find=find, diymenu_list=diymenu_list)

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
def wx_diymenu_delete():
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


@api.route('/add_menu', methods=['POST', 'GET'])
# @role_required()
def wx_add_menu():
    client = WeChatClient(current_app.config['APPID'], current_app.config['APPSECRET'])

    list = []

    menu1 = WxDiymenu.query.filter_by(pid=0).order_by(WxDiymenu.sort.desc()).all()

    for i in range(len(menu1)):
        tmp = {}
        tmp['name'] = menu1[i].name
        tmp['type'] = menu1[i].type
        if menu1[i].type == "view":
            tmp['url'] = menu1[i].url
        else:
            tmp['key'] = menu1[i].keyword

        menu2 = WxDiymenu.query.filter_by(pid=menu1[i].id).order_by(WxDiymenu.sort.desc()).all()
        if menu2:
            tmp['sub_button'] = []
            for j in range(len(menu2)):
                tmp2 = {}
                tmp2['name'] = menu2[j].name
                tmp2['type'] = menu2[j].type
                if menu2[j].type == "view":
                    tmp2['url'] = menu2[j].url
                else:
                    tmp2['key'] = menu2[j].keyword
                tmp['sub_button'].append(tmp2)
        list.append(tmp)

    doc = {
        "button": list
    }

    res = client.menu.update(doc)
    CmsLogger('info').info('菜市场上厕所3 %s' % doc)
    CmsLogger('info').info('菜市场上厕所3 %s' % res)
    # return jsonify({'errcode': res['errcode'], 'errmsg': res['errmsg'], 'status': 200})
    return '123'

