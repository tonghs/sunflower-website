#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler
from _route import route

@route('/news/1')
class _1(BaseHandler):
    def get(self):
        self.render()

@route('/news/2')
class _2(BaseHandler):
    def get(self):
        self.render()

@route('/news/.*')
class index(BaseHandler):
    def get(self):
        self.render()

