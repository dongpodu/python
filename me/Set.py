#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Dictionary 通过{}标识
set1 = {1, 2, 3, 3, 1}
print(set1)
set1.add(5)
print(set1)
set1.remove(5)
print(set1)
set2 = set([2, 3])
print(set1 & set2)
print(set1 | set2)
