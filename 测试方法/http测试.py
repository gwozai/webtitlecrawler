import requests

# URL of your Flask app
base_url = 'http://localhost:5000'

def test_start_thread(name):
    response = requests.get(f'{base_url}/start_thread/{name}')
    print(response.text)

def test_stop_thread(name):
    response = requests.get(f'{base_url}/stop_thread/{name}')
    print(response.text)

def test_get_threads():
    response = requests.get(f'{base_url}/threads')
    print(response.json())

def test_get_thread_status(name):
    response = requests.get(f'{base_url}/thread/{name}')
    print(response.text)


# 测试路由
test_start_thread('Thread1')
test_start_thread('Thread2')
# test_start_thread('Thread3')

test_get_threads()
# test_get_thread_status('Thread1')
# test_stop_thread('Thread1')
# test_get_thread_status('Thread1')
# test_get_threads()