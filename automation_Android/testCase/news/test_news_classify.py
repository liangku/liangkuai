import time
import unittest
from framework.logger import MyLog
from framework.app_engine import OpenApp
from framework.base_page import BasePage
from pageobjects.news_page import news
from config.swipe import swipe_up
log = MyLog.get_log()
logger = log.getlog()


class test_news(unittest.TestCase):

        @classmethod
        def setUp(cls):
            app = OpenApp(cls)
            cls.driver = app.open_app()

        @classmethod
        def tearDown(cls):
            cls().driver.quit()
        def test_news_type(self):
            '''事件分类用例'''
            classify=news(self.driver)
            screen = BasePage(self.driver)
            #进入要闻页
            classify.classify()
            screen.get_screen_shot()
            time.sleep(1)
            #分类公告摘要
            classify.classify_ggzy()
            screen.get_screen_shot()
            time.sleep(1)
            #分类大型评级
            classify.classify_dxpj()
            screen.get_screen_shot()
            time.sleep(1)
            #分类业绩会直击
            classify.classify_yjhzj()
            screen.get_screen_shot()
            time.sleep(1)
            #分类港股异动
            classify.classify_ggyd()
            screen.get_screen_shot()
            time.sleep(1)
            #分类公司信息
            classify.classify_gsxx()
            screen.get_screen_shot()
            time.sleep(1)
            #分类行业信息
            classify.classify_hyxx()
            screen.get_screen_shot()
            time.sleep(1)
            #全部
            classify.classify_all()
            screen.get_screen_shot()

        def test_return_key(self):
            '''事件详情页返回键用例'''
            details01=news(self.driver)
            screen=BasePage(self.driver)
            #进入详情页
            details01.list_button()
            screen.get_screen_shot()
            #返回键
            details01.font_button()
            screen.get_screen_shot()
        def test_font(self):
            '''事件详情页字体放大缩小用例'''
            details02= news(self.driver)
            screen = BasePage(self.driver)
            # 进入详情页
            details02.list_button()
            #放大
            details02.font_button()
            time.sleep(2)
            screen.get_screen_shot()
            #缩小
            details02.font_button()
            time.sleep(2)
            screen.get_screen_shot()
        def test_swipe(self):
            '''事件列表的滑动用例'''
            shijian=news(self.driver)
            screen=BasePage(self.driver)
            #进入事件列表
            shijian.classify()
            #向上滑动两次
            swipe_up(self,2)
            screen.get_screen_shot()



if __name__ == '__main__':
    unittest.TestSuite()








