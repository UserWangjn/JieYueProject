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

#获得cookie信息
cookie = driver.get_cookies()
#将获得cookie的信息打印
print(cookie)

#遍历cookies中的name和value信息并打印
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))