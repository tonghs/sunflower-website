#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler, AdminHandler
from _route import route

from model.web_info import WebInfo
from model.news import News
from model.report import Report 

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


@route('/admin/add_news')
@route('/admin/add_news/(\d+)?')
class add_news(AdminHandler):
    def get(self, news_id=None):
        news = None
        if news_id:
            news = News.news_get(news_id)

        if not news:
            news = {
                'title' : '',
                'summary' : '',
                'img' : 0,
                'content' : '',
                'catagory': 1
            }
        self.render(news=news)


@route('/admin/news/(\d+)?')
@route('/admin/news')
class news(AdminHandler):
    def get(self, catagory=0):
        spec = dict()
        if catagory:
            spec.update(catagory=int(catagory))

        news_list = News.news(spec=spec)

        self.render(news_list=news_list)


@route('/admin/add_report')
@route('/admin/edit_report/(\d+)?')
class add_report(AdminHandler):
    def get(self, report_id=None):
        report = None
        if report_id:
            report = Report.report_get(report_id)

        if not report:
            report = {
                'title' : '',
                'summary' : '',
                'url': '',
                'img' : 0,
            }
        self.render(report=report)


@route('/admin/reports')
class reports(AdminHandler):
    def get(self):
        report_list = Report.reports()

        self.render(report_list=report_list)


@route('/admin/logout')
class logout(BaseHandler):
    def get(self):
        self.clear_cookie("admin")
        self.redirect("/admin")
