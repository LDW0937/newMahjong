#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    游戏模块
"""
from bottle import *
from admin import admin_app
from config.config import STATIC_LAYUI_PATH,STATIC_ADMIN_PATH,BACK_PRE
from common.utilt import *
from datetime import datetime
from model.gameModel import *
import json

@admin_app.get('/game/list')
def getGameList(redis):
    """
        游戏列表视图
    """
    lang = getLang()

    isList = request.GET.get('list','').strip()

    info = {
            'title'         :     '游戏列表',
            'addTitle'      :     '创建新游戏',
            'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
            'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH,
            'tableUrl'      :     BACK_PRE+'/game/list?list=1'
    }
    #accesses = eval(session['access'])

    if isList:
        res = getGamesList(redis)
        return json.dumps(res)
    else:
        #info['createAccess'] = True if BACK_PRE+'/game/create' in accesses else False
        info['createUrl']   = BACK_PRE+'/game/create'
        return template('admin_game_list',info=info,lang=lang)

@admin_app.get('/game/create')
def getGameCreate(redis,session):
    """
        创建游戏视图
    """
    lang = getLang()


    info = {
            'title'             :       '创建新游戏',
            'STATIC_LAYUI_PATH'      :       STATIC_LAYUI_PATH,
            'STATIC_ADMIN_PATH'      :       STATIC_ADMIN_PATH,
            'back_pre'          :       BACK_PRE,
            'submitUrl'         :       BACK_PRE+'/game/create',
            'uploadUrl'         :       BACK_PRE+'/game/iconUpload',
            'module_id'         :       '',
            'name'              :       '',
            'icon_path'         :       '',
            'web_tag'           :       '',
            'apk_tag'           :       '',
            'ipa_tag'           :       '',
            'pc_tag'            :       '',
            'apksize'           :       '',
            'apkmd5'            :       '',
            'downloadUrl'       :       '',
            'version'           :       '',
            'minVersion'        :       '',
            'iosVersion'        :       '',
            'pack_name'         :       '',
            'game_rule'         :       ''
    }

    #recordLastURL(session,BACK_PRE+'/game/list')

    return template('admin_game_create',message='',info=info,lang=lang)

@admin_app.post('/game/create')
def do_gameCreate(redis,session):
    """
        创建游戏控制器
    """
    curTime = datetime.now()
    lang    = getLang()

    name     =  request.forms.get('name','').strip()
    version  =  request.forms.get('version','').strip()
    web_tag  =  request.forms.get('web_tag','').strip()
    ipa_tag  =  request.forms.get('ipa_tag','').strip()
    apk_tag  =  request.forms.get('apk_tag','').strip()
    minVersion  =  request.forms.get('minVersion','').strip()
    iosVersion  =  request.forms.get('iosVersion','').strip()
    pack_name  =  request.forms.get('pack_name','').strip()
    downloadUrl  =  request.forms.get('downloadUrl','').strip()
    IPAURL  =  request.forms.get('IPAURL','').strip()
    apk_size  =  request.forms.get('apk_size','').strip()
    apk_md5  =  request.forms.get('apk_md5','').strip()
    game_rule  =  request.forms.get('game_rule','').strip()
    module_id  =  request.forms.get('module_id','').strip()

    checkNullFields = [
        {'field':name,'msg':'游戏名称不能为空'},
        {'field':version,'msg':'游戏版本号不能为空'}
    ]

    for check in checkNullFields:
        if not check['field']:
            return {'code':1,'msg':check['msg']}

    #print
    print '[%s][gameCreate][info] name[%s] version[%s] minVersion[%s] iosVersion[%s] apk_size[%s] module_id[%s]'\
                    %(curTime,name,version,minVersion,iosVersion,apk_size,module_id)

    gameInfo = {

            'name'          :       name,
            'version'       :       version,
            'web_tag'       :       web_tag,
            'ipa_tag'       :       ipa_tag,
            'apk_tag'       :       apk_tag,
            'minVersion'    :       minVersion,
            'iosVersion'    :       iosVersion,
            'pack_name'      :      pack_name,
            'downloadUrl'   :       downloadUrl,
            'apk_size'      :       apk_size,
            'apk_md5'       :       apk_md5,
            'game_rule'     :       game_rule,
            'module_id'     :       module_id
    }

    if createGame(redis,gameInfo):
        return {'code':0,'msg':'游戏[%s]创建成功'%(name),'jumpUrl':BACK_PRE+'/game/list'}

    return {'code':1,'msg':'游戏[%s]创建失败.'%(name)}


@admin_app.get('/game/modify')
def getGameModify(redis,session):
    """
        游戏信息修改视图
    """
    pass

@admin_app.post('/game/modify')
def do_gameModify(redis,session):
    """
        游戏信息修改控制器
    """
    pass

@admin_app.get('/game/module/list')
def getGameModuleList(redis,session):
    """
        游戏模块列表视图
    """
    pass

@admin_app.get('/game/module/create')
def getGameModule(redis,session):
    """
        游戏模块信息创建视图
    """
    pass

@admin_app.post('/game/module/create')
def do_createGameModule(redis,session):
    """
        游戏模块信息创建逻辑
    """
    pass

@admin_app.get('/game/module/modify')
def getGameModuleModify(redis,session):
    """
        游戏模块信息修改视图
    """
    pass

@admin_app.post('/game/module/modify')
def do_gameModuleModify(redis,session):
    """
        游戏模块信息修改逻辑
    """
    pass