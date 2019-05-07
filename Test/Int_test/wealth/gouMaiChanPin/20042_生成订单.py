# -*- coding:utf-8 -*-
#如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。

import random	#random 提供了生成随机数的工具
from Test.Int_test.util import *	#util.py

interfaceNo = 20042
for pid in range(1, getExcelNrows(interfaceNo)):	#range() 函数可创建一个整数列表，一般用在 for 循环中	#getExcelNrows:获取场景数
	#接口请求：做接口字段做分类：1 固定字段，2 业务分类字段（字典值），3 业务字段 3.1新增字段 3.2存量字段，4有固定规则字段
	BodyData = {
		"payAmount":"10000",
        "planName":"佳宁空包",
        "interfaceNo":"20042",
        "orderType":"1",
        "investMode":"2",
        "productCode":"PTF180201312",
        "planNo":"P20180412101114649713",
        "productVersion":"1",
        "transNo":"20171017155814292",
        "yieldRate":"8",
        "transTime":"2017-10-17 15:58:14",
        "couponUse":"0",
        "payType":"0",
        "custName":"蒋璐",
        "ecifId":"CR20180101441678",
        "sysSource":"5",
        "investAmount":"10000",
        "productName":"空包30天j09",
        "mobile":"15878712241"
	}
        print("pid：%s"%pid)
	rebody = getInterfaceRes(BodyData)	#getInterfaceRes 取请求报文
        print("rebody：%s"%rebody)
    #rebody = getInterfaceRes(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
	#setExcelData(rebody, "返回报文", pid, interfaceNo)
        setExcelData("testsetstestsetest", "返回报文", pid, interfaceNo)
        print("写入“返回报文”")
	#对接口返回结果进行判断	尝试对非以下结果抛异常
	res = rebody["responseBody"]["retCode"]
	if res == "0000":
		setExcelData("pass", "测试结果", pid, interfaceNo)
                print("写入“测试结果”pass")
	elif res == "0001":
		setExcelData("fail", "测试结果", pid, interfaceNo)
                print("写入“测试结果”fail")
	elif res == "9999":
		setExcelData("day_of_end", "测试结果", pid)
		print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
		break
	#连接数据库进行判断
	sql = "select * from t_tn_online_bind_flow a where a.account_no = '6222020200097521997'"	####根据各个接口场景的数据流
	setExcelData(sql, "查询SQL", pid, interfaceNo)
        print("写入“查询SQL”：%s"%sql)
	setExcelData(getSQLResult(sql)[1][5], "SQL结果", pid, interfaceNo)	#获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        print("写入“SQL结果”")
	setExcelData(BodyData, "请求报文", pid, interfaceNo)
        print("写入请求报文")
	print(getExcelData("custCode", pid, interfaceNo), getExcelData("bankCardNo", pid, interfaceNo))


