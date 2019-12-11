# -*- coding:utf-8 -*-

import os   #os 提供了很多与操作系统交互的函数
import xlrd #xlrd   读取Excel的扩展工具
import cx_Oracle    #cx_Oracle
from xlutils.copy import copy   #xlutils.copy
import requests #requests
import json #json
import sys
import random
import importlib
importlib.reload(sys)


#接口请求
#def getInterfaceRes(interfaceNo, body):
def getInterfaceRes(url,body):
    #url = "http://172.18.100.89:8082/core-interface/api/loan/2003/v1"     #%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    # 本案例中是把body的字段转化为json格式的字符串后发送Post请求，把返回的json格式的字符串结果loads为Python数据类型继续方便做处理，比如字典，获得key、value
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
def getInterfaceResjc05_2003(body):
    url = "http://172.18.100.89:8082/core-interface/api/loan/2003/v1"     #%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
def getInterfaceResjc05_2118(body):
    url = "http://172.18.100.89:8082/core-interface/api/loan/2118/v1"     #%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#获取数据库account_no的查询结果   #尝试去做增删改
def getSQLResult(sql,dsnpar):
    if dsnpar == 'jc01':
        dsn = '172.18.100.107'
        username = 'jc01_core'
        password = 'jc01_core'
    if dsnpar == 'jc02':
        dsn = '10.50.180.32'
        username = 'jc02_core'
        password = 'jc02_core'
    if dsnpar == 'jc03':
        dsn = '172.18.100.126'
        username = 'core0915'
        password = 'sdcv547uhfsf'
    if dsnpar == 'jc04':
        dsn = '10.50.182.11'
        username = 'jc04_core'
        password = 'jc04_core'
    if dsnpar == 'jc05':
        dsn = '172.18.100.183'
        username = 'jc05_core'
        password = 'jc05_core'
    #dsn = cx_Oracle.makedsn("172.18.100.104", 1521, "testdb")   #cx_Oracle.makedsn
    dsn = cx_Oracle.makedsn(dsn, 1521, "testdb")
    #conn = cx_Oracle.connect("jc02_core", "core246685", dsn)  #cx_Oracle.connect
    conn = cx_Oracle.connect(username,password, dsn)  # cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
def getSQLResult_jc05_core(sql=None):
    dsn = cx_Oracle.makedsn("172.18.100.183", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("jc05_core", "jc05_core", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#从excel中取值
def getExcelData(path,cellname, pid, sheetname):
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    # print('proDir:',proDir)
    print('getcwd:',os.getcwd())
    #dataPath = os.path.join(proDir, "../interface.xls")      #os.path.join    把目录和文件名合成一个路径
    dataPath = os.path.join(proDir, path)
    fd = xlrd.open_workbook(dataPath, formatting_info=True) #xlrd.open_workbook
    sh = fd.sheet_by_name(sheetname)
    for row_index in range(sh.nrows):
        colvalue = sh.cell(int(row_index), 0).value
        if pid == colvalue:
            break
    for col_index in range(sh.ncols):
        rowvalue = sh.cell(0,int(col_index)).value
        if cellname == rowvalue:
            break
    cellvalue = sh.cell(row_index, col_index).value
    return cellvalue
#写入EXCEL
def setExcelData(path,cellvalue, cellname, pid, sheetname):
    cellvalue = str(cellvalue)
    if cellname == "请求报文" or cellname == "返回报文":
       cellvalue = cellvalue.replace(" ", "\n")
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]
    dataPath = os.path.join(proDir, path)
    #dataPath = os.path.join(proDir, "../interface.xls")
    fd = xlrd.open_workbook(dataPath, formatting_info=True)
    sh = fd.sheet_by_name(sheetname)
    for row_index in range(sh.nrows):
        colValue = sh.cell(int(row_index), 0).value
        if pid == colValue:
            break
    for col_index in range(sh.ncols):
        rowvalue = sh.cell(0, int(col_index)).value
        if cellname == rowvalue:
            break
    sheetIndex = fd._sheet_names.index(sheetname)
    wb = copy(fd)
    sheet = wb.get_sheet(sheetIndex)
    sheet.write(row_index, col_index, cellvalue)
    wb.save(dataPath)
#获取sheet行数
def getExcelNrows(path,sheetname):
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(proDir, path)   #os.path.join    把目录和文件名合成一个路径
    #dataPath = os.path.join(proDir, '../interface.xls')  # os.path.join    把目录和文件名合成一个路径
    fd = xlrd.open_workbook(dataPath, formatting_info=True) #xlrd.open_workbook 打开excel文件
    sh = fd.sheet_by_name(sheetname)    #fd.sheet_by_name
    print("nrows:%s"%sh.nrows)
    return sh.nrows #sh

#生成一个随机的5位数
def bank_num():
    list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = random.sample(list_num, 5)
    res = str(res[0]) + str(res[1]) + str(res[2]) + str(res[3]) + str(res[4])
    return int(res)

if __name__ == '__main__':
    getExcelData('',',','','')