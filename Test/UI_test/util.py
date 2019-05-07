# -*- coding:utf-8 -*-

import os   #os 提供了很多与操作系统交互的函数
import xlrd #xlrd   读取Excel的扩展工具
import cx_Oracle    #cx_Oracle
from xlutils.copy import copy   #xlutils.copy
import requests #requests
import json #json


#接口请求
def getInterfaceRes(interfaceNo, body):
    url = "http://172.18.100.211:8082/core-interface/api/loan/%d/v1"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#获取数据库account_no的查询结果   #尝试去做增删改
def getSQLResult(sql=None):
    dsn = cx_Oracle.makedsn("172.18.100.159", 1521, "kfdb")  # cx_Oracle.makedsn
    conn = cx_Oracle.connect("core0303", "core0303", dsn)  # cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
def updateSQL(sql=None):
    dsn = cx_Oracle.makedsn("172.18.100.159", 1521, "kfdb")  # cx_Oracle.makedsn
    conn = cx_Oracle.connect("core0303", "core0303", dsn)  # cx_Oracle.connect
    cursor = conn.cursor()  # conn.cursor
    cursor.execute(sql)  # execute
    #res = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
#从excel中取值
def getExcelData(dataPath, cellname, pid, sheetname):
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(proDir, dataPath)      #os.path.join    把目录和文件名合成一个路径
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
def setExcelData(dataPath,cellvalue, cellname, pid, sheetname):
    cellvalue = str(cellvalue)
    if cellname == "请求报文" or cellname == "返回报文":
        cellvalue = cellvalue.replace(" ", "\n")
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]
    dataPath = os.path.join(proDir, dataPath)
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
'''#获取sheet行数
def getExcelNrows(sheetname):
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(proDir, "hfFangKuan1\FangKuan1.xls")   #os.path.join    把目录和文件名合成一个路径
    fd = xlrd.open_workbook(dataPath, formatting_info=True) #xlrd.open_workbook 打开excel文件
    sh = fd.sheet_by_name(sheetname)    #fd.sheet_by_name
    return sh.nrows #sh
'''
#获取sheet行数
def getExcelNrows(dataPath , sheetname):
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(proDir, dataPath )   #os.path.join    把目录和文件名合成一个路径
    fd = xlrd.open_workbook(dataPath, formatting_info=True) #xlrd.open_workbook 打开excel文件
    sh = fd.sheet_by_name(sheetname)    #fd.sheet_by_name
    return sh.nrows #sh




