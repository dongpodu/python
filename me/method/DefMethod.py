#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def my_abs(x):  # 自定义函数
    return 1


def m1(x):  # 没有返回值的函数，默认返回None，等同于return None
    print("m1函数执行....")


def returnMutiValue(x, y):
    return x, y  # 看上去返回的是多个值，其实是一个tuple对象，语法可以这么简写


def m2(x, y=2, z="name"):  # y默认等于1，外部调用时可以不传n参数。
    print("x is %s" % x)
    print("y is %s" % y)
    print("z is %s" % z)
    print('***************')


m2(3)
m2(3, 4)  # 按顺序写参数，不需要指定名
m2(3, z='name1')  # 不按顺序写参数，需指定参数名


def add(l=[]):  # 定义默认参数要牢记一点：默认参数必须指向不变对象。这里定义的函数就有问题，会导致第n（n>1）次调用时，l的默认值不再是[]
    l.append("end")
    return l


def add1(l=None):  # 修复add问题
    if l is None:
        l = []
    l.append("end")
    return l


print(add())
print(add())
print(add())


def cal(*numbers):  # 定义可变参数函数，函数内部是通过tuple接受的
    print(isinstance(numbers, tuple))
    s = 0
    for n in numbers:
        s = s + n
    return s


print(cal(1, 2, 3))
print(cal(1, 2, 3, 4))
l = [1, 2]
print(cal(*l))  # list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
t = (1, 2)
print(cal(*t))


def dd(a, b, **other):  # ** 代表字典类型的可变参数，名叫关键字可变参数
    print(isinstance(other, dict))
    print("a:", a, "b:", b, other)


dd(1, 2, c=3)


def ddd(a, b, *, c, d):  # 将关键字参数名字限定为c和d，名为命名关键字参数
    print("c:", c, "d:", d)


ddd(1, 2, c=4, d=5)
