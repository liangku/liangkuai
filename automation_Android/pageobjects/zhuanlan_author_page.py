# coding=utf-8
from framework.base_page import BasePage
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()

class zl_author(BasePage):
      #元素

      #返回按钮
      fh_button='id=>com.gelonghui.glhapp:id/iv_back'
      #数量图标
      count_icon='id=>com.gelonghui.glhapp:id/tv_nickname'
      #订阅按钮
      dy_button='id=>com.gelonghui.glhapp:id/btn_subscribe'
      #第一篇文章
      first_message='xpath=>(//android.widget.LinearLayout)[0]'

      #动作

      def  author_fh(self):
           self.click(self.fh_button)
           logger.info('点击返回按钮')
      def  author_dy(self):
            self.click(self.dy_button)
            logger.info('点击订阅')
      def  author_first(self):
            self.click(self.first_message)
            logger.info('点击第一篇文章')