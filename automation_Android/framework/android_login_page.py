# coding=utf-8
import time
from framework.base_page import BasePage
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()

class android_login(BasePage):
      #返回键
      login_return_button='id=>com.gelonghui.glhapp:id/ib_back'
      #登录页标题
      login_title='id=>com.gelonghui.glhapp:id/tv_main_title'
      #用户名
      username_input='id=>com.gelonghui.glhapp:id/login_username'
      #密码
      password_input='id=>com.gelonghui.glhapp:id/login_password'
      #登录按钮
      login_button='id=>com.gelonghui.glhapp:id/btn_login'


      def login_text(self,username,passwd):
          self.click(self.username_input)
          self.send_keys(self.username_input,username)
          logger.info('输入账号')
          self.click(self.password_input)
          self.send_keys(self.password_input,passwd)
          logger.info('输入密码')
          self.click(self.login_button)
          logger.info('点击登录按钮')
          time.sleep(1)

