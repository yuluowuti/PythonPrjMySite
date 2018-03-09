#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from common.adbDevices import *
from appium import webdriver
from common.move_swipe import *
import time

class ShopAppTestCase():
    def __init__(self,deviceName):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.lq.kldshopping'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.swipe = MySwipe(self.driver)

    def skip_guide_page(self):
        """
        引导页--->立即体验
        """
        time.sleep(2)
        print self.driver.current_activity
        # 引导页
        if ".activity.WelcomeGuideActivity" == self.driver.current_activity:
            for i in range(3):
                self.swipe.swipLeft()
                self.driver.implicitly_wait(3)
            # 最后一张引导页空白处点击一下即可进入首页
            self.driver.find_element_by_id("com.lq.kldshopping:id/btn_enter").click()

    def sign_in(self):
        self.skip_guide_page()
        self.driver.wait_activity(".permission.ui.GrantPermissionsActivity", 30)

    def __del__(self):
        self.driver.quit()

if __name__ == '__main__':
    adb = Adb()
    devices_name = adb.get_devices()
    if devices_name:
        # 启动app前最好先检查一下有无对应的进程，否则强制终止
        shop_test = ShopAppTestCase(devices_name)
        shop_test.sign_in()