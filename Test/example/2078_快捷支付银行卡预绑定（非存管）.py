# -*- coding:utf-8 -*-
#如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。

import random	#random 提供了生成随机数的工具
from Com.util import getSQLResult, getExcelData, setExcelData, getInterfaceRes, getExcelNrows	#util.py

interfaceNo = 2078
for pid in range(1, getExcelNrows(interfaceNo)):	#range() 函数可创建一个整数列表，一般用在 for 循环中	#getExcelNrows:获取场景数
	#接口请求：做接口字段做分类：1 固定字段，2 业务分类字段（字典值），3 业务字段 3.1新增字段 3.2存量字段，4有固定规则字段
	BodyData = {
		"sysSource": "2",
		"frontTransNo": "1701830089%d"%random.randint(00000000,99999999),	#random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
		"frontTransTime": "2017-09-01 10:51:00",	#尝试对交易时间取值，例如取系统当前时间，或者随机时间
		"interfaceNo": "2078",
		"busiCode": "LBB78",
		"custCode": "%s"%getExcelData("custCode", pid, interfaceNo),	#getExcelData	从excel中取值
		"bankCardNo": "%s"%getExcelData("bankCardNo", pid, interfaceNo),
		"isAppFlg": "1",
		"depositCode": "00",
		"payChannelType": "HX_0013",
		"payChannelName": "金运通",
		"clientSource": "LOAN001"
	}
	rebody = getInterfaceRes(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
	setExcelData(rebody, "返回报文", pid, interfaceNo)	#
	#对接口返回结果进行判断	尝试对非以下结果抛异常
	res = rebody["responseBody"]["retCode"]
	if res == "0000":
		setExcelData("pass", "测试结果", pid, interfaceNo)
		setExcelData("pass","测试结果",pid,interfaceNo)
	elif res == "0001":
		setExcelData("fail", "测试结果", pid, interfaceNo)
		setExcelData("fail","测试结果",pid,interfaceNo)
	elif res == "9999":
		setExcelData("day_of_end", "测试结果", pid)
		print("day_of_end","测试结果",pid)
		print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
		break
	#连接数据库进行判断
	sql = "select * from t_tn_online_bind_flow a where a.account_no = '6222020200097521997'"	####根据各个接口场景的数据流
	setExcelData(sql, "查询SQL", pid, interfaceNo)
	setExcelData(getSQLResult(sql)[1][5], "SQL结果", pid, interfaceNo)	#获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
	setExcelData(BodyData, "请求报文", pid, interfaceNo)
	print(getExcelData("custCode", pid, interfaceNo), getExcelData("bankCardNo", pid, interfaceNo))


