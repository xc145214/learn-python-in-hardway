#!/usr/bin/env python
# -*- coding: utf-8 -*-

m = 12
i = 0
numbers = []

while i < m:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "numbers now:", numbers
    print "At the bottom i is %d" % i

print "the numbers: "
for num in numbers:
    print num


# use function

def loop_one(m):
    numbers = []
    i = 0
    while i < m:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "numbers now:", numbers
        print "At the bottom i is %d" % i

    print numbers


def loop_two(m, n):
    numbers = []
    i = 0
    while i < m:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + n
        print "numbers now:", numbers
        print "At the bottom i is %d" % i

    print numbers


def loop_three(m, n):
    numbers = []
    for x in range(0, m, n):
        numbers.append(x)

    print numbers


loop_one(11)
loop_two(11, 2)
loop_three(11, 2)
