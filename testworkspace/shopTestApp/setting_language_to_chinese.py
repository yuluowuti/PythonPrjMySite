#!/user/bin/env python
# -*- coding:utf-8 -*-
import time
from appium import webdriver

class SettingChinese():
    def __init__(self):
        """
        初期化设备desired_caps
        """
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '192.168.221.103:5555'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def getSize(self):
        """
        获得机器屏幕大小x,y
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

    def find_element_languages(self):
        """
        查找设定中的语言设置（英文版本）
        :return：languages元素
        """
        ele_lang_xpath = '//android.widget.LinearLayout/android.widget.TextView[@resource-id="android:id/title"]'
        ele_id = "android:id/title"
        element_languages = None
        while True:
            self.swipeUp()  # 滑动
            ele_lang = self.driver.find_elements_by_xpath(ele_lang_xpath)  # 通过xpath获取不到语言设定改用resource-id
            eles = self.driver.find_elements_by_id(ele_id)
            print [one.text for one in eles]
            for one in eles:
                if "Languages" in one.text:
                    element_languages = one
                    break
            if element_languages:
                break
        return element_languages

    def setting_to_chinese(self,element_languages):
        """
        在子页面中查找chinese并设置为：简体中文->中国
        :return：languages元素
        """
        if element_languages:
            element_languages.click()
            print self.driver.current_activity
            # 等xxx activity出现,30秒内，就可以不用sleep了
            self.driver.wait_activity(".Settings$InputMethodAndLanguageSettingsActivity", 30)

            # 语言设定
            self.driver.find_element_by_xpath(
                "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
            self.driver.find_element_by_id("com.android.settings:id/add_language").click()
            self.driver.find_element_by_id("android:id/locale_search_menu").click()
            self.driver.find_element_by_id("android:id/search_src_text").send_keys("chinese")

            languages_lists = self.driver.find_elements_by_id("android:id/locale")
            element_chinese = None
            if languages_lists.__len__() > 0:
                for one in languages_lists:
                    if u"简体中文"== one.text:
                        element_chinese = one
                        break
            if element_chinese:
                element_chinese.click()
                print self.driver.current_activity
                city_list = self.driver.find_elements_by_id("android:id/locale")
                if city_list.__len__() > 0:
                    for one in city_list:
                        if u"中国" == one.text:
                            one.click()
                            print self.driver.current_activity
                            self.driver.find_element_by_xpath(
                                "//android.widget.LinearLayout/android.widget.ImageButton").click()
                            self.driver.find_element_by_xpath(
                                "//android.widget.RelativeLayout/android.widget.TextView").click()

                            checkboxs = self.driver.find_elements_by_id("com.android.settings:id/checkbox")
                            for checkbox in checkboxs:
                                if "English (United States)"== checkbox.text:
                                    checkbox.click()
                                    self.driver.find_element_by_android_uiautomator(
                                        'new UiSelector().description("Remove")').click()
                                    time.sleep(1)
                                    # 弹框
                                    self.driver.find_element_by_id("android:id/button1").click()
                                    break
                            break

    def __del__(self):
        self.driver.quit()

if __name__ == '__main__':
    sc = SettingChinese()
    element_languages = sc.find_element_languages()
    sc.setting_to_chinese(element_languages)