"""
Bottle_session is a session manager for the Bottle microframework that uses a
cookie to maintain your web session and stores a hash associated with that
cookie using the redis key-value store. It is designed as a simple Bottle
plugin.

Examples and additional documentation are available in the README and
on the website: https://bitbucket.org/devries/bottle-session

Copyright (c) 2013, Christopher De Vries.
License: Artistic License 2.0 (see LICENSE.txt)
"""

__version__ = '0.4'

import redis
import inspect
from bottle import PluginError
from bottle import request
from bottle import response
import uuid

try:
    from Crypto.Random import get_random_bytes
    def getUuid():
        return uuid.UUID(bytes=get_random_bytes(16))

except ImportError:
    def getUuid():
        return uuid.uuid4()

MAX_TTL = 7*24*3600 # 7 day maximum cookie limit for sessions
SESSION_TTL = 8*60 # session lifetime

class SessionPlugin(object):
    """Bottle sessions using redis plugin class.

    This class creates a plugin for the bottle framework which uses cookies
    to handle sessions and stores session information in a redis database.
    """

    name = 'session'
    api = 2

    def __init__(self,host='localhost',port=6379,db=1,cookie_name='session',cookie_lifetime=SESSION_TTL,keyword='session'):
        """Session plugin for the bottle framework.

        Args:
            host (str): The host name of the redis database server. Defaults to
                'localhost'.
            port (int): The port of the redis database server. Defaults to
                6379.
            db (int): The redis database numbers. Defaults to 0.
            cookie_name (str): The name of the browser cookie in which to store
                the session id. Defaults to 'bottle.session'.
            cookie_lifetime (int): The lifetime of the cookie in seconds. When
                the cookie's lifetime expires it will be deleted from the redis
                database. The browser should also cause it to expire. If the
                value is 'None' then the cookie will expire from the redis
                database in 7 days and will be a session cookie on the 
                browser. The default value is 300 seconds.
            keyword (str): The bottle plugin keyword. By default this is
                'session'.

        Returns:
            A bottle plugin object.
        """

        self.host = host
        self.port = port
        self.db = db
        self.cookie_name = cookie_name
        self.cookie_lifetime = cookie_lifetime
        self.keyword = keyword
        self.connection_pool = None

    def setup(self,app):
        for other in app.plugins:
            if not isinstance(other, SessionPlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found another session plugin with "\
                        "conflicting settings (non-unique keyword).")

        if self.connection_pool is None:
            self.connection_pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)

    def apply(self,callback,context):
        conf = context.config.get('session') or {}
        args = inspect.getargspec(context.callback)[0]

        if self.keyword not in args:
            return callback

        def wrapper(*args,**kwargs):
            r = redis.Redis(connection_pool=self.connection_pool)
            kwargs[self.keyword] = Session(r,self.cookie_name,self.cookie_lifetime)
            rv = callback(*args,**kwargs)
            return rv
        return wrapper

    def getSession(self):
        r = redis.Redis(connection_pool=self.connection_pool)
        return Session(r,self.cookie_name,self.cookie_lifetime)


class Session(object):
    """A bottle session object.

    This object is a dictionary like object in which you can place data
    associated with the current session. It is created by the bottle
    framework and accessible using the keyword defined when creating
    the plugin.
    """

    def __init__(self,rdb,cookie_name='bottle.session',cookie_lifetime=None):
        self.rdb = rdb
        self.cookie_name = cookie_name
        if cookie_lifetime is None:
            self.ttl = MAX_TTL
            self.max_age = None
        else:
            self.ttl = cookie_lifetime
            self.max_age = cookie_lifetime
        self.cookie_value = self.get_cookie()
        if self.cookie_value:
            self.validate_session_id(self.cookie_value)
        else:
            self.new_session_id()

    def get_cookie(self):
        uid_cookie = request.get_cookie(self.cookie_name)
        return uid_cookie

    def set_cookie(self,value):
        response.set_cookie(self.cookie_name,value,max_age=self.max_age,path='/')

    def validate_session_id(self,cookie_value):
        keycheck = 'session:%s'%(str(uuid.UUID(cookie_value)))
        if self.rdb.exists(keycheck):
            self.session_hash = keycheck
            self.expire()
        else:
            self.new_session_id()

    def new_session_id(self):
        uid = getUuid()
        self.session_hash = 'session:%s'%(str(uid))
        self.cookie_value = uid.hex
        self.set_cookie(self.cookie_value)

    def expire(self):
        self.set_cookie(self.cookie_value)
        self.rdb.expire(self.session_hash,self.ttl)

    def destroy(self):
        """Destroy the session.

        This function deletes the current session id from the database along
        with all associated data. It will create a new session id for the
        remainder of the transaction.
        """

        self.rdb.delete(self.session_hash)
        self.new_session_id()

    def regenerate(self):
        """Regenerate the session id.

        This function creates a new session id and stores all information
        associated with the current id in that new id. It then destroys the
        old session id. This is useful for preventing session fixation attacks
        and should be done whenever someone uses a login to obtain additional
        authorizaiton.
        """

        oldhash = self.session_hash
        self.new_session_id()
        try:
            self.rdb.rename(oldhash,self.session_hash)
            self.expire()
        except:
            pass

    def __contains__(self,key):
        """Check if a key is in the session dictionary.
        
        Args:
            key (str): The dictionary key.
        """

        return self.rdb.hexists(self.session_hash,key)

    def __delitem__(self,key):
        """Delete an item from the session dictionary.
        
        Args:
            key (str): The dictionary key.
        """

        self.rdb.hdel(self.session_hash,key)

    def __getitem__(self,key):
        """Return a value associated with a key from the session dictionary.
        
        Args:
            key (str): The dictionary key.

        Returns:
            str: The value associate with that key or None if the key is
                not in the dictionary.
        """

        self.expire()
        return self.rdb.hget(self.session_hash,key)

    def __setitem__(self,key,value):
        """Set an existing or new key, value association.

        Args:
            key (str): The dictionary key.
            value (str): The dictionary value
        """

        self.rdb.hset(self.session_hash,key,value)
        self.expire()

    def __len__(self):
        """Get the number of key,value pairs in the dictionary.

        Returns:
            int: Number of key value pairs in the dictionary.
        """

        return self.rdb.hlen(self.session_hash)

    def __iter__(self):
        """Iterate through the key,value pairs.

        Generates:
            (str, str): Key and value tuples in the dictionary.
        """

        all_items = self.rdb.hgetall(self.session_hash)
        for t in all_items.items():
            yield t

    def get(self,key,default=None):
        """Get a value from the dictionary.

        Args:
            key (str): The dictionary key.
            default (any): The default to return if the key is not in the
                dictionary. Defaults to None.

        Returns:
            str or any: The dictionary value or the default if the key is not
                in the dictionary.
        """

        retval = self.__getitem__(key)
        if not retval:
            retval = default

        return retval

    def has_key(self,key):
        """Check if the dictionary contains a key.

        Args:
            key (str): The dictionary key.

        Returns:
            bool: True if the key is in the dictionary. False otherwise.
        """
        return self.__contains__(key)

    def items(self):
        """Return a list of all the key, value pair tuples in the dictionary.

        Returns:
            list of tuples: [(key1,value1),(key2,value2),...,(keyN,valueN)]
        """
        all_items = self.rdb.hgetall(self.session_hash)
        return all_items.items()

    def keys(self):
        """Return a list of all keys in the dictionary.

        Returns:
            list of str: [key1,key2,...,keyN]
        """
        all_items = self.rdb.hgetall(self.session_hash)
        return all_items.keys()

    def values(self):
        """Returns a list of all values in the dictionary.

        Returns:
            list of str: [value1,value2,...,valueN]
        """
        all_items = self.rdb.hgetall(self.session_hash)
        return all_items.values()

