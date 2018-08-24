import requests
import API_automation.config.readConfig as readConfig
from API_automation.common.logger import MyLog as Log
import json

localReadConfig = readConfig.ReadConfig()


class ConfigHttp(object):

    def __init__(self):
        global host, timeout
        host = localReadConfig.get_http("base_url")
        timeout = localReadConfig.get_http("timeout")
        # 不知道用哪个
        # self.logger = Logger(logger="OpenApp").getlog()
        self.logger = Log.get_log()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        """
        组装URL
        :param url: 
        :return: 
        """
        self.url = host + url

    def set_headers(self, header):
        """
        传headers
        :param header: 
        :return: 
        """
        self.headers = header

    def set_params(self, param):
        """
        params传参
        :param param: 
        :return: 
        """
        self.params = param

    def set_data(self, data):
        """
        data传参
        :param data: 
        :return: 
        """
        self.data = json.dumps(data)

    def set_files(self, file):
        """
        发送文件
        :param file: 
        :return: 
        """
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
