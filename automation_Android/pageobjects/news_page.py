# coding=utf-8
import time
from framework.base_page import BasePage
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()

class news(BasePage):
      #电报按钮
      dianbao_button='xpath=>(//android.widget.TextView[@text="电报"])[0]'
      #要闻按钮
      yaowen_button='xpath=>(//android.widget.TextView[@text="事件"])[0]'
      #分类按钮
      fenlei_button='id=>com.gelonghui.glhapp:id/fab'
      #公告摘要
      zhaiyao_button='xpath=>(//android.widget.TextView[@text="公告摘要"])[0]'
      #大行评级
      pingji_button='xpath=>(//android.widget.TextView[@text="大行评级"])[0]'
      #业绩会直击
      zhiji_button='xpath=>(//android.widget.TextView[@text="业绩会直击"])[0]'
      #港股异动
      yidong_button='xpath=>(//android.widget.TextView[@text="港股异动"])[0]'
      #公司信息
      gs_button='xpath=>(//android.widget.TextView[@text="公司信息"])[0]'
      #行业信息
      hy_button='xpath=>(//android.widget.TextView[@text="行业信息"])[0]'
      #全部
      all_button = 'xpath=>(//android.widget.TextView[@text="全部"])[0]'
      #列表第一篇要闻
      list_button = 'xpath=>(//android.widget.LinearLayout)[0]'
      #详情页返回键
      return_key_utton='id=>com.gelonghui.glhapp:id/ab_back'
      #字体放大缩小键
      font_button='id=>com.gelonghui.glhapp:id/extra_space'
      #分享按钮
      share_button='id=>com.gelonghui.glhapp:id/ab_right_icon'



      #分类
      def classify(self):
          #点击电报按钮
          self.click(self.dianbao_button)
          logger.info('点击电报')
          # 点击事件按钮
          self.click(self.yaowen_button)
          logger.info('点击事件')
          # 点击分类按钮
          self.click(self.fenlei_button)
          logger.info('点击分类按钮')
          time.sleep(1)
      def classify_ggzy(self):
          # 点击公告摘要按钮
          self.click(self.zhaiyao_button)
          logger.info('点击公告摘要分类')
          time.sleep(1)
      def classify_dxpj(self):
          # 点击大行评级按钮
          self.click(self.pingji_button)
          logger.info('点击大型评级分类')
          time.sleep(1)
      def classify_yjhzj(self):
          # 点击业绩会直击按钮
          self.click(self.zhiji_button)
          logger.info('点击业绩会直击分类')
          time.sleep(1)
      def classify_ggyd(self):
          # 点击港股异动按钮
          self.click(self.yidong_button)
          logger.info('点击港股异动分类')
          time.sleep(1)
      def classify_gsxx(self):
          # 点击公司信息按钮
          self.click(self.gs_button)
          logger.info('点击公司信息分类')
          time.sleep(1)
      def classify_hyxx(self):
          # 点击行业信息按钮
          self.click(self.hy_button)
          logger.info('点击行业信息分类')
          time.sleep(1)
      def classify_all(self):
          # 点击全部按钮
          self.click(self.all_button)
          logger.info('点击全部分类')
          time.sleep(1)
      def news_list(self):
          self.click(self.list_button)
          logger.info('点击第一条要闻')
      def news_details_return(self):
          self.click(self.return_key_utton)
          logger.info('点击返回键按钮')
      def news_details_font(self):
          self.click(self.font_button)
          logger.info('点击字体放大键')
