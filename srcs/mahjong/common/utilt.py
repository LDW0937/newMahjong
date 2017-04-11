#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    通用工具模块  
"""
from bottle import request,response,redirect,abort
from i18n.i18n import getLangInst
import inspect


def getLang():
    """
        获取语言包
    """
    return getLangInst(getCurLangByCookie())


def getCurLangByCookie():
    if not request.get_cookie('gglang'):
        return request.get_cookie('gglang','CHN')
    else:
        return request.get_cookie('gglang')

def checkLogin(fn):
    def _check(*args,**kw):
        session = session_plugin.getSession()
        if not session.get('account',None):
            return redirect('/admin/login')

        argNames = inspect.getargspec(fn)[0]
        if redis_plugin.keyword in argNames:
            kw[redis_plugin.keyword] = session.rdb
        if session_plugin.keyword in argNames:
            kw[session_plugin.keyword] = session

        return fn(*args,**kw)

    return _check