#!/usr/bin/python3
# -*- coding: UTF-8 -*-

s = "abcdef"
s1 = 'abcdef'
print("s1:" + s1)  # ''和""都可以用来标识字符串
print(s[1:3])  # 返回bc，类似java的substring(start,end)，正数是从左向右，起点是0，负数是从右向左，起点是-1
print(s[-3:-1])  # 返回de
print(s[1:])  # 返回bcdef
print(s[1])  # 返回bcdef
print(s * 2)  # 星号（*）是重复操作
print(s + "ss")  # 加号（+）是连接操作
print('''ddd
bbb
ccc''')  # 多行可以用'''括起来
print(r'\t')  # r''括起来的字符串默认不转义

print("i am %d" % 20)
print("i %s %d" % ('am', 20))
a = 'am'
b = 20
print(f"i {a} {b}")  # f开头的字符串的站位符会被对应的变量替换
print(ord('A'))  # ord()函数可以用来获取单个字符的编码（整数表示）
print(chr(65))  # chr()函数可以将编码转为单个字符
print('\u4e2d\u6587')  # 用16进制的编码指定字符串
print(b'abc')  # b''代表字节，英文的字节就是英文本身
print('中'.encode('utf-8'))  # 中文字节没法用字符显示，所以显示为\x##
print(b'\xe4\xb8\xad'.decode('utf-8'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))  # 如果bytes中包含无法解码的字节，decode()方法会报错
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  # 可以传入errors='ignore'忽略错误的字节
print(len("abc"))  # len()函数里的参数如果是字符串，则返回字符数；如果是字节，则返回字节数
print(len(b'abc'))  # len(b)函数返回字节数
print(len(b'\xe4\xb8\xad'))
print(len(b'\xe4\xb8\xad'.decode('utf-8')))
