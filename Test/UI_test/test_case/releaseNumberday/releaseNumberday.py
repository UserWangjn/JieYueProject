#coding=utf-8
#转让天数设置
from selenium import webdriver
import unittest
from time import *
import Test.UI_test.test_case.pub
from selenium.webdriver.support.select import Select
import sys
import importlib
importlib.reload(sys)

class testinvestExpire(unittest.TestCase):
    #setUp初始化部分（环境的搭建）
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.base_url = "http://172.18.100.59:8080/core-web/user/caslogin"      #集成1环境
		#self.base_url = "http://172.18.100.211:8080/core-web/user/caslogin"      #集成2环境

    #testcase测试开始、执行步骤（实现测试过程的代码）
	def test_investExpire(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.implicitly_wait(10)
		login = Test.UI_test.test_case.pub.Login()
		login.user_login(driver)    #调用登录模块
		sleep(4)
		driver.find_element_by_xpath("//*[@id='firstMenu0']").click()  #选择左侧菜单
		sleep(2)
		driver.find_element_by_xpath("//*[@id='firstMenu11']").click()
		sleep(2)
		driver.find_element_by_xpath("//span[text()=' 撮合规则设置']").click()
		sleep(2)
		target = driver.find_element_by_xpath("//*[@id='firstMenu14']")
		driver.execute_script("arguments[0].scrollIntoView();", target)  # 将滚动条拖动到元素可见的位置上
		sleep(5)
		driver.find_element_by_xpath("//li[contains(@url,'tCCdReleaseNumberday/prepareExecute')]").click()
		driver.implicitly_wait(10)
		driver.switch_to.frame(
		driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPage')]"))  # 跳转到右侧iframe
		sleep(2)
		driver.find_element_by_xpath("//table[contains(@id,'btn_tname')]/tbody/tr/th/div/input").click() #选中第一行复选框
		sleep(3)
		driver.find_element_by_xpath("//a[text()='修改']").click()
		sleep(3)
		driver.find_element_by_xpath("//input[@id='dtodelayDays']").clear()
		sleep(5)
		driver.find_element_by_xpath("//input[@id='dtodelayDays']").send_keys("1")
		sleep(3)
		driver.find_element_by_xpath("//span[text()='保存']").click()
		sleep(3)
		driver.switch_to.alert.accept()
		sleep(5)


    #tearDown测试结束、测试环境的还原（tearDown的过程很重要，要为下一个test case留下一个干净的环境）
	def tearDown(self):
		self.driver.quit()

#通过unittest.main()方法来运行当前文件中的测试方法，其默认匹配并运行以test开头的方法。
#unittest提供了全局的main()方法，使用它可以方便的将一个单元测试模块变成可以直接运行的测试脚本。main()方法使用TestLoader类来搜索所有包含在该
#模块中以“test”命名开头的测试方法，并自动执行它们。
if __name__ == "__main__":
    unittest.main()