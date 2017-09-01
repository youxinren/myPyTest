#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = "d"
print(d)
print(1 - 2)

print("hello", "world")

#name = input()  # 接受控制台输入
#print("hello", name)

str='''test
    test
'''
print(str)


#大小写敏感,惯例使用全大写标识常量
Name="up"
name="low"
print(Name,name)

#python对整数没有大小限制


#python 中变量引用和java中有很大区别,python每次都会对新的变量值申请新的内存空间
a=1
b=a
a=a+2
print(a,b)#结果为 3 1


"中文".encode("utf-8")
print(len("中文"))



