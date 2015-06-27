#!/usr/bin/env python
#coding:utf-8

from view._base import JsonHandler
from _route import route

@route('/j/reg')
class reg(JsonHandler):
    def post(self):
        print self.json
        self.finish()
