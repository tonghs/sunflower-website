#!/usr/bin/env python
#coding:utf-8

import tornado
from model import ShortUrl

class MainHandler(tornado.web.RequestHandler):
    def get(self, s):
        msg = '<div style="margin:auto; width: 400px; text-align: center; margin-top: 150px;"><p>hello world!</p><p>没有此短域名</p><div>'
        self.finish(msg)
