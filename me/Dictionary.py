#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Dictionary 通过{}标识
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
# print(dict['two'])  # key不存在会报错
print(dict.get('two'))  # key不存在不会报错
print("two" in dict)
dict.pop('one')  # 删除key
print(dict)
