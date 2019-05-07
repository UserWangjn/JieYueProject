# -*- coding:utf-8 -*-
#如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。
from selenium import webdriver
import os
import time
import random	#random 提供了生成随机数的工具
from Com.util import getSQLResult, getExcelData, setExcelData, getInterfaceResloanjc05, getExcelNrows,getSQLResulthxjc05 #GGFF.py
def Openingcard():
    interfaceNo = 2118
    for pid in range(1, getExcelNrows(interfaceNo)): #读取Excel表格
        mobile = getExcelData("mobile", pid, "20181216")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "20181216")  # 读取Excel列数
        custName = getExcelData("custName", pid, "20181216")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "20181216")  # 读取Excel列数
        custCode = getExcelData("custCode", pid, "20181216")  # 读取Excel列数
        intoappid = getExcelData("intoappid", pid, "20181216")  # 读取Excel列数
        BodyData = {
            "bankCardNo": bankCardNo,
            "bankCardType": "10", #银行卡类型 10-个人借记 20-个人贷记
            "bankCode": "105",
            "busiCode": "LBB118", #业务编码
            "callPageUrl": "http://172.18.100.39:8081/fintech-appbiz/deposit/appCashRecordCallback",
            "certId": cardId,
            "certType": "1",
            "checkFlag": "0",
            "custCode": custCode,
            "custName": custName,
            "custType": "0",
            "depositCode": "02", #存管渠道 00-非存管01-华瑞（存管）02-恒丰（存管）03-向上（存管）
            "frontTransNo": "201801830089%d"%random.randint(00000000,99999999),
            "frontTransTime": "2018-09-01 10:51:00",
            "interfaceNo": "2118",
            "isAppFlg": "0",
            "phone": mobile,
            "serialNumber": "201801830089%d"%random.randint(00000000,99999999),
            "subsidiaryCode": "JYJF",#开户主体
            "sysSource": "2"
        }
        print(BodyData)
        rebody = getInterfaceResloanjc05(interfaceNo, BodyData)	#getInterfaceRes 取请求报文
        print(rebody)
        htmlContext = rebody["responseBody"]["returnMsg"] #读取返回报文htmlContext值
        print(rebody)
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
        result =getSQLResulthxjc05(sql)
        for i in range(len(result)):
            account = result[i][3]
            print(account)
        print("借款人开户绑卡2118接口："+str(result))	#获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        setExcelData(sql, "查询SQL", pid, interfaceNo)
        setExcelData(result, "SQL结果", pid, interfaceNo)  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果
        setExcelData(BodyData, "请求报文", pid, interfaceNo)
        setExcelData(rebody, "返回报文", pid, interfaceNo)
        setExcelData(account, "account", pid, interfaceNo)
#Openingcard()