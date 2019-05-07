#coding=utf-8
from selenium import webdriver
import cx_Oracle
import os   #os 提供了很多与操作系统交互的函数
import xlrd #xlrd   读取Excel的扩展工具
from xlutils.copy import copy   #xlutils.copy
from time import sleep

#登录、注销
class Login():
    #登录
    def user_login(self,driver):
        #driver = webdriver.Firefox()
        driver.find_element_by_xpath("//input[@id='username']").send_keys("hxjauser")
        driver.find_element_by_xpath("//input[@id='pwd']").send_keys("Cs654321")
        #driver.find_element_by_xpath("//input[@value='登录']").click()
        driver.find_element_by_xpath("//button[text()='登录']").click()

#退出
    def user_logout(self,driver):
        driver.find_element_by_xpath("//a[@title='退出']").click()


#连接数据库
def getSQLResult(sql=None):
    #dsn = cx_Oracle.makedsn("172.18.100.107",1521,"testdb")        #集成1
    dsn = cx_Oracle.makedsn("172.18.100.104", 1521, "testdb")       #集成2
    #conn = cx_Oracle.connect("jc01_core","core",dsn)        #连接数据库-集成1
    conn = cx_Oracle.connect("jc02_core","core246685",dsn)        #连接数据库-集成2
    cursor = conn.cursor()      #获取cursor
    cursor.execute(sql)     #使用cursor进行各种操作
    res = cursor.fetchall()
    cursor.close()      #关闭cursor
    conn.close()          #关闭连接
    return res

#写入EXCEL
def setExcelData(cellvalue, cellname, pid, sheetname):
    cellvalue = str(cellvalue)
    if cellname == "请求报文" or cellname == "返回报文":
        cellvalue = cellvalue.replace(" ", "\n")
    cellname = str(cellname)
    pid = str(pid)
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]
    dataPath = os.path.join(proDir, "UI_test\Report\Report.xls")
    fd = xlrd.open_workbook(dataPath, formatting_info=True)
    sh = fd.sheet_by_name(sheetname)
    for row_index in range(sh.nrows):
        colValue = sh.cell(int(row_index), 0).value
        if pid == colValue:
            break
    for col_index in range(sh.ncols):
        rowvalue = sh.cell(0, int(col_index)).value
        if cellname == rowvalue:
            break
    sheetIndex = fd._sheet_names.index(sheetname)
    wb = copy(fd)
    sheet = wb.get_sheet(sheetIndex)
    sheet.write(row_index, col_index, cellvalue)
    wb.save(dataPath)

#获取sheet行数
def getExcelNrows(sheetname):
    sheetname = str(sheetname)
    proDir = os.path.split(os.getcwd())[0]  #os.path.split()#把路径分割成dirname和basename，返回一个元组 os.getcwd() 方法用于返回当前工作目录
    dataPath = os.path.join(proDir, "UI_test\Report\Report.xls")   #os.path.join    把目录和文件名合成一个路径
    fd = xlrd.open_workbook(dataPath, formatting_info=True) #xlrd.open_workbook 打开excel文件
    sh = fd.sheet_by_name(sheetname)    #fd.sheet_by_name
    return sh.nrows #sh