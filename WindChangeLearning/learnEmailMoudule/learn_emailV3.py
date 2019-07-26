import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header 
import csv

#定义变量
username = input('请输入你的邮箱账号:') #'jkuanming@qq.com'
password = input('请输入你的邮箱密码:') 
from_addr = input('请输入你的发件人邮箱地址:') #'jkuanming@qq.com'
smtp_server = 'smtp.qq.com'
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python'''

data = [['jkm1','jkuanming@aliyun.com'],['jkm2','kuanming.jiang@georgfischer.com']]
# 写入收件人数据
with open(r'D:\Python Code\WindChangeLearning\learnEmailMoudule\to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# 读取收件人数据，并启动写信和发信流程
with open(r'D:\Python Code\WindChangeLearning\learnEmailMoudule\to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader: 
        #从CSV文件中遍历邮件地址
        to_addrs=row[1]
        #定义邮件正文内容、发件人、收件人、主题
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        #开启发信服务
        server.connect(smtp_server,465)
        #登陆发信邮箱
        server.login(from_addr, password)
        #发送邮件
        server.sendmail(from_addr, to_addrs, msg.as_string())

# 关闭服务器
server.quit()