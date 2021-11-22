#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from DefMethod import my_abs
from DefMethod import m1
from DefMethod import returnMutiValue

print(str(1))
print(bool(1))
print(int(1.2))

a = abs  # 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
print(a(-1))

print(my_abs(2000))
print(m1(2000))

print(isinstance(1, (str, float)))  # 判断1是否是类型str或者float

print(returnMutiValue(1, 3))
