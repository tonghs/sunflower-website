#!/usr/bin/env python
#coding:utf-8

from view._base import JsonHandler
from _route import route
# from model.reg import Reg
from model.qiniu_ import qiniu_token
from model.gid_ import gid

# @route('/j/reg')
# class reg(JsonHandler):
#     def post(self):
#         o = self.json
#         # Reg.reg_new(o)
# 
#.finish()

@route('/j/upload_token')
class upload_token(JsonHandler):
    def get(self):
        # TODO generate key
        key = gid()
        self.finish(qiniu_token(key))
