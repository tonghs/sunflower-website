#!/usr/bin/env python
#coding: utf-8

import time

def time_fmt(timestamp): 
    return time.strftime('%Y-%m-%d %H:%M:%d', time.localtime(timestamp))

