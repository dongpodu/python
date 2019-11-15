#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 数据类型 Numbers、String、List、Tuple（元组）、Dictionary

# Number
print('----------Number------------')
var1 = 1  # int
var2 = 1  # long
var3 = 1.0  # float
var4 = 1 + 2j  # 复数
var5 = complex(1, 2)  # 复数
print("var1:" + str(var1))
print("var2:" + str(var2))
print("var3:" + str(var3))
print("var4:" + str(var4))

# String
print('----------String------------')
s = "abcdef"
print(s[1:3])  # 返回bc，类似java的substring(start,end)，正数是从左向右，起点是0，负数是从右向左，起点是-1
print(s[-3:-1])  # 返回de
print(s[1:])  # 返回bcdef
print(s[1])  # 返回bcdef
print(s * 2)  # 星号（*）是重复操作
print(s + "ss")  # 加号（+）是连接操作

# List 通过[]标识
print('----------List------------')
t = [1, 2, 3, 4]
t1 = [5, 6]
print(t)
print(t[1:3])  # 类似字符串
print(t[:3])
print(t[3])
print(t * 2)  # 星号（*）是重复操作
print(t + t1)  # 加号（+）是连接操作

# Tuple 元组类似于 List（列表），用 () 标识。元组不能二次赋值，相当于只读列表。
print('----------Tuple------------')
tu = (1, 2, 3, 4, 5, 6, 7, 8)
print(tu)
print(tu[:3])
print(tu[1:3])
print(tu * 2)  # 星号（*）是重复操作
print(tu + tu)  # 加号（+）是连接操作
# tu[2] = 1000    # 元组中是非法应用

# Dictionary 通过{}标识
print('----------Dictionary------------')
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


