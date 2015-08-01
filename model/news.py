#!/usr/bin/env python
#coding: utf-8

import _env
from db import Doc
from config import HOST
from gid_ import gid

class News(Doc):
    structure = dict(
        id_ = int,
        title = basestring,
        summary = basestring,
        img = int,
        content = basestring 
    )

    indexes = [
        { 'fields': ['title'] },
        { 'fields': ['id_'] },
    ]

    @classmethod
    def news_upsert(cls, doc):
        o = News(doc)
        id_ = 0
        if not doc.id_:
            id_ = gid() 
        else:
            id_ = doc.id_

            
        o.upsert(dict(id_=id_))

    def news_get(cls, id_):
        o = None
        try:
            o = News.find_one(dict(id_=int(id_)))
        except:
            pass

        return o


if __name__ == "__main__":
    pass

