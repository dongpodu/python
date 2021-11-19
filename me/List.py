#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# List 通过[]标识，是一个可变的有序表
l = [1, 2, 3, 4]
print('长度：' + str(len(l)))
print(l)
print(l[1:3])  # 类似字符串
print(l[:3])
print(l[3])
print(l * 2)  # 星号（*）是重复操作
print(l + [5, 6])  # 加号（+）是连接操作
l.append(5)  # 追加
print(l)
l.insert(0, 0)  # 插入
print(l)
l.pop()  # 删除末尾元素
print(l)
l.pop(0)  # 删除指定位置元素
print(l)
l[0] = 2  # 替换指定位置元素
print(l)
l.append("ss")
print(l)  # 存放的元素类型不同
