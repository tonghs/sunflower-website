#!/usr/bin/env python
#coding: utf-8

DEBUG = True

PORT = 8080

APP = '向日葵传媒'

HOST = 'http://sunflower.tonghs.com'
STATIC_HOST = 'http://static.tonghs.com'

DB = 'sunflower'

MONGO_CONFIG = dict(
    host = "mongodb://127.0.0.1:27017",
)

REDIS_CONFIG = dict(
    host='127.0.0.1',
    port=6379,
    db=0
)
