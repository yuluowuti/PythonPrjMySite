#!/user/bin/env python
# -*- coding:utf-8 -*-
from common.adbDevices import *
from appium import webdriver
import time

def main():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'ead1cc4a'
    desired_caps['appPackage'] = 'com.lianchuan.kaledai'
    desired_caps['appActivity'] = 'com.lianchuan.kaledai.activity.SplashActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    driver.find_element_by_id('com.lianchuan.kaledai:id/repay').click()

    driver.quit()
def open_shop():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'ead1cc4a'
    desired_caps['appPackage'] = 'com.lq.kldshopping'
    # com.lq.kldshopping /.activity.SplashActivity
    desired_caps['appActivity'] = 'com.lq.kldshopping.activity.SplashActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(10)
    # driver.find_element_by_id("com.lq.kldshopping:id/footer_text[@text='卡乐']").click()
    path ="//android.widget.HorizontalScrollView/android.support.v7.app.ActionBar"
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '卡乐')]").click()
    time.sleep(2)
    driver.find_element_by_id("com.lq.kldshopping:id/tv_goopen").click()
    time.sleep(2)
    webelement = driver.find_element_by_xpath("//*")
    driver.quit()


class appSignIn:
    def __init__(self):
        pass


if __name__ == '__main__':
    # 启动appium-server
    # 设备是否连接判断
    # 获取设备名称（先不考虑有多个设备）
    adb = Adb()
    devices_name = adb.get_devices()
