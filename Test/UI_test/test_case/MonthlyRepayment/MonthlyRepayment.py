#coding=utf-8
#MonthlyRepayment为月还
from Test.UI_test.util import *	#util.py
from time import *
import random
import sys
import importlib
importlib.reload(sys)

dataPath = "MonthlyRepayment\MonthlyRepayment.xls"
interfaceNo = 2003
for pid in range(1, getExcelNrows(dataPath , interfaceNo)):	#range() 函数可创建一个整数列表，一般用在 for 循环中	#getExcelNrows:获取场景数
    contractNo = getExcelData(dataPath,"contractNo",pid,interfaceNo)
    print("合同号：%s"%contractNo)

    amount = getExcelData(dataPath,"amount",pid,interfaceNo)
    print("amount定义成功")
    BodyData = {
        "sysSource":"2",
        "frontTransNo":"1701830089%d"%random.randint(00000000,99999999),
        "frontTransTime":"2014-12-17 15:33:20",
        "interfaceNo":"2003",
        "busiCode":"LBI05",
        "contractNo":"%s"%contractNo,
        "channel":"01",
        "payAmount":amount
    }
    setExcelData(dataPath, BodyData, "发送报文", pid, interfaceNo)

    rebody = getInterfaceRes(interfaceNo, BodyData)  # getInterfaceRes 取请求报文
    setExcelData(dataPath,rebody, "返回报文", pid, interfaceNo)
    print("写入excel的返回报文成功")
    res = rebody["responseBody"]["retCode"]
    if res == "0000":
        setExcelData(dataPath,"pass", "发送报文是否成功", pid, interfaceNo)
        print("发送报文成功")
    elif res == "0001":
        setExcelData(dataPath,"fail", "发送报文是否成功", pid, interfaceNo)
        print("发送报文失败")
    elif res == "9999":
        setExcelData(dataPath,"day_of_end", "发送报文是否成功", pid, interfaceNo)
        print("核心日终啦，测不了啦，下班吧~~~~~~~~~~~~~")
        break

sleep(5)
#sql = "select * from t_tn_transaction_record where bus_code in('2016120230718J1G0') order by id desc "
sql = "select * from t_tn_transaction_record where bus_code in('%s') order by id desc "%contractNo

#tran_status = getSQLResult(sql)[0][5]
id = getSQLResult(sql)[0][0]
print("登记表ID=%s"%id)
sql2 = "update T_TN_TRANSACTION_RECORD set tran_status='5',req_code='HX_0000',req_msg='交易处理完成' " \
       " where tran_status in ('4','3') and id in ('%s')"%id
sql3 = "update t_tn_record_split set tran_status='2',req_code='HX_0000',req_msg='交易成功',batch_id='99999'," \
       "complete_processing_time=sysdate where regist_id in (select id from T_TN_TRANSACTION_RECORD where " \
       "tran_status in ('4','3') and id in ('%s'))"%id

for i in range(1,30):
    tran_status = getSQLResult(sql)[0][5]
    if tran_status == 3 or tran_status == 4:
        print("tran_status == 3，下面修改登记表状态，执行SQL")
        updateSQL(sql3)
        print("sql3：%s"%sql3)
        sleep(3)
        updateSQL(sql2)
        print("sql2：%s" % sql2)
        for u in range(1,30):
            if getSQLResult(sql)[0][30] == 1:
                setExcelData(dataPath,"1", "OUTER_COMPLATE_FLAG", pid, interfaceNo)
                print("OUTER_COMPLATE_FLAG为1，处理成功！")
                break
            else:
                print("OUTER_COMPLATE_FLAG为0，请等待定时任务执行！第%s次"%u)
                sleep(10)
        break
    elif tran_status == 6:
        print("tran_status检验，tran_status=%s"%tran_status)
        print("划扣登记表还没有拆分，登记表tran_status=6，请等待定时任务执行！第%s次"%i)
        sleep(20)
    elif tran_status == 5:
        print("登记表tran_status=5")
        for y in range(1,30):
            if getSQLResult(sql)[0][30] == 1:
                setExcelData(dataPath,"1", "OUTER_COMPLATE_FLAG", pid, interfaceNo)
                print("OUTER_COMPLATE_FLAG为1，处理成功！")
                break
            else:
                print("OUTER_COMPLATE_FLAG为0，请等待定时任务执行！第%s次"%y)
                sleep(10)
            break
