#!/usr/bin/env python
#coding: utf-8

import time

def time_fmt(timestamp, fmt='%Y-%m-%d %H:%M:%d'): 
    return time.strftime(fmt, time.localtime(timestamp))

