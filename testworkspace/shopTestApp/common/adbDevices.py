#!/user/bin/env python
# -*- coding:utf-8 -*-

import os

class Adb:
    def __init__(self):
        pass

    def get_devices(self):
        """
        获取设备名称
        :return:设备名称
        """
        a = os.popen('adb devices')
        devices = a.readlines()
        spl = devices[1].find('\t')
        devices_name = devices[1][:spl]
        devices_status =devices[1][spl+1:]
        if devices_name=='':
            print u"请确认设备是否连接"
            return None
        else:
            print u'当前连接的设备名：',devices_name
            print u'设备状态：', devices_status
            return devices_name

    def get_cpuinfo(self,package_name,cpulog_url):
        """
        获取cpu信息
        :param package_name：包名
        :param cpulog_url：日志存放路径
        :return:None
        """
        a = os.popen('adb shell dumpsys cpuinfo '+ package_name)
        cpuinfos = a.readlines()
        print cpuinfos

    def get_meminfo(self,package_name,cpulog_url):
        """
        获取cpu信息
        :param package_name：包名
        :param cpulog_url：日志存放路径
        :return:None
        """
        a = os.popen('adb shell dumpsys meminfo '+ package_name)
        cpuinfos = a.readlines()
        print cpuinfos

if __name__ == '__main__':
    adb = Adb()
    adb.get_devices()
    adb.get_cpuinfo('com.lq.kldshopping','')
    adb.get_meminfo('com.lq.kldshopping', '')