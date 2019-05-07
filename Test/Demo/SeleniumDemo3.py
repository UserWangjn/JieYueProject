#coding=utf-8
from selenium import webdriver
from time import *


driver = webdriver.Chrome()
driver.get("http://172.18.100.59:8080/core-web/user/caslogin")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@name='username']").send_keys("hxjauser")
driver.find_element_by_xpath("//input[@name='passwordInput']").send_keys("Cs654321")
driver.find_element_by_xpath("//button[text()='登录']").click()
#driver.find_element_by_xpath("//button[@type='button']").click()
sleep(5)

print("点击登录成功")

driver.close()

