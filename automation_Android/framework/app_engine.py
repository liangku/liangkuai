from appium import webdriver
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()


class OpenApp(object):

    def __init__(self, driver):
        self.driver = driver

    def open_app(self):
        desired_caps = {"platformName": "iOS", "platformVersion": "11.4", "deviceName": "iPhone 6",
                        "automationName": "XCUITest", "bundleId": "com.gelonghui.glhapp",
                        "udid": "d41188e5675afe4996c7f5a5d8850694ffe14f79"}

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        logger.info("打开app")
        driver = self.driver
        return driver

    def quit_app(self):
        logger.info("退出app")
        self.driver.quit()
