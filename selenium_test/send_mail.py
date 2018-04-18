import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户/密码
user = '15757166414@163.com'
password = 'cyx19940118'
#发送邮箱
sender = '15757166414@163.com'
#接收邮箱
receiver = '523872429@qq.com'
#发送邮件主题
subject = 'Python email test'
#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['subject'] = Header(subject,'utf-8')
#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()