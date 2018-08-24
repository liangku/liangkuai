import unittest
import HTMLTestRunner
import time
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
def send_email(newfile):

    # 第一步
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    content = f.read()
    f.close()



    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码
    user = 'm17512064966@163.com'
    password = 'zhy995217'
    # 发送邮箱
    sender = 'm17512064966@163.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['1172676410@qq.com','2025694956@qq.com']
    # 发送邮件主题
    subject = '要闻列表自动化测试报告'

    # 编写 HTML类型的邮件正文
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    #    msg = MIMEText(mail_body,'html','utf-8')

    #添加附件
    msg = MIMEMultipart('mixed')
    msg_html = MIMEText(content, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    #邮件头信息
    msg['From'] = user
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接服务器，发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    print('=====开始测试======')
    # 1.执行测试用例，生成最新的测试用例
    # 指定测试用例为当前文件夹下的test_case目录
    # 如果用/可以不用r
    test_dir='./test_case'
    # Windows的cmd执行：python "D:\system files\workspace\selenium\test_project\runtest_htmltestrunner_autosendemail.py"
    # 不用绝对路径会报：ImportError: Start directory is not importable: './test_case'
    # test_dir = 'C:\auto\news\test_Case'
    # 知道测试报告的路径
    test_report_dir = '.\\test_report\\html_result'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime('%Y-%m-%d %H-%M')
    filename = test_report_dir + '\\' + now + 'html_result.html'
    fp = open(filename, 'wb')

    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          title='测试报告',
                                          description='用例执行情况：')
    runner.run(discover)
    fp.close()

    # 取最新测试报告
    new_report = new_file(test_report_dir)
    # 调试用的
    #    print new_report

    #发送邮件，发送最新测试报告html
    send_email(new_report)
    print('测试结束，注意查收报告邮件!')