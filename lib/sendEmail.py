# -*- coding: utf-8 -*- 
# @Time    : 2021/1/25 下午3:49
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : sendEmail.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import setting


class SendEmail:
    """
    封装发送邮件类
    """

    def __init__(self):
        # 把qq邮箱的服务器地址赋值到变量mail_host上，地址应为字符串格式
        self.qqmail = smtplib.SMTP()
        # 实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
        self.qqmail.connect(setting.mail_host, setting.mail_port)
        # 连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
        # 以上，皆为连接服务器。

        # 获取邮箱密码，为字符串格式 密码为授权码，不可用真实密码
        self.qqmail.login(setting.mail_sender, setting.mail_pass)
        # 登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
        # 以上，皆为登录邮箱。

    def send_text(self):
        """
        文本邮件
        :return:
        """
        # 获取收件人的邮箱。
        msg = MIMEText(setting.content, 'plain', 'utf-8')
        # 实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
        msg['Subject'] = Header(setting.subject, 'utf-8')
        # 在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
        # 以上，为填写主题和正文。
        try:
            self.qqmail.sendmail(setting.mail_sender, setting.mail_receiver, msg.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')
        self.qqmail.quit()

    def send_file(self):
        """
        发送测试报告邮件
        """
        # 读取报告文件中的内容
        file_content = open(setting.reports_path, "rb").read()
        # 2.使用email构造邮件
        # （1）构造一封多组件的邮件
        msg = MIMEMultipart()
        # (2)往多组件邮件中加入文本内容
        msg.attach(MIMEText(setting.content, 'plain', "utf8"))
        # (3)往多组件邮件中加入文件附件
        file_msg = MIMEApplication(file_content)
        file_msg.add_header('content-disposition', 'attachment', filename=setting.file_name)
        msg.attach(file_msg)
        # 添加发件人
        msg["From"] = setting.mail_sender
        # 添加收件人
        msg["To"] = setting.mail_receiver
        # 添加邮件主题
        msg["subject"] = setting.subject
        # 第四步：发送邮件
        try:
            self.qqmail.send_message(msg, from_addr=setting.mail_sender, to_addrs=setting.mail_receiver)
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')
        self.qqmail.quit()


if __name__ == '__main__':
    se = SendEmail()
    se.send_file()
