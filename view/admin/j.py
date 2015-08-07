#!/usr/bin/env python
#coding:utf-8

import json

from view._base import AdminJsonHandler, JsonHandler
from _route import route
from model.admin import Admin
from model.web_info import WebInfo
from model.news import News 

@route('/j/admin/login')
class _(JsonHandler):
    def post(self):
        msg = ''
        success = False
        o = self.json
        admin = Admin.admin_login(o.user_name, o.password)
        if admin:
            self.set_secure_cookie("admin", json.dumps(dict(admin)))
            msg = ''
            success = True 
        else:
            msg = "登录错误"

        self.finish(dict(success=success, msg=msg))


@route('/j/admin/settings')
class _(AdminJsonHandler):
    def post(self):
        o = self.json
        WebInfo.web_info_upsert(o)

        self.finish()


@route('/j/admin/add_news')
class add_news(AdminJsonHandler):
    def post(self):
        o = self.json
        News.news_upsert(o)

        self.finish()
