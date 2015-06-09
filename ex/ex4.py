#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 车的数量
cars = 100

# 车内空间
space_in_a_car = 4.0

# 司机数
drivers = 30

# 乘客数
passengers = 90

# 未运行的车辆数
cars_not_driven = cars - drivers

# 运行的车辆数
cars_drivern = drivers

# 车辆的可乘坐人数
carpool_capacity = cars_drivern * space_in_a_car

# 每车乘客数
average_passengers_per_car = passengers / cars_drivern

print "there are",cars,"cars available"

print "there are only ",drivers,"drivers available"

print "there will be",cars_not_driven,"empty cars today"

print "We can transport",carpool_capacity,"people today"

print "We have" ,passengers,"to carpool today"

print "We need to put about",average_passengers_per_car,"in each car."




