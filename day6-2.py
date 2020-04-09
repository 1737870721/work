#!/usr/bin/env python
#-*- coding:utf8 -*-
#@Time    :
#@Authon  :
#@File    :

def pri(str,w,c=1):
    print(str)
    print(w)
    print(c)

pri("55",550)
pri("66",66,66)

def lis(mun):
    num[0] = 20

num = [10]
lis(num)
print(num)

def funcSum(*num):
    sum = 0
    for i in num:
        sum +=i
    return sum

print(funcSum(1,2,3,5,6))