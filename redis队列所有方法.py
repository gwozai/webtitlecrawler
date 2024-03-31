import redis

class RedisDBConfig:
    HOST = '1.15.7.2'
    PORT = 6379
    DBID = 0
    PASSWORD = 'sY38KEspDNZjptN6'

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
            host=RedisDBConfig.HOST,
            port=RedisDBConfig.PORT,
            db=RedisDBConfig.DBID,
            password=RedisDBConfig.PASSWORD)

    @operator_status
    def lpush(self, key, values):
        return self._connection.lpush(key, *values)

    @operator_status
    def rpush(self, key, values):
        return self._connection.rpush(key, *values)

    @operator_status
    def lpop(self, key):
        return self._connection.lpop(key)

    @operator_status
    def rpop(self, key):
        return self._connection.rpop(key)

    @operator_status
    def ll_len(self, key):
        return self._connection.llen(key)

    @operator_status
    def lrange(self, key, start, end):
        return self._connection.lrange(key, start, end)

    @operator_status
    def ltrim(self, key, start, end):
        return self._connection.ltrim(key, start, end)
    @operator_status
    def rpoplpush(self, source, destination):
        return self._connection.rpoplpush(source, destination)

    @operator_status
    def brpoplpush(self, source, destination, timeout=0):
        return self._connection.brpoplpush(source, destination, timeout)

    @operator_status
    def lindex(self, key, index):
        return self._connection.lindex(key, index)

    @operator_status
    def lset(self, key, index, value):
        return self._connection.lset(key, index, value)

    @operator_status
    def linsert(self, key, where, refvalue, value):
        return self._connection.linsert(key, where, refvalue, value)

    @operator_status
    def lrem(self, key, value, num=0):
        return self._connection.lrem(key, value, num)
redis_cache = RedisCache()

# lpush示例
response = redis_cache.lpush('mylist', ['A', 'B', 'C'])
print(response)

# rpush示例
response = redis_cache.rpush('mylist', ['X', 'Y', 'Z'])
print(response)

# lpop示例
response = redis_cache.lpop('mylist')
print(response)

# rpop示例
response = redis_cache.rpop('mylist')
print(response)

# ll_len示例
response = redis_cache.ll_len('mylist')
print(response)

# lrange示例
response = redis_cache.lrange('mylist', 0, -1)
print(response)

# ltrim示例
response = redis_cache.ltrim('mylist', 1, -1)
print(response)

# rpoplpush示例
response = redis_cache.rpoplpush('mylist1', 'mylist2')
print(response)

# brpoplpush示例
response = redis_cache.brpoplpush('mylist1', 'mylist2', timeout=0)
print(response)

# lindex示例
response = redis_cache.lindex('mylist', 0)
print(response)

# lset示例
response = redis_cache.lset('mylist', 0, 'NewValue')
print(response)

# linsert示例
response = redis_cache.linsert('mylist', 'BEFORE', 'Pivot', 'NewValue')
print(response)

# lrem示例
response = redis_cache.lrem('mylist', 'ValueToRemove', 1)
print(response)