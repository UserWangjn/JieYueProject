#coding=utf-8
from selenium import webdriver
from time import  sleep
import sys
#reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.Chrome()
driver.get("http://172.18.100.59:8080/core-web/user/home")
driver.maximize_window()
sleep(2)
driver.find_element_by_xpath("//input[@id='username']").send_keys("hxjauser")
driver.find_element_by_xpath("//input[@id='pwd']").send_keys("Cs654321")
driver.find_element_by_xpath("//input[@value='登录']").click()

sleep(3)
driver.find_element_by_xpath("//h3[@id='firstMenu12']").click()
sleep(3)
driver.find_element_by_xpath("//span[text()=' 居间人债权管理']").click()
sleep(3)
driver.find_element_by_xpath("//div[@aria-labelledby='firstMenu12']/ul/li[2]/ul/li[text()='债权明细查询']").click()
sleep(8)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPage')]"))
sleep(3)
#driver.find_element_by_xpath("//input[@name='creditId']").send_keys("123")


#laladriver.quit()