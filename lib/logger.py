# -*- coding: utf-8 -*- 
# @Time    : 2021/1/7 11:45 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : logger.py
# @Software: PyCharm

import logging
import time


class Logger:
    def __init__(self):
        # 第一步，创建一个logger
        self.logger = logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第二步，创建一个handler，利用时间戳命名用于写入日志文件
        now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
        logfile = '/Users/healer/Desktop/Code/apiTest/logs/' + now + "testlog.txt"
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)

    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger
