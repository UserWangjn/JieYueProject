# -*- coding:utf-8 -*-

from Com.log import MyLog
from Com import configHttp
from Com.util import *
import unittest
import paramunittest
from Com import configDB

interface = "2078"
name = "快捷支付银行卡预绑定(非存管)"

req = configHttp.ConfigHttp()
sql = configDB.ConfigDB()

@paramunittest.parametrized(*get_xls("interface.xls", interface))
class Test(unittest.TestCase):
	def setParameters(self, No, 测试结果, 请求报文, 返回报文, 查询SQL, SQL结果, custCode, bankCardNo, sql):
		self.custCode = str(custCode)
		self.bankCardNo = str(bankCardNo)
		self.No = str(No)
		self.sql = str(sql)

	def setUp(self):
		self.log = MyLog.get_log()
		self.logger = self.log.logger
		self.log.build_start_line(interface + name + "CASE " + self.No)
		print(interface + name + "CASE " + self.No)
	
	def test_body(self):
		self.url = "/core-interface/api/loan/2078/v1"
		headers = {"Content-Type": "application/json"}
		self.data = {
		"sysSource": "2",
		"frontTransNo": "1701830089"+get_number(8),
		"frontTransTime": "2017-09-01 10:51:00",
		"interfaceNo": "2078",
		"busiCode": "LBB78",
		"custCode": self.custCode,
		"bankCardNo": self.bankCardNo,
		"isAppFlg": "1",
		"depositCode": "00",
		"payChannelType": "HX_0013",
		"payChannelName": "金运通",
		"clientSource": "LOAN001"
		}
		req.httpname = "COREJC2"
		req.set_url(self.url)
		req.set_headers(headers)
		req.set_data(self.data)
		self.response = req.post()
		try:
			self.retcode = self.response["responseBody"]["retCode"]
		except Exception:
			self.logger.exception("报文返回为空！")
			print("报文返回为空！")
		self.check_sql()
		self.check_result()
		self.wr_excel()

	def check_result(self):
		try:
			self.assertEqual(self.retcode, "0000", "pass")
			self.assertEqual(self.res, "辛文", "测试通过")
			set_excel("pass", "测试结果", self.No, interface)
			self.logger.info("测试通过")
		except AssertionError:
			set_excel("fail", "测试结果", self.No, interface)
			self.logger.error("测试失败")

	def check_sql(self):
		sql.dbname = "CORE2DB"
		self.SQL = get_sql('集成一', 'test1', "测试") % self.sql
		cursor = sql.executeSQL(self.SQL)
		try:
			self.resql = sql.get_one(cursor)
			# self.resql = sql.get_all(cursor)
			self.res = self.resql[6]
		except Exception:
			print("SQL查询结果为空！")
			self.logger.error("SQL查询结果为空！")
		sql.closeDB()

	def check_web(self):
		pass
	
	def wr_excel(self):
		set_excel(self.data, "请求报文", self.No, interface)
		set_excel(self.response, "返回报文", self.No, interface)
		set_excel(self.SQL, "查询SQL", self.No, interface)
		set_excel(self.resql, "SQL结果", self.No, interface)
	
	def tearDown(self):
		self.log.build_case_line("请求报文", self.data)
		self.log.build_case_line("返回报文", self.response)
		self.log.build_case_line("查询SQL", self.SQL)
		self.log.build_case_line("SQL结果", self.resql)
		self.log.build_end_line(interface + "--CASE" + self.No)




