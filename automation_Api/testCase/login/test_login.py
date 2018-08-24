import paramunittest
import unittest
from API_automation.common.configHttp import ConfigHttp
from API_automation.common.logger import MyLog
from API_automation.common import configExcel
import os

configHttp = ConfigHttp()
login_xls = configExcel.get_xls("login.xlsx", "login")
print(login_xls)


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):
    """GET  /api/recommend/article/getList"""

    def setParameters(self, case_name, method, userName, password, statusCode, message):
        """
        set param
        :param case_name:
        :param method:
        :param userName:
        :param password:
        :param statusCode:
        :param message:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.userName = str(userName)
        self.password = str(password)
        self.statusCode = str(statusCode)
        self.message = str(message)
        self.info = None
        self.response = None

    def description(self):
        """
        test report description
        :return:
        """
        return self.case_name

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def test_postlogin(self):
        # set header
        header = {"Content-Type": "application/json"}
        configHttp.set_headers(header)
        # set url
        configHttp.set_url('/api/user/login')
        # set data
        data = {'userName': self.userName, 'password': self.password}
        configHttp.set_data(data)
        # change method
        if self.method == 'get':
            self.response = configHttp.get()
        elif self.method == 'post':
            self.response = configHttp.post()
        else:
            self.logger.info("No this interface's method:" + self.method)

        # check result
        self.checkResult()

    def tearDown(self):
        pass

    def checkResult(self):
        """
        check result
        :return:
        """
        self.info = self.response.json()
        print(self.info)
