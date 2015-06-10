#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 导入包
from sys import argv
from os.path import exists

# 脚本参数
script, from_file, to_file = argv

# 复制文件路径
print "Copying from %s to %s" % (from_file, to_file)

# from文件的内容
input = open(from_file)
indata = input.read()

# 输出字符数
print "The input file is %d bytes long" % len(indata)

# 判断to_file是否存在
print "Does the output file exists? %r" % exists(to_file)
print "Ready ,hit RETURN to continue,CTRL-C to abort."
raw_input()

#写入文件内容
output = open(to_file, 'w')
output.write(indata)

print 'Alright,all done.'

# 关闭文件流
output.close()
input.close()


# 执行脚本python ex17.py test.txt copied.txt
