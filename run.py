# -*- coding: utf-8 -*- 
# @Time    : 2021/1/6 11:42 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : run.py
# @Software: PyCharm

from testcase.test_login import TestLogin

if __name__ == '__main__':
    login = TestLogin().test_cart_list()
