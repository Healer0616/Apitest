# -*- coding: utf-8 -*- 
# @Time    : 2021/1/12 9:59 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : read_config.py
# @Software: PyCharm


from configparser import ConfigParser


class ReadConfig:
    def read_config(self, section, option, file_name=None):
        cf = ConfigParser()  # 实例化这个模块里的ConfigParser类
        cf.read(file_name, encoding='utf-8')  # 打开配置文件
        res = eval(cf.get(section, option))
        return res
