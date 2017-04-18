#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    代理模型
"""
from web_db_define import *
import random

TYPE2TXT={
    '0' : '系统管理员',
    '1' : '总公司',
    '2' : '一级代理',
    '3' : '二级代理'
}



def getAgentIdNo(redis):
    """
        生成会员Id号(6位且不重复)
    """
    agentId = ''
    for i in range(6):

        # a = random.randint(0,9)
        a = random.randrange(9)
        agentId += str(a)
    if not redis.sadd(AGENT_ID_TABLE,agentId):
        getAgentIdNo(redis,session)
    return agentId

def getAgentId(redis,account):
    agentIdTable = AGENT_ACCOUNT_TO_ID%(account)
    return redis.get(agentIdTable)
