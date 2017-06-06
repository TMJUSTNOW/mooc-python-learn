#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string as String

from pymongo import MongoClient

mongodb_config = {
    # 'host': 'mongodb://192.168.2.25:27017',
    'host': "mongodb://127.0.0.1:27017",
    'port': 27017
}


def mongodb_conn():
    conn = MongoClient(**mongodb_config)
    # conn.admin.authenticate("sxw_deploy", "sxw.deploy", mechanism='MONGODB-CR')
    # conn.admin.authenticate("sxw_deploy", "sxw.deploy", mechanism='SCRAM-SHA-1')
    db = conn['demo-hZm9C']
    return db


### 以上为 mongodb 驱动

def randomStr(num):
    return ''.join(random.sample(String.ascii_letters + String.digits, num))

def test():
    db = mongodb_conn()
    db.drop_collection("test")
    doc = {
        "name": randomStr(5),
        "nick_name": randomStr(12),
        "status": random.choice(String.digits)
    }

    loadSplitSize = 10000
    docs = []
    for i in range(10):
        docs.append(doc)

    # 分页的插入数据库
    offset = 0
    while (offset < len(docs)):
        db.test.insert(docs[offset:offset + loadSplitSize])
        offset += loadSplitSize

test()
