#-*- coding:utf-8 -*-
#!/usr/bin/env python

"""
Author : $Author$
Date   : $Date$
Revision:$Revision$

Description:
    后台用户验证模块
"""
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from bottle import request,abort,template,response,redirect
from admin import admin_app
#from common.log import *
from config.config import *
from common.utilt import *
from common.validcode import create_validate_code
from datetime import datetime
import hashlib
import md5

@admin_app.get('/login')
def getLoginPage(redis,session):
    """
        后台管理验证模块
    """
    lang = getLang()

    info = {
                    'vcodeUrl'               :           BACK_PRE+'/vcode',
                    'STATIC_LAYUI_PATH'      :           STATIC_LAYUI_PATH,
                    'STATIC_ADMIN_PATH'      :           STATIC_ADMIN_PATH
    }

    return template('admin_login',info=info,lang=lang)

@admin_app.post('/login')
def do_Login(redis,session):
    """
        管理系统登录
    """
    pass

@admin_app.get('/vcode')
def changeVerfiyCode(session):
    # if checkServiceOutDate(redis):
    #     return ''
    img, vcode = create_validate_code()
    session['maj_vcode'] = vcode.upper()

    mstream = StringIO()
    img.save(mstream, "GIF")
    response.set_header('Content-Type', 'image/gif')
    return mstream.getvalue()