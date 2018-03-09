#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from common.adbDevices import *
from appium import webdriver
from common.move_swipe import *
import time

class ShopAppTestCase():
    def __init__(self,deviceName):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = 'com.lq.kldshopping'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.swipe = MySwipe(self.driver)

        print u"设备分辨率：",self.swipe.getSize()

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
        login_flag = False
        self.skip_guide_page()
        print "1:",self.driver.current_activity
        if ".activity.SplashActivity" == self.driver.current_activity:
            # 拨打电话权限的弹框，设置->允许
            if self.isElement(By.ID,"com.android.packageinstaller:id/dialog_container"):
            # if self.driver.find_element_by_id("com.android.packageinstaller:id/dialog_container"):
                self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

            # “我的”，使用模拟屏幕坐标点击
            self.driver.tap([(536,1100),(744,1178)],100)
            time.sleep(2)
            print "2:", self.driver.current_activity
            if ".activity.MainActivity" == self.driver.current_activity:
                self.driver.tap([(271, 197), (495, 265)], 100)
                # id是唯一的，不知道什么原因不能定位
                # self.driver.find_element_by_id("com.lq.kldshopping:id/tv_tologin").click()
                time.sleep(4)
                print "3:", self.driver.current_activity
            self.driver.wait_activity(".activity.login.LoginActivity",10)
            if ".activity.login.LoginActivity" == self.driver.current_activity:
                self.driver.find_element_by_id("com.lq.kldshopping:id/et_phone").send_keys("13572489850")
                self.driver.find_element_by_id("com.lq.kldshopping:id/et_passWord").send_keys("123456")
                time.sleep(2)
                ele_logins = self.driver.find_elements_by_id("com.lq.kldshopping:id/tv_login")
                for one in ele_logins:
                    if u"登录" == one.text:
                        one.click()
                        login_flag = True
                        break
                time.sleep(5)
                print "4:", self.driver.current_activity

        return login_flag

    def sing_in_kld(self):
        pass

    def isElement(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        time.sleep(1)
        flag = None
        try:
            if identifyBy == By.ID:
                self.driver.find_element_by_id(c)
            elif identifyBy == By.XPATH:
                self.driver.find_element_by_xpath(c)
            elif identifyBy == By.CLASS_NAME:
                self.driver.find_element_by_class_name(c)
            elif identifyBy == By.LINK_TEXT:
                self.driver.find_element_by_link_text(c)
            elif identifyBy == By.PARTIAL_LINK_TEXT:
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == By.NAME:
                self.driver.find_element_by_name(c)
            elif identifyBy == By.TAG_NAME:
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == By.CSS_SELECTOR:
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            print "no find this element ",c
            flag = False
        finally:
            return flag

    def __del__(self):
        self.driver.quit()

if __name__ == '__main__':
    adb = Adb()
    devices_name = adb.get_devices()
    if devices_name:
        # 启动app前最好先检查一下有无对应的进程，否则强制终止
        shop_test = ShopAppTestCase(devices_name)
        if shop_test.sign_in():
            pass            # 登录成功
