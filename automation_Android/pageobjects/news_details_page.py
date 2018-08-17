from framework.base_page import BasePage
from framework.logger import MyLog

# 实例化日志
log = MyLog.get_log()
logger = log.getlog()

class news_details(BasePage):
      #列表第一篇要闻
      list_button='xpath=>//android.widget.LinearLayout'