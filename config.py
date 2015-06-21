#!/usr/bin/env python
#coding: utf-8

DEBUG = True

PORT = 8080

APP = '向日葵传媒'

HOST = 'http://c.cc:8080'
STATIC_HOST = 'http://static.c.cc:8080'

DB = 'SUNFLOWER'

MONGO_CONFIG = dict(
    host = "mongodb://root:fxZc0EoW7K9G@10.9.9.100:27017",
)

REDIS_CONFIG = dict(
    host='127.0.0.1',
    port=6379,
    db=0
)
