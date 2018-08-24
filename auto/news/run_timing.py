import os,time
k=1
while k <2:
   now_time=time.strftime('%H_%M')# 获取当前时间
   if now_time == '14_14':#定义运行时的时间
      print("开始运行脚本:")
      os.chdir("C:\\auto\\news")#获取文件位置
      os.system('Python run_test.py') #执行脚本
      print ("执行结束")
      break
   else:#如果不等于设定的时间就每隔两秒打印一次时间，直到执行程序
      time.sleep(2)#  睡眠两秒
      print(now_time)# 打印当前时间
