import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header 
from email.mime.application import MIMEApplication

#定义变量
username = 'jkuanming@qq.com'
password = input('请输入QQ邮箱的授权码:')
from_addr = 'jkuanming@qq.com'
to_addrs = ['jkuanming@aliyun.com']#'kuanming.jiang@georgfischer.com'
smtp_server = 'smtp.qq.com'
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
#msg = MIMEText(text,'plain','utf-8')#发送纯文本时用此行代码
msg = MIMEMultipart()
msg['From'] = Header('阿宽')
msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header('hello python world')

wordFile = 'WindChangeLearning\learnEmailMoudule\Ai-ways生成二维码.docx'
wordApart = MIMEApplication(open(wordFile, 'rb').read())
wordApart.add_header('Content-Disposition', 'attachment', filename='Ai-ways生成二维码.docx')
msg.attach(wordApart)

#开启发信服务
#以下两行为默认不加密的端口25链接邮箱服务器的方法
'''server = smtplib.SMTP()           
server.connect(smtp_server, 25) '''  
#以下两行为加密SSL端口465链接邮箱服务器的方法
server = smtplib.SMTP_SSL(smtp_server)  #如果端口是用SSL加密，请这样写代码。其中server是变量名
server.connect(smtp_server,465)         #如果出现编码错误UnicodeDecodeError，你可以这样写：server.connect('smtp.qq.com', 465,'utf-8')

#登陆发信邮箱
server.login(username, password) 

#发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())

#关闭邮箱服务
server.quit()