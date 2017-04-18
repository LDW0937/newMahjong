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
from web_db_define import *
from wechat.wechatData import *
from common.install_plugin import install_redis_plugin,install_session_plugin
#from common.log import *
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


def onReg(redis, account, passwd, type): #传入参数：账号，密码，类型；返回参数：成功返回账号和密码，失败返回None, None

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
                redis.hmset(table, {'accessToken':accessToken, 'refreshToken':refreshToken, 'password':md5.new(account).hexdigest()})
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
    elif type == 0:
        account2user_table = FORMAT_ACCOUNT2USER_TABLE%(account)
        if redis.exists(account2user_table):
            table = redis.get(account2user_table)
            truePassword = redis.hget(table, 'password')
            if truePassword == md5.new(passwd).hexdigest():
                return account, passwd

    return None, None

@hall_app.post('/login')
def do_hallLogin(redis,session):
    """
    大厅登录接口
    """
    tt = request.forms.get('tt', '').strip()
    ip = request['REMOTE_ADDR']
    account = request.forms.get('account', '').strip()
    passwd = request.forms.get('passwd', '').strip()
    type = request.forms.get('type', '').strip() #登录类型

    reAccount, rePasswd = onReg(redis, account, passwd, type)

    if reAccount:
        if type:
            realAccount = redis.get(WEIXIN2ACCOUNT%(reAccount))
        else:
            realAccount = reAccount
        #读取昵称和group_id
        account2user_table = FORMAT_ACCOUNT2USER_TABLE%(realAccount)
        table = redis.get(account2user_table)
        name, ag = redis.hmget(table, ('nickname', 'parentAg'))
        return {'code':0, 'userInfo':{'name':name, 'group_id':ag, 'account':reAccount, 'passwd':rePasswd}}
    else: #失败
        return {'code':101}

@hall_app.post('/joinGroup')
def do_joinGroup(redis,session):
    """
    加入公会接口
    """
    curTime = datetime.now()
    sid  =  request.forms.get('sid','').strip()
    groupId = request.forms.get('groupId','').strip()

    #print
    print '[%s][joinGroup][info] sid[%s] groupId[%s] sid[%s]'%(curTime,groupId,sid)

    adminTable = AGENT_TABLE%(groupId)

    if redis.exists(adminTable):
        #如果存在,绑定
        pass
    else:
        return {'code':-1}

@hall_app.post('/refresh')
def do_Refresh(redis,session):
    """
    刷新接口
    """
    curTime = datetime.now()
    sid     = request.forms.get('sid','').strip()

    pass


@hall_app.post('/getRoomSetting')
def do_getRoomSetting(redis,session):
    """
    获取创建房间设置信息
    """
    curTime = datetime.now()
    gameId  = request.forms.get('gameId','').strip()

    #print 
    print '[%s][getRoomSetting][info] gameId[%s]'%(curTime,gameId)

    gameTable = GAME_TABLE%(gameId)
    if not redis.exists(gameTable):
        return {'code':-1}

    gameSettingStr = redis.hget(gameTable,'game_rule')
    print '[%s][getRoomSetting][info] gameId[%s] gameRule[%s]'%(curTime,gameId,gameSettingStr)

    return {'code':0,'setting':gameSettingStr}


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