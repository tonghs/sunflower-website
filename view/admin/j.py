#!/usr/bin/env python
#coding:utf-8

import json

from view._base import JsonHandler
from _route import route
from model.admin import Admin

@route('/j/admin/login')
class login(JsonHandler):
    def post(self):
        msg = ''
        success = False
        o = self.json
        admin = Admin.admin_login(o.user_name, o.password)
        if admin:
            self.set_secure_cookie("user", json.dumps(dict(admin)))
            msg = ''
            success = True 
        else:
            msg = "登录错误"

        self.finish(dict(success=success, msg=msg))

