#!/user/bin/env python
# -*- coding:utf-8 -*-
from common.adbDevices import *
from appium import webdriver
from common.move_swipe import *
import time

class JinniuAppTestCase:
    def __init__(self,deviceName):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.lianqian.jinniuguanjia'
        desired_caps['appActivity'] = '.moudles.splash.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.swipe = MySwipe(self.driver)

    def skip_guide_page(self):
        """
        引导页--->立即体验
        """
        time.sleep(2)
        print self.driver.current_activity
        # 引导页
        if ".moudles.guide.GuideActivity" == self.driver.current_activity:
            for i in range(3):
                self.swipe.swipLeft()
                self.driver.implicitly_wait(3)

            self.driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.ImageView").click()
        time.sleep(1)
        print self.driver.current_activity
        if ".moudles.home.MainActivity" == self.driver.current_activity:
            # 进入首页
            pass



    def sign_in(self):
        pass


    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    # 启动appium-server
    # 设备是否连接判断
    # 获取设备名称（先不考虑有多个设备）
    adb = Adb()
    devices_name = adb.get_devices()
    if devices_name:
        jin_test = JinniuAppTestCase(devices_name)
        jin_test.skip_guide_page()
