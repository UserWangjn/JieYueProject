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
driver.get_screenshot_as_file("D:\\test\\b1.jpg")
#driver.get_screenshot_as_file("D:\\RobotFrameInstallfiles\\Test\\TestSelenium.jpg")
#driver.save_screenshot("D:\\RobotFrameInstallfiles\\Test\\TestSelenium.png")
time.sleep(2)

driver.quit()