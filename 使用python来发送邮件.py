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
from BeautifulReport import BeautifulReport

smtp = smtplib.SMTP_SSL(host="smtp.qq.com",port=465)
smtp.login(user="994682157@qq.com",password="tezhglztswgrbecj")

# content = "林亮钦发送邮件试试"

with open(os.path.join(REPORTSDIR,"reports2.html"),"rb") as f:
    content = f.read()


msg = MIMEMultipart()

msg_text = MIMEText(content,_subtype="html",_charset="utf8")

msg.attach(msg_text)

report_file = MIMEApplication(content)

report_file.add_header('content-disposition','attachment',filename="测试报告.html")

msg.attach(report_file)

msg["Subject"] = "林亮钦的邮件"

msg["From"] = "994682157@qq.com"

msg["To"] = "994682157@qq.com"

smtp.send_message(msg,from_addr="994682157@qq.com",to_addrs="994682157@qq.com")









