#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    个人信息模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from datetime import datetime

@admin_app.get('/self/modifyPasswd')
def getSelfModifyPasswd(redis,session):
    lang = getLang()

    info  =  {

        "title"                  :   '修改密码',
        "submitUrls"             :   BACK_PRE+"/self/modifyPasswd",
        'STATIC_LAYUI_PATH'      :   STATIC_LAYUI_PATH,
        'STATIC_ADMIN_PATH'      :   STATIC_ADMIN_PATH 
    }

    return template('admin_self_modifyPasswd',lang=lang,message='',info=info)

@admin_app.get('/self/syslog')
def getSysLog(redis,session):
    lang      = getLang()

    isList = request.GET.get('list','').strip()
    startDate = request.GET.get('startDate','').strip()
    endDate = request.GET.get('endDate','').strip()

    selfAccount,selfUid = session['account'],session['uid']

    condition = {
            'startDate'           :        startDate+' 00:00:00',
            'endDate'             :        endDate+' 23:59:59'
    }

    if isList:
        pass
    else:
        info = {
                'title'         :    '(%s)相关操作日志查询'%(selfAccount),
                'searchStr'     :    '',
                'showLogType'   :    '',
                'listUrl'       :    BACK_PRE+'/self/syslog?list=1',
                'STATIC_LAYUI_PATH'      :   STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :   STATIC_ADMIN_PATH 
        }

        return template('admin_self_syslog',info=info,lang=lang)

@admin_app.get('/self/loginLog')
def getLoginLog(redis,session):
    lang  =  getLang()

    isList = request.GET.get('list','').strip()
    startDate = request.GET.get('startDate','').strip()
    endDate   = request.GET.get('endDate','').strip()

    selfAccount,selfUid = session['account'],session['uid']

    condition = {
                'startDate'         :       startDate+' 00:00:00',
                'endDate'           :       endDate  +' 23:59:59'
    }

    if isList:
        pass
    else:
        info = {
                'title'                  :       '(%s)登录日志查询'%(selfAccount),
                'listUrl'                :       BACK_PRE+'/self/loginLog?list=1',
                'searchStr'              :       '',
                'showLogType'            :       True,
                'STATIC_LAYUI_PATH'      :   STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :   STATIC_ADMIN_PATH 
        }

        return template('admin_self_loginLog',info=info,lang=lang)