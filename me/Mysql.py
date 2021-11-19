#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='pugv_coupon',
                             port=3306,
                             charset='utf8')
cursor = connection.cursor()
sql = 'select * from t_coupon_batch_info'
count = cursor.execute(sql)
print('数量' + str(count))
print('\n')

print('-----------数组游标-----------')
for row in cursor.fetchall():
    print("第一列:" + str(row[0]) + "，第二列:" + str(row[1]))
print('\n')

print('-----------字典游标-----------')
cursor1 = connection.cursor(pymysql.cursors.DictCursor)  # 字典
cursor1.execute(sql)
for row in cursor1.fetchall():
    print(row)
    print("name:" + str(row['name']))
print('\n')

sql1 = 'select count(*) count from t_coupon_batch_info'
cursor2 = connection.cursor(pymysql.cursors.DictCursor)  # 字典
cursor2.execute(sql1)
result = cursor2.fetchone()
print('数量：'+str(result['count']))
