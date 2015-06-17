#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from view.root import index 

define('port', default=8080, help='run on this port', type=int)
define('debug', default=True, help='enable debug mode')

settings = dict(
    debug=options.debug,
    template_path="html"
)

application = tornado.web.Application([
    (r"/", index),
], **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
