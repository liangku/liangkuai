from automation_iOS_app.framework.base_page import BasePage


class Popup_window_button(BasePage):

    popup_window_tag = "type == 'XCUIElementTypeButton' AND label == '稍后查看'"

    def click_popup_window_tag(self):
        self.click(self.popup_window_tag)
