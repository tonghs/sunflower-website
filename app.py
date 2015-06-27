#!/usr/bin/env python
#coding:utf-8

import tornado
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from config import PORT, DEBUG
import _url
from model.db import mongo

from _route import route

settings = dict(
    debug=DEBUG,
    template_path="html"
)

def write_error(self, status_code, **kwargs):
    if status_code == 404:
        self.render('404.html')
    elif status_code == 500:
        self.template = '500.html'
        self.render()
    else:
        self.write('error:' + str(status_code))

tornado.web.RequestHandler.write_error = write_error

application = tornado.web.Application(route.url_list, **settings)

for k,v in mongo._registered_documents.iteritems():
    print "indexing", k
    v.generate_index(v._collection)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
