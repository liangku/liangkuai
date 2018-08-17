# _*_coding=utf-8_*_
import logging
from datetime import datetime
import os
import threading

class Logger(object):


    def __init__(self):
        """
        指定保存日志的文件路径，级别，一级调用文件将日志存入指定的文件中
        """
        global logPath, resultPath

        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志地址
        project_path = os.path.dirname(os.path.abspath('.'))
        resultPath = project_path + r'/test_report/'
        # 创建result文件夹
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # 使用当前时间作为log文件名
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 创建log文件
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        # 创建一个 handler 到log文件
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))

        # # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(handler)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

    def get_result_path(self):
        """
        获取log存放地址
        :return:
        """
        return logPath

    def get_report_path(self):
        """
        获取report存放地址
        :return:
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

class MyLog(object):
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Logger()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")