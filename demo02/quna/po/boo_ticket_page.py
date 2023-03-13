# -*- coding=utf-8 -*-
# @Time: 2023/3/13 10:48
# @Author: 北巷
# @File: boo_ticket_page.py
# @Software: PyCharm
import time
from selenium.webdriver import ActionChains
from quna.base.base import Base
from selenium.webdriver.common.keys import Keys



class BookTicket(Base):

    def go_element(self):
        return self.by_name("fromStation")

    def to_element(self):
        return self.by_name("toStation")

    def write_date(self,date):
        self.by_name("date").send_keys(Keys.CONTROL,"a")
        self.by_name("date").send_keys(Keys.BACKSPACE)
        self.by_name("date").send_keys(date)

    def move_click(self):
        action=ActionChains(self.driver)
        action.move_by_offset(0,0)
        action.click()
        action.perform()

    def get_button(self):
        return self.by_name("stsSearch")

    def book_ticket(self,start,end,date):
        self.go_element().send_keys(start)
        time.sleep(1)
        self.move_click()

        self.to_element().send_keys(end)
        time.sleep(1)
        self.move_click()

        self.write_date(date)
        time.sleep(1)
        self.move_click()

        self.get_button().click()
        time.sleep(2)







