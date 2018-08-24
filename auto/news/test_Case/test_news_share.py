import time
from news.common.app_start import setUp_app,tearDown_app
#要闻分享
def test_news_share(self):
    '''分享测试用例'''
    setUp_app()

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

    tearDown_app()