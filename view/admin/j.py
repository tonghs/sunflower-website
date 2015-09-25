#!/usr/bin/env python
#coding:utf-8

import json

from view._base import AdminJsonHandler, JsonHandler
from _route import route
from model.admin import Admin
from model.web_info import WebInfo
from model.news import News, DEL_FLAG
from model.report import Report, DEL_FLAG

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

        self.finish(o.__dict__)

@route('/j/admin/del_news')
class del_news(AdminJsonHandler):
    def post(self):
        o = self.json
        o.__dict__.update(is_del=DEL_FLAG.TRUE)
        News.news_upsert(o)

        self.finish()

@route('/j/admin/add_report')
class add_report(AdminJsonHandler):
    def post(self):
        o = self.json
        Report.report_upsert(o)

        self.finish(o.__dict__)

@route('/j/admin/del_report')
class del_report(AdminJsonHandler):
    def post(self):
        o = self.json
        o.__dict__.update(is_del=DEL_FLAG.TRUE)
        Report.report_upsert(o)

        self.finish()

