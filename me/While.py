#!/usr/bin/python
# -*- coding: UTF-8 -*-
print('----------1------------')
count = 0
while count < 10:
    count += 1
    print(count)

print('----------2------------')
numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

print('----------3------------')
count1 = 0
while count1 < 10:
    count1 += 1
    if count1 % 2 == 1:
        continue
    print(count1)

print('----------4------------')
names = ['张三', '李四', '杜五', '王六']
index = 0
while index < len(names):
    if names[index] == '杜五':
        break
    index += 1
print('位置：' + str(index))

print('----------5------------')
count2 = 0
while count2 < 5:
    print(count2, " is  less than 5")
    count2 = count2 + 1
else:
    print(count2, " is not less than 5")

print('----------6------------')
flag1 = 1
while flag1:
    print("Given flag is really true!")  # 无限循环你可以使用 CTRL+C 来中断循环
print("Good bye!")
