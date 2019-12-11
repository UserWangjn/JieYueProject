from Test.Int_test.util import *
import random

interfaceNo = 2003
for pid in range(1,getExcelNrows('../interface.xls',interfaceNo)):
    contractNo = getExcelData('../interface.xls',"合同号", pid, interfaceNo)
    print("合同号：%s"%contractNo)
    # BodyData是字典类型
    BodyData = {
        "sysSource": "2",
        "frontTransNo": "as3z1898656%d"%random.randint(0,99999),
        "frontTransTime": "2014-12-17 15:33:20",
        "interfaceNo": "2003",
        "busiCode": "LBI03",
        "contractNo": contractNo,
        "channel": "01",
        "payAmount": 88888.77
    }
    print("pid:%s"%pid)
    setExcelData('../interface.xls',BodyData,"请求报文",pid,interfaceNo)
    print("写入请求报文")

    #rebody = getInterfaceResjc05(BodyData)
    rebody = getInterfaceRes('http://core-interface-jc1.jieyue.com/core-interface/api/loan/2003/v1',BodyData)
    print("rebody:%s"%rebody)
    setExcelData('../interface.xls',rebody,"返回报文",pid,interfaceNo)
    print("写入返回报文")

    res = rebody["responseBody"]["retCode"]
    print("res=%s"%res)
    if res == "0000":
        setExcelData('../interface.xls',"pass","测试结果",pid,interfaceNo)
        print("报文返回成功，交易发送成功")
    elif res == "200":
        setExcelData('../interface.xls',"fail","测试结果",pid,interfaceNo)
        print("交易发送失败")
    elif res == "0001":
        setExcelData('../interface.xls',"fail", "测试结果", pid, interfaceNo)
        print("交易发送失败")
        break

sql = "select * from t_c_at_account a where a.account ='010000224110010000330622'"
setExcelData('../interface.xls',sql,"查询SQL",pid,interfaceNo)
setExcelData('../interface.xls',getSQLResult(sql,'jc02')[0][5],"SQL结果",pid,interfaceNo)
print('sql执行结果：%s'%getSQLResult(sql,'jc02')[0][5])
print("写入SQL结果")

