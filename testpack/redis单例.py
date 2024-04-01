import redis


class RedisDBConfig:
    HOST = '1.15.7.2'
    PORT = 6379
    DBID = 0
    PASSWORD = 'sY38KEspDNZjptN6'


def operator_status(func):
    '''get operatoration status
    '''

    def gen_status(*args, **kwargs):
        error, result = None, None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            error = str(e)

        return {'result': result, 'error': error}

    return gen_status


class RedisCache(object):
    def __init__(self):
        if not hasattr(RedisCache, 'pool'):
            RedisCache.create_pool()
        self._connection = redis.Redis(connection_pool=RedisCache.pool)

    @staticmethod
    def create_pool():
        RedisCache.pool = redis.ConnectionPool(
            host=RedisDBConfig.HOST,
            port=RedisDBConfig.PORT,
            db=RedisDBConfig.DBID,
            password=RedisDBConfig.PASSWORD)

    @operator_status
    def set_data(self, key, value):
        '''set data with (key, value)
        '''
        return self._connection.set(key, value)

    @operator_status
    def get_data(self, key):
        '''get data by key
        '''
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        '''delete cache by key
        '''
        return self._connection.delete(key)


if __name__ == '__main__':
    print(RedisCache().set_data('Testkey', "Simple Test"))
    print(RedisCache().get_data('Testkey'))
    print( RedisCache().del_data('Testkey'))
    print(RedisCache().get_data('Testkey'))