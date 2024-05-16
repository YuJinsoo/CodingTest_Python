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

# ## 각 단계에서 처리하는 함수
# def download(item):
#     return 1

# def resize(item):
#     return 2

# def upload(item):
#     return 3

# ## deque에 이미지를 put으로 추가하고 get을 통해 순차적으로 처리되도록 할 수 있다.
# ## 데이터 경합을 피하기 위해 Lock을 사용해서 deque에 접근
# from collections import deque
# from threading import Lock

# class MyQueue:
#     def __init__(self):
#         self.items = deque()
#         self.lock = Lock()
        
#     def put(self, item):
#         with self.lock:
#             self.items.append(item)
            
#     def get(self):
#         with self.lock:
#             return self.items.popleft()



# import time
# from threading import Thread


# class Worker(Thread):
#     def __init__(self, func, in_queue, out_queue):
#         super().__init__()
#         self.func = func
#         self.in_queue = in_queue
#         self.out_queue = out_queue
#         self.polled_count = 0
#         self.work_done = 0

#     def run(self):
#         while True:
#             self.polled_count += 1
#             try:
#                 item = self.in_queue.get()
#             except IndexError:
#                 # print('index error occur, polled count: ', self.polled_count)
#                 time.sleep(0.01) # 할 일이 없음
#             else:
#                 result = self.func(item)
#                 self.out_queue.put(result)
#                 self.work_done += 1

# ## 각 단계마다 큐를 생성하고 
# # 각 단계에 맞는 작업 스레드를 만들어서 서로 연결할 수 있음                
# download_queue = MyQueue()
# resize_queue = MyQueue()
# upload_queue = MyQueue()

# done_queue = MyQueue()
# threads = [
#     Worker(download, download_queue, resize_queue),
#     Worker(resize, resize_queue, upload_queue),
#     Worker(upload, upload_queue, done_queue),
# ]
        
# for thread in threads:
#     thread.start()

# for _ in range(1000):
#     download_queue.put(object())
    
# # print(len(done_queue.items))

# while len(done_queue.items) < 1000:
#     ## 다른 작업
#     print('length of done_queue: ', len(done_queue.items))

# processed = len(done_queue.items)

# polled = sum(t.polled_count for t  in threads)
# # 1000 개의 아에템을 처리했습니다. 이때 폴링을3006회 했습니다.
# print(f'{processed} 개의 아에템을 처리했습니다. 이때 폴링을{polled}회 했습니다.')



# # 내장 queue를 사용해서 deque로 직접 구현한 파이프라인 문제를 해결할 수 있다.
# from queue import Queue
# import time
# from threading import Thread

# my_queue = Queue()

# def consumer():
#     print('소비자 대기')
#     my_queue.get()    # 아래의 put이 실행된 다음에 실행됨
#     print('소비자 완료')

# thread = Thread(target=consumer)
# thread.start()

# print('생산자 데이터 추가')
# my_queue.put(object())
# print('생산자 완료')
# thread.join()

# # 소비자 대기
# # 생산자 데이터 추가
# # 생산자 완료
# # 소비자 완료

# print('---------------------')

# my_queue = Queue(1)

# def consumer():
#     time.sleep(0.1)
#     my_queue.get()
#     print('소비자 1')
#     my_queue.get()
#     print('소비자 2')
#     print('소비자 완료')
    
# thread = Thread(target=consumer)
# thread.start()

# my_queue.put(object())
# print('생산자1')
# my_queue.put(object())
# print('생산자2')
# print('생산자 완료')
# thread.join()

# # 생산자1
# # 소비자 1
# # 생산자2
# # 소비자 2
# # 생산자 완료
# # 소비자 완료
# print('---------------------')

# from queue import Queue
# from threading import Thread


# in_queue = Queue()
# def consumer():
#     print('소비자 대기')
#     work = in_queue.get()
#     print('소비자 작업 중')
#     print('소비자 완료')
#     in_queue.task_done() ## queue가 완료되었다고 알려줌

# thread = Thread(target=consumer)
# thread.start()

# ## 스레드를 join 하거나 폴링할 필요가 없음
# ## Queue 인스턴스의 join 메서드를 호출함해서 in_queue가 끝나길 기다림

# print('생산자 데이터 추가')
# in_queue.put(object())
# print('생산자 대기')
# in_queue.join()
# print('생산자 완료')
# thread.join()

# # 소비자 대기
# # 생산자 데이터 추가
# # 생산자 대기
# # 소비자 작업 중
# # 소비자 완료
# # 생산자 완료




# class ClosableQueue(Queue):
#     SENTINEL = object()
    
#     def close(self):
#         self.put(self.SENTINEL)
    
#     def __iter__(self):
#         while True:
#             item = self.get()
#             try:
#                 if item is self.SENTINEL:
#                     return # 스레드 종료
#                 yield item
#             finally:
#                 self.task_done()


# class StoppableWorker(Thread):
#     def __init__(self, func, in_queue, out_queue):
#         super().__init__()
#         self.func = func
#         self.in_queue = in_queue
#         self.out_queue = out_queue
    
#     def run(self):
#         for item in self.in_queue:
#             result = self.func(item)
#             self.out_queue.put(result)


# download_queue = ClosableQueue()
# resize_queue = ClosableQueue()
# upload_queue = ClosableQueue()
# done_queue = ClosableQueue()

# threads = [
#     StoppableWorker(download, download_queue, resize_queue),
#     StoppableWorker(resize, resize_queue, upload_queue),
#     StoppableWorker(upload, upload_queue, done_queue),
# ]

# for thread in threads:
#     thread.start()

# for _ in range(1000):
#     download_queue.put(object())


# download_queue.close() # 1000 개 이후 마지막에 SENTINEL 넣어줌
# download_queue.join()  # SENTINEL 만나면 료됨! (return)
# resize_queue.close()
# resize_queue.join()
# upload_queue.close()
# upload_queue.join()

# print(done_queue.qsize(), '개의 원소가 처리됨') # 1000 개의 원소가 처리됨

# for thread in threads:
#     thread.join()




# def start_thread(count, *args):
#     threads = [StoppableWorker(*args) for _ in range(count)]
#     for thread in threads:
#         thread.start()
#     return threads

# def stop_thread(closable_queue, threads):
#     for _ in threads:
#         closable_queue.close()
    
#     closable_queue.join()
    
#     for thread in threads:
#         thread.join()


# download_queue = ClosableQueue()
# resize_queue = ClosableQueue()
# upload_queue = ClosableQueue()
# done_queue = ClosableQueue()

# download_threads = start_thread(3, download, download_queue, resize_queue)
# resize_threads = start_thread(4, resize, resize_queue, upload_queue)
# upload_threads = start_thread(5, upload, upload_queue, done_queue)

# for _ in range(1000):
#     download_queue.put(object())


# stop_thread(download_queue, download_threads)
# stop_thread(resize_queue, resize_threads)
# stop_thread(upload_queue, upload_threads)

# print(done_queue.qsize(), '개의 원소가 처리됨') # 1000 개의 원소가 처리됨


## 57


# EMPTY = '-'
# ALIVE = '*'

# class Grid:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.rows = []
#         for _ in range(self.height):
#             self.rows.append([EMPTY] * self.width)
    
#     def get(self, y, x):
#         return self.rows[y % self.height][x % self.width]

#     def set(self, y, x, state):
#         self.rows[y % self.height][x % self.width] = state
    
#     def __str__(self):
#         result = ""
#         for r in self.rows:
#             for cell in r:
#                 result += cell
#             result += '\n'
#         return result


# ## 어떤 셀의 주변 셀 상태를 얻는 함수
# def count_neighbors(y, x, get):
#     n_ = get(y-1, x+0)
#     ne = get(y-1, x+1)
#     e_ = get(y-0, x+1)
#     se = get(y+1, x+1)
#     s_ = get(y+1, x+0)
#     sw = get(y+1, x-1)
#     w_ = get(y-0, x-1)
#     nw = get(y-1, x-1)
#     neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
#     count = 0
    
#     for state in neibor_states:
#         if state == ALIVE:
#             count += 1
#     return count

# ## 게임 로직 구현
# def game_logic(state, neighbors):
#     if state == ALIVE:
#         if neighbors < 2:
#             return EMPTY
#         elif neighbors >3:
#             return EMPTY
#     else:
#         if neighbors == 3:
#             return ALIVE
#     return state


# ## 그리드 인스턴스를 넘기는 대신 그리드를 설정하는 함수를 set파라미터로 받는 함수 인터페이스를 사용
# ## >> 코드 결합도를 낮춤
# def step_cell(y, x, get, set):
#     state = get(y, x)
#     neighbors = count_neighbors(y, x, get)
#     next_stage = game_logic(state, neighbors)
#     set(y, x, next_stage)
    

# ## 다음 tick(세대)로 진행하는 함수
# def simulate(grid):
#     next_grid = Grid(grid.height, grid.width)
#     for y in range(grid.height):
#         for x in range(grid.width):
#             step_cell(y, x, grid.get, next_grid.set)
#     return next_grid

    
# grid = Grid(5, 9)
# grid.set(0, 3, ALIVE)
# grid.set(1, 4, ALIVE)
# grid.set(2, 2, ALIVE)
# grid.set(2, 3, ALIVE)
# grid.set(2, 4, ALIVE)
# print(grid)

# for i in range(5):
#     grid = simulate(grid)
#     print(grid)
#     print('=============')



# 57


# # 생명게임 스레드로 재구성
# import contextlib
# import io

# fake_stderr = io.StringIO()

# import time
# from threading import Thread, Lock


# EMPTY = '-'
# ALIVE = '*'

# ## (그대로)
# class Grid:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.rows = []
#         for _ in range(self.height):
#             self.rows.append([EMPTY] * self.width)
    
#     def get(self, y, x):
#         return self.rows[y % self.height][x % self.width]

#     def set(self, y, x, state):
#         self.rows[y % self.height][x % self.width] = state
    
#     def __str__(self):
#         result = ""
#         for r in self.rows:
#             for cell in r:
#                 result += cell
#             result += '\n'
#         return result


# ## Thread safe 하도록 Lock 적용한 클래스
# class LockingGrid(Grid):
#     def __init__(self, height, width):
#         super().__init__(height, width)
#         self.lock = Lock()

#     def get(self, y, x):
#         with self.lock:
#             return super().get(y, x)
    
#     def set(self, y, x, state):
#         with self.lock:
#             super().set(y, x, state)
            
#     def __str__(self):
#         with self.lock:
#             return super().__str__()
        
        

# ## 어떤 셀의 주변 셀 상태를 얻는 함수 (그대로)
# def count_neighbors(y, x, get):
#     n_ = get(y-1, x+0)
#     ne = get(y-1, x+1)
#     e_ = get(y-0, x+1)
#     se = get(y+1, x+1)
#     s_ = get(y+1, x+0)
#     sw = get(y+1, x-1)
#     w_ = get(y-0, x-1)
#     nw = get(y-1, x-1)
#     neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
#     count = 0
    
#     for state in neibor_states:
#         if state == ALIVE:
#             count += 1
#     return count



# ## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
# def game_logic(state, neighbors):
#     time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
#     if state == ALIVE:
#         if neighbors < 2:
#             return EMPTY
#         elif neighbors >3:
#             return EMPTY
#     else:
#         if neighbors == 3:
#             return ALIVE
#     return state


# ## 그리드 인스턴스를 넘기는 대신 그리드를 설정하는 함수를 set파라미터로 받는 함수 인터페이스를 사용
# ## >> 코드 결합도를 낮춤
# def step_cell(y, x, get, set):
#     state = get(y, x)
#     neighbors = count_neighbors(y, x, get)
#     next_stage = game_logic(state, neighbors)
#     set(y, x, next_stage)
    
# ## 다음 tick(세대)로 진행하는 함수
# # def simulate(grid):
# #     next_grid = Grid(grid.height, grid.width)
# #     for y in range(grid.height):
# #         for x in range(grid.width):
# #             step_cell(y, x, grid.get, next_grid.set)
# #     return next_grid

# ## 다음 세대로 진행하는 스레드 그리드 함수
# def simulate_threaded(grid):
#     next_grid = LockingGrid(grid.height, grid.width)
    
#     thread_list = []
#     for y in range(grid.height):
#         for x in range(grid.width):
#             args = (y, x, grid.get, next_grid.set)
#             thread = Thread(target=step_cell, args=args)
#             thread.start() ## 팬아웃
#             thread_list.append(thread)
    
#     for thread in thread_list:
#         thread.join()
        
#     return next_grid
    

    
# grid = LockingGrid(5, 9)
# grid.set(0, 3, ALIVE)
# grid.set(1, 4, ALIVE)
# grid.set(2, 2, ALIVE)
# grid.set(2, 3, ALIVE)
# grid.set(2, 4, ALIVE)
# print(grid)
# print('=============')

# for i in range(5):
#     grid = simulate_threaded(grid)
#     print(grid)
#     print('=============')
    
    

# ## 만약 블로킹 IO에서 예외가 발생했다면..
# def game_logic_error(state, neighbors):
#     raise OSError('I/O 문제 발생')

# with contextlib.redirect_stderr(fake_stderr):
#     thread = Thread(target=game_logic_error, args=(ALIVE, 3))
#     thread.start()
#     thread.join()

# print(fake_stderr.getvalue())
# # raise OSError('I/O 문제 발생')
# # OSError: I/O 문제 발생



# 58

# import time
# from queue import Queue
# from threading import Thread, Lock

# EMPTY = '-'
# ALIVE = '*'

# class ClosableQueue(Queue):
#     SENTINEL = object()
    
#     def close(self):
#         self.put(self.SENTINEL)
    
#     def __iter__(self):
#         while True:
#             item = self.get()
#             try:
#                 if item is self.SENTINEL:
#                     return # 스레드 종료 할수 있도록..
#                 yield item
#             finally:
#                 self.task_done() # 


# class StoppableWorker(Thread):
#     def __init__(self, func, in_queue, out_queue):
#         super().__init__()
#         self.func = func
#         self.in_queue = in_queue
#         self.out_queue = out_queue
    
#     def run(self):
#         for item in self.in_queue:
#             result = self.func(item)
#             self.out_queue.put(result)


# class SimulationError(Exception):
#     pass


# class Grid:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.rows = []
#         for _ in range(self.height):
#             self.rows.append([EMPTY] * self.width)
    
#     def get(self, y, x):
#         return self.rows[y % self.height][x % self.width]

#     def set(self, y, x, state):
#         self.rows[y % self.height][x % self.width] = state
    
#     def __str__(self):
#         result = ""
#         for r in self.rows:
#             for cell in r:
#                 result += cell
#             result += '\n'
#         return result

# class LockingGrid(Grid):
#     def __init__(self, height, width):
#         super().__init__(height, width)
#         self.lock = Lock()

#     def get(self, y, x):
#         with self.lock:
#             return super().get(y, x)
    
#     def set(self, y, x, state):
#         with self.lock:
#             super().set(y, x, state)
            
#     def __str__(self):
#         with self.lock:
#             return super().__str__()


# ## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
# def game_logic(state, neighbors):
#     # raise OSError('OSError 발생') # OSError: OSError 발생
#     time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
#     if state == ALIVE:
#         if neighbors < 2:
#             return EMPTY
#         elif neighbors >3:
#             return EMPTY
#     else:
#         if neighbors == 3:
#             return ALIVE
#     return state

# def game_logic_thread(item):
#     y, x, state, neighbors = item
#     try:
#         next_state = game_logic(state, neighbors)
#     except Exception as e:
#         next_state = e
#     return (y, x, next_state)

# def count_neighbors(y, x, get):
#     n_ = get(y-1, x+0)
#     ne = get(y-1, x+1)
#     e_ = get(y-0, x+1)
#     se = get(y+1, x+1)
#     s_ = get(y+1, x+0)
#     sw = get(y+1, x-1)
#     w_ = get(y-0, x-1)
#     nw = get(y-1, x-1)
#     neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
#     count = 0
    
#     for state in neibor_states:
#         if state == ALIVE:
#             count += 1
#     return count

# def simulate_pipeline(grid, in_queue, out_queue):
#     for y in range(grid.height):
#         for x in range(grid.width):
#             state = grid.get(y, x)
#             neighbors = count_neighbors(y, x, grid.get)
#             in_queue.put((y, x, state, neighbors))
    
#     in_queue.join()
#     out_queue.close()
#     next_grid = Grid(grid.height, grid.width)
#     for item in out_queue:
#         y, x, next_state = item
#         if isinstance(next_state, Exception):
#             raise SimulationError(y, x) from next_state
#         next_grid.set(y, x, next_state)
    
#     return next_grid

# ### count_neighbors에 IO 적용 하기 위해 스레드 함수 추가개발
# def simulate_phased_pipeline(grid, in_queue, logic_queue, out_queue):
#     for y in range(grid.height):
#         for x in range(grid.width):
#             state = grid.get(y, x)
#             item = (y, x, state, grid.get)
#             in_queue.put(item) ## 팬아웃
    
#     in_queue.join()
#     logic_queue.join()
#     out_queue.close()
    
#     next_grid = LockingGrid(grid.height, grid.width)
#     for item in out_queue:
#         y, x, next_state = item
#         if isinstance(next_state, Exception):
#             raise SimulationError(y, x) from next_state
#         next_grid.set(y, x, next_state)
    
#     return next_grid

# ### count_neighbors에 IO 적용 하기 위해 스레드 함수 추가개발
# def count_neighbors_thread(item):
#     y, x, state, get = item
#     try:
#         neighbors = count_neighbors(y, x, get)
#     except Exception as e:
#         neighbors = e
#     return (y, x, state, neighbors)

# ### count_neighbors에 IO 적용 하기 위해 스레드 함수 추가개발
# def game_logic_thread(item):
#     y, x, state, neighbors = item
#     if isinstance(neighbors, Exception):
#         next_stage = neighbors
#     else:
#         try:
#             next_stage = game_logic(state, neighbors)
#         except Exception as e:
#             next_stage = e
#     return (y, x, next_stage)


# in_queue = ClosableQueue()
# logic_queue = ClosableQueue()
# out_queue = ClosableQueue()

# threads = []
# for _ in range(5):
#     thread = StoppableWorker(
#         count_neighbors_thread,
#         in_queue,
#         logic_queue
#     )
#     thread.start()
#     threads.append(thread)  

# for _ in range(5):
#     thread = StoppableWorker(
#         game_logic_thread,
#         logic_queue,
#         out_queue
#     )
#     thread.start()
#     threads.append(thread)
    
    
# grid = LockingGrid(5, 9)
# grid.set(0, 3, ALIVE)
# grid.set(1, 4, ALIVE)
# grid.set(2, 2, ALIVE)
# grid.set(2, 3, ALIVE)
# grid.set(2, 4, ALIVE)
# print(grid)
# print('=============')

# for i in range(5):
#     grid = simulate_phased_pipeline(grid, in_queue, logic_queue, out_queue)
#     print(grid)
#     print('=============')

# for t in threads:
#     in_queue.close()
    
# for t in threads:
#     logic_queue.close()
    
# for t in threads:
#     t.join()


# 59

# import time
# from threading import Thread, Lock

# from concurrent.futures import ThreadPoolExecutor, as_completed

# EMPTY = '-'
# ALIVE = '*'

# ## (그대로)
# class Grid:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.rows = []
#         for _ in range(self.height):
#             self.rows.append([EMPTY] * self.width)
    
#     def get(self, y, x):
#         return self.rows[y % self.height][x % self.width]

#     def set(self, y, x, state):
#         self.rows[y % self.height][x % self.width] = state
    
#     def __str__(self):
#         result = ""
#         for r in self.rows:
#             for cell in r:
#                 result += cell
#             result += '\n'
#         return result


# ## Thread safe 하도록 Lock 적용한 클래스
# class LockingGrid(Grid):
#     def __init__(self, height, width):
#         super().__init__(height, width)
#         self.lock = Lock()

#     def get(self, y, x):
#         with self.lock:
#             return super().get(y, x)
    
#     def set(self, y, x, state):
#         with self.lock:
#             super().set(y, x, state)
            
#     def __str__(self):
#         with self.lock:
#             return super().__str__()


# ## 어떤 셀의 주변 셀 상태를 얻는 함수 (그대로)
# def count_neighbors(y, x, get):
#     n_ = get(y-1, x+0)
#     ne = get(y-1, x+1)
#     e_ = get(y-0, x+1)
#     se = get(y+1, x+1)
#     s_ = get(y+1, x+0)
#     sw = get(y+1, x-1)
#     w_ = get(y-0, x-1)
#     nw = get(y-1, x-1)
#     neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
#     count = 0
    
#     for state in neibor_states:
#         if state == ALIVE:
#             count += 1
#     return count


# ## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
# def game_logic(state, neighbors):
#     # raise OSError('OSError 발생') # OSError: OSError 발생
#     time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
#     if state == ALIVE:
#         if neighbors < 2:
#             return EMPTY
#         elif neighbors >3:
#             return EMPTY
#     else:
#         if neighbors == 3:
#             return ALIVE
#     return state

# def step_cell(y, x, get, set):
#     state = get(y, x)
#     neighbors = count_neighbors(y, x, get)
#     next_stage = game_logic(state, neighbors)
#     set(y, x, next_stage)
    

# ## ThreadPoolExecutor 적용!
# def simulate_pool(pool, grid):
#     next_grid = LockingGrid(grid.height, grid.width)
    
#     futures = []
#     for y in range(grid.height):
#         for x in range(grid.width):
#             args = (y, x, grid.get, next_grid.set)
#             future = pool.submit(step_cell, *args) # 팬아웃
#             futures.append(future)
    
#     for f in futures:
#         f.result()  # 팬인
        
#     return next_grid


    
# grid = LockingGrid(5, 9)
# grid.set(0, 3, ALIVE)
# grid.set(1, 4, ALIVE)
# grid.set(2, 2, ALIVE)
# grid.set(2, 3, ALIVE)
# grid.set(2, 4, ALIVE)
# print(grid)
# print('=============')

# ## 사용할 스레드를 10개 미리 생성함
# with ThreadPoolExecutor(max_workers=10) as pool:
#     for i in range(5):
#         grid = simulate_pool(pool=pool, grid=grid)
#         print(grid)
#         print('=============')


# 60

# import time
# from threading import Thread, Lock
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import asyncio

# EMPTY = '-'
# ALIVE = '*'

# class Grid:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#         self.rows = []
#         for _ in range(self.height):
#             self.rows.append([EMPTY] * self.width)
    
#     def get(self, y, x):
#         return self.rows[y % self.height][x % self.width]

#     def set(self, y, x, state):
#         self.rows[y % self.height][x % self.width] = state
    
#     def __str__(self):
#         result = ""
#         for r in self.rows:
#             for cell in r:
#                 result += cell
#             result += '\n'
#         return result


# def count_neighbors(y, x, get):
#     n_ = get(y-1, x+0)
#     ne = get(y-1, x+1)
#     e_ = get(y-0, x+1)
#     se = get(y+1, x+1)
#     s_ = get(y+1, x+0)
#     sw = get(y+1, x-1)
#     w_ = get(y-0, x-1)
#     nw = get(y-1, x-1)
#     neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
#     count = 0
    
#     for state in neibor_states:
#         if state == ALIVE:
#             count += 1
#     return count



# ## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
# async def game_logic(state, neighbors):
#     # raise OSError('OSError 발생') # OSError: OSError 발생
#     time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
#     if state == ALIVE:
#         if neighbors < 2:
#             return EMPTY
#         elif neighbors >3:
#             return EMPTY
#     else:
#         if neighbors == 3:
#             return ALIVE
#     return state

# async def step_cell(y, x, get, set):
#     state = get(y, x)
#     neighbors = count_neighbors(y, x, get)
#     next_stage = await game_logic(state, neighbors) ## async 호출시 await
#     set(y, x, next_stage)

# async def simulate(grid: Grid):
#     next_grid = Grid(grid.height, grid.width)
    
#     tasks = []
#     for y in range(grid.height):
#         for x in range(grid.width):
#             task = step_cell(y, x, grid.get, next_grid.set) # 팬아웃
#             tasks.append(task)
    
#     await asyncio.gather(*tasks) # 팬인
    
#     return next_grid


# grid = Grid(5, 9)
# grid.set(0, 3, ALIVE)
# grid.set(1, 4, ALIVE)
# grid.set(2, 2, ALIVE)
# grid.set(2, 3, ALIVE)
# grid.set(2, 4, ALIVE)
# print(grid)
# print('=============')


# for i in range(5):
#     grid = asyncio.run(simulate(grid))
#     print(grid)
#     print('=============')


# 61

class EOFError(Exception):
    pass

class ConnectionBase:
    def __init__(self, connection):
        self.connection = connection
        self.file = connection.makefile('rb')
    
    def send(self, command):
        line = command + '\n'
        data = line.encode()
        self.connection.send(data)
        
    def receive(self):
        line = self.file.readline()
        if not line:
            raise EOFError('Connection closed')
        return line[:-1].decode()


import random

WARMER = '더 따뜻함'
COLDER = '더 차가움'
UNSURE = '잘 모르겠음'
CORRECT = '맞음'

class UnknownCommandError(Exception):
    pass

# 서버 동작 클래스 정의
class Session(ConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state(None, None)
        
    def _clear_state(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []
        
    ## 들어오는 입력 메시지
    def loop(self):
        while command := self.receive():
            parts = command.split(' ')
            if parts[0] == 'PARAMS':
                self.set_params(parts)
            elif parts[0] == 'NUMBER':
                self.send_number()
            elif parts[0] == 'REPORT':
                self.receive_report(parts)
            else:
                raise UnknownCommandError(command)
    
    def set_params(self, parts):
        assert len(parts) == 3
        lower = int(parts[1])
        upper = int(parts[2])
        self._clear_state(lower, upper)
        
    def next_guess(self):
        if self.secret is not None:
            return self.secret
        
        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess
    
    def send_number(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        self.send(format(guess))
        
    def reveive_report(self, parts):
        assert len(parts) == 2
        decision = parts[1]
        
        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last
            
        print(f'서버: {last}는 {decision}')
        
    
##클라이언트 구현
import contextlib
import math

class Client(ConnectionBase):
    def __inti__(self, *args):
        super().__init__(*args)
        self._clear_state()
        
    def _clear_state(self):
        self.secret = None
        self.last_distance = None
        
    @contextlib.contextmanager
    def session(self, lower, upper, secret):
        print(f'\n{lower}와 {upper} 사이의 숫자를 맞춰보세요! 쉿! 그 숫자는 {secret} 입니다.')
        
        self.secret = secret
        self.send(f'PARAMS {lower} {upper}')
        try:
            yield
        finally:
            self._clear_state()
            self.send('PARAMS 0 -1')
            
    def request_numbers(self, count):
        for _ in range(count):
            self.send('NUMBER')
            data = self.receive()
            yield int(data)
        if self.last_distance == 0:
            return
    
    def report_outcome(self, number):
        new_distance = math.fabs(number - self.secret)
        decision = UNSURE
        
        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            pass
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER
        
        self.last_distance = new_distance
        
        self.send(f'REPORT {decision}')
        return decision
    

# 소켓에 리슨 하는 스레드를 하나 사용하고 
# 새 연결이 들어올 때마다 스레드를 추가로 시작하는 방식으로 서버를 실행
import socket
from threading import Thread

def handle_connection(connection):
    with connection:
        session = Session(connection)
        try:
            session.loop()
        except EOFError:
            pass

def run_server(address):
    with socket.socket() as listener:
        listener.bind(address)
        listener.listen()
        while True:
            connection, _ = listener.accept()
            thread = Thread(target=handle_connection,
                            args=(connection,),
                            daemon=True)
            thread.start()
            

def run_client(address):
    with socket.create_connection(address) as connection:
        client = Client(connection)
        
        with client.session(1, 5, 3):
            results = [(x, client.report_outcome(x)) for x in client.request_numbers(5)]
            
        with client.session(10,15,12):
            for number in client.request_numbers(5):
                outcome = client.report_outcome(number)
                results.append((number, outcome))
        
    return results

def main():
    address = ('127.0.0.1', 1234)
    server_thread = Thread(
        target=run_server,
        args=(address,),
        daemon=True
    )
    server_thread.start()
    
    results = run_client(address)
    for number, outcome in results:
        print(f'클라이언트: {number}는 {outcome}')

main()


## 비동기로 포팅

## 먼저 ConnectionBase클래스가 블로킹 I/O 대신 send 와 receive라는 코루틴을 제공하도록 수정

class AsyncConnectionBase:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        
    async def send(self, command):
        line = command + '\n'
        data = line.encode(0)
        self.writer.write(data)     # 변경
        await self.writer.drain()   # 변경
    
    async def receive(self):
        line = await self.reader.readline() #변경
        if not line:
            raise EOFError('연결에러')
        return line[:-1].decode()
    

## 단일 연결 세션 클래스는 상속하는 클래스가 바뀜
## 코루틴이 적용될 곳만 바뀜
class AsnycSession(AsyncConnectionBase):
    def __init__(self, *args):
        super().__init__(*args)
        self._clear_state(None, None)
        
    def _clear_state(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.secret = None
        self.guesses = []
        
    ## 들어오는 입력 메시지
    ## 코루틴 적용
    async def loop(self):
        while command := await self.receive():
            parts = command.split(' ')
            if parts[0] == 'PARAMS':
                self.set_params(parts)
            elif parts[0] == 'NUMBER':
                await self.send_number()
            elif parts[0] == 'REPORT':
                self.receive_report(parts)
            else:
                raise UnknownCommandError(command)
    
    ## 명령 처리 부분은 그대로
    def set_params(self, parts):
        assert len(parts) == 3
        lower = int(parts[1])
        upper = int(parts[2])
        self._clear_state(lower, upper)
        
    def next_guess(self):
        if self.secret is not None:
            return self.secret
        
        while True:
            guess = random.randint(self.lower, self.upper)
            if guess not in self.guesses:
                return guess
    
    ## 추측한 값을 클라이언트에 보낼 때 비동기 IO
    async def send_number(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        await self.send(format(guess))
        
    def reveive_report(self, parts):
        assert len(parts) == 2
        decision = parts[1]
        
        last = self.guesses[-1]
        if decision == CORRECT:
            self.secret = last
            
        print(f'서버: {last}는 {decision}')
        

## 클라이언트도 상속하는 클래스가 바뀜
class AsyncClient(AsyncConnectionBase):
    def __inti__(self, *args):
        super().__init__(*args)
        self._clear_state()
        
    def _clear_state(self):
        self.secret = None
        self.last_distance = None
    
    ## 클라이언트에서도 명령을 처리하는 함수에 비동기 처리해야함
    ## contextlib도 async로 적용해야함
    @contextlib.asynccontextmanager
    async def session(self, lower, upper, secret):
        print(f'\n{lower}와 {upper} 사이의 숫자를 맞춰보세요! 쉿! 그 숫자는 {secret} 입니다.')
        
        self.secret = secret
        await self.send(f'PARAMS {lower} {upper}')
        try:
            yield
        finally:
            self._clear_state()
            await self.send('PARAMS 0 -1')
            
    async def request_numbers(self, count):
        for _ in range(count):
            await self.send('NUMBER')
            data = self.receive()
            yield int(data)
        if self.last_distance == 0:
            return
    
    async def report_outcome(self, number):
        new_distance = math.fabs(number - self.secret)
        decision = UNSURE
        
        if new_distance == 0:
            decision = CORRECT
        elif self.last_distance is None:
            pass
        elif new_distance < self.last_distance:
            decision = WARMER
        elif new_distance > self.last_distance:
            decision = COLDER
        
        self.last_distance = new_distance
        
        await self.send(f'REPORT {decision}')
        return decision

import asyncio

async def handel_async_connection(reader, writer):
    session = AsnycSession(reader, writer)
    try:
        await session.loop()
    except EOFError:
        pass
    
async def run_async_server(address):
    server = await asyncio.start_server(
        handel_async_connection, *address
    )
    async with server:
        await server.server_forever()

## 게임을 시작하는 run_client함수는 거의 모두 바꿔야 한다.   
async def run_async_clinet(address):
    streams = await asyncio.open_connection(*address)
    client = AsyncClient(*streams)
    
    async with client.session(1, 5, 3):
        results = [(x, await client.report_outcome(x)) async for x in client.request_numbers(5)]
        
    async with client.session(10, 15, 12):
        async for number in client.request_numbers(5):
            outcome = await client.report_outcome(number)
            results.append((number, outcome))
    
    _, writer = streams
    writer.close()
    await writer.wait_closed()
    
    return results


## 전체 실행 코드
async def main_async():
    address = ('127.0.0.1', 1234)
    
    server = run_async_server(address)
    asyncio.create_task(server)
    
    results = await run_async_clinet(address)
    for number, outcome in results:
        print(f'클라이언트: {number}는 {outcome}')
        
asyncio.run(main_async())


# 62

import time
from threading import Lock, Thread

## 새로운 데이터가 없으면 에러를 발생.
class NoNewData(Exception):
    pass

def readline(handle):
    offset = handle.tell()
    handle.seek(0,2)
    length = handle.tell()
    
    if length == offset:
        raise NoNewData
    
    handle.seek(offset, 0)
    return handle.readline()

# 작업자 함수?
def tail_file(handle, interval, write_func):
    while not handle.closed:
        try:
            line = readline(handle)
        except NoNewData:
            time.sleep(interval)
        else:
            write_func(line)

# 입력파일마다 작접자 스레드를 시작
# 스레들의 출력을 한 출력 파일에 모으기
def run_threads(handles, interval, output_path):
    with open(output_path, 'wb') as output:
        lock = Lock()
        def write(data):
            with lock:
                output.write(data)
                threads = []
                for handle in handles:
                    args = (handle, interval, write)
                    thread = Thread(target=tail_file, args=args)
                    thread.start()
                    threads.append(thread)
                
                for thread in threads:
                    thread.join()
                    
# 주어진 입력 결로 집합와 출력경로에 대해 run_threads를 싱행하고
# 코드가 제대로 작동했느지 확이 ㄴ가능

def confirm_merge(input_paths, output_path):
    pass

input_paths = ''
handles = ''
output_path = ...
run_threads(handles, 0.1, output_path)
confirm_merge(input_paths, output_path)


## 하향식 1단계

import asyncio

async def run_tasks_mixed(handles, interval, output_path):
    loop = asyncio.get_event_loop()
    
    with open(output_path, 'wb') as output:
        async def write_async(data):
            output.write(data)
            
        def write(data):
            coro = write_async(data)
            future = asyncio.run_coroutine_threadsafe(coro, loop)
            future.result()
        
        tasks = []
        for handle in handles:
            task = loop.run_in_executor(
                None, tail_file, handle, interval, write
            )
            tasks.append(task)
        
        await asyncio.gather(*tasks)

input_paths = ''
handles = ''
output_path = ...
asyncio.run(run_tasks_mixed(handles, 0.1, output_path))
confirm_merge(input_paths, output_path)

# 하향식 4단계 추가

async def tail_async(handle, interval, write_func):
    loop = asyncio.get_event_loop()
    
    while not handle.closed:
        try:
            line = await loop.run_in_executor(None, readline, handle)
        except NoNewData:
            await asyncio.sleep(interval)
        else:
            await write_func(line)\
                
async def run_tasks(handles, interval, output_path):
    with open(output_path, 'wb') as output:
        async def write_async(data):
            output.write(data)
            
        tasks = []
        for handle in handles:
            coro = tail_async(handle, interval, write_async)
            task = asyncio.create_task(coro)
            tasks.append(task)
        
        await asyncio.gather(*tasks)

input_paths = ''
handles = ''
output_path = ...
asyncio.run(run_tasks(handles, 0.1, output_path))
confirm_merge(input_paths, output_path)



## 상향식

def tail_file(handle, interval, write_func):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    async def write_async(data):
        write_func(data)
    
    coro = tail_async(handle, interval, write_async)
    loop.run_until_complete(coro)

## 변경하지 않고 바로 실행가능
input_paths = ''
handles = ''
output_path = ...
run_threads(handles, 0.1, output_path)
confirm_merge(input_paths, output_path)