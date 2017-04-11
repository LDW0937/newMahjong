#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    系统会员模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from datetime import datetime

@admin_app.get('/member/curOnline')
def getCurOnline(redis,session):
    """
        获取在线用户
    """
    lang    =  getLang()
    curTime =  datetime.now()
    isList  =  request.GET.get('list','').strip()

    if isList:
        pass
    else:
        info = {
                'title'                  :           '会员实时在线',
                'listUrl'                :           BACK_PRE+'/member/curOnline?list=1',
                'STATIC_LAYUI_PATH'      :           STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :           STATIC_ADMIN_PATH
        }

        return template('admin_member_online',info=info,lang=lang)