#!/user/bin/env python
# -*- coding:utf-8 -*-
import os,yaml

if __name__ == '__main__':
    with open(os.getcwd()+'\\caseConfig\\appconfig.yaml') as f:
        neirong = yaml.load(f)
        print neirong['deviceInfo']['platformVersion']
