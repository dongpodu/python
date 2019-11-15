#!/usr/bin/python
# -*- coding: UTF-8 -*-
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串

print('----------1------------')
for l in 'python':
    print(l)

print('----------2------------')
li = [1, 2, 3, 4]
for e in li:
    print(e)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

print('----------3------------')
print(range(10))  # 定义从0-10的有序序列，步长为1
print(range(10, 20))  # 定义从10-20的有序序列，步长为1
print(range(10, 20, 2))  # 定义从10-20的有序序列，步长为2

print('----------4------------')
# 在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样
for index in range(1, 10):
    print('执行for循环')
else:
    print('结束for循环')
