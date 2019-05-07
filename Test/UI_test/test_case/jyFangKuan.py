#coding=utf-8
#捷越放款
from selenium import webdriver
import unittest
from time import *
import Test.UI_test.test_case.pub
import sys
import importlib
importlib.reload(sys)

class testFK(unittest.TestCase):
    #setUp初始化部分（环境的搭建）
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://172.18.100.59:8080/core-web/user/caslogin"      #集成1环境
        #self.base_url = "http://172.18.100.164:8080/core-web/user/caslogin"      #集成2环境

    #testcase测试开始、执行步骤（实现测试过程的代码）
    def test_FK(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        sleep(4)
        login = Test.UI_test.test_case.pub.Login()
        login.user_login(driver)    #调用登录模块
        sleep(4)
        driver.find_element_by_xpath("//*[@id='firstMenu12']").click()  #选择左侧菜单
        sleep(3)
        driver.find_element_by_xpath("//span[text()=' 出金业务管理']").click()
        sleep(3)
        driver.find_element_by_xpath("//li[text()='捷越待放款管理']").click()
        sleep(10)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPage')]"))   #跳转到右侧iframe
        driver.find_element_by_xpath(
            "//div[contains(@class,'tableContent')]/table/tbody/tr[2]/th/div/input").click()  # 选中第二个复选框
        sleep(3)
        contractNo = driver.find_element_by_xpath(
            "//div[contains(@id,'bctn_tname')]/table/tbody/tr[2]/td[2]/div").text
        print("放款合同编号：%s"%contractNo)
        sheetName = "fangkuan"
        for pid in range(1, Test.UI_test.test_case.pub.getExcelNrows(sheetName)):
            Test.UI_test.test_case.pub.setExcelData(contractNo, "合同编号", pid, sheetName)
        driver.find_element_by_xpath("//a[text()='批量放款']").click()      #点击批量放款
        sleep(5)
        driver.switch_to.alert.accept()     #点击确定
        sleep(3)
        driver.switch_to.default_content()      #跳回最外层页面
        driver.find_element_by_xpath("//span[text()=' 居间人债权管理']").click()
        driver.find_element_by_xpath("//div[@aria-labelledby='firstMenu12']/ul/li[2]/ul/li[text()='债权明细查询']").click()
        sleep(8)
        driver.switch_to.frame(
        driver.find_element_by_xpath("//iframe[contains(@src,'tCMhCreditPool/prepareExecute')]"))  # 跳转到右侧iframe
        driver.find_element_by_xpath("//input[@name='creditId']").send_keys(contractNo)     #contractNo参数化  2015121113030004
        driver.find_element_by_xpath("//button[@role='button']/span[text()='查询']").click()
        sleep(12)
        check1 = driver.find_element_by_xpath("//div[@class='tableFooter']/ul/li[8]").text      #设置检查点，获取右下角查询结果是否为0条
        print(check1)

        #用if语句判断检查点是否放款成功，后续可以尝试把check1参数获取内容做截取并判断，同时把判断结果放到测试报告或者excel中(也要考虑用断言)
        if check1 == "当前1-1,总计1,每页10":
            print("查询到1条结果，放款成功啦！")
            #这里应该setExcel一个放款成功
            sheetName = "fangkuan"
            for pid in range(1, Test.UI_test.test_case.pub.getExcelNrows(sheetName)):
                Test.UI_test.test_case.pub.setExcelData("pass", "合同状态", pid, sheetName)
            contractAmt = driver.find_element_by_xpath(
                "//div[@class='tableContent']/table/tbody/tr/td[5]/div").text   # 获取合同金额
            print(contractAmt)
            for pid in range(1, Test.UI_test.test_case.pub.getExcelNrows(sheetName)):
                Test.UI_test.test_case.pub.setExcelData(contractAmt, "合同金额", pid, sheetName)
            fundAmt = driver.find_element_by_xpath(
                "//div[@class='tableContent']/table/tbody/tr/td[6]/div").text  # 获取放款金额
            print(fundAmt)
            for pid in range(1, Test.UI_test.test_case.pub.getExcelNrows(sheetName)):
                Test.UI_test.test_case.pub.setExcelData(fundAmt, "放款金额", pid, sheetName)
            target = driver.find_element_by_xpath("//a[text()='分配信息']")
            driver.execute_script("arguments[0].scrollIntoView();", target)     #将滚动条拖动到元素可见的位置上
            sleep(3)
            driver.find_element_by_xpath("//a[text()='详情']").click()
            sleep(3)
            driver.find_element_by_xpath("//span[text()='关闭']").click()
            sleep(3)
            driver.find_element_by_xpath("//a[text()='分配信息']").click()
            sleep(3)
            handles = driver.window_handles     #切换到新开的浏览器标签
            for handle in handles:
                if driver.current_window_handle != handle:
                    driver.switch_to.window(handle)
                    driver.close()
            sleep(3)
            #contractNo = "2014121014181005"
            #sql = "select * from t_c_at_account acc where acc.account in (select tt.acc_id from T_C_at_loanINFO tt where tt.contract_no in( '%s'))"%contractNo
            sql = "select * from t_c_at_account acc where acc.account in (select tt.acc_id from T_C_at_loanINFO tt where tt.contract_no in( '20140610150P1018'))"
            print(sql)
            try:
                balance = Test.UI_test.test_case.pub.getSQLResult(sql)[0][5]
                for pid in range(1, Test.UI_test.test_case.pub.getExcelNrows(sheetName)):
                    Test.UI_test.test_case.pub.setExcelData(balance, "账户余额", pid, sheetName)
                use_balance = Test.UI_test.test_case.pub.getSQLResult(sql)[0][6]
                for pid in range(1, Test.UI_test.test_case.pub.getExcelNrows(sheetName)):
                    Test.UI_test.test_case.pub.setExcelData(use_balance, "可用余额", pid, sheetName)
            except IndexError:
                print("account表查不到这个账户")
            sleep(3)
        else:
            print("没有查询到结果，放款失败啦！")
            #这里应该setExcel一个放款失败

    #tearDown测试结束、测试环境的还原（tearDown的过程很重要，要为下一个test case留下一个干净的环境）
    def tearDown(self):
        self.driver.quit()

#通过unittest.main()方法来运行当前文件中的测试方法，其默认匹配并运行以test开头的方法。
#unittest提供了全局的main()方法，使用它可以方便的将一个单元测试模块变成可以直接运行的测试脚本。main()方法使用TestLoader类来搜索所有包含在该
#模块中以“test”命名开头的测试方法，并自动执行它们。
if __name__ == "__main__":
    unittest.main()