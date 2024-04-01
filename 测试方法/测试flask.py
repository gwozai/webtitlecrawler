import unittest
import json
from flaskserver import app  # 假设你的 Flask 应用脚本命名为 'flaskApp.py'

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_start_thread(self):
        response = self.client.get('/start_thread/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Thread test started')

    def test_get_thread_status(self):
        response = self.client.get('/thread/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Thread test is running.')

    def test_get_threads(self):
        response = self.client.get('/threads')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('test', data)

    def test_stop_thread(self):
        response = self.client.get('/stop_thread/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Thread test stopped')

        response = self.client.get('/thread/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'No such thread')

if __name__ == '__main__':
    unittest.main()