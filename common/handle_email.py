
"""

smtp服务器：
smtp服务器地址：
qq邮箱：smtp.qq.com   端口：465
163邮箱：smtp.163.com  端口：465

账号：994682157@qq.com
授权码：tezhglztswgrbecj

"""

import os
from common.handlepath import REPORTSDIR
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common.handleconfig import conf

def handle_email(filename,title):

        smtp = smtplib.SMTP_SSL(host=conf.get("email","host"),port=int(conf.get("email","port")))

        smtp.login(user=conf.get("email","user"),password=conf.get("email","password"))

        # content = "林亮钦发送邮件试试"
        with open(filename,"rb") as f:

            content = f.read()

        msg = MIMEMultipart()

        msg_text = MIMEText(content,_subtype="html",_charset="utf8")

        msg.attach(msg_text)

        report_file = MIMEApplication(content)

        report_file.add_header('content-disposition','attachment',filename=title)

        msg.attach(report_file)

        msg["Subject"] = title

        msg["From"] = conf.get("email","from_addr")

        msg["To"] = conf.get("email","to_addrs")

        smtp.send_message(msg,from_addr=conf.get("email","from_addr"),to_addrs=conf.get("email","to_addrs"))







