#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from config import PORT, DEBUG
import _url

from _route import route

settings = dict(
    debug=DEBUG,
    template_path="html"
)

application = tornado.web.Application(route.url_list, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
