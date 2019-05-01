#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py
# @Desc    : 

from flask import request, jsonify, abort, current_app
from wechatpy import WeChatClient

from app.libs.logger import CmsLogger
from app.models.wx_diymenu import WxDiymenu
from app.wechat import wechat

__author__ = 'justin.郑'


@wechat.route('/wechat/test/')
def test_index():
    # client = WeChatClient(current_app.config['APPID'], current_app.config['APPSECRET'])
    # res = client.message.send_text("or4ljt5dHfIfUtCEayf3UnUjm7ms", "okokokokkoo")
    #
    # return jsonify(res)

    # list = []
    #
    # menu1 = WxDiymenu.query.filter_by(pid=0).order_by(WxDiymenu.sort.desc()).all()
    #
    # for i in range(len(menu1)):
    #     tmp = {}
    #     tmp['name'] = menu1[i].name
    #     tmp['type'] = menu1[i].type
    #     if menu1[i].type == "view":
    #         tmp['url'] = menu1[i].url
    #     else:
    #         tmp['key'] = menu1[i].keyword
    #
    #     menu2 = WxDiymenu.query.filter_by(pid=menu1[i].id).order_by(WxDiymenu.sort.desc()).all()
    #     if menu2:
    #         tmp['sub_button'] = []
    #         for j in range(len(menu2)):
    #             tmp2 = {}
    #             tmp2['name'] = menu2[j].name
    #             tmp2['type'] = menu2[j].type
    #             if menu2[j].type == "view":
    #                 tmp2['url'] = menu2[j].url
    #             else:
    #                 tmp2['key'] = menu2[j].keyword
    #             tmp['sub_button'].append(tmp2)
    #     list.append(tmp)
    #
    # doc = {
    #     "button": list
    # }
    #
    # print(type(doc))
    # print(doc)
    # return jsonify(doc)
    pass

