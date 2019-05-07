# -*- coding:utf-8 -*-

import os
import unittest
from Com.log import MyLog as Log
import Com.readConfig as readConfig
from Com.HTMLTestReport import HTMLTestRunner
from Com.configEmail import MyEmail

Config = readConfig.ReadConfig()

class AllTest:
	def __init__(self):
		global log, logger, resultPath, on_off
		log = Log.get_log()
		logger = log.logger
		resultPath = log.get_report_path()
		on_off = Config.get_email("on_off")
		self.caseListFile = os.path.join(readConfig.proDir, "Data", "caselist.txt")
		self.caseFile = os.path.join(readConfig.proDir, "Case")
		# self.caseFile = None
		self.caseList = []
		self.email = MyEmail.get_email()

	def set_case_list(self):
		with open(self.caseListFile, encoding="utf-8") as fb:
			for value in fb.readlines():
				data = str(value)
				if data != '' and not data.startswith("#"):
					self.caseList.append(data.replace("\n", ""))


	def set_case_suite(self):
		self.set_case_list()
		test_suite = unittest.TestSuite()
		suite_module = []

		for case in self.caseList:
			print(case + '.py')
			discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case + '.py', top_level_dir=None)
			suite_module.append(discover)

		if len(suite_module) > 0:
			for suite in suite_module:
				for test_name in suite:
					test_suite.addTest(test_name)
		else:
			return None
		return test_suite

	def run(self):
		try:
			suit = self.set_case_suite()
			#print(suit)
			if suit is not None:
				logger.info("********TEST START********")
				with open(resultPath, 'wb') as fp:
					runner = HTMLTestRunner(stream=fp, title='接口自动化测试报告', description='详细测试用例结果', tester='李威')
					runner.run(suit)
			else:
				logger.info("没有添加一个用例")
		except Exception as ex:
			logger.error(str(ex))
		finally:
			logger.info("*********TEST END*********")
			# send test report by email
			if on_off == 'on':
				self.email.send_email()
			elif on_off == 'off':
				logger.info("不能发送邮件，因为on_off = 'off'")
			else:
				logger.info("Unknow state.")

if __name__ == '__main__':
	obj = AllTest()
	obj.run()


