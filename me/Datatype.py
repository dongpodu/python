#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 数据类型 Numbers、String、List、Tuple（元组）、Dictionary

# Number
print('----------Number------------')
var1 = 1  # int
var3 = 1.0  # float
var4 = 1 + 2j  # 复数
var5 = complex(1, 2)  # 复数
var6 = 100_1000  # 1001000
var7 = 1.2e9  # 科学计数法，e代表10，1.2*10^9
print("var1:" + str(var1))
print("var3:" + str(var3))
print("var4:" + str(var4))
print("var6:" + str(var6))
print("var7:" + str(var7))
print("10/3=" + str(10 / 3))  # 有小数
print("10//3=" + str(10 // 3))  # 取整数，类似java的/
print("10%3=" + str(10 % 3))  # 取余数
print("9/3=" + str(9 / 3))  # /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数

print('----------Boolean------------')
print("True and True:" + str(True and True))
print("True and False:" + str(True and False))
print("False and False:" + str(True and False))
print("True or False:" + str(True or False))
print("False or False:" + str(False or False))
print("not True:" + str(not True))
print("not False:" + str(not False))
