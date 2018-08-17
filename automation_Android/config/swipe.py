import time
def swipe_up(self,n=5):
    size = self.driver.get_window_size()
    print(size)
    width = size['width']
    print(width)
    height = size['height']
    print(height)

    # 执行滑屏操作,向上（上拉）滑动
    x1 = width * 0.5
    y1 = height * 0.9
    y2 = height * 0.25
    time.sleep(3)
    print("滑动前")
    self.driver.swipe(x1, y1, x1, y2)
    print("滑动后")
    for i in range(n):
        print("第%d次滑屏" % i)
        time.sleep(3)
        self.driver.swipe(x1, y1, x1, y2)

#屏幕向下滑动
def swipe_down(self,n=5):
    size = self.driver.get_window_size()
    print(size)
    width = size['width']
    print(width)
    height = size['height']
    print(height)

    # 执行滑屏操作,向上（上拉）滑动
    x1 = width * 0.5
    y1 = height * 0.25
    y2 = height * 0.75
    time.sleep(3)
    print("滑动前")
    self.driver.swipe(x1, y1, x1, y2)
    print("滑动后")
    for i in range(n):
        print("第%d次滑屏" % i)
        time.sleep(3)
        self.driver.swipe(x1, y1, x1, y2)

#屏幕向左滑动
def swipe_left(self,n=5):
    size = self.driver.get_window_size()
    print(size)
    width = size['width']
    print(width)
    height = size['height']
    print(height)

    # 执行滑屏操作,向上（上拉）滑动
    x1 = width * 0.75
    y1 = height * 0.5
    x2 = height * 0.05
    time.sleep(3)
    print("滑动前")
    self.driver.swipe(x1, y1, x2, y1)
    print("滑动后")
    for i in range(n):
        print("第%d次滑屏" % i)
        time.sleep(3)
        self.driver.swipe(x1, y1, x2, y1)

#屏幕向右滑动
def swipe_right(self,n=5):
    size = self.driver.get_window_size()
    print(size)
    width = size['width']
    print(width)
    height = size['height']
    print(height)

    # 执行滑屏操作,向上（上拉）滑动
    x1 = width * 0.05
    y1 = height * 0.5
    x2 = height * 0.75
    time.sleep(3)
    print("滑动前")
    self.driver.swipe(x1, y1, x2, y1)
    print("滑动后")
    for i in range(n):
        print("第%d次滑屏" % i)
        time.sleep(3)
        self.driver.swipe(x1, y1, x2, y1)
