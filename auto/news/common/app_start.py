from  appium  import webdriver
import time

def setUp_app(self):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'MI 4LTE',
        'platformVersion': '6.1.0',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True',
        'appPackage': 'com.gelonghui.glhapp',
        'appActivity': 'com.gelonghui.glhapp.activity.MainActivity'
    }
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver = self.driver
    time.sleep(10)
    ac = self.driver.current_activity
    print(ac)
    self.driver.wait_activity(".activity.MainActivity", 30)

    while 1:
        try:
            driver.find_element_by_id("com.gelonghui.glhapp:id/tv_tab_title").click()  # 电报
            time.sleep(1)
            driver.find_elements_by_xpath('//android.widget.TextView[@text="要闻"]')[0].click()  # 要闻
            break
        except Exception as e:
            print("exception:")
            print(e)
def tearDown_app(self):
    self.driver.quit()
    print('测试结束！')
