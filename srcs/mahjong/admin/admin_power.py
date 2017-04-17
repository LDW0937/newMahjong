#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    用户权限模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from datetime import datetime

@admin_app.get('/power/UserMenus')
def getUserMenu(session):
    lang = getLang()
    pid = request.GET.get('pid','').strip()
    isList = request.GET.get('list','').strip()
    aType = '0'
    if not pid:
        pid = 0
    if isList:
        pass
    else:
        info = {
            'title'                  :       '模块管理',
            'addMenusTitle'          :       '添加模块',
            'listUrl'                :       BACK_PRE+'/power/UserMenus?list=1',
            'showPlus'               :       'true' if aType == '0' else 'false',
            'createUrl'              :       BACK_PRE+'/power/UserMenus',
            'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
            'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH,
            'createAccess'           :       '1'
        }
        return template('admin_power_UserMenus',info=info,lang=lang)