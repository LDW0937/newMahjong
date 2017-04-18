#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    订单模型
"""

from web_db_define import *
from datetime import datetime,timedelta

def createOrder(redis,orderInfo):
    """
    创建新订单
    @param:
        redis       redis链接实例
        orderInfo   游戏信息
    """

    orderInfo['id']  = redis.incr(ORDER_COUNT)

    orderTable = GAME_TABLE%(orderInfo['order_no'])
    pipe = redis.pipeline()

    pipe.hmset(orderTable,orderInfo)
    pipe.lpush(ORDER_LIST,orderInfo['order_no'])
    return pipe.execute()


def getBuyOrdersById(redis,agentId,startDate,endDate):
    """
    获取代理购卡订单列表
    """
    deltaTime = timedelta(1)

    startDate = datetime.strptime(startDate,'%Y-%m-%d')
    endDate  = datetime.strptime(endDate,'%Y-%m-%d')

    orderList = []
    while endDate > startDate:
        print endDate,startDate
        buyOrderTable = AGENT_BUY_ORDER_LIST%(agentId,str(endDate))
        if not redis.exists(buyOrderTable):
            endDate-=deltaTime
            continue
        orderNos = redis.lrange(buyOrderTable,0,-1)
        for orderNo in orderNos:
            orderInfo = redis.hmgetall(ORDER_TABLE%(orderNo))
            orderList.append(orderInfo)

        endDate = endDate-deltaTime
        print endDate

    return orderList

def getSaleOrdersById(redis,agentId,startDate,endDate):
    """
    获取代理购卡订单列表
    """
    deltaTime = timedelta(1)

    startDate = datetime.strptime(startDate,'%Y-%m-%d')
    endDate  = datetime.strptime(endDate,'%Y-%m-%d')
    
    orderList = []
    while endDate > startDate:
        buyOrderTable = AGENT_SALE_ORDER_LIST%(agentId,str(endDate))
        if not redis.exists(buyOrderTable):
            endDate-=deltaTime
            continue
        orderNos = redis.lrange(buyOrderTable,0,-1)
        for orderNo in orderNos:
            orderInfo = redis.hmgetall(ORDER_TABLE%(orderNo))
            orderList.append(orderInfo)

        endDate-=deltaTime

    return orderList
