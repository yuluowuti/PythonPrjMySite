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

def find_element_languages():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1'
    desired_caps['deviceName'] = '192.168.221.103:5555'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(2)
    ele_lang_xpath = '//android.widget.LinearLayout/android.widget.TextView[@resource-id="android:id/title"]'
    ele_id = "android:id/title"
    element_languages = None
    while True:
        swipeUp(driver) # 滑动
        ele_lang = driver.find_elements_by_xpath(ele_lang_xpath)    # 通过xpath获取不到语言设定改用resource-id
        eles= driver.find_elements_by_id(ele_id)
        print [one.text for one in eles]
        for one in eles:
            if "Languages" in one.text:
                element_languages=one
                break
        if element_languages:
            break
    if element_languages:
        element_languages.click()
        setting_to_chinese(driver)

    driver.quit()

def setting_to_chinese(driver):
    print driver.current_activity
    # 等xxx activity出现,30秒内，就可以不用sleep了
    driver.wait_activity(".Settings$InputMethodAndLanguageSettingsActivity", 30)
    # 语言设定
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
    time.sleep(1)

    driver.find_element_by_id("com.android.settings:id/add_language").click()
    time.sleep(1)

    driver.find_element_by_id("android:id/locale_search_menu").click()
    time.sleep(1)

    driver.find_element_by_id("android:id/search_src_text").send_keys("chinese")
    time.sleep(2)

    languages_lists = driver.find_elements_by_id("android:id/locale")
    if languages_lists.__len__()>0:
        for one in languages_lists:
            if u"简体中文" == one.text:
                one.click()
                time.sleep(2)
                break




#获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#屏幕向上滑动
def swipeUp(driver):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)    #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2)


class appSignIn:
    def __init__(self):
        pass


if __name__ == '__main__':
    # 启动appium-server
    # 设备是否连接判断
    # 获取设备名称（先不考虑有多个设备）
    # adb = Adb()
    # devices_name = adb.get_devices()

    find_element_languages()
