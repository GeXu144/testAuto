# -*- coding=utf-8 -*-
# @Time: 2023/3/13 10:18
# @Author: 北巷
# @File: common_fun.py
# @Software: PyCharm
import csv
from datetime import datetime,timedelta


def csv_process(filename):
    res=[]
    data=csv.reader(open(filename,"r",encoding="utf-8"))
    for row in data:
        res.append(row)
    return res

def get_goday(n):
    return str(datetime.today()+timedelta(days=int(n)))