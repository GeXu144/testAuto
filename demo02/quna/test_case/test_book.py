# -*- coding=utf-8 -*-
# @Time: 2023/3/13 11:12
# @Author: 北巷
# @File: test_book.py
# @Software: PyCharm
import pytest
from selenium import webdriver
from quna.common.common_fun import csv_process,get_goday
from quna.po.boo_ticket_page import BookTicket
from quna.po.book_list_page import BookList
from quna.po.order_page import Order


data=csv_process("../data/quna_data.csv")
class Test_Book():

    def setup(self):
        self.driver=webdriver.Chrome("chromedriver.exe")
        url="https://train.qunar.com/"
        self.driver.get(url)
        self.driver.maximize_window()

    @pytest.mark.parametrize(["start","end","name","id","day"],data)
    def test_01(self,start,end,name,id,day):
        book_ticket=BookTicket(self.driver)
        book_ticket.book_ticket(start,end,get_goday(day))

        book_list=BookList(self.driver)
        book_list.buy()

        order=Order(self.driver)
        order.write_info(name,id)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["-s","test_book"])





