#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    数据统计模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from datetime import datetime

@admin_app.get('/statistics/login')
def getLoginStatistics(redis,session):

    lang    =  getLang()
    curTime =  datetime.now()
    isList  =  request.GET.get('list','').strip()
    startDate = request.GET.get('startDate','').strip()
    endDate   = request.GET.get('endDate','').strip()

    if isList:
        pass
    else:
        info = {
                'title'                  :           '日登陆人数统计',
                'listUrl'                :           BACK_PRE+'/statistics/login?list=1',
                'STATIC_LAYUI_PATH'      :           STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :           STATIC_ADMIN_PATH
        }


    return template('admin_statistics_login',info=info,lang=lang)

@admin_app.get('/statistics/buyReport')
def getBuyReport(redis,session):
    """
    获取代理的订单报表
    """
    lang      = getLang()

    isList = request.GET.get('list','').strip()
    startDate = request.GET.get('startDate','').strip()
    endDate = request.GET.get('endDate','').strip()

    selfAccount,selfUid = session['account'],session['uid']

    if not startDate or not endDate:
        #默认显示一周时间
        startDate,endDate = getDaya4Week()

    if isList:
        pass
    else:
        info = {
                'title'         :    '[%s]购卡报表'%(selfAccount),
                'searchStr'     :    '',
                'showLogType'   :    '',
                'startDate'     :    startDate,
                'endDate'       :    endDate,
                'listUrl'       :    BACK_PRE+'/statistics/buyReport?list=1',
                'STATIC_LAYUI_PATH'      :   STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :   STATIC_ADMIN_PATH 
        }

        return template('admin_report_buy',info=info,lang=lang)

@admin_app.get('/statistics/saleReport')
def getSaleReport(redis,session):
    """
    获取代理的订单报表
    """
    lang      = getLang()

    isList = request.GET.get('list','').strip()
    startDate = request.GET.get('startDate','').strip()
    endDate = request.GET.get('endDate','').strip()

    selfAccount,selfUid = session['account'],session['uid']

    if not startDate or not endDate:
        #默认显示一周时间
        startDate,endDate = getDaya4Week()

    if isList:
        pass
    else:
        info = {
                'title'         :    '[%s]售卡报表'%(selfAccount),
                'searchStr'     :    '',
                'showLogType'   :    '',
                'startDate'     :    startDate,
                'endDate'       :    endDate,
                'listUrl'       :    BACK_PRE+'/statistics/saleReport?list=1',
                'STATIC_LAYUI_PATH'      :   STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :   STATIC_ADMIN_PATH 
        }

        return template('admin_report_sale',info=info,lang=lang)