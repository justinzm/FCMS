#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/5/21 10:57
# @Author : justin.郑 3907721@qq.com
# @File : test01.py
# @desc :

import threading
import time


def worder():
    print("i am thread")
    t = threading.current_thread()
    time.sleep(5)
    print(t.getName())

new_t = threading.Thread(target=worder, name="justinThread")
new_t.start()

print("i am justin")
t = threading.current_thread()
print(t.getName())

