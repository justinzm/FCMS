#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from flask import request, jsonify, abort
from app.libs.logger import CmsLogger
from app.models.wx_imgtext import WxImgtext
from app.models.wx_reply import WxReply
from app.models.wx_text import WxText
from app.wechat import wechat

__author__ = 'justin.郑'


from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)


# set token or get from environments
TOKEN = os.getenv('WECHAT_TOKEN', 'stock2019')
AES_KEY = os.getenv('WECHAT_AES_KEY', '')
APPID = os.getenv('WECHAT_APPID', 'wxda91c5eb944fe49a')


@wechat.route('/wechat/index/')
def index():
    content = _subscribe()
    return content


@wechat.route('/wechat/api/', methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')

    reply = False

    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)

    if request.method == 'GET':
        echo_str = request.args.get('echostr', '')
        return echo_str

    if encrypt_type == 'raw':
        # plaintext mode
        msg = parse_message(request.data)

        if msg.type == 'text':
            reply, tmp = _reply_text(msg.content, msg)          # 文本回复
            if not tmp:
                reply, tmp = _reply_img_text(msg.content, msg)  # 文本图文

        elif msg.type == 'image':
            reply = create_reply('暂时不支持图片回复', msg)
        elif msg.type == 'voice':
            reply = create_reply('暂时不支持语音回复', msg)
        elif msg.type == 'event':
            if msg.event == 'unsubscribe':
                reply = create_reply('用户取消关注事件', msg)
            elif msg.event == 'subscribe':
                # 用户关注事件
                content = _subscribe()
                reply = create_reply(content, msg)
            elif msg.event == 'click':
                reply, tmp = _reply_text(msg.key, msg)          # 文本回复
                if not tmp:
                    reply, tmp = _reply_img_text(msg.key, msg)  # 文本图文
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)

        if reply:
            return reply.render()
        return None
    return None


def _subscribe():
    """
    用户关注事件
    :return: 关注回复信息
    """
    find = WxReply.query.filter_by(id=1).first()
    return find.content


def _reply_text(keyword, msg):
    """
    文本回复事件
    :return: 回复文本
    """
    find = WxText.query.filter_by(type=1).filter_by(keyword=keyword).first()
    if not find:
        find = WxText.query.filter_by(type=2).filter(WxText.keyword.like('%'+keyword+'%')).first()
    if find:
        reply = create_reply(find.content, message=msg)
        tmp = True
    else:
        reply = create_reply(None)
        tmp = False
    return reply, tmp


def _reply_img_text(keyword, msg):
    """
    图文回复事件
    :param keyword:
    :return:
    """
    find = WxImgtext.query.filter_by(type=1).filter_by(keyword=keyword).first()
    if not find:
        find = WxImgtext.query.filter_by(type=2).filter(WxText.keyword.like('%' + keyword + '%')).first()

    if find:
        articles = [
            {
                'title': find.title,
                'description': find.intro,
                'image': find.url_img,
                'url': find.url
            }
        ]
        reply = create_reply(articles, message=msg)
        tmp = True
    else:
        reply = create_reply(None)
        tmp = False
    return reply, tmp


