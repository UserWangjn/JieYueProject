#coding=utf-8
from Test.UI_test.test_case import jyFangKuan
from Test.UI_test.test_case.QueryCredit import QueryCredit
import unittest

#构建测试集
suite = unittest.TestSuite()

#suite.addTest(jyFangKuan.testFK("test_FK"))
suite.addTest(QueryCredit.testQuery("test_Query"))      #债权明细查询


if __name__ == '__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

