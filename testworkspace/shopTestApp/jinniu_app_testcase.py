#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
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
            # 最后一张引导页空白处点击一下即可进入首页
            self.driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.ImageView").click()

    def sign_in(self):
        self.skip_guide_page()
        time.sleep(1)
        print self.driver.current_activity
        self.driver.wait_activity()
        if ".moudles.home.MainActivity" == self.driver.current_activity:
            # 进入首页
            # self.driver.find_element_by_xpath("//android.widget.TextView[@text='房贷计算器']").click()
            # 模拟手指点击操作
            self.driver.tap([(42, 454), (188, 515)], 100)
            time.sleep(2)

            # # 输入手机号/密码
            # self.driver.find_element_by_id("com.lianqian.jinniuguanjia:id/et_phone_number").send_keys("13572489850")
            # time.sleep(1)
            # self.driver.find_element_by_id("com.lianqian.jinniuguanjia:id/et_center").send_keys("123456")
            # try:
            #     wait = WebDriverWait(self.driver,10,1)
            #     wait.until(self.driver.find_element_by_id("com.lianqian.jinniuguanjia:id/btn_login"))
            #     self.driver.find_element_by_id("com.lianqian.jinniuguanjia:id/btn_login").click()
            # except Exception as e:
            #     print e.message

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    # 获取设备名称（先不考虑有多个设备）
    adb = Adb()
    devices_name = adb.get_devices()
    if devices_name:
        # 启动app前最好先检查一下有无对应的进程，否则强制终止
        jin_test = JinniuAppTestCase(devices_name)
        jin_test.sign_in()