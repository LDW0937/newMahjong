#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    微信模块(登录大厅验证,微信支付)
"""

from bottle import request, Bottle, abort, redirect, response, template,static_file
from db_define import *
from wechat.wechatData import *
from common.install_plugin import install_redis_plugin,install_session_plugin
from common.log import *
from datetime import datetime
import time
import urllib2
import json
import random
import md5

#wechatApp
hall_app = Bottle()

#安装插件
install_redis_plugin(hall_app)
install_session_plugin(hall_app)


def onReg(account,passwd,type): #传入参数：账号，密码，类型；返回参数：成功返回账号和密码，失败返回None, None

    curTime = datetime.now()

    #print
    print '[%s][wechat onReg][info] account[%s] passwd[%s] type[%s]'%(curTime,account,passwd,type)
    log_debug('[%s][wechat onReg][info] account[%s] passwd[%s] type[%s]'%(curTime,account,passwd,type))

    if type == 1: #微信code登录
        tokenMessage = checkWeixinCode(account)
        if tokenMessage:
            password = account
            accessToken = tokenMessage["access_token"]
            refreshToken = tokenMessage["refresh_token"]
            openID = tokenMessage["openid"]
            userData = getWeixinData(openID, accessToken)
            unionid = userData['unionid']
            if redis.exists(WEIXIN2ACCOUNT%(unionid)):
                realAccount = redis.get(WEIXIN2ACCOUNT%(unionid))
                account2user_table = FORMAT_ACCOUNT2USER_TABLE%(realAccount)
                table = redis.get(account2user_table)
                redis.hmset(table, {'accessToken':accessToken, 'refreshToken':refreshToken, 'password':account})
            else:
                setOpenid2account(openID, accessToken, refreshToken, ip, redis, account)
            return unionid, password
    elif type == 2:
        if redis.exists(WEIXIN2ACCOUNT%(account)):
            realAccount = redis.get(WEIXIN2ACCOUNT%(account))
            account2user_table = FORMAT_ACCOUNT2USER_TABLE%(realAccount)
            table = redis.get(account2user_table)
            truePassword = redis.hget(table, 'password')
            if truePassword == md5.new(passwd).hexdigest():
                return unionid, passwd

    return None, None

@hall_app.post('/login')
def do_hallLogin(redis,session):
    """
    大厅登录接口
    """
    pass

@hall_app.post('/joinGroup')
def do_joinGroup(redis,session):
    """
    加入公会接口
    """
    pass

@hall_app.post('/refresh')
def do_Refresh(redis,session):
    """
    刷新接口
    """
    pass

@hall_app.post('/getRoomSetting')
def do_getRoomSetting(redis,session):
    """
    获取创建房间设置信息
    """
    pass

@hall_app.post('/createRoom')
def do_CreateRoom(redis,session):
    """
    创建房间接口
    """
    pass

@hall_app.post('/getRoomList')
def do_getRoomList(redis,session):
    """
    获取房间列表
    """
    pass