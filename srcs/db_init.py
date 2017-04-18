#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    DB初始化
"""

import sys
sys.path.insert(0, 'server_common')
from web_db_define import *
from datetime import datetime,time
import redis
import hashlib

def getInst(dbNum):
    global redisdb
    redisdb = redis.ConnectionPool(host="192.168.0.99", port=6379, db='1', password='Fkkg65NbRwQOnq01OGMPy5ZREsNUeURm')
    return redis.Redis(connection_pool=redisdb)

AGENT_TABLE = 'agents:account:%s'

redis = getInst(1)

#初始化管理账号
curTime = datetime.now()
pipe = redis.pipeline()

"""
    配置代理名称和房卡
    代理名称            ：       房卡数
"""
agentDict = {
        'id'                    :           1,
        'account'               :           'sysadmin',
        'passwd'                :           hashlib.sha256('sysadmin').hexdigest(),
        'name'                  :           'dawei',
        'shareRate'             :           0.5,
        'valid'                 :            1,
        'roomcard_id'           :           0,
        'parent_id'             :           0,
        'roomcard'              :           0,
        'regIp'                 :           '127.0.0.1',
        'regDate'               :           1,
        'lastLoginIP'           :           1,
        'lastLoginDate'         :           1,
        'isCreate'              :           1,
        'type'                  :           0
}

adminTable = AGENT_TABLE%('sysadmin')
print pipe.hmset(adminTable,agentDict)
print 'create sysadmin[%s] success.'%(adminTable)
pipe.execute()
print 'creare Done.........'