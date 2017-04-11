# -*- coding: utf-8 -*-

mysql_plugin = None
memcache_plugin = None
redis_plugin = None
session_plugin = None

# 安装插件
def install_mysql_plugin(app):
    global mysql_plugin
    if not mysql_plugin:
        from bottle.ext import mysql
        mysql_plugin = mysql.MysqlPlugin()
    app.install(mysql_plugin)

def install_memcache_plugin(app):
    global memcache_plugin
    if not memcache_plugin:
        from bottle.ext import memcache
        memcache_plugin = memcache.MemcachePlugin()
    app.install(memcache_plugin)

def install_redis_plugin(app):
    global redis_plugin
    if not redis_plugin:
        from bottle.ext import redis
        redis_plugin = redis.RedisPlugin()
    app.install(redis_plugin)

#second call
def install_session_plugin(app):
    global session_plugin
    if not session_plugin:
        from bottle.ext import session
        session_plugin = session.SessionPlugin(cookie_lifetime=300)
        global redis_plugin
        assert redis_plugin is not None, "need call install_redis_plugin first."
        session_plugin.connection_pool = redis_plugin.redisdb
    app.install(session_plugin)
