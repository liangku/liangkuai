
import unittest
from framework.logger import MyLog
from framework.app_engine import OpenApp
from pageobjects.zhuanlan_page import zl
from pageobjects.zhuanlan_author_page import zl_author
log = MyLog.get_log()
logger = log.getlog()


class zhuanlan(unittest.TestCase):

        @classmethod
        def setUp(cls):
            app = OpenApp(cls)
            cls.driver = app.open_app()

        @classmethod
        def tearDown(cls):
            cls().driver.quit()
        def test_nologin_dingyue(self):
            '''专栏订阅测试用例(未登录条件)'''
            #进入专栏详情页
            zl.zl_details()
            #点击订阅按钮
            zl.dingyue()
            #断言未登录时跳转到登录页
            Text=self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_main_title')
            text1=Text.text
            self.assertEqual('登录',text1)
        def test_nologin_like(self):
            '''专栏文章点赞（未登录条件）'''
            #进入专栏文章详情页
            zl.zl_details()
            #点击爱心按钮
            zl.like()
            #断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_main_title')
            text2 = Text.text
            self.assertEqual('登录', text2)
        def test_nologin_shoucang(self):
            '''专栏文章收藏（未登录条件）'''
            #进入专栏文章详情页
            zl.zl_details()
            #点击收藏按钮
            zl.shoucang()
            #断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_main_title')
            text3 = Text.text
            self.assertEqual('登录', text3)
        def test_nologin_author_dy(self):
            '''专栏作家的订阅测试用例（未登录）'''
            #进入专栏作家详情页
            zl.zuojia_icon()
            #点击订阅
            zl_author.dy_button()
            #断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_main_title')
            text4 = Text.text
            self.assertEqual('登录', text4)
        def test_nologin_comment(self):
            '''专栏文章评论测试用例（未登录）'''
            #进入文章详情页
            zl.zl_details()
            #点击评论按钮
            zl.comment()
            #输入评论
            zl.send_comment('文章不错')
            #提交评论
            zl.get_comment()
            #断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_main_title')
            text4 = Text.text
            self.assertEqual('登录', text4)


if __name__ == '__main__':
            unittest.TestSuite()
