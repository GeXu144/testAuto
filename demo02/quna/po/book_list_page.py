# -*- coding=utf-8 -*-
# @Time: 2023/3/13 11:06
# @Author: 北巷
# @File: book_list_page.py
# @Software: PyCharm
import time
from quna.base.base import Base


class BookList(Base):

    def buy_element(self):
        return self.by_xpath("//*[@id='list_listInfo']/ul[2]/li[1]/div/div[7]/a[1]")

    def buy(self):
        self.buy_element().click()
        time.sleep(2)
