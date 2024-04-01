import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, thread_id):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_id = int(thread_id)
        self.stop = threading.Event()
        self.pause = threading.Event()

    def run(self):
        while not self.stop.is_set():
            if self.pause.is_set():
                print(f'Thread {self.name} paused.')
                time.sleep(1)
            else:
                print(f'Thread {self.name} running...')
                time.sleep(1)

    def pause_thread(self):
        print(f'Thread {self.name} hss been paused.')
        self.pause.set()

    def resume_thread(self):
        print(f'Thread {self.name} has been resumed.')
        self.pause.clear()

    def stop_thread(self):
        print(f'Thread {self.name} has been stopped.')
        self.stop.set()

threads = {}  # 存储线程的字典

def create_thread(thread_id):
    thread_name = f"Thread{thread_id}"
    thread = MyThread(thread_name, thread_id)
    threads[thread_id] = thread
    thread.start()

create_thread(1)
create_thread(2)

while True:
    cmd = input().split(',')
    if cmd[1].strip() == '暂停':
        threads[int(cmd[0])].pause_thread()
    elif cmd[1].strip() == '继续':
        threads[int(cmd[0])].resume_thread()