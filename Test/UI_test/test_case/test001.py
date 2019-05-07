#coding=utf-8
from selenium import webdriver
import unittest
from time import *
import pub
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


sheetName = "fangkuan"
for pid in range(1,pub.getExcelNrows(sheetName)):
    pub.setExcelData("pass", "合同状态", pid, sheetName)
'''
sheetName = "fangkuan"
test1 = "20141209151E1004"
sql = "select * from t_c_at_account acc where acc.account in (select tt.acc_id from T_C_at_loanINFO tt where tt.contract_no in( '%s'))"%test1
print(sql)

balance = pub.getSQLResult(sql)[0][5]
print(balance)
for pid in range(1,pub.getExcelNrows(sheetName)):
    pub.setExcelData(balance, "账户余额", pid, sheetName)
use_balance = pub.getSQLResult(sql)[0][6]
for pid in range(1,pub.getExcelNrows(sheetName)):
    pub.setExcelData(use_balance, "可用余额", pid, sheetName)
'''