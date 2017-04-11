#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
   线上充值模块
"""


from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH
from common.utilt import *

@admin_app.get('/buy')
def getBuyPage(redis,session):
    """
        购买房卡
    """
    pass

@admin_app.get('/buy/record')
def getBuyRecordPage(redis,session):
    """
        获取购买房卡记录
    """
    pass

@admin_app.get('/sale/record')
def getSaleRecordPage(redis,session):
    """
        获取售卖房卡记录
    """
    pass