# coding=utf-8
import time
from framework.base_page import BasePage
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()

class zl(BasePage):
      #研究按钮
      yanjiu_button='xpath=>(//android.widget.TextView[@text="研究"])'
      #专栏按钮
      zl_button = 'xpath=>(//android.widget.TextView[@text="专栏"])'
      #第一条专栏文章
      first_zl='id=>com.gelonghui.glhapp:id/background'
      #详情页返回键
      zl_return='id=>com.gelonghui.glhapp:id/iv_back'
      #订阅按钮
      dingyue_button='id=>com.gelonghui.glhapp:id/item_btn_subscribe'
      #作家icon
      zuojia_icon='id=>com.gelonghui.glhapp:id/author_page_icon'
      #喜欢按钮
      like_button='id=>com.gelonghui.glhapp:id/iv_like'
      #收藏按钮
      shoucang_button='id=>com.gelonghui.glhapp:id/iv_fav'
      #评论按钮
      comment_button='id=>com.gelonghui.glhapp:id/iv_comment'
      #评论页
      #评论输入框
      comment_send='id=>com.gelonghui.glhapp:id/et_write_comment'
      #发表按钮
      fabiao_button='id=>com.gelonghui.glhapp:id/tv_comment_publish'
      #评论页返回键
      back_button='id=>com.gelonghui.glhapp:id/ib_back'

      #登录页

      title_icon='id=>com.gelonghui.glhapp:id/tv_main_title'

      def zl_details(self):
          self.click(self.yanjiu_button)
          logger.info('点击研究')
          self.click(self.zl_button)
          logger.info('点击专栏')
          self.click(self.first_zl)
          logger.info('点击首篇专栏,进入专栏详情页')
      def reback_zl(self):
          self.click(self.zl_return)
          logger.info('点击详情页的返回键')
      def dingyue(self):
          self.click(self.dingyue_button)
          logger.info('点击订阅按钮')
      def like(self):
          self.click(self.like_button)
          logger.info('点击喜欢按钮')
      def shoucang(self):
          self.click(self.shoucang_button)
          logger.info('点击收藏按钮')
      def comment(self):
          self.click(self.comment_button)
          logger.info('点击评论按钮，进入评论页')
      def send_comment(self,a):
          self.click(self.comment_button)
          self.send_keys(self.comment_button,a)
          logger.info('输入评论',a)
      def get_comment(self):
          self.click(self.fabiao_button)
          logger.info('点击提交评论')
      def comment_back(self):
          self.click(self.back_button)
          logger.info('点击评论页的返回键')
