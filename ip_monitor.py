#!/usr/bin/python
# -*- coding:utf8 -*-

import re
import os
import subprocess
from time import sleep
from datetime import datetime

import requests


class Monitor():
    def __init__(self):
        self.last_ip = None
        self.current_ip = None
        self.ip_filepath = os.path.dirname(os.path.abspath(__file__))+'/ip.txt'

    def getLastIP(self):
        with open(self.ip_filepath) as f:
            self.last_ip = f.read()

    def saveCurrentIP(self):
        with open(self.ip_filepath, 'w') as f:
            f.write(self.current_ip)

    def getCurrentIP(self):
        r = requests.get('http://ip.cn')
        if r.status_code != 200:
            print("[{}] : {} status = {}".format(
                str(datetime.now()), '获取ip地址失败', r.status_code))
            raise Exception(str(datetime.now()) + ': ' + '获取ip地址失败' +
                            'status = %d' % r.status_code)
        res = r.content.decode('utf-8')
        pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        res = re.findall(pattern, res)[0]
        print("[{}] : 获取ip地址成功 {} ".format(str(datetime.now()), res))
        self.current_ip = res

    def isChange(self):
        self.getLastIP()
        self.getCurrentIP()
        if self.last_ip != self.current_ip:
            print("[{}] : IP地址更变 {} {} ".format(str(datetime.now()), self.last_ip, self.current_ip))
            self.saveCurrentIP()
            return True
        return False

    def monitor(self, func):
        if self.isChange():
            func(self.current_ip)


if __name__ == '__main__':
    Monitor().monitor(print)
