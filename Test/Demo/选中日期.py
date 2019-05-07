#coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://172.18.100.211:8080/core-web/user/home")
driver.maximize_window()

time.sleep(2)
driver.find_element_by_xpath("//input[@id='username']").send_keys("hxjauser")
driver.find_element_by_xpath("//input[@id='pwd']").send_keys("Cs654321")
driver.find_element_by_xpath("//input[@value='登录']").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='firstMenu4']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[text()=' 总账交易']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[text()='通用交易']").click()

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'prepareExecute/toQueryPage')]"))
time.sleep(3)

driver.find_element_by_xpath("//input[@name='dealTime_start']").click()
time.sleep(2)

driver.find_element_by_xpath("//td[@onclick='day_Click(2018,2,2);']")