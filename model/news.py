#!/usr/bin/env python
#coding: utf-8

import _env
import time
import re
from db import Doc
from config import HOST
from gid_ import gid

class News(Doc):
    structure = dict(
        id_ = int,
        title = basestring,
        summary = basestring,
        img = int,
        content = basestring,
        time = int,
        catagory = int
    )

    indexes = [
        { 'fields': ['title'] },
        { 'fields': ['id_'] },
    ]

    @classmethod
    def news_upsert(cls, doc):
        id_ = 0
        if not doc.id_:
            id_ = gid() 
            doc.__dict__.update(time=int(time.time()))
        else:
            id_ = doc.id_

        o = News(doc)

        o.upsert(dict(id_=id_))

    @classmethod
    def news_get(cls, id_):
        o = None
        try:
            o = News.find_one(dict(id_=int(id_)))
        except:
            pass

        return o

    @classmethod
    def news(cls, spec=dict(), offset=0, limit=0):
        return News.find(spec, sort=[('time', -1)], offset=offset, limit=limit)


    @classmethod
    def _desc_get(cls, html):
        p = re.compile('<.*?>')
        txt = p.sub('', html)

        return '%s...' % txt[0: 160]


if __name__ == "__main__":
    pass
