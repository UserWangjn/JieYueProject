#coding=utf-8
#债权明细查询
from selenium import webdriver
import unittest
from time import *
import Test.UI_test.test_case.pub
import sys
import importlib
importlib.reload(sys)

class testQuery(unittest.TestCase):
    #setUp初始化部分（环境的搭建）
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://172.18.100.59:8080/core-web/user/caslogin"      #集成1环境
        #self.base_url = "http://172.18.100.211:8080/core-web/user/caslogin"      #集成2环境

    #testcase测试开始、执行步骤（实现测试过程的代码）
    def test_Query(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(10)
        login = Test.UI_test.test_case.pub.Login()
        login.user_login(driver)    #调用登录模块
        sleep(4)
        driver.find_element_by_xpath("//*[@id='firstMenu0']").click()  #选择左侧菜单
        sleep(2)
        driver.find_element_by_xpath("//*[@id='firstMenu10']").click()
        sleep(2)
        driver.find_element_by_xpath("//span[text()=' 债权总览']").click()
        sleep(2)
        driver.find_element_by_xpath("//li[text()='债权明细查询']").click()
        driver.implicitly_wait(10)
        driver.switch_to.frame(
        driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryTCMHCreditCOPoolPage')]"))  # 跳转到右侧iframe
        #driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPage')]"))   #跳转到右侧iframe
        sleep(2)
        #driver.find_element_by_xpath("//div[contains(@id,'bctn_tname')]/table/tbody/tr/td[2]/div").click()
        contractNo = driver.find_element_by_xpath("//div[contains(@id,'bctn_tname')]/table/tbody/tr/td[2]/div").text
        print("查询合同编号：%s"%contractNo)
        driver.find_element_by_xpath("//input[@name='creditId']").send_keys(contractNo)
        driver.find_element_by_xpath("//span[text()='查询']").click()
        sleep(5)
        driver.find_element_by_xpath("//a[text()='详情']").click()
        sleep(5)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPageInfo')]"))
        sleep(2)
        creditState = driver.find_element_by_xpath("//table[@id='updateNewsTableId']/tbody/tr[8]/td[2]").text
        print("债权状态：%s"%creditState)
        sleep(5)

    #tearDown测试结束、测试环境的还原（tearDown的过程很重要，要为下一个test case留下一个干净的环境）
    def tearDown(self):
        self.driver.quit()

#通过unittest.main()方法来运行当前文件中的测试方法，其默认匹配并运行以test开头的方法。
#unittest提供了全局的main()方法，使用它可以方便的将一个单元测试模块变成可以直接运行的测试脚本。main()方法使用TestLoader类来搜索所有包含在该
#模块中以“test”命名开头的测试方法，并自动执行它们。
if __name__ == "__main__":
    unittest.main()