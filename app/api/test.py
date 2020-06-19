#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 0019
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py
# @Desc    : 接口测试文件

from flask import request, jsonify

from . import api


@api.route('/api/test', methods=['GET'])
def api_test():
    """ 文章列表
    @@@
    #### 参数

    | 参数 | 是否必填 | 类型 | 备注 |
    |--------|--------|--------|--------|
    |    member_id    |    是    |    Int   |    账户ID   |
    |    news_type    |    是    |    String   |    文章类型   |

    news_type : 推荐 recommend_news；收藏 my_collect；评论 my_comment；点赞 my_like；阅读 my_read；推送 my_push

    #### 返回
    - ##### json
    > {code:0,count:141,current_count:3,data:[{author_name:"新华网客户端",id:17364,keyword_label:["民生","时政"],member_id:5,news_type:"my_read",publish_time:"2019-08-21 10:10:42",sentiment:"积极",title:"北京：小小“菜篮子”见证民生“大工程”",topic:"时事",url:"http://toutiao.com/group/6727560503368876548/"}],msg:"ok",page_index:1}

    #### 备注

    > http://127.0.0.1:5000/api/article_list_toutiao?member_id=5&startdate=2019-08-20&enddate=2019-08-21&page_index=1&page_size=3&news_type=my_read
    @@@
    """

    if request.method == 'GET':
        return jsonify({"msg": "ok", "data": "", "count": 0, "code": 0})
 

