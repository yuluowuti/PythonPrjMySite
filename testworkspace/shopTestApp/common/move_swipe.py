#!/user/bin/env python
# -*- coding:utf-8 -*-
class MySwipe():
    def __init__(self,driver):
        self.driver = driver

    def getSize(self):
        """
        获得机器屏幕大小x,y[分辨率]
        :return：设备屏幕
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeUp(self):
        """
        屏幕向上滑动
        """
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2)

    def swipeDowm(self):
        """
        屏幕向下滑动
        """
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2)

    def swipLeft(self):
        """
        屏幕向左滑动
        """
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1)

    def swipRight(self):
        """
        屏幕向右滑动
        """
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1)

if __name__ == '__main__':
    pass