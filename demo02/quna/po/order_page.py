# -*- coding=utf-8 -*-
# @Time: 2023/3/13 11:09
# @Author: 北巷
# @File: order_page.py
# @Software: PyCharm
import time

from quna.base.base import Base


class Order(Base):

    def name_element(self):
        return self.by_name("pName_0")

    def id_element(self):
        return self.by_name("pCertNo_0")

    def write_info(self,name,id):
        self.name_element().send_keys(name)
        self.id_element().send_keys(id)
        time.sleep(2)

