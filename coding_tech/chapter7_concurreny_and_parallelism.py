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
import time


def factorize(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i
            
numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
print(f'총 {end-start:.3f} 초 걸림') # 총 0.192 초 걸림


## 위 코드를 멀티스레드로

from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
    
    def run(self):
        self.factors = list(factorize(self.number))
    
start = time.time()
threads = []

for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for th in threads:
    th.join()
    
end = time.time()
print(f'총 {end-start:.3f} 초 걸림') # 총 0.184 초 걸림


import select
import socket

## 이것을 순차적으로 실행하면 시간이 0.1초씩 늘어난다.
def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()

for _ in range(5):
    slow_systemcall()
    
end = time.time()
print(f'총 {end-start:.3f} 초 걸림') # 총 0.531 초 걸림



## 위를 멀티스레드로 실행

def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

def another_cal():
    sum = 0
    for i in range(100):
        sum += i
    print('sum : ', sum)
    
start = time.time()
thread_list = []

for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    thread_list.append(thread)

## 모종의 다른 계산 작업~~
another_cal() # sum :  4950

for thread in thread_list:
    thread.join()

end = time.time()
print(f'총 {end-start:.3f} 초 걸림') # 0.108 초 걸림
