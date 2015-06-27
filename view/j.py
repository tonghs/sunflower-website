#!/usr/bin/env python
#coding:utf-8

from view._base import JsonHandler
from _route import route
from model.reg import Reg

@route('/j/reg')
class reg(JsonHandler):
    def post(self):
        o = self.json
        # Reg.reg_new(o)

        self.finish()
