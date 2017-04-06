#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as t

# 简单计时器
class TimeCount:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.begin = 0
        self.end = 0
        self.ret = '未开始计时'
        self.temp = 0
        self.time = []

    def __str__(self):
        return self.ret

    __repr__ = __str__

    def __add__(self, other):
        tem = self.temp + other.temp
        ret = '总共运行了'
        secs = tem % 60
        minites = int((tem - secs) // 60) % 60
        hours = int((tem - minites * 60 - secs) // 3600) % 24
        days = int((tem - hours * 3600 - minites * 60 - secs) // 86400) % 30
        months = int((tem - days * 86400 - hours * 3600 - minites * 60 - secs) // 2592000) % 12
        years = int((tem - months * 2592000 - days * 86400 - hours * 3600 - minites * 60 - secs) // 31104000)
        temp = [years, months, days, hours, minites, secs]
        for index in range(6):
            if temp[index]:
                ret += (str(temp[index]) + self.unit[index])
        return ret

    def start(self):
        self.begin = t.time()
        self.ret = '请先调用 stop() 停止计时！'
        # print('计时开始！')

    def stop(self):
        if not self.begin:
            print('请先调用 start() 开始计时！')
        else:
            self.end = t.time()
            self.__calc()
            # print('计时停止！')

    def __calc(self):
        self.time = []
        self.ret = '总共运行了'
        self.temp = self.end - self.begin
        secs = self.temp % 60
        minites = int((self.temp - secs) // 60) % 60
        hours = int((self.temp - minites * 60 - secs) // 3600) % 24
        days = int((self.temp - hours * 3600 - minites * 60 - secs) // 86400) % 30
        months = int((self.temp - days * 86400 - hours * 3600 - minites * 60 - secs) // 2592000) % 12
        years = int((self.temp - months * 2592000 - days * 86400 - hours * 3600 - minites * 60 - secs) // 31104000)
        tem = [years, months, days, hours, minites, secs]
        for index in range(6):
            self.time.append(tem[index])
            if self.time[index]:
                self.ret += (str(self.time[index]) + self.unit[index])
        self.begin = 0
        self.end = 0
