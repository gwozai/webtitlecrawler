import unittest
import redis
from redis_singleton import RedisCache  # 这里假设你的实现在一个名为your_module的模块中


class TestRedisCache(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cache = RedisCache()



    def test_del_and_exists_data(self):
        self.cache.set_data('Testkey', 'Testvalue')
        self.cache.del_data('Testkey')
        res = self.cache.exists_data('Testkey')
        self.assertFalse(res['result'])





    def test_set_and_get_data(self):
        self.cache.set_data('Testkey', 'Testvalue')
        res = self.cache.get_data('Testkey')
        self.assertEqual(res['result'].decode(), 'Testvalue')  # 解码成字符串后再进行比较


    def test_hash_data(self):
        self.cache.set_hash_data('Testhash', 'Testkey', 'Hashvalue')
        res = self.cache.get_hash_data('Testhash', 'Testkey')
        self.assertEqual(res['result'].decode(), 'Hashvalue')  # 解码成字符串后再进行比较


    def test_queue(self):
        self.cache.enqueue('Testqueue', 'Testvalue1')
        self.cache.enqueue('Testqueue', 'Testvalue2')
        res = self.cache.dequeue('Testqueue')
        self.assertEqual(res['result'].decode(), 'Testvalue1')  # 解码成字符串后再进行比较
        res = self.cache.dequeue('Testqueue')
        self.assertEqual(res['result'].decode(), 'Testvalue2')  # 解码成字符串后再进行比较
if __name__ == '__main__':
    unittest.main()