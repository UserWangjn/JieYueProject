# coding:utf-8
import unittest
import os
import pandas
from Com import configDB
from datetime import datetime

# 用例路径
# sql = configDB.ConfigDB()
# sql.dbname = "LOAN2DB"
# SQL1 = "select * from LA_T_REDUCTION t where COLL_LIST_NO = '2018013600000025' and CONTRACT_ID = '20140416140I1010-1'"
# cursor = sql.executeSQL(SQL1)
# fields = dict([(field[0],cursor.description.index(field)) for field in cursor.description])
# row=cursor.fetchall()
# for r in row:
#     print (r[fields['CONTRACT_ID']])
#res1 = sql.get_one(cursor)
#results = pandas.read_sql(res1)
#print(res1)
#for field in cursor.description:
# print(str(datetime.now().strftime("%Y%m%d%H%M%S")))
#print(str(1.40001))