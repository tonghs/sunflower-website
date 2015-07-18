#!/usr/bin/env python
#coding: utf-8

import _env
from db import Doc
import time
import json
import hashlib
from gid_ import gid

class User(Doc):
    structure = dict(
        user_id = int,
        user_name=basestring,
        password=basestring,
        time=int
    )

    indexes = [
        { 'fields': ['user_id'] },
        { 'fields': ['user_name'] },
        { 'fields': ['user_name', 'password'] },
    ]

    @classmethod
    def user_new(cls, user_name, password):
        m = hashlib.md5()   
        m.update(password)   
        password = m.hexdigest()  

        o = User(dict(user_id=gid(), user_name=user_name, password=password, time=int(time.time())))
        o.save()

    @classmethod
    def user_login(cls, user_name, password):
        m = hashlib.md5()   
        m.update(password)   
        password = m.hexdigest()  
         
        o = User.find_one(dict(user_name=user_name, password=password))
        return o

    @classmethod
    def from_json(cls, json_):
        d = json.loads(json_)
        o = User.find_one(dict(user_id=d.get('user_id'), user_name=d.get('user_name'), password=d.get('password')))

        return o

if __name__ == "__main__":
    Userr.user_new('tonghs', 'tonghs')
    pass

