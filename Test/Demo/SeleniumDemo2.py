#coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://172.18.100.59:8080/core-web/user/home")


time.sleep(2)
driver.find_element_by_xpath("//input[@id='username']").send_keys("hxjauser")
driver.find_element_by_xpath("//input[@id='pwd']").send_keys("Cs654321")
driver.find_element_by_xpath("//input[@value='登录']").click()

time.sleep(2)

driver.find_element_by_xpath("//h3[text()='会计总账']").click()