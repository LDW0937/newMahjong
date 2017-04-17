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