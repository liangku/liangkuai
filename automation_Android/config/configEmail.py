import os
import smtplib
import threading
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from framework.logger import MyLog
from config.packaging import Packaging
import config.readConfig as readConfig

localReadConfig = readConfig.Readconfig()
zippath = os.path.join(readConfig.project_path, "test_report", "test.zip")


class Email(object):

        def __init__(self):
            global host, user, password, port, sender, title, content
            host = localReadConfig.get_email("mail_host")
            user = localReadConfig.get_email("mail_user")
            password = localReadConfig.get_email("mail_pass")
            port = localReadConfig.get_email("mail_port")
            sender = localReadConfig.get_email("sender")
            title = localReadConfig.get_email("subject")
            self.value = localReadConfig.get_email("receiver")
            self.receiver = []
            # get receiver list
            for n in str(self.value).split("/"):
                self.receiver.append(n)
            # defined email subject
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.subject = title + " " + date
            # self.log = Logger(logger='')
            # self.logger = self.log.getlog()
            self.log = MyLog.get_log()
            self.logger = self.log.getlog()
            self.msg = MIMEMultipart('mixed')

        def config_header(self):
            """
            邮件配置
            :return: 
            """
            self.msg['subject'] = self.subject
            self.msg['from'] = sender
            self.msg['to'] = ";".join(self.receiver)

        def config_content(self):
            """
            发送html内容
            :return: 
            """
            f = open(os.path.join(readConfig.project_path, 'config', 'emailStyle.txt'))
            content = f.read()
            f.close()
            content_plain = MIMEText(content, 'html', 'utf-8')
            self.msg.attach(content_plain)

        def config_file(self):
            """
            添加附件
            :return: 
            """
            packaging = Packaging()
            packaging.packag()
            reportfile = open(zippath, 'rb').read()
            filehtml = MIMEText(reportfile, 'base64', 'utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
            self.msg.attach(filehtml)

        def send_email(self):
            """
            发送邮件
            :return: 
            """
            self.config_header()
            self.config_content()
            self.config_file()

            try:
                smtp = smtplib.SMTP()
                smtp.connect(host)
                smtp.login(user, password)
                smtp.sendmail(sender, self.receiver, self.msg.as_string())
                smtp.quit()
                self.logger.info("测试结果已发送至邮箱.")
            except Exception as ex:
                self.logger.error(str(ex))


class MyEmail(object):
        email = None
        mutex = threading.Lock()

        def __init__(self):
            pass

        @staticmethod
        def get_email():

            if MyEmail.email is None:
                MyEmail.mutex.acquire()
                MyEmail.email = Email()
                MyEmail.mutex.release()
            return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()