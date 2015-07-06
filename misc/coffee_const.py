#!/usr/bin/env python
#coding: utf-8


from mako.template import Template
from mako.lookup import TemplateLookup
import sys
import _env

print sys.path

mylookup = TemplateLookup(directories=['coffee'], output_encoding='utf-8')

mytemplate = mylookup.get_template("const.coffee.mako")
print(mytemplate.render())


