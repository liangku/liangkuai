from  appium  import webdriver
import time
from news.common.screen import screen_shot
from news.common.swipe import swipe_up,swipe_down
import unittest
class glhapp(unittest.TestCase):
      @classmethod
      def setUp(self):
          desired_caps = {
                    'platformName':'Android',
                    'deviceName':'MI 4LTE',
                    'platformVersion':'6.1.0',
                    'unicodeKeyboard':'True',
                    'resetKeyboard':'True',
                    'appPackage':'com.gelonghui.glhapp',
                    'appActivity':'com.gelonghui.glhapp.activity.MainActivity'
                }
          self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
          driver=self.driver
          time.sleep(10)
          ac=self.driver.current_activity
          print(ac)
          self.driver.wait_activity(".activity.MainActivity", 30)

          while 1:
              try:
                  driver.find_element_by_id("com.gelonghui.glhapp:id/tv_tab_title").click()  # 电报
                  time.sleep(1)
                  break
              except Exception as e:
                  print("exception:")
                  print(e)
      @classmethod
      def tearDown(self):
          self.driver.quit()

      #要闻分类
      def test_news_type(self):
        ''''要闻分类用例'''

        driver = self.driver
        ele0 = driver.find_element_by_id('com.gelonghui.glhapp:id/fab')
        ele0.click()
        time.sleep(1)
        ele = driver.find_elements_by_xpath
        ele('//android.widget.TextView[@text="公告摘要"]')[0].click()
        time.sleep(3)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是公共摘要列表页')

        # ele0.click()
        # ele('//android.widget.TextView[@text="公告摘要"]')[0].click()
        # time.sleep(1)
        # screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是公共摘要列表页')

        time.sleep(1)
        ele0.click()
        ele('//android.widget.TextView[@text="大行评级"]')[0].click()
        time.sleep(1)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是大行评级列表页')

        time.sleep(1)
        ele0.click()
        ele('//android.widget.TextView[@text="业绩会直击"]')[0].click()
        time.sleep(1)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是业绩会直击列表页')

        time.sleep(1)
        ele0.click()
        ele('//android.widget.TextView[@text="港股异动"]')[0].click()
        time.sleep(1)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是港股异动列表页')

        time.sleep(1)
        ele0.click()
        ele('//android.widget.TextView[@text="公司信息"]')[0].click()
        time.sleep(1)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是公司信息列表页')

        time.sleep(1)
        ele0.click()
        ele('//android.widget.TextView[@text="行业信息"]')[0].click()
        time.sleep(1)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是行业信息列表页')

        time.sleep(1)
        ele0.click()
        ele('//android.widget.TextView[@text="全部"]')[0].click()
        time.sleep(1)
        screen_shot(self, '//test_report//img_result//img_classify//', '验证是否是全部列表页')

      #要闻返回键功能
      def test_return_key(self):
          '''返回键功能测试用例'''
          driver = self.driver
          driver.find_elements_by_xpath('//android.widget.LinearLayout')[0].click()
          el= driver.find_element_by_id
          el1 = driver.find_elements_by_xpath
          el1('//android.widget.LinearLayout')[0].click()
          time.sleep(1)
          el('com.gelonghui.glhapp:id/ab_back').click()
          time.sleep(1)
          # 截图断言是否回到要闻页
          screen_shot(self,'//news//test_report//img_result//','断言是否回到要闻页')

      #要闻字体放大缩小
      def test_family_font(self):
          '''字体放大缩小用例'''
          driver = self.driver
          ele = driver.find_element_by_id
          ele1 = driver.find_elements_by_xpath
          ele1('//android.widget.LinearLayout')[0].click()
          time.sleep(3)
          ele('com.gelonghui.glhapp:id/extra_space').click()
          time.sleep(3)
          screen_shot(self,'//test_report//img_result//img_font//','要闻详情页字体放大后')

          time.sleep(3)
          ele('com.gelonghui.glhapp:id/extra_space').click()
          time.sleep(3)
          screen_shot(self, '//test_report//img_result//img_font//', '要闻详情页字体还原后')

      #要闻分享
      def test_news_share(self):
          '''分享测试用例'''
          driver=self.driver
          driver.find_elements_by_xpath('//android.widget.LinearLayout')[0].click()
          e01 = driver.find_element_by_id
          e02 = driver.find_elements_by_xpath
          e02('//android.widget.LinearLayout')[0].click()
          try:
              e01('com.gelonghui.glhapp:id/ab_right_icon').click()
          except Exception as e:
              print(e)
          time.sleep(1)
          e02('//android.widget.TextView[@text="QQ空间"]')[0].click()
          time.sleep(2)
          e01('com.tencent.mobileqq:id/ivTitleBtnRightText').click()
      def test_news_swipe_up(self):
          '''上滑、下滑滑动测试用例'''
          swipe_up(self,n=1)
          screen_shot(self, '//test_report//img_result//img_swipe//', '向上滑动截图')
          time.sleep(1)
          swipe_down(self,n=1)
          screen_shot(self, '//test_report//img_result//img_swipe//', '向下滑动截图')