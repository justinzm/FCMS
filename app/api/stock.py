#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024
# @Author  : justin.郑 3907721@qq.com
# @File    : stock.py
# @Desc    : 沪深股票数据API

from flask import request, jsonify
from app.crawler_data.stock import CrawlerStock
from app.validators.forms import StockForm
from app.api import api


@api.route('/api/v1/stock', methods=['GET'])
def v1_stock():
    """ 获取股票基本信息
    @@@
    #### 参数

    | 参数 | 是否必填 | 类型 | 备注 |
    |--------|--------|--------|--------|
    |    code    |    是    |    String   |    股票代码   |
    |    date    |    否    |    String   |    日期；默认今天   |

    #### 返回
    - ##### json
    {
        code: 0,
        msg: "succee",
        data: {
            amount: 2872304.2,
            change: 0.07,
            close: 14.99,
            high: 15.2,
            low: 14.77,
            open: 14.92,
            pct_chg: 0.4692,
            pre_close: 14.92,
            trade_date: "20190820",
            ts_code: "000001.SZ",
            vol: 1921041.5
        }
    }

    #### 备注

    > http://127.0.0.1:5000/api/v1/stock?code=000001.SZ&date=20190820
    @@@
    """

    if request.method == 'GET':
        form = StockForm().validate_for_api()
        res = CrawlerStock().get_stock(ts_code=form.data['code'], trade_date=form.data['date'])
        return jsonify({"msg": res[0], "data": res[1], "code": 0})


        # tmp = request.args.to_dict()
        # code = request.args.get('code')
        # date = request.args.get('date')
        # res = CrawlerStock().get_stock(ts_code=code, trade_date=date)

        # return jsonify({"msg": res[0], "data": res[1], "code": 0})

