#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongodb_config = {
    # 'host': 'mongodb://192.168.2.25:27017',
    'host': "mongodb://dds-bp1c5825e23589241.mongodb.rds.aliyuncs.com:3717,dds-bp1c5825e23589242.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-3016521",
    'port': 27017
}


def mongodb_conn():
    conn = MongoClient(**mongodb_config)
    conn.sxw_score.authenticate("sxw_score", "sxw_score", mechanism='MONGODB-CR')
    db = conn.sxw_score
    return db
