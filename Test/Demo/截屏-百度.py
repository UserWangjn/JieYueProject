
from selenium import webdriver

import time



driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(1)
driver.get_screenshot_as_file("D:\\test\\b1.jpg")

#driver.find_element_by_link_text("hao123").click()
time.sleep(1)
driver.close()