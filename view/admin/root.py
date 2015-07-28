#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler, AdminHandler
from _route import route

from model.web_info import WebInfo

@route('/admin')
class admin(BaseHandler):
    def get(self):
        self.render()


@route('/admin/index')
class index(AdminHandler):
    def get(self):
        self.render()


@route('/admin/settings')
class settings(AdminHandler):
    def get(self):
        o = WebInfo.web_info_get()
        self.render(o=dict(o))

@route('/admin/partner')
class partner(AdminHandler):
    def get(self):
        self.render()


@route('/admin/startups')
class startups(AdminHandler):
    def get(self):
        self.render()

@route('/admin/news')
class news(AdminHandler):
    def get(self):
        self.render()

@route('/admin/add_news')
class add_news(AdminHandler):
    def get(self):
        self.render()


@route('/admin/logout')
class logout(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/admin")
