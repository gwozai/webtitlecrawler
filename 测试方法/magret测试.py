import requests

# 对`/add`发送 GET 请求
add_response = requests.get('http://localhost:5000/add', params={'name': 'test'})

# 打印添加操作的结果
print(add_response.json())

# 使用添加的记录的id获取记录
get_response = requests.get('http://localhost:5000/get', params={'id': 1})

# 打印获取操作的结果
print(get_response.json())


# curl -X GET 'http://localhost:5000/webpage_info?page=1&per_page=10'
get_response = requests.get('http://localhost:5000/get', params={'id': 1})

# 打印获取操作的结果
print(get_response.json())

# 更新记录
update_response = requests.post('http://localhost:5000/update', data={'id': 1, 'name': 'updated'})

# 打印更新操作的结果
print(update_response.json())

# 检索所有记录
all_response = requests.get('http://localhost:5000/all')

# 打印所有记录
print(all_response.json())

# 删除记录
delete_response = requests.post('http://localhost:5000/delete', data={'id': 1})

# 打印删除操作的结果
print(delete_response.json())