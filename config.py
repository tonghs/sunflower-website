#!/usr/bin/env python
#coding: utf-8

DEBUG = True

PORT = 8080

APP = '向日葵传媒'
SLOGAN = '不辜负每一个梦想'

HOST = 'http://c.cc:8080'
STATIC_HOST = 'http://static.c.cc:8080'

DB = 'sunflower'

MONGO_CONFIG = dict(
    host = "mongodb://127.0.0.1:27017",
)

REDIS_CONFIG = dict(
    host='127.0.0.1',
    port=6379,
    db=0
)
