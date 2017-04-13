#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    游戏入口
"""

from bottle import request, Bottle, abort, redirect, response, template,static_file
from db_define import *
from weixin_data import *
from talk_data import sendTalkData
from common.install_plugin import install_redis_plugin
from common.log import *
import urllib2
import json
import random
entry_app = Bottle()

#安装插件
install_redis_plugin(entry_app)

import md5
ACCEPT_NUM_BASE = 198326
MAX_COUNTRY_CODE_TTL = 7*24*3600
ACCEPT_TT = [md5.new(str(ACCEPT_NUM_BASE+i)).hexdigest() for i in xrange(10)]
GET_IP_AREA_URL = "http://ip.taobao.com/service/getIpInfo.php?ip=%s"

"""
自动获取服务器地址接口，返回一个合适的游戏服务器ip及port给客户端
# post
# request sample: http://<server>/game/getServer
params:
    [tt]md5一个随机范围在198326-198335的数字做校验，简单规避爬虫等攻击尝试
    [room]房间号，发送此字段则获得房间所在ip
    [gameId]
        游戏id，区别不同游戏：
            四喜麻将=101
return:
    返回json:
        {
            "code"  :   #返回码，0:正确，可读ip和port字段，否则
                                 1:非法tt，客户端应提示服务器正在维护中，请稍后在进（等同于连接不上）
                                 2:玩家已满，客户端应提示服务器忙碌，请稍后在进
                                 3:非法ac，与1同样提示
                                 4:ac账号不存在，客户端应提示用户名或密码错误
                                 5:跳转cache超时，客户端应提示：“登录超时或不合法，请重新进入游戏。”
                                 6:房间不存在
            "ip"    :   #游戏服务ip地址字串,
            "port"  :   #游戏服务端口字串
        }
"""
@entry_app.post('/getMahjongServer')
@entry_app.post('/getServer')
def getServer(redis):
    tt = request.forms.get('tt', '').strip()
    ip = request['REMOTE_ADDR']
    account = request.forms.get('account', '').strip()
    gameId = request.forms.get('gameId', '').strip()
    roomNum = request.forms.get('room', '').strip() #房间号，后续需要依据房间号获得ip
    
    log_debug("try getServer: account[%s] gameId[%s] roomNum[%s] tt[%s]."%(account, type, gameId, roomNum, tt))

    response.add_header('Access-Control-Allow-Origin', '*')

    if not gameId:
        gameId = 101
    else:
        try:
            gameId = int(gameId)
        except:
            abort(403, "Invalid params.")

    if str(gameId) not in GAME_IDS:
        abort(403, "Invalid gameId.")

    if tt not in ACCEPT_TT:
        log_debug("try getServer: get faild, code[1].")
        return {'code' : 1}

    # 获得省份
    # tableIP2RegionCode = FORMAT_IP2REGIONCODE%(ip)
    # if not redis.exists(tableIP2RegionCode) and ip[:7] != '192.168':
        # for i in xrange(3):
            # try:
                # resp = urllib2.urlopen(GET_IP_AREA_URL%(ip), timeout=3).read()
                # jsonObj = json.loads(resp)
                # regionCode = jsonObj['data']['region']
                # break
            # except Exception, e:
                # regionCode = None
        # if regionCode:
            # pipe = redis.pipeline()
            # pipe.set(tableIP2RegionCode, regionCode)
            # pipe.expire(tableIP2RegionCode, MAX_COUNTRY_CODE_TTL)
            # pipe.execute()

    serverIp = ''
    serverPort = 0
    realAccount = account #微信登录需要根据类型从库中获得账号

    #房间号获得ip
    errCode = 0
    if roomNum:
        if redis.exists(ROOM2SERVER%(roomNum)):
            serverTable = redis.get(ROOM2SERVER%(roomNum))
            serverIp = serverTable.split(':')[1]
            serverPort = serverTable.split(':')[2]
            # log_debug("try getServer: get succed, code[0] ip[%s] port[%s]."%(serverIp, serverPort))
            # return {'code' : 0, 'ip' : serverIp, 'port' : serverPort}
        else:
            errCode = 6

    #重连部分
    if account:
        if redis.exists('unionid2account:unionid:%s:key'%(account)):
            realAccount = redis.get(WEIXIN2ACCOUNT%(account))
            exitPlayerData = 'player:%s:exitPlayer:101:hash'%(realAccount)
            if redis.exists(exitPlayerData):
                serverIp, serverPort = redis.hmget(exitPlayerData, ('ip', 'port'))
            elif redis.sismember(ONLINE_GAME_ACCOUNTS_TABLE%(gameId), realAccount):
                userOnlineTable = FORMAT_CUR_USER_GAME_ONLINE%(realAccount, gameId)
                serviceTag = redis.hget(userOnlineTable, 'serviceTag')
                serverIp = serviceTag.split(':')[1]
                serverPort = serviceTag.split(':')[2]

    #非重连
    if (not serverIp) or (not serverPort):
        countPlayerLimit = GAMEID2COUNT_PLAYER_PER_SERVER[gameId]
        reservedServers = []
        serverList = redis.lrange(FORMAT_GAME_SERVICE_SET%(gameId), 0, -1)
        for serverTable in serverList:
            playerCount = redis.hincrby(serverTable, 'playerCount', 0)
            if countPlayerLimit and playerCount >= countPlayerLimit:
                continue
            _, _, _, currency, ipData, portData = serverTable.split(':')
            reservedServers.append((ipData, portData))

        if reservedServers:
            serverIp, serverPort = reservedServers[0]
            # serverIp, serverPort = random.choice(reservedServers)

    if serverIp and serverPort:
        log_debug("try getServer: get succed, code[%s] ip[%s] port[%s]."%(errCode, serverIp, serverPort))
        return {'code' : errCode, 'ip' : serverIp, 'port' : serverPort}
    else:
        log_debug("try getServer: get faild, code[2] poenID[%s]."%(openID))
        return {'code' : 2}

