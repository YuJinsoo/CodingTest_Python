# 목록
1. [BetterWay52. 자식프로세스를 관리하기 위해 subprocess를 사용하라](#betterway52-자식프로세스를-관리하기-위해-subprocess를-사용하라)
2. [BetterWay53. 블로킹 I/O의 경우 스레드를 사용하고 병렬성을 피하라](#betterway53-블로킹-io의-경우-스레드를-사용하고-병렬성을-피하라)
3. [BetterWay54. 스레드에서 데이터 경합을 피가히 위해 Lock을 사용하라](#betterway54-스레드에서-데이터-경합을-피가히-위해-lock을-사용하라)
4. [BetterWay55. Queue를 사용해 스레드 사이의 작업을 조율하라](#betterway55-queue를-사용해-스레드-사이의-작업을-조율하라)
5. [BetterWay56. 언제 동시성이 필요한지 인식하는 방법을 알아두라](#betterway56-언제-동시성이-필요한지-인식하는-방법을-알아두라)
6. [BetterWay57. 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라](#betterway57-요구에-따라-팬아웃을-진행하려면-새로운-스레드를-생성하지-말라)
7. [BetterWay58. 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라](#betterway58-동시성과-queue를-사용하기-위해-코드를-어떻게-리팩터링해야-하는지-이해하라)
8. [BetterWay59. 동시성을 위해 스레드가 필요한 경우에는 ThreadpoolExecutor를 사용해라](#betterway59-동시성을-위해-스레드가-필요한-경우에는-threadpoolexecutor를-사용해라)
9. [BetterWay60. I/O를 할 때는 코루틴을 사용해 동시성을 높여라](#betterway60-io를-할-때는-코루틴을-사용해-동시성을-높여라)
10. [BetterWay61. 스레드를 사용한 I/O를 어떻게 asyncio로 포팅할 수 있는지 알아두라](#betterway61-스레드를-사용한-io를-어떻게-asyncio로-포팅할-수-있는지-알아두라)
11. [BetterWay62. asyncio로 쉽게 옮겨갈 수 있도록 스레드와 코루틴을 함께 사용하라](#betterway62-asyncio로-쉽게-옮겨갈-수-있도록-스레드와-코루틴을-함께-사용하라)
12. [BetterWay63. 응답성을 최대로 높이려면 asyncio 이벤트 루프를 블록하지 말라](#betterway63-응답성을-최대로-높이려면-asyncio-이벤트-루프를-블록하지-말라)
13. [BetterWay64. 진정한 병렬성을 살리려면 concurrent.futures를 사용하라](#betterway64-진정한-병렬성을-살리려면-concurrentfutures를-사용하라)



# Chapter7 : 동시성과 병렬성

- 동시성 (Concurenncy)
    - 여러 작업을 코어 1개에서 번갈아가며 처리하여 동시에 처리하는 것처럼 보이는 것
    - CPU 코어 1 개에서 시간을 쪼개어 번갈아 가며 수행
    - CPU 바운드 작업 일 때, 속도 차이가 별로 없다.

- 병렬성 (Parallelism)
    - 여러 작업을 동시에 처리하는 것
    - 여러 코어에서 각각 다른 명령을 처리
    - CPU 바운드 작업 일 때, 속도가 현저히 빨라진다. 

- Python 동시성 프로그램
    - 스레드
    - 코루틴
    - 하위 프로세스(subprocess)
    - C 확장(C extension)
    - 시스템 콜(system call)

- 동시성 python 코드가 실제 병렬적으로 실행되게 만드는 것은 매우 어렵다.


## BetterWay52. 자식프로세스를 관리하기 위해 subprocess를 사용하라
### 기억해야 할 Point

- 프로세스 실행 및 관리 라이브러리. subprocess
- 셸 스크립트의 가독성과 유지보수성을 높이기 위해 스크립트를 파이썬으로 다시 작성하는 경우도 있음
- python이 시작한 자식 프로세스는 서로 병렬적으로 실행
    - 모든 CPU 코어를 사용할 수 있음
    - 프로그램 스루풋을 높일 수 있음
- python 자체는 하나의 CPU에 묶여있찌만, 파이썬을 사용해 CPU를 많이 사용하는 여러 부하를 조작하면서 서로 협력하게 조정하는 것은 쉽다.
- 하위 프로세스 실행 방법
    - os.popen
    - os.exec*
    - subpocess

- 위 세 예제 중 `subprocess` 모듈을 추천함
    - 프로세스를 쉽게 실행할 수 있음 (`run()` 함수)
    - 프로세스의 출력을 읽고 프로세스가 오류 없이 종료됐는지 검사

- `run()` 함수 예제
```python
import subprocess

## encoding 에 utf8 안됨.. 왜지? 
# 'cmd', '/c', 부분은 실행할 CLI 이름과 /c 는 뒤 요소들을 cmd의 실행 인자로 전달함. 
result = subprocess.run(['cmd', '/c', 'echo', '자식 프로세스가 보내는 인사!'],
                        capture_output=True,
                        encoding='cp949')

# 종료코드가 0이 아니면 예외 발생하는 함수.
result.check_returncode()

print(result.stdout)
# print(result.stdout.decode('cp949')) ## euc-kr or cp949
```

- `Popen` 을 활용하여 subprocess실행
    - python이 다른 일을 하면서 주기적으로 자식 프로세스의 상태를 검사(polling)할 수 있음
    - - 자식과 부모 프로세스를 분리하면, 부모 프로세스가 원하는 개수만큼 많은 자식 프로세스를 병렬로 실행할 수 있음
```python
import subprocess

# cmd 에는 sleep 명령어가 없음
proc = subprocess.Popen(['powershell', '/c', 'sleep', '1'])
while proc.poll() is None:
    print('작업 중...')
    
print('종료 상태', proc.poll())
```


- 여러 개의 프로세스 예제
    - 각 프로세스가 순차적으로 실행되었다면, 총 지연시간은 10초 이었을 것
    - 하지만 총 시간은 3초 대
```python
import time
start = time.time()

sleep_procs = []

for _ in range(10):
    proc = subprocess.Popen(['powershell', '/c', 'sleep', '1'])
    sleep_procs.append(proc)

for proc in sleep_procs:
    proc.communicate()

end = time.time()

running_time = end - start
print(f'{running_time:.3}초 만에 끝남') # 3.58초 만에 끝남
```

- 데이터를 파이프를 이용해 하위 프로세스로 보내거나 하위 프로세스의 출력을 받을 수 있음
- 이를 이용해 프로그램을 병렬적으로 작업을 수행할 수 있음

- 예를 들어.. `openssl` 명령줄 도구를 사용해 데이터를 암호화 하는 예제
    - 명령줄 인자로 자식 프로세스를 실행하고, I/O 파이프를 연결하는것은 쉬움
```python
import os
import subprocess

def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(
        # *** WARNING : deprecated key derivation used.
        # Using -iter or -pbkdf2 would be better.
        ['powershell', '/c', 'openssl', 'enc', '-des3', '-pass', 'env:password', '-pbkdf2'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    out, err = proc.communicate(input=data)
    if err:
        print("Error:", err.decode())
    return out

results = []

for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    results.append(proc)

for result in results:
    print(result[-10:])

# b'\x8f\x8d\xf7\xb03N\xc3\x1b\xefm'
# b'\xc9dx\xc3\xa0\xe9v\xcb|\x82'
# b'O\xe3\x9d\xce\x9f\xe1\x0eL|\x97'
    
```

- 한 자식 프로세스의 출력을 다음 프로세스의 입력으로 계속 연결시켜서 여러 병렬 프로세스를 연쇄적으로 연결할 수도 있다.
- `openssl` 명령줄 도구를 하위 프로세스로 만들어 입력 스트림의 월풀 해시를 계산하는 예쩨

```python
## 예제이상..
```


- `communicate` 메서드는 실행된 프로세스와 통신하는 데 사용됩니다. 
    - 호출한 프로세스가 완료될 때까지 기다림
    - 이 메서드는 프로세스와 표준 입력, 표준 출력, 표준 오류 간의 통신을 관리
    - stdout_data, stderr_data = proc.communicate(input)
        - input: 프로세스의 표준 입력으로 전달할 데이터입니다. 바이트열로 전달됩니다.
        - stdout_data: 프로세스의 표준 출력에서 읽은 데이터입니다. 바이트열 형식입니다.
        - stderr_data: 프로세스의 표준 오류에서 읽은 데이터입니다. 바이트열 형식입니다
- `communicate`메서드에 timeout 파라미터 전달 예제
```python
import subprocess

proc = subprocess.Popen(['powershell', '/c', 'sleep', '10'])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('종료상태', proc.poll()) # 종료상태 1
```

> - `subprocess`모듈을 사용해 자식 프로세스를 실행하고 입력과 출력 스트림을 관리할 수 있다.<br>
> - 자식 프로세스는 파이썬 인터프리터와 병렬로 실행되므로 CPU 코어를 최대로 쓸 수 있다.<br>
> - 간단하게 자식 프로세스를 실행하고 싶은 경우에는 run 편의 함수를 사용하라. 유닉스 스타일의 파이프라인이 필요하면 `Popen`클래스를 사용<br>
> - 자식 프로세스가 멈추는 경우나 교착 상태를 방지하려면 `communicate`메서드에 대해 `timeout`파라미터를 사용하라.<br>

<br>

## BetterWay53. 블로킹 I/O의 경우 스레드를 사용하고 병렬성을 피하라
- 파이썬 표준 구현체 : CPython

- 파이썬 프로그램 실행 단계
    - 1단계
        - 소스코드를 구문 분석해서 바이트코드(bytecode)로 변환
        - 바이트코드는 8비트 명령어를 사용하는 저수준 프로그램 표현(3.6 부터는 16비트 멸영어)

    - 2단계
        - 바이트코드를 스택 기반 인터프리터를 통해 실행
        - 바이트코드 인터프리터에는 파이썬 프로그램이 실행되는 동안 일관성 있게 유지해야 하는 상태가 존재함
        - GIL이라는 방법을 사용해 일관성을 유지함

- GIL
    - 상호 배제 Lock(뮤텍스)
    - CPython이 선점형 멀티스레드로 인해 영향받는 것을 방지함
        - 선점형에서는 다른 스레드 실행을 중간에 인터럽트 시키고 제어를 가져올 수 ㅣㅆ음
        - 이때 예상치 못한 인터럽트라면 참조카운터가 오염될 수 있음
    - GIL 때문에 스레드로 cpu bound 작업을 분산화하면 속도가 빨라지지 않는다.

```python
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
```


- 다른 언어에서는 컴퓨터의 모든 CPU 코어를 사용할 수 있으므로, 다중 스레드를 사용해 계산을 수행하는 것이 타당함
- 이를 파이썬으로 시도한다면, 아래와 같다
    - 속도 측면에서 별로 차이가 나지 않는다. (0.01 초 차이)

```python
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
```

- 성능 향상이 없는데도 멀티스레딩을 지원하는 이유
    - 동시에 여러 일을 하는 것처럼 코딩하기 쉽다.
    - 블로킹 I/O 를 다루기 위해서
        - 파일 쓰기, 네트워크 상호작용, 디스플레이 장치와 통신 등
        - 운영체제가 시스템 콜 요청에 응답하는 시간 동안 파이썬 프로그램이 다른 일을 할 수 있음

- 직렬포트를 통해 원격 제어 헬리콥터 신호를 보내는 예제
    - 이 동작을 대신해 느린 시스템 콜(select)를 사용할 것
    - 이것은 운영체제에게 0.1초 동안 블록한 뒤 제어를 돌려달라고 요청하는데, 동기적으로 직렬 포트를 사용할 때와 같은 상황임

```python
import select
import socket

## 느린 시스템 콜 함수
## 이것을 순차적으로 실행하면 시간이 0.1초씩 늘어난다.
def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)

start = time.time()

for _ in range(5):
    slow_systemcall()
    
end = time.time()
print(f'총 {end-start:.3f} 초 걸림') # 총 0.531 초 걸림
```

- 위 예제를 멀티스레드로 실행
    - 0.5 초 >> 0.1 초 (심지어 중간에 다른 계산을 추가했는데도 시간이 줄어들었음)
    - GIL은 CPython 코드를 하나만 실행하도록 막지만, 시스템 콜을 막지는 못함.
    - 파이썬 스레드가 시스템 콜을 하기 전에 GIL을 해제하고 시스템 콜에서 반환되자마자 GIL을 다시 획득하기 때문
```python
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

```

- 스레드 외에도 `asyncio`내장 모듈 등 블로킹 I/O 처리하는 방법이 많이 있음
- 대안마다 중요한 장점이 존재
- 코드를 가급적 손보지 않고 블로킹 I/O를 병렬로 실행하고 싶을 때에는 스레드를 사용하는 것이 편리함

### 기억해야 할 Point
> - 파이썬 쓰레드는 GIL로 인해 다중 CPU 코어에서 병렬로 실행될 수 없다. </br>
> - GIL이 있음에도 불구하고 파이썬 스레드는 여전히 유용함</br>
> - 파이썬 스레드를 사용해 여러 시스템 콜을 병렬로 할 수 있음. 이를 이용하면 블로킹 I/O 와 계산을 동시에 수행할 수 있음</br>


<br>

## BetterWay54. 스레드에서 데이터 경합을 피가히 위해 Lock을 사용하라


- GIL이 동시 접근을 보장해주는 락 역할을 하는 것처럼 보이지만, 실제로는 전혀 그렇지 않음
    - 파이썬 쓰레드는 하나의 하나만 실행될 수 있지만, 
    - 스레드가 어떤 데이터 구조에 대해 수행하는 연산은 연속된 두 바이트코드 사이에 언제든 인터럽트 될수 있음
    - 그래서 여러 스레드에서 같은 데이터 구조에 동시에 접근하면 위험

- 병렬적으로 여러 가지 개수를 세는 프로그램 예제
    - 네트워크에서 광센서를 통해 빛이 들어온 경우를 샘플링하는 예제

    - `Count`클래스에서 `increment()` 메서드 동작은 atomic 하지 않음
        - 실제로는 세 단계로 작업됨
            1. value = getattr(counter, 'count')
            2. result = value + 1
            3. setattr(count, 'count', result)
        - 세 단계 사이에 인터럽트가 발생하면 +1 연산 동작이 무시되는 경우가 생김
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self, offset):
        self.count += offset


def read_sensor(number):
    pass
    # print(f'Reading sensor... {number}')
    # time.sleep(1)

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        ## 센서를 읽는다.
        read_sensor(sensor_index)
        counter.increment(1)
        

from threading import Thread

how_many = 10**5
counter = Counter()
threads = []

for i in range(5):
    thread = Thread(target=worker,
                    args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count


## 책 예제는 두 숫자가 다르게 나오던데....
# 카운터 값은 500000여야 하는데 실제로는 500000 입니다
print(f'카운터 값은 {expected}여야 하는데 실제로는 {found} 입니다.')
```

- 이렇게 같은 자료구조에 접근해야 하는 경우, 오염을 해결하기 위한 기능 제공
    - `Lock` 클래스 (상호 배제 Lock 클래스: Mutex)
    - `with`문을 사용한 `Lock` 예제

```python
from threading import Lock, Thread

class LockCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0
        
    def increment(self, offset):
        ## with 문을 활용해 lock을 획득함하고 해제함
        with self.lock:
            self.count += offset


def read_sensor(number):
    pass
    # print(f'Reading sensor... {number}')
    # time.sleep(1)

def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        ## 센서를 읽는다.
        read_sensor(sensor_index)
        counter.increment(1)

counter = LockCounter()
how_many = 10**5
threads = []

for i in range(5):
    thread = Thread(target=worker,
                    args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f'카운터 값은 {expected}여야 하는데 실제로는 {found} 입니다.')
```

### 기억해야 할 Point
> - 파이썬 GIL이 있지만, 스레드 사이에서 발생하는 데이터 경합으로부터 보호해야 함 </br>
> - 코드에서 여러 스레드가 상호 배제 락(뮤텍스) 없이 같은 객체를 변경하도록 허용하면 코드가 데이터 구조를 오염시킴</br>
> - 여러 스레드 사이에서 데이터 경합을 막아 무결서을 유지하려면 `Lock`클래스를 활용하자</br>


<br>

## BetterWay55. Queue를 사용해 스레드 사이의 작업을 조율하라


- 프로그램이 동시에 여러 일을 수행한다면 작업 조율하는 것이 중요
- 동시성 작업을 처리할 때 가장 유용한 방식은 함수 파이프라인

- 파이프라인
    - 순차적으로 실행해야 하는 여러 단계가 있음
    - 단계벌로 실행할 구체적인 함수가 정해짐
    - 파이프라인 한쪽 끝에서 새로운 작업이 계속 추가됨
    - 각 함수는 동시에 실행될 수 있고, 각 단계에서 처리해야 하는 일을 담당
    - 함수가 완료되면 다음 단계로 전달되면, 더이상 실행할 것이 없으면 종료됨

- 이런 방법은 블로킹 IO나 하위 프로세스가 포함되는 경우에 좋음
    - 쉽게 병렬화 할 수 있기 때문

- 디지털 카메라에서 이미지 스트림을 가져와 크기를 변경하고 온라인 포토 갤러리에 저장하는 예제
    - 파이프라인 을 3단계로 구성
        - 저장 - 조작 - 업로드

```python
## 각 단계에서 처리하는 함수
def download(item):
    pass

def resize(item):
    pass

def upload(item):
    pass

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
```

- 가져온 작업에 함수를 적용하고, 결과를 다른 큐에 넣는 스레드를 통해 파이프라인의 각 단계를 구성
    - 까다로운 점: 입력 큐가 비어있는 경우(이전 단계 자업 미완성)의 처리
        - 아래 예제에서는 IndexError 예외를 잡아내어 일시 중단하는 것으로 처리함
```python
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
```

- 위 구조는 문제점이 있음
- 작업자(Worker) 함수의 속도가 달라지면 앞에 있는 단계가 그보다 더 뒤에있는 단계의 진행을 방해함
    - 뒤에 있는 단계는 작업을 받지 못해 기아 상태가 되어 처리할 작업이없음
    - 그럼 쓸데없이 계속 polling을 해서 `IndexError`를 발생시킴 >> 리소스 낭비

- 피해야 할 세 가지 문제점
    1. 모든 작업이 끝났는지 검사하기 위해 `done_queue`에 추가로 바쁜 대기를 수행해야 함.
    2. Worker의 run 메서드가 루프를 무한히 반복함.(루프를 중단할 방법이 없음)
    3. 파이프라인 진행이 막히면 프로그램이 임의로 종료될 수 있음
        (Worker별 속도 차이에 의해 메모리 과부하로 이런 일이 생길 수 있음)

### 대안: Queue
- 내장 `Queue`를 사용해서 위 문제를 해결할 수 있음
- `Queue`는 새로운 데이터가 나타날 때까지 get메서드가 블록되게 만들어 작업자의 바쁜 대기문제를 해결
    - 스레드가 먼저 실행되지만, `Queue`인스턴스에 원소가 `put`되서 `get`메서드가 반환할 원소가 생기기 전까지 쓰레드가 끝나지 않음
```python
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
```

- 파이프라인 중간임 가히는 경우를 해결하기 위해 `Queue` 클래스에 단 두 단계 사이에 허용할 수 있는 미완성 작업 최대 개수를 지정
    - 즉 Queue를 버퍼처럼 사용하고 버퍼 크기를 지정함
    - 그럼 위에서 본 Queue 동작 방식처럼 가득 차면 대기하는 스레드가 됨
```python
my_queue = Queue(1) ## 최대 버퍼 크기 1 

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
```

- `Queue`클래스의 `task_done`을 통해 작업 진행 추적 가능
```python
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
```

- Queue의 하위 클래스에 구현해보자.
    - 큐에 다른 입력이 없음을 표시하는 `센티넬`원소를 추가하는 close 메서드 정의
```python
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
```

- Queue를 활용한 것을 확장해 각 단계마다 여러 작업자를 사용할 수 있다.
    - IO병렬성을 높일 수 있음 (속도증가)
    - 이를 위해 다중 스레드를 시작하고 끝내는 도우미 함수를 제작
    - 선형적인 파이프라인의 경우 `Queue`가 효과적이지만, I/O를 할 때에는 코루틴을 사용하면 더 좋다.
```python
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
```

### 기억해야 할 Point
> - 순차적인 작업을 동시에 여러 파이썬 스레드에서 실행되도록 구성하고 싶다면, 특히 I/O 위주의 프로그램이라면 파이프라인이 매우 유용하다</br>
> - 동시성 파이프라인을 만들 때 발생할 수 있는 문제를 잘 알아두자(바쁜 대기, 종료 알림, 메모리 사용량 폭발 등)</br>
> - `Queue`클래스를 튼튼한 파이프라인을 구축할 때 필요한 기능인 블로킹 연산, 버퍼크기, join을 통한 완료 대기 등을 모두 지원</br>


<br>

## BetterWay56. 언제 동시성이 필요한지 인식하는 방법을 알아두라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay57. 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay58. 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay59. 동시성을 위해 스레드가 필요한 경우에는 ThreadpoolExecutor를 사용해라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay60. I/O를 할 때는 코루틴을 사용해 동시성을 높여라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay61. 스레드를 사용한 I/O를 어떻게 asyncio로 포팅할 수 있는지 알아두라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay62. asyncio로 쉽게 옮겨갈 수 있도록 스레드와 코루틴을 함께 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay63. 응답성을 최대로 높이려면 asyncio 이벤트 루프를 블록하지 말라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay64. 진정한 병렬성을 살리려면 concurrent.futures를 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>
