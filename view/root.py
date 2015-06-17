#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler

class index(BaseHandler):
    def get(self):
        self.render()
