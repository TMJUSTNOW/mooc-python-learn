#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql as mdb

# # Mysql 连接配置
# mysql_config = {
#     'host': "192.168.2.58",
#     'port': 3306,
#     'user': 'db_whh',
#     'passwd': 'db_whh',
#     'db': "sxw_score",
#     'charset': 'utf8'
# }

mysql_config = {
    'host': "rdsog11y674i7vf61ac3o.mysql.rds.aliyuncs.com",
    'port': 3306,
    'user': 'reader',
    'passwd': 'Sxw753951',
    'db': "sxw_score",
    'charset': 'utf8'
}


# 连接 Mysql
def conn_db():
    conn = mdb.connect(**mysql_config)
    cur = conn.cursor(mdb.cursors.DictCursor)
    return conn, cur


# 执行sql语句，返回操作游标
def exe_query(cur, sql):
    cur.execute(sql)
    return cur
