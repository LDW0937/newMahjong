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

def getAgentGames(redis,agentId):
    """
        获取代理下的所有游戏
    """
    if agentId == '1':
        gameList = redis.lrange(GAME_LIST,0,-1)
    else :
        gameList = redis.smembers(AGENT_OWN_GAME%(agentId))

    gamesInfo =[]
    for game in gameList:
        gameInfo = {}
        name = redis.hget(GAME_TABLE%(game),'name')
        gameInfo['name'] = name
        gameInfo['id'] = game
        gamesInfo.append(gameInfo)
    return gamesInfo

def setAgentGames(request,redis,parentId,agentId):
    """
        通过父代理Id 给代理存储代理的游戏
    """
    agentOwnGamesTabel = AGENT_OWN_GAME%(agentId)
    if parentId == '1':
        gameList = redis.lrange(GAME_LIST,0,-1)
    else :
        gameList = redis.smembers(AGENT_OWN_GAME%(parentId))
    gamesInfo =[]
    for game in gameList:
        if request.forms.get('game%s'%(game)):
            redis.sadd(agentOwnGamesTabel,game)

def getAgentId(redis,account):
    agentIdTable = AGENT_ACCOUNT_TO_ID%(account)
    return redis.get(agentIdTable)
