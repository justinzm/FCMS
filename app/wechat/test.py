#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py
# @Desc    :
import os

from flask import request, jsonify, abort, current_app
from wechatpy import WeChatClient, WeChatPay
from app.libs.logger import logger
from app.models.wx_diymenu import WxDiymenu
from app.wechat import wechat


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


# 微信 现金红包
@wechat.route('/wechat/redpack')
def redpack_index():
    try:
        appid = 'wx2a109de15e40c66b'
        api_key = 'O93034XrenxxKpPZmMAq8Aox2K77HuV3'
        mch_id = '1604159836'
        mch_cert = os.path.join(current_app.static_folder, 'apiclient_cert.pem')
        mch_key = os.path.join(current_app.static_folder, 'apiclient_key.pem')

        wechatObj = WeChatPay(appid=appid, api_key=api_key, mch_id=mch_id, mch_cert=mch_cert, mch_key=mch_key)

        res = wechatObj.redpack.send(
            user_id='oXd4h6etiWALpsIlrnWFM8OwqK5k',
            total_amount='101',
            send_name='极橙社',
            act_name='红包',
            wishing='红包祝福语',
            remark='备注')
        print(res)
        return jsonify({"msg": str(res), "error_code": 200})
    except Exception as e:
        return jsonify({"msg": str(e), "error_code": 400})