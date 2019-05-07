# -*- coding:utf-8 -*-
#如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。

import random	#random 提供了生成随机数的工具

import time
from util import getSQLResult, getExcelData, setExcelData, getInterfaceRes, getExcelNrows	#util.py
interfaceNo = 5002
frontTransTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

print(frontTransTime)
for pid in range(1, getExcelNrows(interfaceNo)):	#range() 函数可创建一个整数列表，一般用在 for 循环中	#getExcelNrows:获取场景数
	#接口请求：做接口字段做分类：1 固定字段，2 业务分类字段（字典值），3 业务字段 3.1新增字段 3.2存量字段，4有固定规则字段
	BodyData = {
        "frontTransNo": "1701830089%d" % random.randint(00000000, 99999999),#random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
        "frontTransTime": "%s"%time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
        "accountName": "%s"%getExcelData("accountName", pid, interfaceNo),      #账户名称
        "accountNum":"%s"%getExcelData("accountNum", pid, interfaceNo),        #账号
        "bankCode":"%s"%getExcelData("bankCode", pid, interfaceNo),            #银行编码
        "busiCode":"WMB56",
        "certId":"%s"%getExcelData("certId", pid, interfaceNo),                  #身份证号
        "certType":"1",
        "interfaceNo":"5002",
        "mobile":"%s"%getExcelData("mobile",pid,interfaceNo),
        "sysSource": "3",
        "source": "%s" % getExcelData("source", pid, interfaceNo)
    }

	rebody = getInterfaceRes(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
	print(rebody["responseBody"]["retMsg"])

	setExcelData(rebody, "返回报文", pid, interfaceNo)	#
	#对接口返回结果进行判断	尝试对非以下结果抛异常
	res = rebody["responseBody"]["retCode"]
	if res == "0000":
		setExcelData("fail",)
		setExcelData("dfs")
		setExcelData("sdfa")
	elif res == "0001":
		setExcelData("fail", "测试结果", pid, interfaceNo)
	elif res == "9999":
		setExcelData("day_of_end", "测试结果", pid)
		print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
		break
	#连接数据库进行判断
	sql = "select * from t_tn_online_bind_flow a where a.account_no = '6222020200097521997'"	####根据各个接口场景的数据流
	setExcelData(sql, "查询SQL", pid, interfaceNo)
	setExcelData(getSQLResult(sql)[1][5], "SQL结果", pid, interfaceNo)	#获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
	print ("getSQLResult(sql)")
	setExcelData(BodyData, "请求报文", pid, interfaceNo)
	print(getExcelData("custCode", pid, interfaceNo), getExcelData("bankCardNo", pid, interfaceNo))