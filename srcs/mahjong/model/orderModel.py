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