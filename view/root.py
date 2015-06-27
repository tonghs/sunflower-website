#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler
from _route import route

@route('/')
class index(BaseHandler):
    def get(self):
        self.render()

@route('/reg')
class reg(BaseHandler):
    def get(self):
        self.render()

@route('/reg_success')
class reg_success(BaseHandler):
    def get(self):
        self.render()

@route('/about')
class about(BaseHandler):
    def get(self):
        self.render()

@route('/contact')
class contact(BaseHandler):
    def get(self):
        self.render()
