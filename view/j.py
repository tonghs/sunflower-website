#!/usr/bin/env python
#coding:utf-8

from view._base import JsonHandler
from _route import route
from model.user import User
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
        key = gid()
        self.finish(qiniu_token(key))


@route('/j/login')
class _(JsonHandler):
    def post(self):
        o = self.json
        user = User.user_login(o.user_name, o.password)
        if user:
            self.set_secure_cookie("user", json.dumps(dict(user)))
        else:
            self.err.msg = '登录错误'

        self.finish(dict(err=self.err.__dict__))


