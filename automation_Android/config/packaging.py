import os
import glob
import zipfile
import config.readConfig as readConfig
from email.mime.multipart import MIMEMultipart
from framework.logger import MyLog


localReadConfig = readConfig.Readconfig()


class Packaging(object):

    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.getlog()
        self.msg = MIMEMultipart('mixed')

    def packag(self):
        """
        打包文件
        :return: 
        """
        if self.check_file():
            reportpath = self.log.get_result_path()
            zippath = os.path.join(readConfig.project_path, "test_report", "test.zip")
            # zip file
            files = glob.glob(reportpath + '/*')
            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            for file in files:
                f.write(file, '/report/'+os.path.basename(file))
            f.close()

    def check_file(self):
        reportpath = self.log.get_result_path()
        if not os.path.isfile(reportpath) and os.stat(reportpath) != 0:
            return True
        else:
            return False
