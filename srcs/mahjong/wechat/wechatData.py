#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    微信模块数据
"""
import hashlib
import xml.dom.minidom
import json

import datetime
import random

import urllib2
import urllib
import socket

from db_define import *

WAIT_WEB_TIME = 10 #访问网页超时时间

APPID = 'wx95aa8cae4b211b37'
SECRET = '5f9af930d3af7a042be0b7504c019271'
MCH_ID = '1368063302' #商户ID
DEVICE_INFO = 'WEB' #设备号
MCH_KEY = '6ac8c8d854b1fbd5b38e730326a02786' #商户秘钥
# NOTIFY_URL = 'http://game.sixiyule.com/wechat/notify_server'#通知地址
NOTIFY_URL = 'http://36.1.238.246:9790/wechat/notify_server'#通知地址^
TRADE_TYPE = 'APP' #支付类型

def setRandomNumList():
    randomList = []
    for num in xrange(10):
        randomList.append(str(num))
    return randomList

def setRandomBigStrList():
    randomList = []
    for num in xrange(26):
        char = chr(num + 65)
        randomList.append(char)
    return randomList

def setRandomSmallStrList():
    randomList = []
    for num in xrange(26):
        char = chr(num + 97)
        randomList.append(char)
    return randomList
    
def setRandomAccountList():
    randomList = []
    randomList.extend(setRandomNumList())
    randomList.extend(setRandomBigStrList())
    randomList.extend(setRandomSmallStrList())
    return randomList
RANDOM_LIST = setRandomAccountList() #字母数字表，用于生成随机账号
RANDOM_ACCOUNT_COUNT = 5 #随机账号个数

def setRandomStrList():
    randomList = []
    randomList.extend(setRandomNumList())
    # randomList.extend(setRandomBigStrList())
    randomList.extend(setRandomSmallStrList())
    return randomList
RANDOM_STR_LIST = setRandomStrList() #支付用随机字符串
MAX_RANDOM_STR_COUNT = 12 #支付用随机字符串最大长度

def packSignDict2List(signDict): #字典转为list，生成签名用
    signList = []
    for key, value in signDict.items():
        signStr = '%s=%s'%(key, value)
        signList.append(signStr)
    return signList

def packSignDict2XML(signDict, sign): #打包为xml字符串
    XMLStr = '<xml>'
    for key, value in signDict.items():
        str = '<%s>%s</%s>'%(key, value, key)
        XMLStr = XMLStr + str
    signStr = '<sign>%s</sign>'%(sign)
    XMLStr = XMLStr + signStr + '</xml>'
    return XMLStr

def getSign(strList): #生成签名
    strList.sort()
    signStr = strList[0]
    strList.remove(signStr)
    for data in strList:
        signStr += ('&' + data)
    signStr += ('&key=' + MCH_KEY)
    signMD5 = hashlib.md5()
    signMD5.update(signStr)
    sign =  signMD5.hexdigest().upper()
    return sign

def getOutTradeNo(goodsNum, num): #生成订单号
    outTradeNo = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    outTradeNo += "%03d"%(int(goodsNum))
    outTradeNo += "%010d"%(int(num))
    for count in xrange(MAX_TRADE_NO_COUNT - len(outTradeNo)):
        outTradeNo += str(random.choice([0,1,2,3,4,5,6,7,8,9]))
    return outTradeNo
MAX_TRADE_NO_COUNT = 32 #订单号最大长度

def getUrlMessage(getUrl):
    socket.setdefaulttimeout(WAIT_WEB_TIME)
    try:
        url = urllib.urlopen(getUrl)
        data = url.read()
        message = json.loads(data)
    except Exception,e:
        print 'get weixin message error:', e
        message = {'errcode':123}
    return message

def checkWeixinCode(code):#校验微信code
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code"%(APPID, SECRET, code)
    message = getUrlMessage(url)
    if 'errcode' in message:
        print 'weixin check code error:', message
        return False
    else:
        return message

def getWeixinData(openID, accessToken):#获得微信信息
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s"%(accessToken, openID)
    message = getUrlMessage(url)
    if 'errcode' in message:
        print 'weixin get player data error:', message
        return False
    else:
        return message

def onRefreshToken(refreshToken):#刷新accessToken
    url = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=%s&grant_type=refresh_token&refresh_token=%s"%(APPID, refreshToken)
    message = getUrlMessage(url)
    if 'access_token' in message:
        return message['access_token']
    else:
        print 'weixin refresh token error:', message
        return False

def checkAccessToken(openID, access_token):#校验accessToken
    url = "https://api.weixin.qq.com/sns/auth?access_token=%s&openid=%s"%(access_token, openID)
    message = getUrlMessage(url)
    if message['errcode']:
        print 'weixin check access token error:', message
        return False
    else:
        return True

def getRandomAccount(num, id, redis): #随机账号生成
    account = ''
    for count in xrange(num):
        char = random.choice(RANDOM_LIST)
        account = account+char
    account = '%s%s'%(account, id)
    account2user_table = FORMAT_ACCOUNT2USER_TABLE%(account)
    table = redis.get(account2user_table)
    if table:
        return getRandomAccount(num, id, redis)
    else:
        return account

def setOpenid2account(openID, accessToken, refreshToken, ip, redis, code):#微信号绑定账号
    userData = getWeixinData(openID, accessToken)
    unionid = userData['unionid']

    if not userData:
        return

    curTime = datetime.datetime.now()
    curRegDateTable = FORMAT_REG_DATE_TABLE%(curTime.strftime("%Y-%m-%d"))
    #创建新的用户数据
    id = redis.incr(FORMAT_USER_COUNT_TABLE)
    account = getRandomAccount(RANDOM_ACCOUNT_COUNT, id, redis)
    table = FORMAT_USER_TABLE%(id)
    pipe = redis.pipeline()
    pipe.hmset(table, 
        {
            'account'       :   account, 
            'password'      :   code,
            'nickname'      :   userData['nickname'] if userData['nickname'] else account,
            'name'          :   account,
            'currency'      :   'CNY', #国家需要做微信到数据库的变换映射
            'money'         :   0.0,
            'wallet'        :   0.0,
            'vip_level'     :   0,
            'exp'           :   0,
            'level'         :   0,
            'charge'        :   0.0,
            'charge_count'  :   0,
            'game_count'    :   0,
            'coin_delta'    :   0,
            'parentAg'      :   'CHNWX', #上线代理需要获得
            'email'         :   '',
            'phone'         :   '',
            'valid'         :   1,
            'last_join_ip'  :   '',
            'last_join_date':   '',
            'last_exit_ip'  :   '',
            'last_exit_date':   '',
            'last_login_ip' :   '',
            'last_login_date':  '',
            'last_logout_ip':   '',
            'last_logout_date': '',
            'last_present_date' : '',
            'newcomer_present_date' : '',
            'reg_ip'        :   ip,
            'reg_date'      :   curTime.strftime("%Y-%m-%d %H:%M:%S"),
            'coin'          :   0,
            'accessToken'   :   accessToken, #以下新增
            'refreshToken'  :   refreshToken,
            'openid'        :   openID,
            'sex'           :   userData['sex'], #性别
            'roomCard'      :   5,
            'headImgUrl'    :   userData['headimgurl'], #头像
            'unionID'       :   userData['unionid'],
            'playCount'     :   0
        }
    )
    pipe.set(WEIXIN2ACCOUNT%(unionid), account) #微信ID到账号映射
    pipe.sadd(ACCOUNT4WEIXIN_SET, account) #微信账号集合
    account2user_table = FORMAT_ACCOUNT2USER_TABLE%(account)
    pipe.set(account2user_table, table)
    pipe.sadd(FORMAT_ADMIN_ACCOUNT_MEMBER_TABLE%('CHNWX'), id) #上线代理需要获得
    pipe.sadd(curRegDateTable, account)
    pipe.execute()

    return account

