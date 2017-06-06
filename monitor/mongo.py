#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongodb_config = {
    # 'host': 'mongodb://192.168.2.25:27017',
    'host': "mongodb://118.178.84.72/xwcz-process-service-server",
    'port': 28017
}

def mongodb_conn():
    conn = MongoClient(**mongodb_config)
    conn.sxw_score.authenticate("sxw_deploy", "sxw.deploy", mechanism='MONGODB-CR')
    # conn.sxw_score.authenticate("sxw_deploy", "sxw.deploy", mechanism='SCRAM-SHA-1')
    db = conn.sxw_score
    return db