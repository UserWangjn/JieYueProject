# -*- coding:utf-8 -*-

from Com.log import MyLog
from Com import configHttp
from Com.util import *
import unittest
import paramunittest
from Com import configDB
from datetime import datetime

interface = "3004"
name = "催收减免"

req = configHttp.ConfigHttp()
sql = configDB.ConfigDB()

@paramunittest.parametrized(*get_xls("interface.xls", interface))
class Test(unittest.TestCase):
	global frontTransNo
	frontTransNo = str(datetime.now().strftime("%Y%m%d%H%M%S"))+get_number(2)
	def setParameters(self, No, 测试结果, 请求报文, 返回报文, 查询SQL1, 查询SQL2, 查询SQL3, 查询SQL4, CONTRACT_ID, RED_OVER_BASE, RED_OVER_INST,\
	REDPUN_INTEREST, REDUCE_DEFAULT, LIST_STAT, LOAN_STATUS, REDUCE_FLAG, REG_TYPE, STATE):
		self.No = str(No)
		self.CONTRACT_ID = str(CONTRACT_ID)
		self.RED_OVER_BASE = float(RED_OVER_BASE)
		self.RED_OVER_INST = float(RED_OVER_INST)
		self.REDPUN_INTEREST = float(REDPUN_INTEREST)
		self.REDUCE_DEFAULT = float(REDUCE_DEFAULT)
		self.LIST_STAT = int(LIST_STAT)
		self.LOAN_STATUS = int(LOAN_STATUS)
		self.REDUCE_FLAG = int(REDUCE_FLAG)
		self.REG_TYPE = int(REG_TYPE)
		self.STATE = int(STATE)

	def setUp(self):
		self.log = MyLog.get_log()
		self.logger = self.log.logger
		self.log.build_start_line(interface + name + "CASE " + self.No)
		print(interface + name + "CASE " + self.No)
	
	def test_body(self):
		self.url = "/loan/api/aftloancoll/3004/v1"
		headers = {"Content-Type": "application/json"}
		self.data = {
			"sysSource": "3",
			"frontTransNo": frontTransNo,
			"frontTransTime": "2018-01-25 15:16:00",
			"interfaceNo": interface,
			"busiCode": "CSB05",
			"contractNo": self.CONTRACT_ID,#合同编号
			"reduceOverdueBase": self.RED_OVER_BASE,#减免逾期本金
			"reduceOverdueInst": self.RED_OVER_INST,#减免逾期利息
			"reducePenalty": self.REDPUN_INTEREST,#减免罚息
			"reduceDefault": self.REDUCE_DEFAULT,#减免违约金
			"reduceType": "01",
			"remark": "减免减免减免减免减免第八笔",
			"annexUrl": "/temp6/MobileCallList1_33.zip"
			}
		req.httpname = "LOANJC2"
		req.set_url(self.url)
		req.set_headers(headers)
		req.set_data(self.data)
		self.response = req.post()
		try:
			self.retcode = self.response["responseBody"]["retCode"]
		except Exception:
			self.logger.error("报文返回为空！")
			print("报文返回为空！")
		
		self.check_sql()
		self.check_result()
		self.wr_excel()
	
	def check_result(self):
		try:
			#LOAN2DB
			self.assertEqual(self.retcode, "200", self.logger.info("检查retcode"))
			self.assertEqual(self.resql1, self.RED_OVER_BASE, self.logger.info("检查点1"))
			self.assertEqual(self.resql2, self.RED_OVER_INST, self.logger.info("检查点2"))
			self.assertEqual(self.resql3, self.REDPUN_INTEREST, self.logger.info("检查点3"))
			self.assertEqual(self.resql4, self.REDUCE_DEFAULT, self.logger.info("检查点4"))
			self.assertEqual(self.resql5, self.LIST_STAT, self.logger.info("成功")) # 05-审批中 06-成功
			#CORE2DB
			self.assertEqual(self.resql6, self.LOAN_STATUS, self.logger.info("逾期")) #贷款状态：0-正常 1-逾期  2-正常结清 3.撤销 4.提前结清，5.展期结清
			self.assertEqual(self.resql7, self.REDUCE_FLAG, self.logger.info("减免确认")) #减免标识:0-正常 1-减免申请 2-减免确认
			self.assertEqual(self.resql8, self.REG_TYPE, self.logger.info("检查点8"))
			self.assertEqual(self.resql9, 1, self.logger.info("检查点9"))
			self.assertEqual(self.resql10, 2, self.logger.info("检查点10"))
			self.assertEqual(self.resql11, self.STATE, self.logger.info("检查点11"))
			self.assertEqual(self.resql12, self.STATE, self.logger.info("检查点12"))
			set_excel("pass", "测试结果", self.No, interface)
			self.logger.info("测试通过")
		except AssertionError:
			set_excel("fail", "测试结果", self.No, interface)
			self.logger.error("测试失败")
	
	def check_sql(self):
		sql.dbname = "LOAN2DB"
		self.SQL1 = get_sql('LOAN2DB', 'LA_T_REDUCTION', "COLL_LIST_NO") % (frontTransNo, self.CONTRACT_ID)
		cursor = sql.executeSQL(self.SQL1)
		try:
			self.res1 = sql.get_one(cursor)
			# self.resql = sql.get_all(cursor)
			self.resql1 = float(self.res1[66])
			self.resql2 = float(self.res1[69])
			self.resql3 = float(self.res1[35])
			self.resql4 = float('%.1f' % self.res1[37])
			self.resql5 = int(self.res1[53])
		except Exception:
			print("SQL1查询结果为空！")
			self.logger.exception("SQL1查询结果为空！")
		
		sql.dbname = "CORE2DB"
		self.SQL2 = get_sql('CORE2DB', 't_c_at_loaninfo', "CONTRACT_NO") % self.CONTRACT_ID
		cursor = sql.executeSQL(self.SQL2)
		try:
			self.res2 = sql.get_one(cursor)
			# self.resql = sql.get_all(cursor)
			self.resql6 = int(self.res2[21])
			self.resql7 = int(self.res2[23])
		except Exception:
			print("SQL2查询结果为空！")
			self.logger.exception("SQL2查询结果为空！")
		
		self.SQL3 = get_sql('CORE2DB', 't_c_ln_reducereg', "CONTRACT_NO") % (self.CONTRACT_ID, self.RED_OVER_BASE, self.RED_OVER_INST, self.REDUCE_DEFAULT, self.REDPUN_INTEREST)
		cursor = sql.executeSQL(self.SQL3)
		try:
			self.res3 = sql.get_all(cursor)
			#self.resql = sql.get_all(cursor) #返回全部查询结果，字典的形式
			self.resql8 = int(self.res3[0][2])
			self.resql9 = len(self.res3)
		except Exception:
			print("SQL3查询结果为空！")
			self.logger.exception("SQL3查询结果为空！")
			
			
		self.SQL4 = get_sql('CORE2DB', 't_c_cd_repay_reg', "CREDIT_ID") % (self.CONTRACT_ID, self.res3[0][16])
		cursor = sql.executeSQL(self.SQL4)
		try:
			#self.resql = sql.get_one(cursor)
			self.res4 = sql.get_all(cursor)
			self.resql10 = (len(self.res4))
			self.resql11 = int(self.res4[0][4])
			self.resql12 = int(self.res4[1][4])
		except Exception:
			print("SQL4查询结果为空！")
			self.logger.exception("SQL4查询结果为空！")
		sql.closeDB()
	
	def check_web(self):
		pass
	
	def wr_excel(self):
		set_excel(self.data, "请求报文", self.No, interface)
		set_excel(self.response, "返回报文", self.No, interface)
		set_excel(self.SQL1, "查询SQL1", self.No, interface)
		set_excel(self.SQL2, "查询SQL2", self.No, interface)
		set_excel(self.SQL3, "查询SQL3", self.No, interface)
		set_excel(self.SQL4, "查询SQL4", self.No, interface)
		#set_excel(self.resql, "SQL结果", self.No, interface)
	
	def tearDown(self):
		self.log.build_case_line("请求报文", self.data)
		self.log.build_case_line("返回报文", self.response)
		self.log.build_case_line("查询SQL1", self.SQL1)
		self.log.build_case_line("返回SQL1", self.res1)
		self.log.build_case_line("查询SQL2", self.SQL2)
		self.log.build_case_line("返回SQL2", self.res2)
		self.log.build_case_line("查询SQL3", self.SQL3)
		self.log.build_case_line("返回SQL3", self.res3)
		self.log.build_case_line("查询SQL4", self.SQL4)
		self.log.build_case_line("返回SQL4", self.res4)
		self.log.build_end_line(interface + "--CASE" + self.No)


