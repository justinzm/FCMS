#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'justin.郑'


class Redprint():
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, blueprint, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(url_prefix + rule, endpoint, f, **options)


