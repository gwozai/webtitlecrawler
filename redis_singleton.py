import redis
from config import REDIS_CONFIG

def operator_status(func):
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
            host=REDIS_CONFIG['host'],
            port=REDIS_CONFIG['port'],
            db=REDIS_CONFIG['dbid'],
            password=REDIS_CONFIG['password'])
    @operator_status
    def set_data(self, key, value):
        return self._connection.set(key, value)

    @operator_status
    def get_data(self, key):
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        return self._connection.delete(key)

    @operator_status
    def exists_data(self, key):
        return self._connection.exists(key)

    @operator_status
    def set_hash_data(self, name, key, value):
        return self._connection.hset(name, key, value)

    @operator_status
    def get_hash_data(self, name, key):
        return self._connection.hget(name, key)

    @operator_status
    def exists_hash_data(self, name, key):
        return self._connection.hexists(name, key)

    @operator_status
    def enqueue(self, key, value):
        return self._connection.rpush(key, value)  # rpush appends value to the list

    @operator_status
    def dequeue(self, key):
        return self._connection.lpop(key)  # lpop pops out the first element of the list
# if __name__ == '__main__':
#     print(RedisCache().set_data('Testkey', "Simple Test"))
#     print(RedisCache().get_data('Testkey'))
#     print(RedisCache().del_data('Testkey'))
#     print(RedisCache().get_data('Testkey'))
#     print(RedisCache().exists_data('Testkey'))
#     print(RedisCache().set_hash_data('Testhash', 'Testkey', "Hash Test"))
#     print(RedisCache().get_hash_data('Testhash', 'Testkey'))
#     print(RedisCache().get_hash_data('Testhash', 'Testkey'))
#     print(RedisCache().get_hash_data('Testhash', 'Testkey'))
#     print(RedisCache().exists_hash_data('Testhash', 'Testkey'))
#     print(RedisCache().enqueue('Testqueue', "Test Enqueue"))
#     print(RedisCache().enqueue('Testqueue', "Test1 Enqueue"))
#     print(RedisCache().dequeue('Testqueue'))
#     print(RedisCache().dequeue('Testqueue'))