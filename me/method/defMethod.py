#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def my_abs(x):  # 自定义函数
    return 1


def m1(x):  # 没有返回值的函数，默认返回None，等同于return None
    print("m1函数执行....")


def returnMutiValue(x, y):
    return x, y  # 看上去返回的是多个值，其实是一个tuple对象，语法可以这么简写


def m2(x, y=2, z="name"):  # y默认等于1，外部调用时可以不传n参数
    print("x is %s" % x)
    print("y is %s" % y)
    print("z is %s" % z)
    print('***************')


m2(3)
m2(3, 4)  # 按顺序写参数，不需要指定名
m2(3, z='name1')  # 不按顺序写参数，需指定参数名
