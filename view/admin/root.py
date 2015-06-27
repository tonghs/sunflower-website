#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler, AdminHandler
from _route import route

@route('/admin')
class admin(BaseHandler):
    def get(self):
        self.render()

@route('/admin/index')
class index(AdminHandler):
    def get(self):
        self.render()

@route('/admin/logout')
class logout(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/admin")
