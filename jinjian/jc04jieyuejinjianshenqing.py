# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
import datetime
import random
import random as r
import cx_Oracle    #cx_Oracle
from Com.cardid import gennerator
from selenium.webdriver.chrome.options import Options
import os   #os 提供了很多与操作系统交互的函数
import xlrd #xlrd   读取Excel的扩展工具
import cx_Oracle    #cx_Oracle
from xlutils.copy import copy   #xlutils.copy
import requests #requests
import json #json
from datetime import date
from datetime import timedelta
from selenium import webdriver
import threading
from Com.util import getSQLResulthxjc02,getSQLResultloanxgjc02,getSQLResultloanjc02,getInterfaceResloanseverjc02, getExcelData, setExcelData, createPhone,name,idcard, getExcelNrows,scoll_root,getInterfaceRes,getSQLResult
from Com.util import *
from jinjian.Openingcard import Openingcard
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


# loanjc="http://dkjc4.jieyuechina.com/loan/user/home"
loanjc="http://dk.asset.jc4.jieyue.com/loan/user/home"
xinshenjc="http://fintechjc4.jieyuechina.com/loan-credit"
coreDB=getSQLResulthxjc04
loanDBXG=getSQLResultloanxgjc04
loanDB=getSQLResultloanjc04
loansever=getInterfaceResloanseverjc04

def Incominginformation():#进件信息
    interfaceNo = 1118
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        mobile = createPhone()
        cardId = gennerator()
        custName = name()
        bankCardNo = idcard()
        setExcelData(cardId, "cardId", pid, interfaceNo) #写入Excel
        setExcelData(custName, "custName", pid, interfaceNo)
        setExcelData(mobile, "mobile", pid, interfaceNo)
        setExcelData(bankCardNo, "bankCardNo", pid, interfaceNo)

def jineqixian(): #金额期限申请
    interfaceNo = 1118
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数

        BodyData = {
            "sysSource": "4",
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),# random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b,
            "frontTransTime": "2019-01-07 16:49:33",
            "interfaceNo": "1118",
            "busiCode": "CSB18",
            "telephone": mobile, #手机号
            "appAmount": "100000", #申请金额
            "appPeriod": "24", #申请期限
            "custmerManger": "11049136",#客户经理 11059349田世豪   11049136 黄源浩-进件   10022298-质检
            "position": "301000817", #位置
            "telemarketing": "0", #是否电销 是：1 否：0
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33"
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("金额期限申请118接口:",rebody)
        consultId = rebody["responseBody"]["consultId"]  # 读取返回报文consultId值
        setExcelData(consultId, "consultId", pid, interfaceNo)#

def certification(): #实名认证
    interfaceNo = 1037
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        BodyData = {
            "position": "301002007",
            "cardId": cardId,
            "birthday": "1989-12-03",
            "sex": "M",
            "cardUrlB": "group1/M00/08/0D/rBJkp1vBsueAdgdBAAK0IbbA_UA010.jpg",
            "interfaceNo": "1037",
            "consultId": consultId, #咨询单号
            "cardUrlA": "group1/M00/08/0D/rBJkp1vBsueAJeBWAAIxovgaVjM426.jpg",
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "custmerManger": "11049136",
            "cardEndT": "2018-05-22",
            "busiCode": "CSB37",
            "nation": "汉",
            "areaName": "北京市大兴区",
            "telemarketing": "0",
            "cardStartT": "2008-05-22",
            "sysSource": "1",
            "custName": custName,
            "telephone": mobile,
            "frontTransTime": "2018-10-13 16:56:56",
            "transTime": "2018-10-13 16:56:56",
            "transNo": "1901730089%d" % random.randint(00000000, 99999999)

        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceRes 取请求报文
        print(rebody)
        # setExcelData(rebody, "返回报文", pid, interfaceNo)
        # 对接口返回结果进行判断	尝试对非以下结果抛异常
        res = rebody["responseBody"]["retCode"]
        if res == "0000":
            setExcelData("pass", "测试结果", pid, interfaceNo)
        elif res == "0001":
            setExcelData("fail", "测试结果", pid, interfaceNo)
        elif res == "9999":
            setExcelData("day_of_end", "测试结果", pid)
            print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
            break
        # 连接数据库进行判断
        sql = "select * from  lb_t_cust_auth_cert tb where tb.cust_Name='" + custName + "'"
        result = loanDB(sql)
        for i in range(len(result)):
            cust_code = result[i][1]
            cust_name = result[i][2]
            card_Id = result[i][4]
            telephone = result[i][5]
            print(cust_code)
        print("实名认证1037接口：" + str(result))
        setExcelData(sql, "查询SQL", pid, interfaceNo)
        setExcelData(result, "SQL结果", pid, interfaceNo)  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        setExcelData(BodyData, "请求报文", pid, interfaceNo)
        setExcelData(rebody, "返回报文", pid, interfaceNo)
        setExcelData(cust_code, "custCode", pid, interfaceNo)
        setExcelData(cust_name, "custName", pid, interfaceNo)
        setExcelData(card_Id, "cardId", pid, interfaceNo)
        setExcelData(telephone, "mobile", pid, interfaceNo)

def dianziqianzhang(): #实名认证中3个电子签章-1084
    interfaceNo = 1084
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "sysSource": "1",
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),# random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b,
            "cardId": cardId,
            "interfaceNo": "1084",
            "consultId": consultId,
            "opType": "02",
            "custName": custName,
            "busiCode": "CSB84",
            "telephone": mobile,
            "frontTransTime": "2018-10-13 16:56:57",
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33"
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("实名认证中3个电子签章-1084接口:",rebody)

def huotirenzhengdengji(): #活体认证登记接口-1038
    interfaceNo = 1038
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "sysSource": "1",
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),# random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b,
            "cardId": cardId,
            "interfaceNo": "1038",
            "consultId": consultId,
            "custName": custName,
            "busiCode": "CSB38",
            "telephone": mobile,
            "frontTransTime": "2018-10-13 16:56:57",
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33"
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("活体认证登记接口-1038接口:",rebody)

def wanshanfangchanxinxi(): #完善房产信息-1049
    interfaceNo = 1049
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33",
            "cardId": cardId,
            "position": "沈阳",
            "interfaceNo": "1049",
            "consultId": consultId,
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "custmerManger": "11049136",#客户经理 田世豪
            "busiCode": "CSB49",
            "sysSource": "1",
            "custName": custName,
            "telephone": mobile,
            "intoDetailType": "lbTIntoInfoHouse",
            "frontTransTime": "2018-10-12 19:48:03",
            #房产信息
            "lbTIntoInfoHouse": [{
                "hProRightRate": "97",
                "hType": "1",
                #房产图片
                "housePicList": [{
                    "picName": "FC_01.jpg",
                    "picUrl": "group1/M00/08/02/rBJkp1vAiYeAS_nRAAFjJszry8U516.jpg"
                }]
            }]
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("完善房产信息-1049接口:",rebody)

def wanshangerenxinxi(): #完善个人信息-1049
    interfaceNo = 1049
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33",
            "cardId": cardId,
            "position": "301002007",
            "interfaceNo": "1049",
            "consultId": consultId,
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "custmerManger": "11049136",#客户经理 田世豪
            "busiCode": "CSB49",
            "sysSource": "1",
            "custName": custName,
            "telephone": mobile,
            "intoDetailType": "lbTIntoInfoCustomer",
            "frontTransTime": "2018-10-12 19:48:03",
            #个人信息
            "lbTIntoInfoCustomer": [{
                "jAddr": "银河SOHO",
                "jAddrAreacode": "110101",
                "jEnterT": "2018-10-13",
                "jName": "捷越联合",
                "jPhone": "12345678",
                "loanPurpose": "3",
                "jPhoneAreaCode": "010"
            }]
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("完善个人信息-1049接口:",rebody)

def wanshanlianxirenxinxi(): #完善联系人信息-1049
    interfaceNo = 1049
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        conPhoneA = createPhone()
        conPhoneB = createPhone()
        BodyData = {
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33",
            "cardId": cardId,
            "position": "301002007",
            "interfaceNo": "1049",
            "consultId": consultId,
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "custmerManger": "11049136",#客户经理 田世豪
            "busiCode": "CSB49",
            "sysSource": "1",
            "custName": custName,
            "telephone": mobile,
            "intoDetailType": "lbTIntoInfoContact",
            "frontTransTime": "2018-10-12 19:48:03",
            #联系人信息
            "lbTIntoInfoContact": [{
                "conName": "联系人一",
                "conPhone": conPhoneA,
                "conRelation": "10",
                "contactType": "3"
            }, {
                "conName": "联系人二",
                "conPhone": conPhoneB,
                "conRelation": "6",
                "contactType": "3"
            }]
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("完善联系人信息-1049接口:",rebody)

def wanshanyinhangkaxinxi(): #完善银行卡信息-1049
    interfaceNo = 1049
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "cardId": cardId,
	        "position": "301002007",
	        "interfaceNo": "1049",
            "consultId": consultId,
            "frontTransNo": "20181013141732684",
            "custmerManger": "11049136",
            "busiCode": "CSB49",
            "lbtIntoInfoBankCard": [{
                "accountName": custName,
                "bankCardAccount": bankCardNo,
                "bankCode": "105",
                "bankReservedPhone": mobile
            }],
            "sysSource": "1",
            "custName": custName,
            "telephone": mobile,
            "intoDetailType": "lbTIntoInfoBankCard",
            "frontTransTime": "2018-10-13 14:17:32"
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("完善银行卡信息-1049接口:",rebody)

def kehuxinxichaxun(): #客户信息查询-1034
    interfaceNo = 1034
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "interfaceNo": "1034",
            "telephone": mobile,
            "frontTransTime": "2018-10-13 16:56:57",
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33",
            "busiCode": "CSB34",
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "sysSource": "1"

        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("客户信息查询-1034接口:",rebody)

def shifoufuzhujinjian(): #是否辅助进件接口-1117
    interfaceNo = 1117
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "interfaceNo": "1117",
            "consultId": consultId,
            "telephone": mobile,
            "frontTransTime": "2018-10-13 16:56:57",
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33",
            "busiCode": "CSB117",
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "sysSource": "4",
            "isAssistInto": "0"

        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("是否辅助进件-1117接口:",rebody)

def tijiaoziliaozixunxinxi(): #提交资料咨询信息-1058
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        consultId = getExcelData("consultId", pid, "1118")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "interfaceNo": "1058",
            "frontTransTime": "2018-10-13 16:56:57",
            "transNo": "1901730089%d" % random.randint(00000000, 99999999),
            "transTime": "2019-01-07 16:49:33",
            "busiCode": "CSB58",
            "sysSource": "1",
            "frontTransNo": "1024",
            "telephone": mobile,
            "custName": custName,
            "cardId": cardId,
            "consultId": consultId
        }
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("提交资料咨询信息-1058接口:",rebody)
        # 连接数据库进行判断
        sql = "SELECT * FROM LB_T_INTO_INFO a where a.loan_name='" + custName + "' and a.loan_bank_account="+bankCardNo
        print(sql)
        result = loanDB(sql)
        for i in range(len(result)):
            intoappid = result[i][1]
            custCode = result[i][2]
            bankCardNo = result[i][19]
            custName = result[i][20]
        # print(custName)
        setExcelData(custCode, "custCode", pid, interfaceNo)
        setExcelData(intoappid, "intoappid", pid, interfaceNo)
        setExcelData(bankCardNo, "bankCardNo", pid, interfaceNo)
        setExcelData(custName, "custName", pid, interfaceNo)
        setExcelData(sql, "查询SQL", pid, interfaceNo)
        setExcelData(result, "SQL结果", pid, interfaceNo)  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果

def Crossqualityinspection():#交叉质检
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        custCode = getExcelData("custCode", pid, "1058")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = '10022298'  # 交叉质检-11036813-苗双伟   10022298-陈少萍-质检
        e = 'Cs654321'
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(loanjc)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()

        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu2']").click() #进件管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 交叉质检']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'queryEachCheckLbTIntoInfo')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoAppId']").clear()  # 清空进件编号查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoAppId']").send_keys(intoappid)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='fkCustCode']").clear()  # 清空客户编号查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='fkCustCode']").send_keys(custCode)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='mainCustomer.custName']").clear()  # 清空客户名称查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='mainCustomer.custName']").send_keys(custName)
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='查询']").click()  # 点击查询
        time.sleep(3)
        driver.find_element_by_xpath("//div[text()='"+custName+"']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[1]/div/div[3]/div[1]/a[1]").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'eachCheckLbTIntoInfo')]"))
        time.sleep(5)
        Select(driver.find_element_by_name("eachCheckResultCode")).select_by_value("10") #质检结果 10：通过20：质检回退30：拒绝
        time.sleep(7)
        driver.find_element_by_xpath("//*[@id='btns']/input").click() #//*[@id="doSubmitInto"]
        time.sleep(2)
        driver.quit() #退出浏览器

def Batchsubstitution():#管理员批量换人
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = 'admin'
        e = 'Cs654321'
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(xinshenjc)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()

        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu9']").click() #系统管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 流程管理']").click()
        time.sleep(3)
        # 引用滚动条
        scoll_root(driver)
        time.sleep(6)
        driver.find_element_by_xpath("//li[text()='监控流程']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'myProcessMonitor')]"))
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'monitorTodo')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='busInfoName']").clear() #清空查询条件 monitorTodo
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='busInfoName']").send_keys(intoappid)
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[text()='信审专员初审']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*//a[text()='批量换人']").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'updateAssignee')]"))
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'sysUserSelect')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("姜海丽")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='userNo']").send_keys("11058541")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="userTableDiv"]/div/div[2]/div/button[1]').click() #点击查询
        time.sleep(2)
        driver.find_element_by_xpath("//div[text()='有效']").click() #选择
        time.sleep(2)
        driver.find_element_by_xpath("//*//a[text()='确认']").click()#点击确认
        time.sleep(2)
        #点击页面弹窗
        driver.switch_to_alert().accept() #您确定要转移待办任务吗？ 点击确定
        time.sleep(2)
        driver.switch_to_alert().accept() #操作成功 点击确定
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.quit()

def Approvalofincomingpartsbudai():#进件审批--不带带调查表
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = '11058541'
        e = 'Cs654321'
        # driver = webdriver.Chrome()
        # driver = webdriver.Chrome(executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(xinshenjc)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()

        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu3']").click() #信审管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 工作件审批']").click()
        time.sleep(2)
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toApprovalWrokFile')]")) #进入审批iframe
        time.sleep(2)
        #driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'monitorTodo')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoId']").clear() #清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoId']").send_keys(intoappid)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").send_keys(custName)
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(3)
        driver.find_element_by_link_text(intoappid).click()  # 点击进件编号超链接
        time.sleep(2)
        #弹出超链接页面
        time.sleep(5)
        time.sleep(2)
        # 获取当前窗口handle name
        current_window = driver.current_window_handle
        # 获取所有窗口handle name
        all_windows = driver.window_handles
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            # 新打开的window不等于当前window时
            if window != current_window:
                # 则打开新的window
                driver.switch_to.window(window)
        #进入调查表tab
        '''
        driver.find_element_by_xpath("//a[text()='调查表']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toQueryPage')]"))  # 进入调查表iframe
        time.sleep(2)
        driver.find_element_by_link_text("电联").click()
        time.sleep(2)
        driver.switch_to.default_content() #退出调查表iframe
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='保存']").click()
        driver.find_element_by_xpath("//span[text()='关闭']").click()
        time.sleep(2)
        '''

        ###点击信审表
        driver.find_element_by_xpath("//a[text()='信审表']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'creditAuditView')]"))  # 进入信审表iframe
        time.sleep(2)
        Select(driver.find_element_by_name("workMode")).select_by_value("06") #工作方式：02自雇人士 03公务员04事业编制05国企员工06其他企业员工07退休
        time.sleep(2)
        #Select(driver.find_element_by_name("companyType")).select_by_value("3") #单位性质：1机关及事业单位2国营3民营4三资企业 companyIndustry //*[@id="currentCompanyWorkYear"]
        #time.sleep(2)
        #Select(driver.find_element_by_name("companyIndustry")).select_by_value("C40") #单位所属行业：C40教育、科研、设计机构-普通中学、一般民办教学机构
        time.sleep(2)
        #Select(driver.find_element_by_name("maritalStatus")).select_by_value("1") #婚姻状况：1未婚2已婚3离异4丧偶
        #time.sleep(2)
        #Select(driver.find_element_by_name("childHas")).select_by_value("0")  # 是否有子女：0否1是
        #time.sleep(2)
        #Select(driver.find_element_by_name("houseHas")).select_by_value("0")  # 名下是否有房产：0否1是
        #driver.find_element_by_xpath("//*[@id='companyIndustryTd']/span/input").click()
        driver.find_element_by_xpath("//*[@id='companyIndustryTd']/span/input").clear()  # 清空单位所属行业输入数据
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='companyIndustryTd']/span/input").send_keys("高新技术制造业-软件开发")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='currentCompanyWorkYear']").clear()  # 清空输入数据
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='currentCompanyWorkYear']").send_keys("2")  # 本公司工作年限
        time.sleep(2)
        driver.switch_to.default_content()#退出信审表
        time.sleep(5)
        driver.find_element_by_id("creditAuditSaveBtn").click()#点击保存按钮
        time.sleep(1)
        driver.find_element_by_xpath("//a[text()='关闭']").click()
        time.sleep(5)
        ####点击审核意见
        driver.find_element_by_xpath("//a[text()='审核意见']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'updateLbTIntoAuditResult')]"))  # 进入审核意见iframe
        time.sleep(2)
        Select(driver.find_element_by_name("auditConclusion")).select_by_value("3100") #审批结论：3100同意3200有条件同意3300审核拒绝
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='addNewsTableId']/tbody/tr[5]/td[1]/span/input").clear()
        driver.find_element_by_xpath("//*[@id='addNewsTableId']/tbody/tr[5]/td[1]/span/input").send_keys("A101") #通过代码
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='auditAmount']").clear()
        driver.find_element_by_xpath("//input[@name='auditAmount']").send_keys("100000") #审批额度
        time.sleep(2)
        #driver.find_element_by_xpath("//input[@name='checkIncome']").clear()
        #driver.find_element_by_xpath("//input[@name='checkIncome']").send_keys("50000")  # 核实收入 dtoauthorizedAccordin
        # 控制拉动滚动条，可见负债率，内部负债率
        # 定位授信依据，定位到元素的源位置
        appr = driver.find_element_by_id("dtoagreeCondition")
        # 将鼠标移动到定位的元素上面
        ActionChains(driver).move_to_element(appr).perform()
        # 任意点一个文本框，跳出核实收入，回显负债率，内部负债率 //*[@id="jyMessage0210230455_close"]
        driver.find_element_by_id("dtoagreeCondition").click()
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(3)
        driver.find_element_by_id("intoAuditSaveBtn").click()
        #点“保存”按钮
        '''
        while 1:
            start = time.clock()
            try:
                driver.find_element_by_id("//*[@id='divSubBtnId']/input[12]").click()
                print("已定位到元素!input[@type='button'][@value='保存']")
                end = time.clock()
                break
            except Exception as err:
                print(err)
        print('定位耗费时间：' + str(end - start))
        '''
        # 点击“提交”按钮
        driver.find_element_by_xpath("//*[@id='divSubBtnId']/input[2]").click()
        time.sleep(4)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'querySelectPartner')]")) #进入选择下一环节参与者
        time.sleep(4)
        driver.find_element_by_xpath("//input[@name='parUserNo']").clear()  # 清空输入数据
        time.sleep(4)
        driver.find_element_by_xpath("//input[@name='parUserNo']").send_keys("10035704")  #输入用户编号
        time.sleep(4)
        driver.find_element_by_xpath("//input[@name='parRealName']").clear()  # 清空输入数据
        time.sleep(4)
        driver.find_element_by_xpath("//input[@name='parRealName']").send_keys("万里娜")  # 输入用户编号
        time.sleep(4)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[text()='万里娜']").click()
        time.sleep(6)
        driver.find_element_by_xpath("//*//a[text()='确认']").click()  # 点击确认
        time.sleep(2)
        driver.switch_to.default_content() #退出选择下一环节参与者iframe
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[11]/div[3]/div/button[1]/span").click()  # 点击确认
        driver.quit()

def Examinationandapprovalofincomingparts():#进件审批复核
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = '10035704'
        e = 'Cs654321'

        chromeOpitons = Options()
        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }
        chromeOpitons.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)

        driver.get(xinshenjc)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()

        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu3']").click() #信审管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 工作件审批']").click()
        time.sleep(2)
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toApprovalWrokFile')]")) #进入审批iframe
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoId']").clear() #清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoId']").send_keys(intoappid)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").send_keys(custName)
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(3)
        driver.find_element_by_link_text(intoappid).click()  # 点击进件编号超链接
        time.sleep(5)
        # 获取当前窗口handle name
        current_window = driver.current_window_handle
        # 获取所有窗口handle name
        all_windows = driver.window_handles
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            # 新打开的window不等于当前window时
            if window != current_window:
                # 则打开新的window
                driver.switch_to.window(window)
        ####点击审核意见
        driver.find_element_by_xpath("//a[text()='审核意见']").click()
        time.sleep(2)
        driver.switch_to_frame(
            driver.find_element_by_xpath("//iframe[contains(@src,'updateLbTIntoAuditResult')]"))  # 进入审核意见iframe
        time.sleep(2)
        Select(driver.find_element_by_name("auditConclusion")).select_by_value("3100")  # 审批结论：3100同意3200有条件同意3300审核拒绝
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='addNewsTableId']/tbody/tr[5]/td[1]/span/input").clear()
        driver.find_element_by_xpath("//*[@id='addNewsTableId']/tbody/tr[5]/td[1]/span/input").send_keys("A101")  # 通过代码
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='auditAmount']").clear()
        driver.find_element_by_xpath("//input[@name='auditAmount']").send_keys("100000")  # 审批额度
        time.sleep(2)
        # 控制拉动滚动条，可见负债率，内部负债率
        # 定位授信依据，定位到元素的源位置
        appr = driver.find_element_by_id("dtoagreeCondition")
        # 将鼠标移动到定位的元素上面
        ActionChains(driver).move_to_element(appr).perform()
        # 任意点一个文本框，跳出核实收入，回显负债率，内部负债率 //*[@id="jyMessage0210230455_close"]
        driver.find_element_by_id("dtoagreeCondition").click()
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(3)
        driver.find_element_by_id("intoAuditSaveBtn").click()
        time.sleep(2)
        driver.switch_to.default_content()  # 退出审核意见
        # 点击“提交”按钮
        driver.find_element_by_xpath("//*[@id='divSubBtnId']/input[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]/span").click()  # 点击确认 /html/body/div[10]/div[3]/div/button[1]/span
        driver.quit()

def zhuguanfuhe():#进件审批复核-复核
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = '10001363'
        e = 'Cs654321'

        chromeOpitons = Options()
        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }
        chromeOpitons.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(xinshenjc)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()

        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu3']").click() #信审管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 工作件审批']").click()
        time.sleep(2)
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toApprovalWrokFile')]")) #进入审批iframe
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoId']").clear() #清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoId']").send_keys(intoappid)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").send_keys(custName)
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(3)
        driver.find_element_by_link_text(intoappid).click()  # 点击进件编号超链接
        time.sleep(5)
        # 获取当前窗口handle name
        current_window = driver.current_window_handle
        # 获取所有窗口handle name
        all_windows = driver.window_handles
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            # 新打开的window不等于当前window时
            if window != current_window:
                # 则打开新的window
                driver.switch_to.window(window)
        ####点击审核意见
        driver.find_element_by_xpath("//a[text()='审核意见']").click()
        time.sleep(2)
        driver.switch_to_frame(
            driver.find_element_by_xpath("//iframe[contains(@src,'updateLbTIntoAuditResult')]"))  # 进入审核意见iframe
        time.sleep(2)
        Select(driver.find_element_by_name("auditConclusion")).select_by_value("3100")  # 审批结论：3100同意3200有条件同意3300审核拒绝
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='addNewsTableId']/tbody/tr[5]/td[1]/span/input").clear()
        driver.find_element_by_xpath("//*[@id='addNewsTableId']/tbody/tr[5]/td[1]/span/input").send_keys("A101")  # 通过代码
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='auditAmount']").clear()
        driver.find_element_by_xpath("//input[@name='auditAmount']").send_keys("100000")  # 审批额度
        # 控制拉动滚动条，可见负债率，内部负债率
        # 定位授信依据，定位到元素的源位置
        appr = driver.find_element_by_id("dtoinnerReviews")
        # 将鼠标移动到定位的元素上面
        ActionChains(driver).move_to_element(appr).perform()
        # 任意点一个文本框，跳出核实收入，回显负债率，内部负债率
        driver.find_element_by_id("dtoinnerReviews").click()
        time.sleep(3)
        '''
        # 引用滚动条
        scoll_root(driver)
        time.sleep(5)
        # 点“保存”按钮
        while 1:
            start = time.clock()
            try:
                driver.find_element_by_xpath("//*[@id='saveBtn']").click()
                print("已定位到元素!input[@type='button'][@value='保存']")
                end = time.clock()
                break
            except Exception as err:
                print(err)
        print('定位耗费时间：' + str(end - start))
        '''
        # 退出“审核意见”的iframe
        time.sleep(5)
        driver.switch_to.default_content()  # 退出审核意见
        # 点击“提交”按钮
        driver.find_element_by_xpath("//*[@id='divSubBtnId']/input[1]").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()  # 点击确认 /html/body/div[9]/div[3]/div/button[1]/span
        driver.quit()


def Contractmanagementsc():  # 签约管理-生成合同
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格 getExcelNrows(interfaceNo)
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = 'admin'
        e = 'Cs654321'
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(loanjc)

        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu7']").click()  # 签约管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 签约管理']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toQueryPage')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='cardId']").clear()  # 清空查询条件
        # time.sleep(2)
        driver.find_element_by_xpath("//input[@name='cardId']").send_keys(cardId)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").send_keys(custName)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoAppId']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoAppId']").send_keys(intoappid)
        time.sleep(3)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[text()='" + custName + "']").click()  # 选中客户名称
        time.sleep(2)
        driver.find_element_by_xpath("//*//a[text()='生成合同']").click()
        time.sleep(2)
        # 输入预约放款日期
        driver.find_element_by_xpath("//input[@id='dtoplanLoansDate']").click()  # 点击预约放款日期输入框
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@src='about:blank']"))  # 进入日期控件iframe
        time.sleep(3)
        driver.find_element_by_xpath("//input[@id='dpTodayInput']").click()  # 点击确定
        time.sleep(2)
        driver.switch_to.default_content()  # 退出日期控件
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toQueryPage')]"))
        time.sleep(2)
        s1 = Select(driver.find_element_by_xpath("//select[@name='loanBank']"))  # 实例化Select
        s1.select_by_value("105")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='loanSubBranchName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='loanSubBranchName']").send_keys("天津市和平分行")
        time.sleep(2)
        Select(driver.find_element_by_name("loanBankProvAreacode")).select_by_value("120000")  # 天津市

        Select(driver.find_element_by_name("loanBankCityAreacode")).select_by_value("120100")  # 天津市
        time.sleep(5)
        # 点“保存”按钮
        while 1:
            start = time.clock()
            try:
                driver.find_element_by_xpath("//span[text()='保存']").click()
                print("已定位到元素!//span[text()='保存']")
                end = time.clock()
                break
            except Exception as err:
                print(err)
        print('定位耗费时间：' + str(end - start))

        time.sleep(10)
        driver.find_element_by_xpath("//div[text()='" + custName + "']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*//a[text()='合同下载']").click()
        time.sleep(3)
        # 点“手机电子签章”按钮
        while 1:
            start = time.clock()
            try:
                driver.find_element_by_xpath("//span[text()='手机电子签章']").click()
                print("已定位到元素!//span[text()='手机电子签章']")
                end = time.clock()
                break
            except Exception as err:
                print(err)
        print('定位耗费时间：' + str(end - start))
        time.sleep(2)
        driver.quit()

def Contractenquiry(): #合同查询并插入再互保信息
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        custCode = getExcelData("custCode", pid, "1058")  # 读取Excel列数
        contract_no = getExcelData("contract_no", pid, "1058")  # 读取Excel列数
        # 连接数据库进行判断
        sql = "select * from lb_t_contract_info  a where a.fk_cust_id='"+custCode+"'"
        result = loanDB(sql)
        for i in range(len(result)):
            contract_no = result[i][1]
            print(contract_no)
        print("查询合同信息：" + str(result))  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果 #'"+contract_no+"'
        setExcelData(sql, "查询SQL", pid, interfaceNo)
        setExcelData(result, "SQL结果", pid, interfaceNo)  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        setExcelData(contract_no, "contract_no", pid, interfaceNo)
        sql2 = "insert into lb_t_insurance_order (id,order_code,order_relation_code,contract_no,start_time,end_time,amount,premium,order_status,order_rate,signingdate,insurance_company,remark,validate_state,create_by,create_time,modify_by,modify_time)values(seq_LB_T_INSURANCE_ORDER.nextval,'" + contract_no + "','" + contract_no + "','" + contract_no + "',sysdate,sysdate+100,5000.00,80.00,'1',0.01,sysdate,'再互保','','1',1,sysdate,1,sysdate)"
        result = loanDBXG(sql2)
        print("插入数据：" + str(result))  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果

def Openingcard():#存管开户信息-1105接口
    interfaceNo = 1105
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "1118")  # 读取Excel列数
        custCode = getExcelData("custCode", pid, "1058")  # 读取Excel列数
        BodyData = {
            "bankCode": "105",
            "certType": "1",
            "serialNumber": "201801830089%d"%random.randint(00000000,99999999),
            "bankCardNo": bankCardNo,
            "frontTransNo": "201801830089%d"%random.randint(00000000,99999999),
            "sysSource": "4",
            "busiCode": "CSB105",
            "bankCardType": "10",
            "bankName": "建设银行",
            "certId": cardId,
            "custName": custName,
            "custCode": custCode,
            "checkFlag": "1",
            "callPageUrl": "http://172.18.100.46:8080/fintech-appbiz/deposit/appOpenDepositoryBankCallback",
            "interfaceNo": "1105",
            "depositCode": "02",
            "phone": mobile,
            "custType": "0",
            "isAppFlg": "1",
            "frontTransTime": "2019-01-1 14:53:56",
            "subsidiaryCode": "JYJF",
            "acctPhone": mobile
        }
        print(BodyData)
        rebody = loansever(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
        print("存管开户信息-1105接口:", rebody)
        htmlContext = rebody["responseBody"]["returnMsg"] #读取返回报文htmlContext值
        fh = open("htmlContext%d.html"%pid, "w",encoding="utf-8")
        fh.write(htmlContext)
        fh.close()


        driver = webdriver.Chrome(executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        url = 'file:///' + os.path.abspath("htmlContext%d.html"%pid)
        url2 = url.replace('\\', '/')
        driver.get(url2)
        time.sleep(2)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='sendSmsVerify']").click() #发送短信验证码
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='alertLayer-2']/div[2]/a").click()
        driver.find_element_by_xpath("//*[@id='smsCode']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("q1111111")
        driver.find_element_by_xpath("//*[@id='confirmPassword']").send_keys("q1111111")
        driver.find_element_by_xpath("//*[@id='nextButton']").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id='nextBtn']").click()  #//*[@id="nextBtn"] //*[@id="nextBtn"] //*[@id="sendSmsVerify"]
        time.sleep(3)
        driver.quit()

        # setExcelData(rebody, "返回报文", pid, interfaceNo)
        #对接口返回结果进行判断	尝试对非以下结果抛异常
        res = rebody["responseBody"]["retCode"]
        if res == "0000":
            setExcelData("pass", "测试结果", pid, interfaceNo)
        elif res == "0001":
            setExcelData("fail", "测试结果", pid, interfaceNo)
        elif res == "9999":
            setExcelData("day_of_end", "测试结果", pid)
            print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
            break
        #连接数据库进行判断
        sql = "select * from  t_c_at_account tb where tb.master_id='"+custCode+"'"
        result =coreDB(sql)
        for i in range(len(result)):
            account = result[i][3]
            print(account)
        print("存管开户信息-查询："+str(result))	#获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        setExcelData(sql, "查询SQL", pid, interfaceNo)
        setExcelData(result, "SQL结果", pid, interfaceNo)  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        setExcelData(BodyData, "请求报文", pid, interfaceNo)
        setExcelData(rebody, "返回报文", pid, interfaceNo)
        setExcelData(account, "account", pid, interfaceNo)

def hefengweituotixianshouquan():#恒丰委托提现授权-1114
    interfaceNo = 1114
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        contract_No = getExcelData("contract_No", pid, "1058")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        BodyData = {
            "serialNumber": "201801830089%d"%random.randint(00000000,99999999),
            "callPageUrl": "http://172.18.100.46:8080/fintech-appbiz/deposit/appEntrustmentAgreementback",
            "interfaceNo": "1114",
            "depositCode": "02",
            "frontTransNo": "201801830089%d"%random.randint(00000000,99999999),
            "sysSource": "4",
            "contractNo": contract_No,
            "busiCode": "CSB114",
            "cardId": cardId,
            "cardType": "1",
            "frontTransTime": "2019-01-14 14:54:34",
            "subsidiaryCode": "JYJF",
            "mobile": mobile
        }
        print(BodyData)
        rebody = loansever(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
        print("恒丰委托提现授权-1114接口:", rebody)
        htmlContext = rebody["responseBody"]["returnMsg"] #读取返回报文htmlContext值
        fh = open("htmlContext%d.html"%pid, "w",encoding="utf-8")
        fh.write(htmlContext)
        fh.close()


        driver = webdriver.Chrome(executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        url = 'file:///' + os.path.abspath("htmlContext%d.html"%pid)
        url2 = url.replace('\\', '/')
        driver.get(url2)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='password']").send_keys("q1111111")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='nextButton']").click()
        time.sleep(5)
        driver.quit()
        #对接口返回结果进行判断	尝试对非以下结果抛异常
        res = rebody["responseBody"]["retCode"]
        if res == "0000":
            setExcelData("pass", "测试结果", pid, interfaceNo)
        elif res == "0001":
            setExcelData("fail", "测试结果", pid, interfaceNo)
        elif res == "9999":
            setExcelData("day_of_end", "测试结果", pid)
            print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
            break
def xieyizhifuyinhangkabangding():#协议支付银行卡绑定-1113
    interfaceNo = 1113
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        BodyData = {
            "serialNumber": "201801830089%d"%random.randint(00000000,99999999),
            "bankCardNo": bankCardNo,
            "frontTransNo": "201801830089%d"%random.randint(00000000,99999999),
            "sysSource": "4",
            "busiCode": "CSB113",
            "cardType": "10",
            "custName": custName,
            "acctCardId": cardId,
            "acctPhone": mobile,
            "checkFlag": "1",
            "clientSource": "LOAN001",
            "bankId": "105",
            "callPageUrl": "http://172.18.100.46:8080/fintech-appbiz/deposit/appAgreementPaymentback",
            "interfaceNo": "1113",
            "depositCode": "02",
            "acctCardType": "1",
            "isAppFlg": "1",
            "frontTransTime": "2019-01-14 14:54:52",
            "subsidiaryCode": "JYJF"
        }
        print(BodyData)
        rebody = loansever(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
        print("协议支付银行卡绑定-1113接口:", rebody)
        htmlContext = rebody["responseBody"]["returnMsg"] #读取返回报文htmlContext值
        fh = open("htmlContext%d.html"%pid, "w",encoding="utf-8")
        fh.write(htmlContext)
        fh.close()


        driver = webdriver.Chrome(executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        url = 'file:///' + os.path.abspath("htmlContext%d.html"%pid)
        url2 = url.replace('\\', '/')
        driver.get(url2)
        time.sleep(5)
        driver.find_element_by_id("sendBtn").click() #点击获取验证码
        driver.find_element_by_xpath("//*[@id='smsSeq']").send_keys("112233") #输入验证码
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/button/span").click()  # 点击关闭
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='nextBtn']").click() #点击提交
        time.sleep(5)
        driver.quit()
        #对接口返回结果进行判断	尝试对非以下结果抛异常
        res = rebody["responseBody"]["retCode"]
        if res == "0000":
            setExcelData("pass", "测试结果", pid, interfaceNo)
        elif res == "0001":
            setExcelData("fail", "测试结果", pid, interfaceNo)
        elif res == "9999":
            setExcelData("day_of_end", "测试结果", pid)
            print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
            break

def daiqianyuehetongliebiao(): #待签约合同列表-1056
    interfaceNo = 1056
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        contract_no = getExcelData("contract_no", pid, "1058")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "interfaceNo": "1056",
            "frontTransNo": "201801830089%d"%random.randint(00000000,99999999),
            "sysSource": "4",
            "contractNo": contract_no,
            "busiCode": "CSB56",
            "cardId": cardId,
            "telephone": mobile,
            "templateCode": "020021,020008",
            "custName": custName,
            "frontTransTime": "2019-01-14 14:55:19"
        }
        print("待签约合同列表-1056接口:",BodyData)
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("待签约合同列表-1056接口:", rebody)



def shoujidianziqianzhang(): #合同电子签约
    interfaceNo = 1057
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        contract_no = getExcelData("contract_no", pid, "1058")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "1118")  # 读取Excel列数
        BodyData = {
            "frontTransNo": "1901730089%d" % random.randint(00000000, 99999999),
            "sysSource": "4",
            "busiCode": "CSB57",
            "telephone": mobile,
            "templateCode": "020024,020021,020020,020019,020011,020008,020007,020006,020005,020004,020003,020002,020001",
            "custName": custName,
            "type": "1",#签约类型1：签章 2 ：作废签章 3： 放款后签章
            "interfaceNo": "1057",
            "cardId": cardId,
            "contractId": contract_no,
            "signType": "01", #签约方式01电子02手写
            "state": "01", #手机操作类型 0-手机确认
            "intoDevice ": "4",#进件渠道
            "frontTransTime": "2019-01-14 14:55:50"

        }
        print("合同电子签约-1057请求接口:",BodyData)
        rebody = loansever(interfaceNo, BodyData)  # getInterfaceResloansever 取请求报文
        print("合同电子签约-1057返回接口:", rebody)



def Contractmanagementtj():  # 签约管理-提交
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格 getExcelNrows(interfaceNo)
        cardId = getExcelData("cardId", pid, "1118")  # 读取Excel列数
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = 'admin'
        e = 'Cs654321'
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(loanjc)

        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()
        time.sleep(2)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu7']").click()  # 签约管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 签约管理']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toQueryPage')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='cardId']").clear()  # 清空查询条件
        # time.sleep(2)
        driver.find_element_by_xpath("//input[@name='cardId']").send_keys(cardId)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").send_keys(custName)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoAppId']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='intoAppId']").send_keys(intoappid)
        time.sleep(3)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[text()='" + custName + "']").click()  # 选中客户名称 //*[@id="custName_120154629729"]/div
        time.sleep(2)
        driver.find_element_by_xpath("//*//a[text()='提交审核']").click()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toAdd')]"))
        time.sleep(2)
        Select(driver.find_element_by_name("passReason")).select_by_value("1")  # 通过原因 1正常通过 2客户差异化
        driver.switch_to.default_content()
        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toQueryPage')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]/span[text()='保存']").click()
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]/span").click()  #点击确认/html/body/div[10]/div[3]/div/button[1]/span
        time.sleep(2)
        driver.quit()

def ContractReview():  # 合同管理
    interfaceNo = 1058
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格 getExcelNrows(interfaceNo)
        custName = getExcelData("custName", pid, "1118")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "1058")  # 读取Excel列数
        d = 'admin'
        e = 'Cs654321'
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(loanjc)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys(d)
        driver.find_element_by_id("pwd").send_keys(e)
        driver.find_element_by_class_name("btn").click()

        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='firstMenu8']").click()  # 合同管理 queryEachCheckLbTIntoInfo
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' 合同审核']").click()

        time.sleep(2)
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[contains(@src,'toAudit')]"))
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='baseExt7']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='baseExt7']").send_keys(intoappid)
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").clear()  # 清空查询条件
        time.sleep(2)
        driver.find_element_by_xpath("//input[@name='custName']").send_keys(custName)
        time.sleep(3)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[text()='通过']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='operateContent']").send_keys("同意") #
        time.sleep(2)
        # 点“提交”按钮
        while 1:
            start = time.clock()
            try:
                driver.find_element_by_xpath("//span[text()='提交']").click()
                print("已定位到元素!//span[text()='提交']")
                end = time.clock()
                break
            except Exception as err:
                print(err)
        print('定位耗费时间：' + str(end - start))
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]/span").click() #点击确认 /html/body/div[10]/div[3]/div/button[1]/span
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/button/span").click()  # 点击关闭
        time.sleep(2)
        driver.quit()

def jieyuejinjianjiekou():#借悦进件接口
    Incominginformation()  # 进件信息
    jineqixian()  # 金额期限申请1118
    certification()  # 实名认证1037
    dianziqianzhang()  # 实名认证中3个电子签章-1084
    huotirenzhengdengji()  # 活体认证登记接口-1038
    wanshangerenxinxi() #完善个人信息1049
    wanshanlianxirenxinxi()#完善联系人信息1049
    wanshanyinhangkaxinxi()#完善银行卡信息1049
    wanshanfangchanxinxi()#完善房产信息1049
    kehuxinxichaxun() #客户信息查询-1034
    shifoufuzhujinjian() #是否辅助进件-1117接口
    tijiaoziliaozixunxinxi()#提交资料咨询信息-1058

def jieyuedianziqianzhang():#借悦开户及电子签章接口
    Openingcard() #存管开户信息-1105接口
    hefengweituotixianshouquan() #恒丰委托提现授权-1114
    xieyizhifuyinhangkabangding() #协议支付银行卡绑定-1113
    daiqianyuehetongliebiao() #待签约合同列表-1056
    shoujidianziqianzhang() #手机电子签章-1057

# jieyuejinjianjiekou() #借悦进件接口
Crossqualityinspection() #交叉质检-苗双伟
# Batchsubstitution() #管理员批量换人
#Approvalofincomingpartsbudai() #进件审批--不带调查表
#Examinationandapprovalofincomingparts() #进件审批复核
#zhuguanfuhe() #信审审批-主管复核
#Contractmanagementsc() # 签约管理-生成合同
#Contractenquiry() #合同查询并插入再互保信息
#jieyuedianziqianzhang() #借悦开户及电子签章接口
#Contractmanagementtj() # 签约管理-提交
#ContractReview() # 合同管理




