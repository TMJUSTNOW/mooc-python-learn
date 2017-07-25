#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis.client import Redis, ConnectionPool

# redis_host = "10.26.253.195"
redis_host = "127.0.0.1"
redis_port = "6379"
redis_db = "0"
redis_pwd = ""

pool = ConnectionPool(host=redis_host, port=redis_port, db=redis_db)
rc = Redis(connection_pool=pool)

class RedisTool:
    @staticmethod
    def delete(*keys):
        rc.delete(*keys)

    @staticmethod
    def set(key, val):
        return rc.set(key, val)

    @staticmethod
    def get(key):
        return rc.get(key)

    @staticmethod
    def scan(cursor, match, count):
        return rc.scan(cursor, match, count)


RedisTool.set("K-A", "AAA")
RedisTool.set("K-AB", "BBB")
RedisTool.set("K-ABC", "CCC")

print("=======")

cursor = 0
while (1):
    result = RedisTool.scan(cursor, "K-A*", 1)
    if (result[0] > 0):
        cursor = result[0]
        print(result)
        continue
    break
