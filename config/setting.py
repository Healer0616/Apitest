# -*- coding: utf-8 -*- 
# @Time    : 2021/1/23 下午3:12
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : config.py
# @Software: PyCharm

# [DATABASE]
host = "127.0.0.1"
username = "root"
password = "123456"
port = "3306"
database = ""

# [HTTP]
# 接口的url
base_url = "http://zx.1daas.com/api"
# port = "8080"
timeout = "1.0"

# [EMAIL]
mail_host = "smtp.qq.com"
# 发件人邮箱
mail_sender = "1175429380@qq.com"
# 发件人授权码
mail_pass = "wpanjothgyvkhcif"
# 端口号默认:25 SSL:465
mail_port = 25
# 收件人邮箱
mail_receiver = "healer0616@126.com"
# 主题
subject = "主题"
# 正文
content = "正文"
# 测试报告路径
reports_path = "/Users/healer/Desktop/测试文件/测试图片/30.jpg"
# 文件名称filename可以任意写，写什么名字，邮件中显示什么名字
file_name = "自动化测试报告"
testuser = "Someone"
on_off = 1
