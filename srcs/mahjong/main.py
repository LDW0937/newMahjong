#-*- coding:utf-8 -*-
#!/usr/bin/env python

"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    平台入口
"""
import bottle
import json
import random
import subprocess
import redis
from i18n.i18n import initializeWeb
from common.config import *
from common.install_plugin import install_redis_plugin,install_session_plugin

#实例化语言包
initializeWeb()

#模板
bottle.TEMPLATE_PATH.append('mahjong/template/%s'%(TEMPLATE_NAME))
random.seed()

#主应用
main_app = bottle.default_app()
#配置文件
config_file = 'conf_release.json'
# #从json中读取配置文件
with open(config_file) as f:
    main_app.config.load_dict(json.load(f))

#安装插件
install_redis_plugin(main_app)
install_session_plugin(main_app)

if main_app.config.get('download_view', 1):
    @main_app.get('/download/<res_path:path>')
    def download_path(res_path):
        '''
        @description:               是否允许下载
        '''
        return bottle.static_file(res_path,root=DOWNLOAD_PATH, download=True)

@main_app.get('/<res_path:path>')
def content_path(res_path):
    '''
     @description: 设置资源文件路径
    '''
    #支持跨域请求
    print res_path
    print bottle.static_file(res_path,root='mahjong/static/')
    return bottle.static_file(res_path,root='mahjong/static/')


if main_app.config.get('admin_view', 1):
    #是否允许访问后台
    from admin import admin_app
    main_app.mount('/admin',admin_app)