#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    游戏及游戏模块模型
"""

from web_db_define import *


def getGamesList(redis,limit=None):
    """
    获取游戏列表
    """
    games = redis.lrange(GAME_LIST,0,-1)
    gameList = []

    for game in games:
        gameInfo = {
                'id'            :       game['id'],
                'name'          :       game['name'],
                'web_tag'       :       game['web_tag'],
                'ipa_tag'       :       game['ipa_tag'],
                'apk_tag'       :       game['apk_tag']
        }
        gameList.append(gameInfo)

    return gameList

def createGame(redis,gameInfo):
    """
    创建新游戏
    @param:
        redis      redis链接实例
        gameInfo   游戏信息
    """

    gameId    = redis.incr(GAME_COUNT)
    gameInfo['id'] = gameId
    
    gameTable = GAME_TABLE%(gameId)
    pipe = redis.pipeline()

    pipe.hmset(gameTable,gameInfo)
    pipe.lpush(GAME_LIST,gameId)
    return pipe.execute()

def getGameInfoById(redis,gameId):
    """
    获取游戏信息
    """
    gameTable = GAME_TABLE%(gameId)

    return redis.hmget(gameTable)