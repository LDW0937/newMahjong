import redis
import inspect
from bottle import default_app
from common.config import LINK2DB

class RedisPlugin(object):
    name = 'redis'

    def __init__(self,host=LINK2DB['redis']['host'],port=LINK2DB['redis']['port'],database=LINK2DB['redis']['db'],keyword='redis'):
        conf = default_app().config
        self.host = str(conf.get('redis.host', host))
        self.port = conf.get('redis.port', port)
        self.database = conf.get('redis.database', database)
        self.keyword = str(conf.get('redis.keyword', keyword))
        self.redisdb = None

    def setup(self,app):
        for other in app.plugins:
            if not isinstance(other,RedisPlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found another redis plugin with "\
                        "conflicting settings (non-unique keyword).")
        if self.redisdb is None:
            self.redisdb = redis.ConnectionPool(host=self.host, port=self.port, db=self.database, password=LINK2DB['redis']['passwd'])

    def apply(self,callback,context):
        args = inspect.getargspec(context['callback'])[0]
        if self.keyword not in args:
            return callback

        def wrapper(*args,**kwargs):
            kwargs[self.keyword] = redis.Redis(connection_pool=self.redisdb)
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

Plugin = RedisPlugin
