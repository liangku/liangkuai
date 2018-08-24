import time
from news.common.screen import screen_shot
from news.common.app_start import setUp_app,tearDown_app
from news.common.swipe import swipe_up,swipe_down
def test_news_swipe_up_down(self):
          '''上滑、下滑滑动测试用例'''
          setUp_app()

          swipe_up(n=1)
          screen_shot(self, '//test_report//img_result//img_swipe//', '向上滑动截图')
          time.sleep(1)
          swipe_down(n=1)
          screen_shot(self, '//test_report//img_result//img_swipe//', '向下滑动截图')

          tearDown_app()