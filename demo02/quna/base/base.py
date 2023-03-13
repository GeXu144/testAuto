# -*- coding=utf-8 -*-
# @Time: 2023/3/13 10:36
# @Author: 北巷
# @File: base.py
# @Software: PyCharm
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Base():
    def __init__(self,driver):
        self.driver=driver #type WebDriver

    def by_name(self,element):
        return self.driver.find_element(By.NAME,element)

    def by_xpath(self,element):
        return self.driver.find_element(By.XPATH, element)

    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def close(self):
        self.driver.quit()



