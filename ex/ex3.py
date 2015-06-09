#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 -7?"

print 3 + 2 < 5 - 7

print "what is 3 + 2?", 3 + 2
print "what is 5 - 7?", 5 - 7

print "Oh,that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2


# 输出浮点数
print "%.2f" % (100 - 25 * 3 % 4)

# 格式化输出
print "his name is %s" % ("Aviad")

# 打印浮点数
print "he is %f m" % (1.83)

# 保留小数点
print "he is %.2f m" % (1.83)

# 指定占位符宽度
print "Name:%10s Age:%8d Height:%8.2f" % ("Aviad", 25, 1.83)

# 左对齐
print "Name:%-10s Age:%-8d Height:%-8.2f" % ("Aviad", 25, 1.83)

# 指定占位符
print "Name:%-10s Age:%08d Height:%08.2f" % ("Aviad", 25, 1.83)

#科学计数
print format(0.00015,'.2e')