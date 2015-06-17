#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from url import MainHandler

define('port', default=8888, help='run on this port', type=int)
define('debug', default=True, help='enable debug mode')

settings = dict(debug=options.debug)

application = tornado.web.Application([
    (r"/([a-zA-Z0-9-_]*)", MainHandler),
], **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
