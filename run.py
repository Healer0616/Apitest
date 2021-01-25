# -*- coding: utf-8 -*- 
# @Time    : 2021/1/6 11:42 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : run.py
# @Software: PyCharm

import os
import pytest
from testcase.test_login import TestLogin

# if __name__ == '__main__':
#     login = TestLogin().test_cart_list()

# # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /report 目录
pytest.main(['--alluredir', './report', '--clean-alluredir'])

# 执行指定文件测试用例 -v丰富模式显示
pytest.main(['-v', "testcase/test_login.py"])

# 执行指定文件-类-方法测试用例
pytest.main(["-v", "testcase/test_login.py::TestLogin::test_cart_list"])
