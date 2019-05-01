#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 0026
# @Author  : justin.郑 3907721@qq.com
# @File    : crawler_new.py
# @Desc    :
import html

import requests
import re
from app.spider.cons import CODES, HK_CODES, SINA_STOCK_NEWS
from app.spider.util import replace_tag
from lxml import etree


class SinaNew:
    def __init__(self):
        self.codes = CODES
        self.hk_codes = HK_CODES
        self.news_url = SINA_STOCK_NEWS
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    def news_crawler(self, date=None):
        page = 1
        for code in self.codes:
            url = self.news_url % (code, page)
            print(url)
            r = requests.get(url, headers=self.headers)
            r.encoding = 'gb2312'
            html = etree.HTML(r.text)
            news_href = html.xpath('//div[@class=\"datelist\"]/ul/a/@href')
            news_list = html.xpath('//div[@class=\"datelist\"]/ul/a/text()')
            data = []
            for i in range(len(news_list)):
                ds = {}
                ds['title'] = news_list[i]
                ds['url'] = news_href[i]
                ds['date'] = self._get_date(news_href[i])
                ds['source'] = self._get_content(news_href[i])[0]
                ds['content'] = self._get_content(news_href[i])[1]
                if ds['content'] != '':
                    data.append(ds)

            print(data)

    def _get_content(self, url):
        try:
            r = requests.get(url, headers=self.headers)
            r.encoding = 'utf-8'
            htmls = etree.HTML(r.text)
            source = htmls.xpath('//*[@class="date-source"]/a/text()')[0]

            content = htmls.xpath('//*[@class="article"]')[0]
            content = etree.tostring(content).decode('utf-8')
            content = html.unescape(content)
            content = replace_tag(content)
            return source, content.strip()
        except:
            return '', ''


    def _get_date(self, str):
        try:
            dl = re.findall(r"\d{4}-\d{1,2}-\d{1,2}", str)
            return dl[0]
        except Exception:
            return ''




if __name__ == '__main__':
    SinaNew().news_crawler()
