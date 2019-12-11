# codeing = utf-8
from Test.Int_test.util import *
import re
import random
from selenium import webdriver
from time import *

interfaceNo = 2118
for pid in range(1,getExcelNrows('../interface.xls',interfaceNo)):
    #list_num = [0,1,2,3,4,5,6,7,8,9]
    #res = random.sample(list_num,5)
    BodyData = {
        "sysSource": "9",
        "frontTransNo": "2018016515512%d"%random.randint(0,999999),
        "frontTransTime": "2018-01-31 12:00:31",
        "interfaceNo": "2118",
        "busiCode": "LBB118",
        "custCode": "CR18110600000088",
        "custName": "二期数据三",
        "custType": "1",
        "certId": "441426199101176873",
        "phone": "13426239711",
        "sex": "",
        "telephone": "",
        "fax": "",
        "address": "",
        "postalcode": "",
        "email": "",
        "bankCardType": "10",
        "bankCardNo": "6214830%d8932"%bank_num(),
        "bankCode": "105",
        "bankCd": "",
        "bankName": "",
        "acctProv": "",
        "acctCity": "",
        "acctBrchName": "北京三里屯支行",
        "serialNumber": "180102133%s452423"%random.randint(0,999999),
        "callPageUrl": "http://172.18.100.39:8081/fintech-appbiz/deposit/appCashRecordCallback",
        "isAppFlg": "1",
        "depositCode": "02",
        "subsidiaryCode": "JYJF",
        "checkFlag": "0"
    }
    print("pid:%s"%pid)
    setExcelData('../interface.xls',BodyData,"请求报文",pid,interfaceNo)
    print('写入请求报文成功')
    rebody = getInterfaceRes('http://172.18.100.123:8082/core-interface/api/loan/2118/v1',BodyData)
    print("返回报文rebody:%s"%rebody)
    setExcelData('../interface.xls',rebody,"返回报文",pid,interfaceNo)
    print("写入返回报文成功")

    #截取返回报文
    returnMsg = rebody["responseBody"]["returnMsg"]     #获得returnMsg内容
    setExcelData('../interface.xls',returnMsg,"returnMsg",pid,interfaceNo)
    print("returnMsg:%s" % returnMsg)
    rule = r'action=\"(.*?)}'        #截取returnMsg     rule = r'<(.*?)>'
    subList = re.findall(rule,returnMsg)[0]
    print("subList:%s"%subList)
    setExcelData('../interface.xls',subList,"subList",pid,interfaceNo)
    print("写入subList成功")
    #replaceList = subList.replace('\\','')
    replaceList = subList.replace('" method="POST"><input type="hidden" name="','?')
    replaceList = replaceList.replace('" value=\'','=')
    print('replaceList:%s'%replaceList)
    replaceList = replaceList + '}'
    print('replaceList:%s'%replaceList)
    setExcelData('../interface.xls',replaceList,'replaceList',pid,interfaceNo)
    print('写入replaceList成功')

    driver = webdriver.Chrome()
    driver.get(replaceList)
    sleep(3)
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="sendSmsVerify"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="alertLayer-2"]/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="smsCode"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('q1111111')
    driver.find_element_by_xpath('//*[@id="confirmPassword"]').send_keys('q1111111')
    #driver.find_element_by_xpath('//*[@id="nextButton"]')
