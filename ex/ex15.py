#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 读取文件

from sys import argv

script, filename = argv

txt = open(filename)

print "here's your file %r:" % filename

print txt.read()

print "Type the filename again:"
file_againe = raw_input('> ')

txt_again = open(filename)
print txt_again.read()
