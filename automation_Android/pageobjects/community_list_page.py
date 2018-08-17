# coding=utf-8
from framework.base_page import BasePage


class CommunityList(BasePage):

    dynamic_tag = "predicate=>type == 'XCUIElementTypeButton' AND label == '动态'"
    add_newactivity = "xpath=>//XCUIElementTypeButton[@name='Community NewActivity']"
    check_newactivity = "xpath=>//XCUIElementTypeButton[@name='Community NewActivity']"
    hengqing = "xpath=>//XCUIElementTypeButton[@name='行情']"

    # 点击顶部"社区"tag
    def click_dynamic_tag(self):
        self.click(self.dynamic_tag)

    # 点击"新增动态"按钮
    def click_new_activit(self):
        self.click(self.add_newactivity)

    # 检查
    def check_new_activit(self):
        self.check_element(self.check_newactivity)

    # 点击行情页
    def click_hengqing_tag(self):
        self.click(self.hengqing)
