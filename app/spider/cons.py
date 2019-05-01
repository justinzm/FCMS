#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : cons.py
# @Desc    : 采集 常量数据

VERSION = '1.0.0'

CODES = ['sz000725', 'sz000651']
HK_CODES = ['02008', '02768']


# 新浪财经 股票 个股资讯
SINA_STOCK_NEWS = 'http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllNewsStock.php?symbol=%s&Page=%s'

# 新浪财经 港股 个股资讯
SINA_HK_STOCK_NEWS = 'http://stock.finance.sina.com.cn/hkstock/go/CompanyNews/page/%s/code/%s.html'