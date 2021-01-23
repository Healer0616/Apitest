# -*- coding: utf-8 -*- 
# @Time    : 2021/1/12 9:59 上午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : read_config.py
# @Software: PyCharm


from configparser import ConfigParser
import os


class ReadConfig:
    def read_config(self, section, option, file_name):
        cf = ConfigParser()  # 实例化这个模块里的ConfigParser类
        cf.read(file_name, encoding='utf-8')  # 打开配置文件
        result = cf.get(section, option)
        return result


if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.abspath("read_config.py"))  # 获取当前文件所在目录的上一级目录,绝对路径
    res = ReadConfig().read_config(section='HTTP', option='host', file_name=os.path.join(root_dir, "config.ini"))
    print(res)
