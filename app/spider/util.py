#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : util.py
# @Desc    :
import re


def replace_tag(m):
    """
    #过滤掉页面中除了<p></p>和<img>以外所有的标签
    """
    p = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)   #style
    m = p.sub('', m)
    p = re.compile(r'\b(?!(?:href|src))\w+=(["\']).+?\1', re.I)
    m = p.sub('', m)
    m = m.replace('\n', '')
    m = m.replace('\t', '')
    m = m.replace('\u3000', '')
    all = re.findall(r'</?.*?>', m)
    save = re.findall(r'</?(?:img).*?>|</?[pP]*?>', m)

    for e in all:
        if e not in save:
            m1 = m.replace(e, '')
            m = m1
    return m

