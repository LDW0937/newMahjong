#-*- coding:utf-8 -*-
#!/usr/bin/python
"""
Author:$Author$
Date:$Date$
Revision:$Revision$

Description:
    后台APP应用入口
"""

from bottle import Bottle
from common.install_plugin import install_redis_plugin,install_session_plugin

admin_app = Bottle()

install_redis_plugin(admin_app)
install_session_plugin(admin_app)

import admin_index
import admin_auth
#会员模块
import admin_member