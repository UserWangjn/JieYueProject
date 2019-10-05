# -*- coding:utf-8 -*-

import os   #os 提供了很多与操作系统交互的函数
import xlrd #xlrd   读取Excel的扩展工具
import cx_Oracle    #cx_Oracle
from xlutils.copy import copy   #xlutils.copy
import requests #requests
import json #json
import random
import random as r

#统一用户地址理财APP-集成1
'''def getInterfaceResLCAPP(interfaceNo, body):
    url = "http://172.18.101.151:9180/fintech-appuser/api/financial/%d/v1"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res'''

def loanjc02():#借款系统
    jc01 = "http://dkjc1.jieyuechina.com/loan"
def daikuanxitong():  # 借款系统
    jc02 = "http://dkjc2.jieyuechina.com/loan"
    jc03 = "http://dkjc3.jieyuechina.com/loan"
    jc04 = "http://dkjc4.jieyuechina.com/loan"
    jc05 = "http://dkjc5.jieyuechina.com/loan"

def xinshenxitong():#信审系统
    jc01 = "http://fintechjc1.jieyuechina.com/loan-credit"
    jc02 = "http://fintechjc1.jieyuechina.com/loan-credit"
    jc03 = "http://fintechjc1.jieyuechina.com/loan-credit"
    jc04 = "http://fintechjc1.jieyuechina.com/loan-credit"
    jc05 = "http://fintechjc1.jieyuechina.com/loan-credit"

#统一用户地址-准生产私有云--------------------------------------------------------------------------------
# 理财APP地址
def getInterfaceResLCAPP(interfaceNo, body):
    url = "http://10.50.170.62:8080/fintech-appuser/api/financial/%d/v1"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
# APPuser地址
def getInterfaceResAPPUSER(interfaceNo, body):
    url = "http://172.18.101.151:9180/fintech-appuser/api/AppUser/%s"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
# customer地址
def getInterfaceResCUSTOMER(interfaceNo, body):
    url = "http://172.18.101.151:9180/fintech-appuser/api/customer/customer/%s/v1"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res

def getInterfaceResCUSTOMER_get(interfaceNo, body):
    url = "http://172.18.101.151:9180/fintech-appuser/api/customer/customer/%s/v1?cardType= 1 &cardNumber=%s"%interfaceNo#熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res

# black地址
def getInterfaceResBLACK(interfaceNo, body):
    url = "http://172.18.101.151:9180/masterdata/api/customer/black/%s/v1"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res

#接口请求
def getInterfaceRes(interfaceNo, body):
    url = "http://lc.jieyuechina.com:9082/wmsystem/service/%d/v1"%interfaceNo #熟悉%d的用法，熟悉其他字符串替换方法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res

#信贷调用核心集成1环境接口地址：
def getInterfaceResloanjc01(interfaceNo, body):
    url = "http://172.18.100.59:8082/core-interface/api/loan/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#信贷调用核心集成2环境接口地址：
def getInterfaceResloanjc02(interfaceNo, body):
    url = "http://172.18.100.164:8082/core-interface/api/loan/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#信贷调用核心集成3环境接口地址：
def getInterfaceResloanjc03(interfaceNo, body):
    url = "http://172.18.100.211:8082/core-interface/api/loan/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#信贷调用核心集成4环境接口地址：
def getInterfaceResloanjc04(interfaceNo, body):
    url = "http://172.18.100.123:8082/core-interface/api/loan/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#信贷调用核心集成5环境接口地址：
def getInterfaceResloanjc05(interfaceNo, body):
    url = "http://172.18.100.89:8082/core-interface/api/loan/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#借悦sever调用信贷集成5接口地址：
def getInterfaceResloanseverjc01(interfaceNo, body):
    url = "http://10.50.181.48:21007/loan-api-link/api/appbiz/LoanEasyRest/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#借悦sever调用信贷集成2接口地址：
def getInterfaceResloanseverjc02(interfaceNo, body):
    url = "http://10.50.181.48:22007/loan-api-link/api/appbiz/LoanEasyRest/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#借悦sever调用信贷集成3接口地址：
def getInterfaceResloanseverjc03(interfaceNo, body):
    url = "http://10.50.181.48:23007/loan-api-link/api/appbiz/LoanEasyRest/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#借悦sever调用信贷集成4接口地址：
def getInterfaceResloanseverjc04(interfaceNo, body):
    # url = "http://10.50.181.48:24007/loan-api-link/api/appbiz/LoanEasyRest/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    url = "http://loan-api-link.asset.jc4.jieyue.com/loan-api-link/api/appbiz/LoanEasyRest/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#借悦sever调用信贷集成5接口地址：
def getInterfaceResloanseverjc05(interfaceNo, body):
    url = "http://10.50.181.48:25007/loan-api-link/api/appbiz/LoanEasyRest/%d/v1"%interfaceNo #熟悉%d的用法，熟法
    headers = {"Content-Type": "application/json"}  #报文头
    req = requests.post(url, data=json.dumps(body), headers=headers)    #requests.post  发送post请求方法  json.dumps  将 Python 对象编码成 JSON 字符串
    res = json.loads(req.content)   #json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    return res
#获取数据库account_no的查询结果   #尝试去做增删改
#连接理财数据库
def getSQLResult(sql=None):
    dsn = cx_Oracle.makedsn("10.50.180.32", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("lc1009", "lc1009", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接核心集成1数据库
def getSQLResulthxjc01(sql=None):
    dsn = cx_Oracle.makedsn("172.18.100.107", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("jc01_core", "efl134kgoewa", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接核心集成2数据库
def getSQLResulthxjc02(sql=None):
    dsn = cx_Oracle.makedsn("10.50.180.32", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("core1009", "ffvbgh45tghh", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接核心集成3数据库
def getSQLResulthxjc03(sql=None):
    dsn = cx_Oracle.makedsn("172.18.100.126", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("core0915", "sdcv547uhfsf", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接核心集成4数据库
def getSQLResulthxjc04(sql=None):
    dsn = cx_Oracle.makedsn("10.50.182.11", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("jc04_core", "jc04_core", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接核心集成5数据库
def getSQLResulthxjc05(sql=None):
    dsn = cx_Oracle.makedsn("172.18.100.183", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("jc05_core", "jc05_core", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接主数据数据库
def getSQLResultMD(sql=None):
    dsn = cx_Oracle.makedsn("10.50.180.32", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("md1009", "md1009", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    cursor.execute(sql) #execute
    res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接贷款集成1数据库
def getSQLResultloanjc01(sql=None):
    dsn = cx_Oracle.makedsn("10.50.180.62", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  # conn.cursor
    cursor.execute(sql)  # execute
    res = cursor.fetchall()  # fetchall
    cursor.close()  # cursor.close
    conn.close()  # conn.close
    return res
#连接贷款集成2数据库
def getSQLResultloanjc02(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.58", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  # conn.cursor
    cursor.execute(sql)  # execute
    res = cursor.fetchall()  # fetchall
    cursor.close()  # cursor.close
    conn.close()  # conn.close
    return res
#连接贷款集成3数据库
def getSQLResultloanjc03(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.59", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  # conn.cursor
    cursor.execute(sql)  # execute
    res = cursor.fetchall()  # fetchall
    cursor.close()  # cursor.close
    conn.close()  # conn.close
    return res
#连接贷款集成4数据库
def getSQLResultloanjc04(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.60", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  # conn.cursor
    cursor.execute(sql)  # execute
    res = cursor.fetchall()  # fetchall
    cursor.close()  # cursor.close
    conn.close()  # conn.close
    return res
#连接贷款集成5数据库
def getSQLResultloanjc05(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.61", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  # conn.cursor
    cursor.execute(sql)  # execute
    res = cursor.fetchall()  # fetchall
    cursor.close()  # cursor.close
    conn.close()  # conn.close
    return res
#连接贷款集成1数据库修改数据
def getSQLResultloanxgjc01(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.62", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    res = cursor.execute(sql) #execute
    conn.commit()
    #res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接贷款集成2数据库修改数据
def getSQLResultloanxgjc02(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.58", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    res = cursor.execute(sql) #execute
    conn.commit()
    #res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接贷款集成3数据库修改数据
def getSQLResultloanxgjc03(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.59", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    res = cursor.execute(sql) #execute
    conn.commit()
    #res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接贷款集成4数据库修改数据
def getSQLResultloanxgjc04(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.60", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    res = cursor.execute(sql) #execute
    conn.commit()
    #res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#连接贷款集成5数据库修改数据
def getSQLResultloanxgjc05(sql=None):
    dsn = cx_Oracle.makedsn("10.50.181.61", 1521, "testdb")   #cx_Oracle.makedsn
    conn = cx_Oracle.connect("loan_l", "loan_l", dsn)  #cx_Oracle.connect
    cursor = conn.cursor()  #conn.cursor
    res = cursor.execute(sql) #execute
    conn.commit()
    #res = cursor.fetchall() #fetchall
    cursor.close()  #cursor.close
    conn.close()    #conn.close
    return res
#从excel中取值
def getExcelData(cellname, pid, sheetname):
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(str(proDir), "jinjian\interface.xls")      #os.path.join    把目录和文件名合成一个路径
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
def setExcelData(cellvalue, cellname, pid, sheetname):
    cellvalue = str(cellvalue)
    if cellname == "请求报文" or cellname == "返回报文":
        cellvalue = cellvalue.replace(" ", "\n")
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]
    dataPath = os.path.join(proDir, "jinjian\interface.xls")
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
def getExcelNrows(sheetname):
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(proDir, "jinjian\interface.xls")   #os.path.join    把目录和文件名合成一个路径
    fd = xlrd.open_workbook(dataPath, formatting_info=True) #xlrd.open_workbook 打开excel文件
    sh = fd.sheet_by_name(sheetname)    #fd.sheet_by_name
    return sh.nrows #sh


def scoll_root(driver):
    # 把滚动条拉到底部
    js = "var q=document.body.scrollTop=50000"
    return driver.execute_script(js)
# 获取手机号
def createPhone():
	prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
			   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
	return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
# print(createPhone())

def name():

    a1 = ['张', '金', '李', '王', '赵', "刘", "马", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许", "何", "吕", "施", "喜", "灰", "冯"]

    a2 = ['玉', '明', "椿", "洋", '龙', '芳', '军', '玲', "发", "新", "与", "太", "胜"]

    a3 = ['立', '玲', '国', '中', "发", "刚", "正", "明", "华", "灰", "馀", "洋", "浪"]

    for i in range(1):
        name1 = r.choice(a1) + r.choice(a2) + r.choice(a3)
    name = name1
    return name

def idcard():
    prelist = ["62170000"]
    card=["45678"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(6))+""+random.choice(card)
def hshcintoappcode():
    prelist = ["131"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(6))



