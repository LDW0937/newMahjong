#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    代理模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from common.log import *
from datetime import datetime
from web_db_define import *
from model.agentModel import *
from access_module import *
import hashlib
import json

def getAgListInfos(redis,agentId):
    """
        获取代理列表
    """
    parentTable = AGENT_CHILD_TABLE%(agentId)

    subIds = redis.smembers(parentTable)

    subAgLists = []
    for subId in subIds:

        agentTable = AGENT_TABLE%(subId)

        aType,valid,reg_date,account,roomCard,aId,isCreate = \
                        redis.hmget(agentTable,('type','valid','regDate','account','roomcard','id','isCreate'))

        if not account:
            continue
        agInfo = {
                'valid'     :       valid,
                'parentId'  :       aId,
                'regDate'   :       reg_date,
                'parentAg'  :       account,
                'roomCard'  :       roomCard
        }

        #获取操作权限
        agInfo['op'] = []
        for access in ACCESS_AGENT_LIST:
            if (aType == '3' or isCreate != '1' ) and access['url'] == '/admin/agent/create':
                #最多只能创建二级代理
                continue
            if access['url'] == '/admin/agent/freeze':
                agInfo['op'].append({'url':access['url'],'txt':'冻结' \
                            if agInfo['valid'] == '1' else '解冻','method':access['method']})
            else:
                agInfo['op'].append({'url':access['url'],'method':access['method'],'txt':access['txt']})

        subAgLists.append(agInfo)

    return subAgLists

@admin_app.get('/agent/list')
def getAgentList(redis,session):
    """
        代理列表
    """
    curTime = datetime.now()
    lang    = getLang()
    isList  = request.GET.get('list','').strip()
    agentId = request.GET.get('id','').strip()
    if not agentId:
        agentId = session['id']
    adminTable = AGENT_TABLE%(agentId)
    createAgChildAccess,aType = redis.hmget(adminTable,('isCreate','type'))
    if isList:
        res = getAgListInfos(redis,agentId)
        return json.dumps(res)
    else:
        info = {
                'title'                  :       '下线代理列表',
                'showPlus'               :       'true' if aType == '0' else 'false',
                'createAccess'           :       createAgChildAccess,
                'createUrl'              :       BACK_PRE+'/agent/create',
                'listUrl'                :       BACK_PRE+'/agent/list?list=1',
                'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
                'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH 
        }
        return template('admin_agent_list',info=info,lang=lang)

@admin_app.get('/agent/info')
def getAgInfo(redis,session):
    """
        代理信息查看
    """
    curTime = datetime.now()
    lang    = getLang()
    agentId = request.GET.get('id','').strip()
    if not agentId:
        return {'code':'1','msg':'非法操作!'}

    adminTable = AGENT_TABLE%(agentId)
    account,aid,name,roomCard,regDate,regIp,valid,aType = \
                redis.hmget(adminTable,('account','id','name','roomCard','regDate','regIp','valid','type'))

    agentInfo = {
            'title'         :       '代理(%s)详细信息'%(account),
            'backUrl'       :       '/admin/agent/list',
            'name'          :        name,
            'account'       :        account,
            'roomCard'      :        roomCard,
            'regDate'       :        regDate,
            'regIp'         :        regIp,
            'valid'         :        '有效' if valid else '冻结',
            'aType'         :        TYPE2TXT[aType],
            'aid'           :        aid,
            'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
            'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH 
    }

    log_debug('[%s][agent][Info][info] agent[%s] detail info [%s]'%(curTime,account,agentInfo))
    return template('admin_agent_info',info=agentInfo,lang=lang)

@admin_app.get('/agent/create')
def getAgentCreate(redis,session):
    """
        创建代理
    """
    curTime = datetime.now()
    agentId =  request.GET.get('id','').strip()
    lang    = getLang()

    if not agentId:
        agentId = session['id']

    adminTable = AGENT_TABLE%(agentId)
    aType = redis.hget(adminTable,'type')
    log_debug('[%s][admin][ag][info] create ag.parentId[%s]'%(curTime,agentId))

    info = {
            'title'                  :       '创建代理（上级代理:%s）'%(agentId),
            'parentAg'               :       agentId,
            'aType'                  :       aType,
            'backUrl'                :       BACK_PRE+'/agent/list',
            'submitUrl'              :       BACK_PRE+'/agent/create',
            'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
            'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH 
    }

    return template('agent_create',info=info,lang=lang)



@admin_app.post('/agent/create')
def do_agCreate(redis,session):
    """
        创建代理操作
    """
    curTime = datetime.now()
    agentparentId = request.forms.get('parentAg','').strip()
    account = request.forms.get('account','').strip()
    passwd = request.forms.get('passwd','').strip()
    isCreate = request.forms.get('isCreate','').strip()
    comfirPasswd = request.forms.get('comfirPasswd','').strip()

    if not agentparentId:
        return {'code':1,'msg':'非法创建代理!'}
    # agentparentId = redis.get(AGENT_ACCOUNT_TO_ID%(parentAg))
    #当前创建的是
    aType,aName = redis.hmget(AGENT_TABLE%(agentparentId),('type','name'))

    log_debug('[%s][agent][create][info] try to create agent.parentAg[%s] account[%s] passwd[%s] comfirmPasswd[%s]'\
                    %(curTime,agentparentId,account,passwd,comfirPasswd))

    checkFields = [
        {'field':account,'msg':'代理账号不能为空'},
        {'field':passwd,'msg':'密码不能为空'},
        {'field':comfirPasswd,'msg':'密码不能为空'}
    ]

    for field in checkFields:
        if not field['field']:
            return {'code':1,'msg':field['msg']}
    parentSetTable  =  AGENT_CHILD_TABLE%(agentparentId)
    admimtoIdTalbel = AGENT_ACCOUNT_TO_ID%(account)
    pipe = redis.pipeline()
    if not redis.exists(admimtoIdTalbel):

        agentId = getAgentIdNo(redis)
        adminTable  =  AGENT_TABLE%(agentId)

        agentInfo = {
                
                'id'                    :           agentId,
                'account'               :           account,
                'passwd'                :           hashlib.sha256(passwd).hexdigest(),
                'name'                  :           '',
                'shareRate'             :           0.5,
                'valid'                 :            1,
                'roomcard_id'           :           0,
                'parent_id'             :           agentparentId,
                'roomcard'              :           0,
                'regIp'                 :           '127.0.0.1',
                'regDate'               :           curTime.strftime("%Y-%m-%d %H:%M:%S"),
                'lastLoginIP'           :           1,
                'lastLoginDate'         :           1,
                'isCreate'              :           isCreate,
                'type'                  :           int(aType)+1,
        }

        pipe.hmset(adminTable,agentInfo)
        #创建代理账号映射id
        pipe.set(admimtoIdTalbel,agentId)
        #将该代理添加进父代理集合
        pipe.sadd(parentSetTable,agentId)
        pipe.execute()
    else:
        log_debug('[%s][agent][create][error] agent account[%s] is exists!'%(curTime,account))
        return {'code':1,'msg':'代理账号(%s)已经存在.'%(account)}

    #创建成功日志
    log_debug('[%s][agent][create][success] agent Id is [%s] ！'%(curTime,agentId))
    log_debug('[%s][agent][create][success] agent create success! info[%s]'%(curTime,agentInfo))
    return {'code':0,'msg':'创建代理(%s)成功'%(account),'jumpUrl':'/admin/agent/list'}

@admin_app.get('/agent/modify')
def getAgentModify(redis,session):
    """
        代理修改
    """
    pass
