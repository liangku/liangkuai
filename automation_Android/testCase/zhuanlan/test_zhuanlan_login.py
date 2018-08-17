import time
import unittest
from framework.logger import MyLog
from framework.app_engine import OpenApp
from framework.base_page import BasePage
from pageobjects.zhuanlan_page import zl
from pageobjects.zhuanlan_author_page import zl_author
from framework.android_login_page import android_login
log = MyLog.get_log()
logger = log.getlog()


class zhuanlan_login(unittest.TestCase):

        @classmethod
        def setUp(cls):
            app = OpenApp(cls)
            cls.driver = app.open_app()

        @classmethod
        def tearDown(cls):
            cls().driver.quit()

        def test_login_dingyue(self):
            '''专栏订阅测试用例'''
            # 进入专栏详情页
            zl.zl_details()
            # 点击订阅按钮
            zl.dingyue()
            # 未登录去登录
            android_login.login_text('17512064966','995217')
            #订阅
            zl.dingyue()
            time.sleep(1)
            screen=BasePage(self.driver)
            screen.get_screen_shot()
            text_dingyue=self.driver.find_element_by_id('com.gelonghui.glhapp:id/btn_subscribe').text
            self.assertEqual('已订阅',text_dingyue)


        def test_login_like(self):
            '''专栏文章点赞'''
            # 进入专栏文章详情页
            zl.zl_details()
            text_like01=self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_rd_like_num').text
            # 点击爱心按钮
            zl.like()
            screen = BasePage(self.driver)
            screen.get_screen_shot()
            # 断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_rd_like_num')
            text_like02 = Text.text
            #断言点赞成功,数量+1
            self.assertEqual(text_like01+1, text_like02)

        def test_login_shoucang(self):
            '''专栏文章收藏'''
            # 进入专栏文章详情页
            zl.zl_details()
            # 点击收藏按钮
            text_shoucang01=self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_rd_fav_num').text
            zl.shoucang()
            screen = BasePage(self.driver)
            screen.get_screen_shot()
            # 断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/tv_main_title')
            text_shoucang02= Text.text
            self.assertEqual(text_shoucang01+1, text_shoucang02)

        def test_login_author_dy(self):
            '''专栏作家的订阅测试用例'''
            # 进入专栏作家详情页
            zl.zuojia_icon()
            # 点击订阅
            zl_author.dy_button()
            # 断言
            Text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/btn_subscribe')
            text = Text.text
            self.assertEqual('已订阅', text)

            screen = BasePage(self.driver)
            screen.get_screen_shot()

        def test_nologin_comment(self):
            '''专栏文章评论测试用例'''
            # 进入文章详情页
            zl.zl_details()
            # 点击评论按钮
            zl.comment()
            # 输入评论
            zl.send_comment('文章不错')
            # 提交评论
            zl.get_comment()
            time.sleep(1)
            screen = BasePage(self.driver)
            screen.get_screen_shot()
            # 断言
            text = self.driver.find_element_by_id('com.gelonghui.glhapp:id/comment_content').text
            self.assertEqual('文章不错', text)


if __name__ == '__main__':
            unittest.TestSuite()