#!/usr/bin/python3
# -*- coding: UTF-8 -*-

flag = True
if flag:
    print("hello")
else:
    print("你好")

print(1 == 2 and 2 == 2)
print(1 == 2 or 2 == 2)

count = -1  # 要count是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if count:
    print("count不等于0")
else:
    print("count等于0")
