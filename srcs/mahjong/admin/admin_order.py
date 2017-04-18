#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
   订单模块
"""


from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH
from common.utilt import *
from datetime import datetime

@admin_app.get('/buy')
def getBuyPage(redis,session):
    """
        购买房卡
    """
    curTime = datetime.now()
    lang    = getLang()

    info = {
                'title'               :       '房卡购买'
                'STATIC_LAYUI_PATH'   :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'   :       STATIC_ADMIN_PATH
    }

    return template('admin_order_buy',info=info,lang=lang)

@admin_app.post('/buy')
def do_BuyPage(redis,session):
    """
        购买房卡操作
    """
    pass

@admin_app.get('/buy/record')
def getBuyRecordPage(redis,session):
    """
        获取购买房卡记录
    """
    curTime = datetime.now()
    lang    = getLang()

    info = {
                'title'               :       '购卡记录'
                'STATIC_LAYUI_PATH'   :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'   :       STATIC_ADMIN_PATH
    }

    return template('admin_order_buy_record',info=info,lang=lang)

@admin_app.get('/sale/record')
def getSaleRecordPage(redis,session):
    """
        获取售卖房卡记录
    """
    curTime = datetime.now()
    lang    = getLang()

    info = {
                'title'               :       '售卡记录'
                'STATIC_LAYUI_PATH'   :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'   :       STATIC_ADMIN_PATH
    }

    return template('admin_order_sale_record',info=info,lang=lang)