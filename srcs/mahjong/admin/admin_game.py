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

@admin_app.get('/game/list')
def getGameList(redis):
    """
        游戏列表视图
    """
    pass

@admin_app.get('/game/create')
def getGameCreate(redis,session):
    """
        创建游戏视图
    """
    pass

@admin_app.post('/game/create')
def do_gameCreate(redis,session):
    """
        创建游戏控制器
    """
    pass

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