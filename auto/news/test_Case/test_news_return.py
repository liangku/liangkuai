import time
from news.common.screen import screen_shot
from news.common.app_start import setUp_app,tearDown_app
# 要闻返回键功能
def test_return_key(self):
    '''返回键功能测试用例'''
    setUp_app()

    driver = self.driver
    driver.find_elements_by_xpath('//android.widget.LinearLayout')[0].click()
    el = driver.find_element_by_id
    el1 = driver.find_elements_by_xpath
    el1('//android.widget.LinearLayout')[0].click()
    time.sleep(1)
    el('com.gelonghui.glhapp:id/ab_back').click()
    time.sleep(1)
    # 截图断言是否回到要闻页
    screen_shot(self, '//news//test_report//img_result//', '断言是否回到要闻页')

    tearDown_app()