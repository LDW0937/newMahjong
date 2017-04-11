#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    this is Description
"""

from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH
from common.utilt import *

@admin_app.get('/')
def getAdminPage(redis,session):
    lang = getLang()

    info = {
            'STATIC_ADMIN_PATH'     :   STATIC_ADMIN_PATH,
            'ADMIN_DEFAULT_PAGE'    :   '/admin/home'
    }
    return template('admin_base',info=info,lang=lang)

@admin_app.get('/home')
def getSystemInfoPage(redis,session):
    """
        系统配置信息页面
    """
    lang = getLang()
    info    =   {
                    'title'                  :           '系统信息',
                    'STATIC_LAYUI_PATH'      :           STATIC_LAYUI_PATH,
                    'STATIC_ADMIN_PATH'      :           STATIC_ADMIN_PATH
    }

    return template('admin_home',info=info,lang=lang)