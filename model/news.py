#!/usr/bin/env python
#coding: utf-8

import _env
import time
import re
from db import Doc
from config import HOST
from gid_ import gid


class DEL_FLAG:
    TRUE = 1
    FALSE = 0


class News(Doc):
    structure = dict(
        id_ = int,
        title = basestring,
        summary = basestring,
        img = int,
        content = basestring,
        time = int,
        catagory = int,
        is_del = int,
    )

    indexes = [
        { 'fields': ['title'] },
        { 'fields': ['id_'] },
    ]

    default_values = {
        'is_del': DEL_FLAG.FALSE
    }

    @classmethod
    def news_upsert(cls, doc):
        id_ = 0
        if not doc.id_:
            id_ = gid() 
            doc.__dict__.update(time=int(time.time()))
            doc.__dict__.update(is_del=DEL_FLAG.FALSE)
        else:
            id_ = doc.id_

        o = News(doc)

        o.upsert(dict(id_=id_))

    @classmethod
    def news_get(cls, id_):
        o = None
        try:
            o = News.find_one(dict(id_=int(id_), is_del=DEL_FLAG.FALSE))
        except:
            pass

        return o

    @classmethod
    def news(cls, spec=dict(), offset=0, limit=0):
        if 'is_del' not in spec:
            spec.update(is_del=DEL_FLAG.FALSE)

        return News.find(spec, sort=[('time', -1)], offset=offset, limit=limit)

    @classmethod
    def latest_news(cls, catagory): 
        news_ = News.news(spec=dict(catagory=catagory, is_del=DEL_FLAG.FALSE), limit=1)
        news = None
        if news_:
            news = news_[0]

        return news


    @classmethod
    def _desc_get(cls, html):
        p = re.compile('<.*?>')
        txt = p.sub('', html)

        return '%s...' % txt[0: 160]


if __name__ == "__main__":
    pass
    for o in News.iterdoc():
        o.is_del = 0
        o.save()
