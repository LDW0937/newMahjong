#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    后台配置文件
"""

#[consts config]
BACK_PRE           =           '/admin'
TEMPLATE_NAME      =           'default'

#[path config]
DOWNLOAD_PATH             =            'mahjong/static/download/'
STATIC_PATH               =            'mahjong/static/'
STATIC_ADMIN_PATH         =            '/assest/default'
STATIC_LAYUI_PATH         =            '/assest/common/layui'

#[]

#[link config]
LINK2DB = {
    'mysql'  :   {
                    'user'      :       'swadmin',
                    'host'      :       '192.168.0.99',
                    'port'      :       '3306',
                    'db'        :       'smart_win',
                    'passwd'    :       '6NUXzNfbezQ54Q7gV2tsJdKG5J8s5d1t'
     },

     'redis' :   {
                     'host'     :       '192.168.0.99',
                     'db'       :       '1',
                     'port'     :       '6379',
                     'passwd'   :       'Fkkg65NbRwQOnq01OGMPy5ZREsNUeURm'
     }
}