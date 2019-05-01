#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : crawler.py
# @Desc    : 

import requests

# 因为不能访问, 所以我们加个头试试
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# urllib 的相关操作如下
url = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllNewsStock/symbol/sh601318.phtml'



r = requests.get(url, headers=headers)
r.encoding = 'gb2312'
print(r.text)

