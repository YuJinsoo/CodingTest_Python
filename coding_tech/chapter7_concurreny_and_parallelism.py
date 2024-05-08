# 52

import subprocess

## encoding 에 utf8 안됨.. 왜? 'cmd', '/c', 
result = subprocess.run(['cmd', '/c', 'echo', '자식 프로세스가 보내는 인사!'],
                        capture_output=True,
                        encoding='cp949')


# 종료코드가 0이 아니면 예외 발생하는 함수.
result.check_returncode()

print(result.stdout)
# print(result.stdout.decode('cp949')) ## euc-kr or cp949



# proc = subprocess.Popen(['powershell', '/c', 'sleep', '1'])
# while proc.poll() is None:
#     print('작업 중...')
    
# print('종료 상태', proc.poll())


# import time
# start = time.time()

# sleep_procs = []

# for _ in range(10):
#     proc = subprocess.Popen(['powershell', '/c', 'sleep', '1'])
#     sleep_procs.append(proc)

# for proc in sleep_procs:
#     proc.communicate()

# end = time.time()

# running_time = end - start
# print(f'{running_time:.3}초 만에 끝남') # 3.58초 만에 끝남

# import os
# import subprocess

# def run_encrypt(data):
#     env = os.environ.copy()
#     env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
#     proc = subprocess.Popen(
#         ['powershell', '/c', 'openssl', 'enc', '-des3', '-pass', 'env:password', '-pbkdf2'],
#         env=env,
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE)
#     out, err = proc.communicate(input=data)
#     if err:
#         print("Error:", err.decode())
#     return out

# results = []

# for _ in range(3):
#     data = os.urandom(10)
#     proc = run_encrypt(data)
#     results.append(proc)

# for result in results:
#     print(result[-10:])

# b'\x8f\x8d\xf7\xb03N\xc3\x1b\xefm'
# b'\xc9dx\xc3\xa0\xe9v\xcb|\x82'
# b'O\xe3\x9d\xce\x9f\xe1\x0eL|\x97'
    

# import subprocess
# proc = subprocess.Popen(['powershell', '/c', 'sleep', '10'])
# try:
#     proc.communicate(timeout=0.1)
# except subprocess.TimeoutExpired:
#     proc.terminate()
#     proc.wait()

# print('종료상태', proc.poll()) # 종료상태 1

# import os
# import subprocess

# def run_encrypt(data):
#     env = os.environ.copy()
#     env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
#     proc = subprocess.Popen(
#         ['powershell', '/c', 'openssl', 'enc', '-des3', '-pass', 'env:password', '-pbkdf2'],
#         env=env,
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE)
#     out, err = proc.communicate(input=data)
#     if err:
#         print("Error:", err.decode())
#     return out


# # 월풀해쉬계산
# def run_hash(input_stdin):
#     p = subprocess.Popen(
#         ['powershell', '/c', 'openssl', 'dgst', 'whirlpool', '-binary'],
#         # stdin=input_stdin,
#         stdin=subprocess.PIPE,
#         stdout=subprocess.PIPE
#     )
#     result, _ = p.communicate(input=input_stdin)
#     return result

# # 데이터를 암호화하는 프로세스 집합 실행
# # 함호화된 출력의 해시를 계싼하는 프로세스 집합 실행

# encrypt_procs = []
# hash_procs = []

# for _ in range(3):
#     data = os.urandom(100)
    
#     encrypt_proc = run_encrypt(data)
#     encrypt_procs.append(encrypt_proc)
    
#     hash_proc = run_hash(encrypt_proc)
#     hash_procs.append(hash_proc)
    
#     # encrypt_proc.stdout.close()
#     # encrypt_proc.stdout = None

# for p in encrypt_procs:
#     print(p[-10:])
#     # p.communicate()
#     # assert p.returncode == 0

# for p in hash_procs:
#     print(p[-10:])


# 54

## 계산량이 많은 작업. 인수찾기 알고리즘
# import time


# def factorize(number):
#     for i in range(1, number+1):
#         if number % i == 0:
#             yield i
            
# numbers = [2139079, 1214759, 1516637, 1852285]
# start = time.time()

# for number in numbers:
#     list(factorize(number))

# end = time.time()
# print(f'총 {end-start:.3f} 초 걸림') # 총 0.192 초 걸림


# ## 위 코드를 멀티스레드로

# from threading import Thread

# class FactorizeThread(Thread):
#     def __init__(self, number):
#         super().__init__()
#         self.number = number
    
#     def run(self):
#         self.factors = list(factorize(self.number))
    
# start = time.time()
# threads = []

# for number in numbers:
#     thread = FactorizeThread(number)
#     thread.start()
#     threads.append(thread)

# for th in threads:
#     th.join()
    
# end = time.time()
# print(f'총 {end-start:.3f} 초 걸림') # 총 0.184 초 걸림


# import select
# import socket

# ## 이것을 순차적으로 실행하면 시간이 0.1초씩 늘어난다.
# def slow_systemcall():
#     select.select([socket.socket()], [], [], 0.1)

# start = time.time()

# for _ in range(5):
#     slow_systemcall()
    
# end = time.time()
# print(f'총 {end-start:.3f} 초 걸림') # 총 0.531 초 걸림



# ## 위를 멀티스레드로 실행

# def slow_systemcall():
#     select.select([socket.socket()], [], [], 0.1)

# def another_cal():
#     sum = 0
#     for i in range(100):
#         sum += i
#     print('sum : ', sum)
    
# start = time.time()
# thread_list = []

# for _ in range(5):
#     thread = Thread(target=slow_systemcall)
#     thread.start()
#     thread_list.append(thread)

# ## 모종의 다른 계산 작업~~
# another_cal() # sum :  4950

# for thread in thread_list:
#     thread.join()

# end = time.time()
# print(f'총 {end-start:.3f} 초 걸림') # 0.108 초 걸림



# import time


# class Counter:
#     def __init__(self):
#         self.count = 0
    
#     def increment(self, offset):
#         self.count += offset


# def read_sensor(number):
#     pass
#     # print(f'Reading sensor... {number}')
#     # time.sleep(1)

# def worker(sensor_index, how_many, counter):
#     for _ in range(how_many):
#         ## 센서를 읽는다.
#         read_sensor(sensor_index)
#         counter.increment(1)
        

# from threading import Thread

# how_many = 10**5
# counter = Counter()
# threads = []

# for i in range(5):
#     thread = Thread(target=worker,
#                     args=(i, how_many, counter))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# expected = how_many * 5
# found = counter.count


# ## 책 예제는 두 숫자가 다르게 나오던데....
# # 카운터 값은 500000여야 하는데 실제로는 500000 입니다
# print(f'카운터 값은 {expected}여야 하는데 실제로는 {found} 입니다.')



# from threading import Lock, Thread

# class LockCounter:
#     def __init__(self):
#         self.lock = Lock()
#         self.count = 0
        
#     def increment(self, offset):
#         with self.lock:
#             self.count += offset


# def read_sensor(number):
#     pass
#     # print(f'Reading sensor... {number}')
#     # time.sleep(1)

# def worker(sensor_index, how_many, counter):
#     for _ in range(how_many):
#         ## 센서를 읽는다.
#         read_sensor(sensor_index)
#         counter.increment(1)

# counter = LockCounter()
# how_many = 10**5
# threads = []

# for i in range(5):
#     thread = Thread(target=worker,
#                     args=(i, how_many, counter))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# expected = how_many * 5
# found = counter.count
# print(f'카운터 값은 {expected}여야 하는데 실제로는 {found} 입니다.')


# 55

## 각 단계에서 처리하는 함수
def download(item):
    return 1

def resize(item):
    return 2

def upload(item):
    return 3

## deque에 이미지를 put으로 추가하고 get을 통해 순차적으로 처리되도록 할 수 있다.
## 데이터 경합을 피하기 위해 Lock을 사용해서 deque에 접근
from collections import deque
from threading import Lock

class MyQueue:
    def __init__(self):
        self.items = deque()
        self.lock = Lock()
        
    def put(self, item):
        with self.lock:
            self.items.append(item)
            
    def get(self):
        with self.lock:
            return self.items.popleft()



import time
from threading import Thread


class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                # print('index error occur, polled count: ', self.polled_count)
                time.sleep(0.01) # 할 일이 없음
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1

## 각 단계마다 큐를 생성하고 
# 각 단계에 맞는 작업 스레드를 만들어서 서로 연결할 수 있음                
download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()

done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]
        
for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())
    
# print(len(done_queue.items))

while len(done_queue.items) < 1000:
    ## 다른 작업
    print('length of done_queue: ', len(done_queue.items))

processed = len(done_queue.items)

polled = sum(t.polled_count for t  in threads)
# 1000 개의 아에템을 처리했습니다. 이때 폴링을3006회 했습니다.
print(f'{processed} 개의 아에템을 처리했습니다. 이때 폴링을{polled}회 했습니다.')



# 내장 queue를 사용해서 deque로 직접 구현한 파이프라인 문제를 해결할 수 있다.
from queue import Queue
import time
from threading import Thread

my_queue = Queue()

def consumer():
    print('소비자 대기')
    my_queue.get()    # 아래의 put이 실행된 다음에 실행됨
    print('소비자 완료')

thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
my_queue.put(object())
print('생산자 완료')
thread.join()

# 소비자 대기
# 생산자 데이터 추가
# 생산자 완료
# 소비자 완료

print('---------------------')

my_queue = Queue(1)

def consumer():
    time.sleep(0.1)
    my_queue.get()
    print('소비자 1')
    my_queue.get()
    print('소비자 2')
    print('소비자 완료')
    
thread = Thread(target=consumer)
thread.start()

my_queue.put(object())
print('생산자1')
my_queue.put(object())
print('생산자2')
print('생산자 완료')
thread.join()

# 생산자1
# 소비자 1
# 생산자2
# 소비자 2
# 생산자 완료
# 소비자 완료
print('---------------------')

from queue import Queue
from threading import Thread


in_queue = Queue()
def consumer():
    print('소비자 대기')
    work = in_queue.get()
    print('소비자 작업 중')
    print('소비자 완료')
    in_queue.task_done() ## queue가 완료되었다고 알려줌

thread = Thread(target=consumer)
thread.start()

## 스레드를 join 하거나 폴링할 필요가 없음
## Queue 인스턴스의 join 메서드를 호출함해서 in_queue가 끝나길 기다림

print('생산자 데이터 추가')
in_queue.put(object())
print('생산자 대기')
in_queue.join()
print('생산자 완료')
thread.join()

# 소비자 대기
# 생산자 데이터 추가
# 생산자 대기
# 소비자 작업 중
# 소비자 완료
# 생산자 완료




class ClosableQueue(Queue):
    SENTINEL = object()
    
    def close(self):
        self.put(self.SENTINEL)
    
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # 스레드 종료
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
    
    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())


download_queue.close() # 1000 개 이후 마지막에 SENTINEL 넣어줌
download_queue.join()  # SENTINEL 만나면 료됨! (return)
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()

print(done_queue.qsize(), '개의 원소가 처리됨') # 1000 개의 원소가 처리됨

for thread in threads:
    thread.join()




def start_thread(count, *args):
    threads = [StoppableWorker(*args) for _ in range(count)]
    for thread in threads:
        thread.start()
    return threads

def stop_thread(closable_queue, threads):
    for _ in threads:
        closable_queue.close()
    
    closable_queue.join()
    
    for thread in threads:
        thread.join()


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()

download_threads = start_thread(3, download, download_queue, resize_queue)
resize_threads = start_thread(4, resize, resize_queue, upload_queue)
upload_threads = start_thread(5, upload, upload_queue, done_queue)

for _ in range(1000):
    download_queue.put(object())


stop_thread(download_queue, download_threads)
stop_thread(resize_queue, resize_threads)
stop_thread(upload_queue, upload_threads)

print(done_queue.qsize(), '개의 원소가 처리됨') # 1000 개의 원소가 처리됨

