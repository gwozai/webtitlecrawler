from flask import Flask, jsonify
import threading
import time
from crawl_and_process_websites import CrawlManager

app = Flask(__name__)
threads = {}  # 存储线程的字典

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.stop = threading.Event()

    def run(self):
        while not self.stop.is_set():
            print(f'{self.name} running...')
            time.sleep(1)

            taskid = "taskidtest"
            crawl_manager = CrawlManager(taskid)
            crawl_manager.proceed()

    def stop_thread(self):
        self.stop.set()

    def get_status(self):  # 返回线程状态
        return 'stopped' if self.stop.is_set() else 'running'

@app.route('/start_thread/<string:name>')
def start_thread(name):
    if name in threads:
        return 'Thread already exists'
    else:
        thread = MyThread(name)
        thread.start()
        threads[name] = thread
        return f'Thread {name} started'

@app.route('/stop_thread/<string:name>')
def stop_thread(name):
    if name in threads:
        threads[name].stop_thread()
        del threads[name]
        return f'Thread {name} stopped'
    else:
        return 'No such thread'

@app.route('/threads')
def get_threads():
    return jsonify(list(threads.keys()))  # 返回所有线程ID

@app.route('/thread/<string:name>')
def get_thread_status(name):
    if name in threads:
        status = threads[name].get_status()  # 获取线程状态
        return f'Thread {name} is {status}.'
    else:
        return 'No such thread'

if __name__ == '__main__':
    app.run(debug=True)