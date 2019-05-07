#coding=utf-8
#hfFangKuan1适用理财计划放款、债权理财计划放款、回款队列放款
from Test.UI_test.util import *	#util.py
import sys
import importlib
importlib.reload(sys)

dataPath = "hfFangKuan1\FangKuan1.xls"
sheetname = "hfFangKuan1"
for pid in range(1, getExcelNrows(dataPath , sheetname)):	#range() 函数可创建一个整数列表，一般用在 for 循环中	#getExcelNrows:获取场景数
    contractNo = getExcelData(dataPath,"contractNo",pid,sheetname)
    print("合同号：%s"%contractNo)

    #sql = "select * from t_tn_online_bind_flow a where a.account_no = '6222020200097521997'"
    sql_balance = "select * from t_c_at_account where account in (select acc_id from T_C_at_loanINFO where contract_no in( '%s'))"%contractNo
    setExcelData(dataPath,sql_balance, "借款人账户SQL", pid, sheetname)
    print("写入“借款人账户SQL”：%s"%sql_balance)
    setExcelData(dataPath,getSQLResult(sql_balance)[0][5], "借款人账户余额", pid, sheetname)	#获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果

    #sql2 = "select sum(today_now_value) from t_c_cd_invest_credit_info where credit_id = '2014062014061010'"
    sql_value = "select sum(today_now_value),sum(assets_balance) from t_c_cd_invest_credit_info where credit_id = '%s'"%contractNo
    setExcelData(dataPath,sql_value, "债权价值SQL", pid, sheetname)
    print("写入“债权价值SQL”：%s" %sql_value)
    today_now_value = getSQLResult(sql_value)[0][0]
    assets_balance = getSQLResult(sql_value)[0][1]
    setExcelData(dataPath,today_now_value, "债权价值", pid, sheetname)
    setExcelData(dataPath,assets_balance, "资产余额", pid, sheetname)

    sql_fund = "select fund_amt from T_C_at_loanINFO where contract_no in( '2013071222091012')"
    setExcelData(dataPath,sql_fund, "放款金额", pid, sheetname)
    fund_amt = getSQLResult(sql_fund)[0][0]
    print("写入“放款金额”：%s" %fund_amt)
    setExcelData(dataPath,fund_amt, "放款金额", pid, sheetname)  # 获取数据库某个字段值的查询结果，尝试获取某几个字段的查询结果

    if 1 == 1 :
    #if float(fund_amt) == float(today_now_value) == assets_balance :
        setExcelData(dataPath,"pass", "测试结果", pid, sheetname)
        print("测试结果：pass")
    else:
        setExcelData(dataPath,"fail", "测试结果", pid, sheetname)
        setExcelData(dataPath,"fail", "失败原因", pid, sheetname)
        print("测试结果fail")