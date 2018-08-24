import time
from news.common.screen import screen_shot
from news.common.app_start import setUp_app,tearDown_app
#要闻字体放大缩小
def test_family_font(self):
    '''字体放大缩小用例'''
    setUp_app()

    driver = self.driver
    ele = driver.find_element_by_id
    ele1 = driver.find_elements_by_xpath
    ele1('//android.widget.LinearLayout')[0].click()
    time.sleep(3)
    ele('com.gelonghui.glhapp:id/extra_space').click()
    time.sleep(3)
    screen_shot(self, '//test_report//img_result//img_font//', '要闻详情页字体放大后')

    time.sleep(3)
    ele('com.gelonghui.glhapp:id/extra_space').click()
    time.sleep(3)
    screen_shot(self, '//test_report//img_result//img_font//', '要闻详情页字体还原后')

    tearDown_app()