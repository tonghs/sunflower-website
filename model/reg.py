#!/usr/bin/env python
#coding: utf-8

from db import Doc
from config import HOST

class Reg(Doc):
    structure = dict(
        name=basestring,
        startup_name=basestring,
        phone=basestring,
        email=basestring,
        desc=basestring 
    )

    indexes = [
        { 'fields': ['name'] },
        { 'fields': ['startup_name'] },
        { 'fields': ['phone'] },
        { 'fields': ['email'] }
    ]

    @classmethod
    def reg_new(cls, doc):
        o = Reg(doc)
        o.save()

if __name__ == "__main__":
    pass

