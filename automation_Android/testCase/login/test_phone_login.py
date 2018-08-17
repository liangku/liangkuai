import time
import unittest
from framework.logger import MyLog
from framework.app_engine import OpenApp
from pageobjects.login_page import Login

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()


class OpenTheApp(unittest.TestCase):

        @classmethod
        def setUp(cls):
            app = OpenApp(cls)
            cls.driver = app.open_app()

        @classmethod
        def tearDown(cls):
            cls().driver.quit()
        # 登录失败

        # 登录成功
        def test_login(self):
            # screen_shot = BasePage(self.driver)
            login_test = Login(self.driver)
            login_test.login()

            time.sleep(2)


if __name__ == '__main__':
    unittest.TestSuite()
    # suite = unittest.TestSuite()
    # suite.addTest(OpenTheApp('test_login'))
