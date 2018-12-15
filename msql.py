#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='123456', database='kiwitest')

cursor = conn.cursor()
# 创建user表:
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into k_docs (title, content, hits) values (%s, %s, %s)', ( 'cccc', 'cont-aaaa', '10'))

print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from k_docs where id >= %s order by id desc', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection
cursor.close()
conn.close()
