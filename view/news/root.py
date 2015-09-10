#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler
from _route import route

from model.news import News


@route('/news/(\d+)')
class index(BaseHandler):
    def get(self, news_id):
        news = News.news_get(news_id)
        if news:
            self.render(news=news)
        else:
            self.template = '404.html'
            self.render()
