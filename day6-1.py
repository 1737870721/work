#!/usr/bin/env python
#-*- coding:utf8 -*-
#@Time    :
#@Authon  :
#@File    :

timestr = input()

print(type(timestr))
timelist = timestr.split(":")

h = int(timelist[0])
m = int(timelist[1])
s = int(timelist[2])

print(h,m,s)