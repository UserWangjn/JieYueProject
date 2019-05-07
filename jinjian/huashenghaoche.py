# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
import datetime
import random
import random as r
import cx_Oracle    #cx_Oracle
import json
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
from Com.util import getSQLResulthxjc05,getSQLResultloanxgjc05,getSQLResultloanjc05,getInterfaceResloanseverjc05, getExcelData, setExcelData, createPhone,name,idcard, getExcelNrows,scoll_root,hshcintoappcode,getSQLResult
from Com.Openingcard import Openingcard
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

hshc="http://test-partner.huashenghaoche.com/hshcpartner/swagger-ui.html#!/partner45http45controller/reqeustByHttpUsingPOST"
loanjc="http://dkjc2.jieyuechina.com/loan/user/home"
xinshenjc="http://fintechjc2.jieyuechina.com/loan-credit"
#coreDB=getSQLResulthxjc02
#loanDBXG=getSQLResultloanxgjc02
#loanDB=getSQLResultloanjc02
#loansever=getInterfaceResloanseverjc02

def scoll_root(driver):
    # 把滚动条拉到底部
    js = "var q=document.body.scrollTop=100000"
    return driver.execute_script(js)

def Incominginformation():#进件信息
    interfaceNo = 12345
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        mobile = createPhone()
        cardId = gennerator()
        custName = name()
        bankCardNo = idcard()
        hsintoappcode = hshcintoappcode()
        setExcelData(cardId, "cardId", pid, interfaceNo) #写入Excel
        setExcelData(custName, "custName", pid, interfaceNo)
        setExcelData(mobile, "mobile", pid, interfaceNo)
        setExcelData(bankCardNo, "bankCardNo", pid, interfaceNo)
        setExcelData(hsintoappcode, "hsintoappcode", pid, interfaceNo)

def hshcjinjianshenqing():#花生进件申请
    interfaceNo = 12340
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "12345")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "12345")  # 读取Excel列数
        hsintoappcode = getExcelData("hsintoappcode", pid, "12345")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "12345")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "12345")  # 读取Excel列数
        d = '11036813'  # 交叉质检-苗双伟
        e = 'Cs654321'

        BodyData = {
                    "channelType": "0027",
                    "methodName": "createOrderTest",
                    "requestData": {
                        "intoAppCode": hsintoappcode,
                        "custName": custName,
                        "certType": "1",
                        "idNumber": cardId,
                        "phone": mobile,
                        "bankCardId": bankCardNo,
                        "bankName": "建设银行",
                        "bankId": "105",
                        "branchBankName": "中国建设银行北京分行",
                        "applyAmt": 100000,
                        "productName": "畅易行A",
                        "productCode": "PTL190100134",
                        "term": 24,
                        "loanMonthRate": 0.83,
                        "hspl": "测试",
                        "hshcAduitResult": "测试",
                        "email": "123@123.com"
                    },
                    "sign": ""
                }
        BodyData = json.dumps(BodyData,ensure_ascii=False)
        #ad = '{"channelType": "0027", "methodName": "createOrderTest","requestData": {"intoAppCode": hsintoappcode,}}'
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(hshc)
        driver.maximize_window()
        time.sleep(3)
        scoll_root(driver) #引用滚动条
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="partner45http45controller_reqeustByHttpUsingPOST_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(BodyData)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='partner45http45controller_reqeustByHttpUsingPOST_content']/form/div[3]/input").click()
        time.sleep(5)
        driver.quit()

def shagnchuanyxfwq():
    interfaceNo = 12340
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        hsintoappcode = getExcelData("hsintoappcode", pid, "12345")  # 读取Excel列数

        BodyData = {
                "channelType": "0027",
                "methodName": "syncImageFile",
                "requestData": {
                    "intoAppCode": hsintoappcode,
                    "fileList": [{
                            "fileCategory": "B1",
                            "fileName": "2222.png",
                            "fileType": "1"
                        },
                        {
                            "fileCategory": "B9",
                            "fileName": "333.png",
                            "fileType": "1"
                        }, {
                            "fileCategory": "U1",
                            "fileName": "天猫合同.pdf",
                            "fileType": "4"
                        }
                    ]
                }
            }
        BodyData = json.dumps(BodyData, ensure_ascii=False)
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(hshc)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="partner45http45controller_reqeustByHttpUsingPOST_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(
            BodyData) #请求接口
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='partner45http45controller_reqeustByHttpUsingPOST_content']/form/div[3]/input").click() #点击提交
        time.sleep(5)
        driver.quit()

def xiangbanzhengxin():
    interfaceNo = 12340
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        custName = getExcelData("custName", pid, "12345")  # 读取Excel列数
        bankCardNo = getExcelData("bankCardNo", pid, "12345")  # 读取Excel列数
        hsintoappcode = getExcelData("hsintoappcode", pid, "12345")  # 读取Excel列数
        mobile = getExcelData("mobile", pid, "12345")  # 读取Excel列数
        cardId = getExcelData("cardId", pid, "12345")  # 读取Excel列数

        BodyData = {
                  "channelType": "0027",
                  "methodName": "createCreditDetail",
                  "requestData":
                  {
                  "intoAppCode":hsintoappcode,
                  "custName":custName,
                  "idNumber":cardId,
                  "isMarry":"10",
                  "phone":mobile,
                  "compTele":"1111",
                  "houseAddr":"1111",
                  "spouseName":"张琳",
                  "spouseIdNumber":"110101198001010053",
                  "spouseCompany":"1111",
                  "spousePhone":"13315878956",
                  "dkyqbs":"1111",
                  "dkyqyf":"1111",
                  "dkyqdyzgyqze":"1111",
                  "dkyqzcyqys":"1111",
                  "djkyqyqbs":"1111",
                  "djkyqyqyf":"1111",
                  "djkyqyqdyzgyqze":"1111",
                  "djkyqyqzcyqys":"1111",
                  "djkdqyqje":"1111",
                  "djkdqyqzhs":"1111",
                  "dkdqyqje":"1111",
                  "dkdqyqzhs":"1111",
                  "fkfrjgs":"1111",
                  "fkjgs":"1111",
                  "zhs":"1111",
                  "sxze":"1111",
                  "djhzgsxe":"1111",
                  "djhzdsxe":"1111",
                  "yyed":"1111",
                  "zjlgypjsyed":"1111",
                  "ygynjgcxcsdksp":"1111",
                  "ygynjgcxcsxyksp":"1111",
                  "ygyncxcsdksp":"1111",
                  "ygyncxcsxyksp":"1111",
                  "ygyncxcsbrcx":"1111",
                  "lgynjgcxcs":"1111",
                  "companyInfoList":[{
                  "company":"1",
                  "companyAddr":"11122",
                  "infoTime":"20191010012100"}]
                  }
                }
        BodyData = json.dumps(BodyData, ensure_ascii=False)
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(hshc)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="partner45http45controller_reqeustByHttpUsingPOST_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(
            BodyData)  # 请求接口
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='partner45http45controller_reqeustByHttpUsingPOST_content']/form/div[3]/input").click()  # 点击提交
        time.sleep(5)
        driver.quit()

def sanfanshujuluru():
    interfaceNo = 12340
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        hsintoappcode = getExcelData("hsintoappcode", pid, "12345")  # 读取Excel列数

        BodyData = {
              "channelType": "0027",
              "methodName": "dataInput",
              "requestData": {
              "faceRecognitionResult":{
             "recognitionResult":"1"
              },
              "brNaturalPerson":{
             "checkCount2":"0",
             "caseTypeCode":"1010000",
             "item":"1",
             "ztCheckresult":"0",
             "wfxwCheckresult":"0",
             "sdCheckresult":"0",
             "xdCheckresult":"0",
             "caseTime":"[0,0.25)"
              },
              "brMobileThreeElements":{
             "operation":"3",
             "result":"1"
              },
              "brMobileNetTime":{
             "value":"[24,+)"
              },
              "brMobileNetStatus":{
             "value":"1"
              },
              "hfData":{
             "isHit":"0"
              },
              "ficoData":{
             "initContent":"测试"
              },
              "tdCreditData":{
             "riskResult":"0.5",
             "firstContactInThreeMonthNum":"1",
             "multiPlatInOneMonthNum":"0",
             "multiPlatInThreeMonthNum":"1"
              },
              "intoAppCode":hsintoappcode
            },
              "sign": ""
            }
        BodyData = json.dumps(BodyData, ensure_ascii=False)
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(hshc)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="partner45http45controller_reqeustByHttpUsingPOST_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(
            BodyData)  # 请求接口
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='partner45http45controller_reqeustByHttpUsingPOST_content']/form/div[3]/input").click()  # 点击提交
        time.sleep(5)
        driver.quit()

def fangkuantongzhi():
    interfaceNo = 12340
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        hsintoappcode = getExcelData("hsintoappcode", pid, "12345")  # 读取Excel列数

        BodyData = {
                  "channelType": "0027",
                  "methodName": "loanNotice",
                  "requestData": {
                "intoAppCode":"hsintoappcode",
                "loanNotice":"1"
                },
                  "sign": ""
                }
        BodyData = json.dumps(BodyData, ensure_ascii=False)
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(hshc)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="partner45http45controller_reqeustByHttpUsingPOST_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(
            BodyData)  # 请求接口
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='partner45http45controller_reqeustByHttpUsingPOST_content']/form/div[3]/input").click()  # 点击提交
        time.sleep(5)
        driver.quit()

def fuyi():
    interfaceNo = 12340
    for pid in range(1, getExcelNrows(interfaceNo)):  # 读取Excel表格
        hsintoappcode = getExcelData("hsintoappcode", pid, "12345")  # 读取Excel列数

        BodyData = {
                      "channelType": "0027",
                      "methodName": "reconsiderApply",
                      "requestData": {
                      "amount":100000,
                      "term":24,
                    "intoAppCode":"0123456781"
                    },
                      "sign": ""
                    }
        BodyData = json.dumps(BodyData, ensure_ascii=False)
        chromeOpitons = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

        }

        chromeOpitons.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
                                  chrome_options=chromeOpitons)
        driver.get(hshc)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="partner45http45controller_reqeustByHttpUsingPOST_content"]/form/table[1]/tbody/tr/td[2]/textarea').send_keys(
            BodyData)  # 请求接口
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='partner45http45controller_reqeustByHttpUsingPOST_content']/form/div[3]/input").click()  # 点击提交
        time.sleep(5)
        driver.quit()



#Incominginformation()
#hshcjinjianshenqing()
#在影像服务器增加进件文件：172.18.100.31 21 core_test/core_test
shagnchuanyxfwq()
#xiangbanzhengxin()
#sanfanshujuluru()
#执行SQL语句：
#update T_C_MM_HS_THIRD_DATA set init_Content  = '{"sysSource":"S004","frontTransNo":"9ab88580efc5483a8d6fa68397423b28","frontTransTime":"2019-03-01 11:40:08","interfaceNo":"1002","busiCode":"LFB02","hsGlobalId":"012345678","applyInfo":{"appAmount":100000,"appPeriod":"12","loanPrePurpose":"101","loanPurpose":"11","productCode":"hs123456","orgId":"90101","custManager":"90100002","custService":"90100002"},"creRptType":null,"customerInfo":null,"contactList":[{"contactType":"1","conRelation":"父子","conName":"张二","conPhone":"15888888888"}],"jobInfo":{"companyName":"公司名称","companyArea":"北京市","companyAddr":"北京市东城区建国门街道"},"bankCardInfo":{"accountName":"张三","bankCardAccount":"26490137589378271","bankCode":"102","bankProvCityAreacode":"0111/北京市","subBranchName":"中国工商银行北京分行","bankReservedPhone":"13700000001"},"hsCreditInfo":{"conclusion":"测试","comment":"测试"},"attachInfoList":[{"attachType":"C1","attachName":"012345678.jpg","attachUrl":"C:/cust/image/012345678.jpg"}],"credRptSimple":null,"credRptDetail":null,"thirdData":{"faceRecognitionResult":{"recognitionResult":"1"},"brNaturalPerson":{"checkCount2":"0","ztCheckresult":"0","wfxwCheckresult":"0","sdCheckresult":"0","xdCheckresult":"0","item":null,"caseTypeCode":null,"caseTime":"[0,0.25)"},"brMobileThreeElements":{"operation":"3","result":"1"},"brMobileNetTime":{"value":null},"brMobileNetStatus":null,"hfData":{"isHit":"0"},"ficoData":{"initContent":"测试"},"tdCreditData":{"riskResult":"测试","firstContactInThreeMonthNum":null,"multiPlatInOneMonthNum":"0","multiPlatInThreeMonthNum":null}}}'
#fangkuantongzhi()
#fuyi()



