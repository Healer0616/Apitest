# -*- coding: utf-8 -*- 
# @Time    : 2021/1/7 11:45 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : logger.py
# @Software: PyCharm

import logging

# filemode:覆盖写入
logging.basicConfig(filename="logs", filemode="w", level=logging.DEBUG,
                    format='日期：%(asctime)s - 名称：%(name)s - %(message)s - %(levelno)s - %(levelname)s - %(pathname)s - %(filename)s - %(funcName)s - %(lineno)d - %(thread)d - %(threadName)s - %(process)d')

logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')
logging.error("this is error message")
