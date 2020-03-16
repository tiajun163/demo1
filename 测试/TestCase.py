import unittest
from selenium import webdriver
from selenium.webdriver.remote import switch_to
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options

import time
import os

driver1=webdriver.Chrome()
driver1.get("http://pc.jijile.net/login.html")
# driver1.maximize_window()
# driver1.implicitly_wait(20)
# driver1.get("www.baidu.com")
time.sleep(5)
driver1.find_element_by_name("phone2").send_keys("16675528004")
driver1.find_element_by_name("password").send_keys("123456")
driver1.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/form/input[3]").click()
# driver1.find_element_by_link_text("会员查询").click()
# driver1.find_element_by_xpath('/html/body/div[2]/div/ul/li[1]').click()
# driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]').click()
# driver1.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/a/cite').click()