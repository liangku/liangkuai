
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



#取最新测试报告
def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path


#发送邮件，发送最新测试报告html
def send_email(newfile,u_user,u_pwd,u_sender,arr):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    content = f.read()
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码
    user = u_user
    password =u_pwd
    # 发送邮箱
    sender = u_sender
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = arr
    # 发送邮件主题
    subject = '要闻列表自动化测试报告'

    # 添加附件
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    # msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')
    msg_html = MIMEText(content, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)


    msg['From'] = user
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
