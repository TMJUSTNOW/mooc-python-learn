#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Redis 简单操作工具
# 依赖 Python3 / pip install redis-py-cluster / pip install redis
# Run python3 xxx.py
# Author LarryKoo
# Email: gjg@sxw.cn
# 2017-07-14
#



from rediscluster import StrictRedisCluster
import sys

redis_nodes = [
    {'host': '192.168.2.52', 'port': 7000},
    {'host': '192.168.2.52', 'port': 7001},
    {'host': '192.168.2.53', 'port': 7000},
    {'host': '192.168.2.53', 'port': 7001},
    {'host': '192.168.2.54', 'port': 7000},
    {'host': '192.168.2.54', 'port': 7001}
]

try:
    rc = StrictRedisCluster(startup_nodes=redis_nodes)
except Exception as e:
    print("Connect Error!")
    sys.exit(1)


class RedisTool:
    @staticmethod
    def delete(*keys):
        return rc.delete(*keys)

    @staticmethod
    def deletes(match_key):
        count = 0;
        for key in rc.scan_iter(match_key):
            del_count = rc.delete(key)
            count += del_count
        return count

    @staticmethod
    def set(key, val):
        return rc.set(key, val)

    @staticmethod
    def get(key):
        return rc.get(key)

    @staticmethod
    def scan(match):
        for key in rc.scan_iter(match=match):
            print(key)

    @staticmethod
    def run():
        while (1):
            val_input = input("select your operation[get key/set k v/scan match/del key/dels match_key]")
            val = val_input.split(" ")

            if val[0] in ['get']:
                print(RedisTool.get(val[1]))
            elif val[0] in ['set']:
                print(RedisTool.set(val[1], val[2]))
            elif val[0] in ['del']:
                print(RedisTool.delete(val[1]))
            elif val[0] in ['scan']:
                RedisTool.scan(val[1])
            elif val[0] in ['dels']:
                print(RedisTool.deletes(val[1]))
            elif val[0] in ['exit']:
                sys.exit(1)
            else:
                print("input error.")
            continue


### run command tools
RedisTool.run()
