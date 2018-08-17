# _*_coding=utf-8_*_
import time
from framework.logger import MyLog
from selenium.common.exceptions import NoSuchElementException
import os

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 保存图片
    def get_screen_shot(self):
        """
        把file_path这个参数写死，直接保存到项目根目录的一个文件夹.\Screenshots下
        :return:
        """
        project_path = os.path.dirname(os.path.abspath('.'))
        file_path = project_path + r'/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('已采取截图并保存到文件夹：/screenshots')
        except Exception as e:
            logger.error('未能采取截图！%s' % e)
            self.get_screen_shot()

    # 重写定位方法
    def find_element(self, selector):

        element = ''
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        # accessibility_id定位
        if selector_by == 'accessibility_id':
            element = self.driver.find_element_by_name(selector_value)
            try:
                element = self.driver.find_element_by_accessibility_id(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # partial_link定位
        elif selector_by == 'partial_link':
            element = self.driver.find_element_by_partial_link_text(selector_value)
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # link定位
        elif selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # css定位
        elif selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # class_name定位
        elif selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # xpath定位
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # name定位
        elif selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
            try:
                element = self.driver.find_element_by_name(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        # ios_predicate定位
        elif selector_by == 'predicate':
            element = self.driver.find_element_by_ios_predicate(selector_value)
            try:
                element = self.driver.find_element_by_ios_predicate(selector_value)
                logger.info("找到 \' %s \' 元素成功"
                            "by %s via value %s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error('NoSuchElementException: %s' % e)
                self.get_screen_shot()

        return element

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('等待 %d 秒.' % seconds)

    # 点击
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("元素 \' %s \' 已点击。" % el.text)
        except NoSuchElementException as e:
            logger.error("没有点击的元素: %s" % e)

    # 输入框输入
    def send_keys(self, selector, text):
        el = self.find_element(selector)
        el.send_keys(text)

    # 检查元素是否存在
    def check_element(self, selector):
        try:
            self.find_element(selector)
            pass
        except NoSuchElementException as e:
            logger.error('NoSuchElementException: %s' % e)
            self.get_screen_shot()
