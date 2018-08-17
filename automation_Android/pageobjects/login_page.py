# coding=utf-8
import time
from framework.base_page import BasePage
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()

class Login(BasePage):

    # 个人中心图标
    personal_center_icon = 'xpath=>//XCUIElementTypeButton[@name="NavigationBar Mine"]'
    # 个人中心的登录按钮
    login_button = 'xpath=>//XCUIElementTypeButton[@name="登录"]'
    # 登录页的输入框和登录按钮
    account_entry_box = 'predicate=>type == "XCUIElementTypeTextField" AND value == "手机号/电子邮箱"'
    password_entry_box = 'predicate=>type == "XCUIElementTypeSecureTextField" AND value == "密码"'
    big_login_button = 'predicate=>type == "XCUIElementTypeButton" AND label == "登录" AND visible == true'
    # 登录页的返回按钮、页面title、注册按钮
    loginpage_back_button = 'xpath=>//XCUIElementTypeButton[@name="NavigationBar Back"]'
    login_page_title = 'xpath=>//XCUIElementTypeOther[@name="登录"]'
    # 系统设置页
    setting_page_title = 'xpath=>//XCUIElementTypeOther[@name="系统设置"]'
    settingpage_back_button = 'xpath=>//XCUIElementTypeButton[@name="返回"]'
    language_selection = 'xpath=>//XCUIElementTypeStaticText[@name="语言选择"]'
    # 意见反馈页
    feedback_page_title = 'xpath=>//XCUIElementTypeStaticText[@name="NavigationBar-TitleView"]'
    feedbackpage_back_button = 'xpath=>//XCUIElementTypeButton[@name="返回"]'

    # 图标
    # "消息中心"图标
    icon_me_message = 'xpath=>//XCUIElementTypeImage[@name="icon_me_message"]'
    # "我的主页"图标
    icon_me_home = 'xpath=>//XCUIElementTypeImage[@name="icon_me_home"]'
    # "我的发表"图标
    icon_me_sent = 'xpath=>//XCUIElementTypeImage[@name="icon_me_sent"]'
    # "我的收藏"图标
    icon_me_collect = 'xpath=>//XCUIElementTypeImage[@name="icon_me_collect"]'
    # "我的订阅"图标
    icon_me_sub = 'xpath=>//XCUIElementTypeImage[@name="icon_me_sub"]'
    # "系统设置"图标
    icon_me_setting = 'xpath=>//XCUIElementTypeImage[@name="icon_me_setting"]'
    # "意见反馈"图标
    icon_me_feedback = 'xpath=>//XCUIElementTypeImage[@name="icon_me_feedback"]'
    # "关于格隆汇"图标
    icon_me_about = 'xpath=>//XCUIElementTypeImage[@name="icon_me_about"]'

    # 按钮名称
    # 消息中心
    me_message_name = 'xpath=>//XCUIElementTypeStaticText[@name="消息中心"]'
    # 我的主页
    me_home_name = 'xpath=>//XCUIElementTypeStaticText[@name="我的主页"]'
    # 我的发表
    me_sent_name = 'xpath=>//XCUIElementTypeStaticText[@name="我的发表"]'
    # 我的收藏
    me_collect_name = 'xpath=>//XCUIElementTypeStaticText[@name="我的收藏"]'
    # 我的订阅
    me_sub_name = 'xpath=>//XCUIElementTypeStaticText[@name="我的订阅"]'
    # 系统设置
    me_setting_name = 'xpath=>//XCUIElementTypeStaticText[@name="系统设置"]'
    # 意见反馈
    me_feedback_name = 'xpath=>//XCUIElementTypeStaticText[@name="意见反馈"]'
    # 关于格隆汇
    me_about_name = 'xpath=>//XCUIElementTypeStaticText[@name="关于格隆汇"]'

    # 按钮
    # 消息中心
    me_message_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[1]'
    # 我的主页
    me_home_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[2]'
    # 我的发表
    me_sent_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[3]'
    # 我的收藏
    me_collect_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[4]'
    # 我的订阅
    me_sub_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[5]'
    # 系统设置
    me_setting_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[6]'
    # 意见反馈
    me_feedback_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[7]'
    # 关于格隆汇
    me_about_button = 'xpath=>(//XCUIElementTypeButton[@name="更多信息"])[8]'

    # 登录
    def login(self):
        # 点击左上方"个人中心"图标
        self.click(self.personal_center_icon)
        logger.info('点击左上方"个人中心"图标')
        time.sleep(1)
        # 在个人中心点击"登录"按钮
        self.click(self.login_button)
        logger.info('在个人中心点击"登录"按钮')
        time.sleep(1)
        # 在账号输入框输入账号
        self.click(self.account_entry_box)
        self.send_keys(self.account_entry_box, "13714050924")
        logger.info('输入账号')
        time.sleep(1)
        # 在密码输入框输入密码
        self.click(self.password_entry_box)
        self.send_keys(self.password_entry_box, "111111")
        logger.info('输入密码')
        time.sleep(1)
        # 点击登录页"登录"按钮
        self.click(self.big_login_button)
        logger.info('在登录页点击"登录"按钮')

    # 加验证的登录
    def check_login(self):
        # 点击左上方"个人中心"图标
        self.click(self.personal_center_icon)
        logger.info('点击左上方"个人中心"图标')
        time.sleep(2)
        # check图标
        self.check_element(self.icon_me_message)
        self.check_element(self.icon_me_home)
        self.check_element(self.icon_me_sent)
        self.check_element(self.icon_me_collect)
        self.check_element(self.icon_me_sub)
        self.check_element(self.icon_me_setting)
        self.check_element(self.icon_me_feedback)
        self.check_element(self.icon_me_about)
        # check按钮名称
        self.check_element(self.me_message_name)
        self.check_element(self.me_home_name)
        self.check_element(self.me_sent_name)
        self.check_element(self.me_collect_name)
        self.check_element(self.me_sub_name)
        self.check_element(self.me_setting_name)
        self.check_element(self.me_feedback_name)
        self.check_element(self.me_about_name)
        # 检查未登录跳转登录页
        # 消息中心
        self.click(self.me_message_button)
        time.sleep(1)
        self.check_element(self.login_page_title)
        logger.info('未登录----消息中心跳转登录页成功')
        self.click(self.loginpage_back_button)
        time.sleep(1)
        # 我的主页
        self.click(self.me_home_button)
        time.sleep(1)
        self.check_element(self.login_page_title)
        logger.info('未登录----消息中心跳转登录页成功')
        self.click(self.loginpage_back_button)
        time.sleep(1)
        # 我的发表
        self.click(self.me_sent_button)
        time.sleep(1)
        self.check_element(self.login_page_title)
        logger.info('未登录----消息中心跳转登录页成功')
        self.click(self.loginpage_back_button)
        time.sleep(1)
        # 我的收藏
        self.click(self.me_collect_button)
        time.sleep(1)
        self.check_element(self.login_page_title)
        logger.info('未登录----消息中心跳转登录页成功')
        self.click(self.loginpage_back_button)
        time.sleep(1)
        # 我的订阅
        self.click(self.me_sub_button)
        time.sleep(1)
        self.check_element(self.login_page_title)
        logger.info('未登录----消息中心跳转登录页成功')
        self.click(self.loginpage_back_button)
        time.sleep(1)
