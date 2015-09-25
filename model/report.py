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


class Report(Doc):
    structure = dict(
        id_ = int,
        title = basestring,
        summary = basestring,
        img = int,
        time = int,
        url = basestring,
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
    def report_upsert(cls, doc):
        id_ = 0
        if not doc.id_:
            id_ = gid() 
            doc.__dict__.update(time=int(time.time()))
            doc.__dict__.update(is_del=DEL_FLAG.FALSE)
        else:
            id_ = doc.id_

        o = Report(doc)

        o.upsert(dict(id_=id_))

    @classmethod
    def report_get(cls, id_):
        o = None
        try:
            o = Report.find_one(dict(id_=int(id_), is_del=DEL_FLAG.FALSE))
        except:
            pass

        return o

    @classmethod
    def reports(cls, spec=dict(), offset=0, limit=0):
        if 'is_del' not in spec:
            spec.update(is_del=DEL_FLAG.FALSE)

        return Report.find(spec, sort=[('time', -1)], offset=offset, limit=limit)


if __name__ == "__main__":
    pass
