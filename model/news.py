#!/usr/bin/env python
#coding: utf-8

import _env
import time
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

    def news_get(cls, id_):
        o = None
        try:
            o = News.find_one(dict(id_=int(id_)))
        except:
            pass

        return o

    def news(cls, spec=dict(), offset=0, limit=0):
        return News.find(spec, sort=[('time', -1)], offset=offset, limit=limit)


if __name__ == "__main__":
    pass

