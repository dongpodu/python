#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Tuple 元组类似于 List（列表），用 () 标识。元组不能二次赋值，相当于只读列表。
print('----------Tuple------------')
tu = (1, 2, 3, 4, 5, 6, 7, 8)
print(tu)
print(tu[:3])
print(tu[1:3])
print(tu * 2)  # 星号（*）是重复操作
print(tu + tu)  # 加号（+）是连接操作
# tu[2] = 1000    # 元组中是非法应用
t = (1)  # 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
print(t)
t1 = (1,)  # 这才是定义了一个元素的元祖
t2 = ('a', 'b', ['A', 'B'])
t2[2][0] = 'X'  # 位置2是个list，可以变；元祖不变的意思是：tuple的每个元素，指向永远不变
print(t2)