#!/usr/bin/env python
#coding: utf-8

import _env
from db import Doc
import time
import json
import hashlib

class Admin(Doc):
    structure = dict(
        user_name=basestring,
        password=basestring,
        time=int
    )

    indexes = [
        { 'fields': ['user_name'] },
        { 'fields': ['user_name', 'password'] },
    ]

    @classmethod
    def admin_new(cls, user_name, password):
        m = hashlib.md5()   
        m.update(password)   
        password = m.hexdigest()  

        o = Admin(dict(user_name=user_name, password=password, time=int(time.time())))
        o.save()

    @classmethod
    def admin_login(cls, user_name, password):
        m = hashlib.md5()   
        m.update(password)   
        password = m.hexdigest()  
         
        o = Admin.find_one(dict(user_name=user_name, password=password))
        return o

    @classmethod
    def from_json(cls, json_):
        d = json.loads(json_)
        o = Admin.find_one(dict(user_name=d.get('user_name'), password=d.get('password')))

        return o

if __name__ == "__main__":
    Admin.admin_new('tonghs', 'tonghs')
    pass

