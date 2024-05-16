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


- 생명게임 예시
- 생명게임 규칙
    1. 이웃한 셀 중 두 개 이하가 살아있으면 가운데 셀이 죽는다. 
    2. 네 개 이상 살아있으면 가운데 셀이 죽는다.
    3. 세 개가 살아있을 때 가운데 셀이 살아있으면 계속 살아있고, 빈 셀이면 살아있는 상태로 바뀐다.

```python
EMPTY = '-'
ALIVE = '*'

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state
    
    def __str__(self):
        result = ""
        for r in self.rows:
            for cell in r:
                result += cell
            result += '\n'
        return result


## 어떤 셀의 주변 셀 상태를 얻는 함수
def count_neighbors(y, x, get):
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y-0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y-0, x-1)
    nw = get(y-1, x-1)
    neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    
    for state in neibor_states:
        if state == ALIVE:
            count += 1
    return count

## 게임 로직 구현
def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors >3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


## 그리드 인스턴스를 넘기는 대신 그리드를 설정하는 함수를 set파라미터로 받는 함수 인터페이스를 사용
## >> 코드 결합도를 낮춤
def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_stage = game_logic(state, neighbors)
    set(y, x, next_stage)
    

## 다음 tick(세대)로 진행하는 함수
def simulate(grid):
    next_grid = Grid(grid.height, grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(y, x, grid.get, next_grid.set)
    return next_grid

    
grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)

for i in range(5):
    grid = simulate(grid)
    print(grid)
    print('=============')
```

- 위 코드는 단일 스레드에서 잘 동작한다.
- 조건이 바뀌어서 이제 `game_logic`함수에 약간의 IO(소켓통신 등)이 필요하다고 가정하자
- 가장 단순한 방법은 블로킹 IO를 game_logic함수 안에 직접 추가하는 것이다.
    - 하지만 이 방법은 셀 계수가 늘어남에 통신 횟수가 직렬적으로 쌓이기 때문에 시간이 엄청나게 오래 걸리게 된다.
```python
def game_logic(state, neighbors):
    ...
    data = my_socket.recv(100)
    ...
```

- 해결책은 I/O를 병렬로 수행하서 그래드 크기와 관계없이 각 세대를 계산할 수 있게 만드는 것
    - 동시에 실행되는 여러 실행 흐름을 만들어내는 과정을 `팬아웃(fan-out)`이라고 함
    - 다음단계로 진행하기 전 동시 작업이 모두 끝날 때까지 기다리는 것을 `팬인(fan-in)`이라고 함
- 파이썬은 팬인과 팬아웃을 지원하는 도구를 제공
    - Queue, ThreadpoolExcutor, coroutine 등


### 기억해야 할 Point
> - 프로그램이 커지면서 동시에 실행되는 여러 실행 흐름이 필요해짐</br>
> - 동시성을 조율하는 일방적인 방법으로는 팬아웃과 팬인이 있다.</br>
> - 파이썬의 팬아웃, 팬인을 구현하는 방법은 여러가지가 있다.</br>

<br>

## BetterWay57. 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라


- python 에서 병렬 I/O 실행에 스레드를 가장 먼저 생각한다.
- 하지만 여러 흐름을 만ㄷ르어내는 팬아웃을 수행할 때 스레드를 사용할 경우 단점이 있음
    - Thread 인스턴스를 서로 안정하게 조율하려면 특별한 도구가 필요함(Lock 같은것)
        - 코드가 복잡해짐, 디버깅이 어려움, 개발 확장이 어려움
    - 스레드는 메모리를 많이 잡아먹음 (개당 8MB정도)
        - 코드 크기가 늘어갈수록 컴퓨터가 감당하지 못할 용량이 됨 (scalable하지 않음)
    - 스레드는 시작한느 비용이 비싸고, 컨텍스트 전환에 비용이 소모됨
        - 결과적으로 I/O 블록 보다 더 큰 시간을 기다리게 될 수도 있음.

- 생명게임 스레드 여러개 생성한 것으로 재구성
    - 셀 한개 마다 Thread 생성해서 처리. (총 45개)
        - 이런식으로 하면 게임 크기가 커지면 감당 못함.
    - 디버깅이 어렵다.
        - 블로킹 I/O 과정을 신뢰할 수 없기 때무에 예외가 발생할 가능성이 매우 높다.

```python
import time
from threading import Thread, Lock

EMPTY = '-'
ALIVE = '*'

## (그대로)
class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state
    
    def __str__(self):
        result = ""
        for r in self.rows:
            for cell in r:
                result += cell
            result += '\n'
        return result


## Thread safe 하도록 Lock 적용한 클래스
class LockingGrid(Grid):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.lock = Lock()

    def get(self, y, x):
        with self.lock:
            return super().get(y, x)
    
    def set(self, y, x, state):
        with self.lock:
            super().set(y, x, state)
            
    def __str__(self):
        with self.lock:
            return super().__str__()
        
        

## 어떤 셀의 주변 셀 상태를 얻는 함수 (그대로)
def count_neighbors(y, x, get):
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y-0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y-0, x-1)
    nw = get(y-1, x-1)
    neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    
    for state in neibor_states:
        if state == ALIVE:
            count += 1
    return count

## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
def game_logic(state, neighbors):
    time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors >3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


## 그리드 인스턴스를 넘기는 대신 그리드를 설정하는 함수를 set파라미터로 받는 함수 인터페이스를 사용
## >> 코드 결합도를 낮춤
def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_stage = game_logic(state, neighbors)
    set(y, x, next_stage)
    
## 다음 tick(세대)로 진행하는 함수
# def simulate(grid):
#     next_grid = Grid(grid.height, grid.width)
#     for y in range(grid.height):
#         for x in range(grid.width):
#             step_cell(y, x, grid.get, next_grid.set)
#     return next_grid

## 다음 세대로 진행하는 스레드 그리드 함수
def simulate_threaded(grid):
    next_grid = LockingGrid(grid.height, grid.width)
    
    thread_list = []
    for y in range(grid.height):
        for x in range(grid.width):
            args = (y, x, grid.get, next_grid.set)
            thread = Thread(target=step_cell, args=args)
            thread.start() ## 팬아웃
            thread_list.append(thread)
    
    for thread in thread_list:
        thread.join()
        
    return next_grid
    

    
grid = LockingGrid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)
print('=============')

for i in range(5):
    grid = simulate_threaded(grid)
    print(grid)
    print('=============')
```

- 만일 io 과정에서 문제가 생긴다면
    - `OSError`가 발생하지만 Thread를 만들고 join을 호출하는 코드는 영향을 받지 않는다.
        - `Thread`클래스가 target함수에서 발생하는 예외를 독립적으로 잡아내서 sys.stderr로 예외의 트레이스를 출력하기 때문
        - 최초에 스레드를 시작한 곳으로 예외가 던져지지 않음.
    - 그래서 동시성 함수를 시작하고 끝내야 하는 경우 스레드는 적절한 방법이 아님
        - 예외가 던져지지 않으니 언제 끝낼 지 알 수가 없음

```python
import contextlib
import io

fake_stderr = io.StringIO()

def game_logic_error(state, neighbors):
    ...
    raise OSError('I/O 문제 발생')

with contextlib.redirect_stderr(fake_stderr):
    thread = Thread(target=game_logic_error, args=(ALIVE, 3))
    thread.start()
    thread.join()

print(fake_stderr.getvalue())
# raise OSError('I/O 문제 발생')
# OSError: I/O 문제 발생
```

### 기억해야 할 Point
> - 스레드에는 시작 및 실행 비용, 메모리 소모, 코드 복잡성과 같은 단점들이 있다.</br>
> - 스레드를 시작하거나 종료하기를 기다리는 코드에서 스레드 실행 중 발생한 예외를 돌려주는 파이썬 내장 기능이 없다.</br>

<br>

## BetterWay58. 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라


- Queue를 사용 파이프라인을 스레드로 실행하게 구현
    - 셀마다 Thread를 직접 구현하는 것 대신 미리 정해진 작업자 스레드를 생성
    - 미리 생성한 작업자 스레드를 Queue로 태스크를 전달해 처리
    - 새로운 스레드를 계속 만드는 부가 비용을 줄일 수 있음

- 생명게임 예제에 작성해보자.
    - 결과는 이전과 같음
    - 메모리를 폭발적으로 사용하는 문제와 에러 처리 문제는 해결. 아직 문제가 남아있음
        - 새로 구현한 `simulate_pipeline` 구현을 따라가기 어렵다.
        - 코드 가독성을 올리려면 `ClosableQueue`, `StoppableWorker`라는 추가 클래스가 필요함
        - 병렬성을 활용해 자동으로 시스템 규모가 확장되지 않음
        - 디버깅을 활성화 하려면 발생한 예외를 직접 스레드에서 수동으로 잡아 `Queue`로 전달해주고 다시 발생시켜야 함.
```python
import time
from queue import Queue
from threading import Thread

EMPTY = '-'
ALIVE = '*'

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


class SimulationError(Exception):
    pass


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state
    
    def __str__(self):
        result = ""
        for r in self.rows:
            for cell in r:
                result += cell
            result += '\n'
        return result
    

## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
def game_logic(state, neighbors):
    # raise OSError('OSError 발생') # OSError: OSError 발생
    time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors >3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state

def game_logic_thread(item):
    y, x, state, neighbors = item
    try:
        next_state = game_logic(state, neighbors)
    except Exception as e:
        next_state = e
    return (y, x, next_state)

def count_neighbors(y, x, get):
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y-0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y-0, x-1)
    nw = get(y-1, x-1)
    neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    
    for state in neibor_states:
        if state == ALIVE:
            count += 1
    return count

def simulate_pipeline(grid, in_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            neighbors = count_neighbors(y, x, grid.get)
            in_queue.put((y, x, state, neighbors))
    
    in_queue.join()
    out_queue.close()
    next_grid = Grid(grid.height, grid.width)
    for item in out_queue:
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)
    
    return next_grid
            
          
in_queue = ClosableQueue()
out_queue = ClosableQueue()

threads = []
for _ in range(5):
    thread = StoppableWorker(
        game_logic_thread,
        in_queue,
        out_queue
    )
    thread.start()
    threads.append(thread)  
    
grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)
print('=============')

for i in range(5):
    grid = simulate_pipeline(grid, in_queue, out_queue)
    print(grid)
    print('=============')

for t in threads:
    in_queue.close()

for t in threads:
    t.join()

```

- 가장 큰 문제는 요구사항이 변경될 떄 드러남
    - `game_logic` 뿐 아니라 다른 함수`count_neighbors`에도 I/O를 수행해야 할 경우
        - 별도의 스레드에서 실행하는 단계를 파이프라인에 추가해야 함.
        - 예외가 제대로 주 스레드까지 전달되는지 확인해야 함.
        - 작업자 쓰레드 간의 동기화를 위해 Grid 클래스에 Lock을 적용해야 함.
- `count_neighbors()`함수에 I/O 적용할 예제..
    - 문제
        - 코드가 너무 길어짐
        - Thread보다 Queue방식이 낫지만, 다른 도구가 더 나음..(ThreadPoolExcutor)
```python
import time
from queue import Queue
from threading import Thread, Lock

EMPTY = '-'
ALIVE = '*'

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


class SimulationError(Exception):
    pass


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state
    
    def __str__(self):
        result = ""
        for r in self.rows:
            for cell in r:
                result += cell
            result += '\n'
        return result

class LockingGrid(Grid):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.lock = Lock()

    def get(self, y, x):
        with self.lock:
            return super().get(y, x)
    
    def set(self, y, x, state):
        with self.lock:
            super().set(y, x, state)
            
    def __str__(self):
        with self.lock:
            return super().__str__()


## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
def game_logic(state, neighbors):
    # raise OSError('OSError 발생') # OSError: OSError 발생
    time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors >3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state

def game_logic_thread(item):
    y, x, state, neighbors = item
    try:
        next_state = game_logic(state, neighbors)
    except Exception as e:
        next_state = e
    return (y, x, next_state)

def count_neighbors(y, x, get):
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y-0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y-0, x-1)
    nw = get(y-1, x-1)
    neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    
    for state in neibor_states:
        if state == ALIVE:
            count += 1
    return count

def simulate_pipeline(grid, in_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            neighbors = count_neighbors(y, x, grid.get)
            in_queue.put((y, x, state, neighbors))
    
    in_queue.join()
    out_queue.close()
    next_grid = Grid(grid.height, grid.width)
    for item in out_queue:
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)
    
    return next_grid

### count_neighbors에 IO 적용 하기 위해 스레드 함수 추가개발
def simulate_phased_pipeline(grid, in_queue, logic_queue, out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y, x)
            item = (y, x, state, grid.get)
            in_queue.put(item) ## 팬아웃
    
    in_queue.join()
    logic_queue.join()
    out_queue.close()
    
    next_grid = LockingGrid(grid.height, grid.width)
    for item in out_queue:
        y, x, next_state = item
        if isinstance(next_state, Exception):
            raise SimulationError(y, x) from next_state
        next_grid.set(y, x, next_state)
    
    return next_grid

### count_neighbors에 IO 적용 하기 위해 스레드 함수 추가개발
def count_neighbors_thread(item):
    y, x, state, get = item
    try:
        neighbors = count_neighbors(y, x, get)
    except Exception as e:
        neighbors = e
    return (y, x, state, neighbors)

### count_neighbors에 IO 적용 하기 위해 스레드 함수 추가개발
def game_logic_thread(item):
    y, x, state, neighbors = item
    if isinstance(neighbors, Exception):
        next_stage = neighbors
    else:
        try:
            next_stage = game_logic(state, neighbors)
        except Exception as e:
            next_stage = e
    return (y, x, next_stage)


in_queue = ClosableQueue()
logic_queue = ClosableQueue()
out_queue = ClosableQueue()

threads = []
for _ in range(5):
    thread = StoppableWorker(
        count_neighbors_thread,
        in_queue,
        logic_queue
    )
    thread.start()
    threads.append(thread)  

for _ in range(5):
    thread = StoppableWorker(
        game_logic_thread,
        logic_queue,
        out_queue
    )
    thread.start()
    threads.append(thread)
    
    
grid = LockingGrid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)
print('=============')

for i in range(5):
    grid = simulate_phased_pipeline(grid, in_queue, logic_queue, out_queue)
    print(grid)
    print('=============')

for t in threads:
    in_queue.close()
    
for t in threads:
    logic_queue.close()
    
for t in threads:
    t.join()
```

### 기억해야 할 Point
> - 작업자 스레드 수를 고정하고 `Queue`와 함께 사용하면 스레드를 사용할 때 팬인과 팬아웃 규모 확장성을 개선할 수 있다.</br>
> - `Queue`를 사용하도록 기존 코드를 리팩터링하려면 상당히 많은 작업이 필요하다. 특히 다단계로 이뤄진 파이프라인이 필요하면 작업량이 더 많아진다.</br>
> - 다른 파이썬 내장 기능이나 모듈이 제공하는 병렬 I/O 를 가능하게 해주는 다른 기능과 비교하면 `Queue`는 프로그램이 활용할 수 있는 전체 I/O 병렬성의 정도를 제한한다는 단점이 있다.</br>

<br>

## BetterWay59. 동시성을 위해 스레드가 필요한 경우에는 ThreadpoolExecutor를 사용해라


- `concurrent.futures` 라는 내장모듈의 `ThreadPoolExecutor`클래스
    - `Thread`와 `Queue`를 사용한 접근 방법들의 장점을 조합해 병렬 IO문제를 해결합니다.

- 생명게임 예제에 ThreadPoolExecutor 클래스 적용
    - 사용할 스레드를 미리 생성해서 사용함. `ThreadPoolExecuter` 생성시 max_workers 로 지정
        - 스레드를 계속 생성해서 메모리를 과도하게 사용하는 문제 해결
    - `submit`메서드가 반환하는 `Future`인스턴스에 대해 `result()`메서드를 호출하면 스레드 실행 중 발생한 예외를 전파시켜줌
        - 스레드에서 발생한 예외를 감지할 수 있으므로 종료 시점을 정할 수 있다.
    - 만일 다른함수(`count_neighbors()`함수)에도 I/O 병렬성을 제공해야 해도 코드를 변경하지 않아도 됨
        - 이미 각 스레드에서 따로 `step_cell`을 실행하고, 포함되어 있기 때문
```python
import time
from threading import Thread, Lock

from concurrent.futures import ThreadPoolExecutor, as_completed

EMPTY = '-'
ALIVE = '*'

## (그대로)
class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state
    
    def __str__(self):
        result = ""
        for r in self.rows:
            for cell in r:
                result += cell
            result += '\n'
        return result


## Thread safe 하도록 Lock 적용한 클래스
class LockingGrid(Grid):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.lock = Lock()

    def get(self, y, x):
        with self.lock:
            return super().get(y, x)
    
    def set(self, y, x, state):
        with self.lock:
            super().set(y, x, state)
            
    def __str__(self):
        with self.lock:
            return super().__str__()


## 어떤 셀의 주변 셀 상태를 얻는 함수 (그대로)
def count_neighbors(y, x, get):
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y-0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y-0, x-1)
    nw = get(y-1, x-1)
    neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    
    for state in neibor_states:
        if state == ALIVE:
            count += 1
    return count


## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
def game_logic(state, neighbors):
    # raise OSError('OSError 발생') # OSError: OSError 발생
    time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors >3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state

def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_stage = game_logic(state, neighbors)
    set(y, x, next_stage)
    

## ThreadPoolExecutor 적용!
def simulate_pool(pool, grid):
    next_grid = LockingGrid(grid.height, grid.width)
    
    futures = []
    for y in range(grid.height):
        for x in range(grid.width):
            args = (y, x, grid.get, next_grid.set)
            future = pool.submit(step_cell, *args) # 팬아웃
            futures.append(future)
    
    for f in futures:
        f.result()  # 팬인
        
    return next_grid

grid = LockingGrid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)
print('=============')

## 사용할 스레드를 10개 미리 생성함
with ThreadPoolExecutor(max_workers=10) as pool:
    for i in range(5):
        grid = simulate_pool(pool=pool, grid=grid)
        print(grid)
        print('=============')
```

- `ThreadPoolExecutor`의 단점은 제한된 수의 I/O 병렬성만 제공한다는 것
- 비동기적인 해법이 존재하지 않는 상황(파일 I/O)을 처리할 때는 좋은 방법이지만..
    - 그 외 많은 경우에는 I/O 병렬성을 최대화 할 수 있는 더 나은 방법이 있음(ex 코루틴)

### 기억해야 할 Point
> - `ThreadPoolExecutor`를 사용하면 한정도니 리팩터링만으로 간단한 I/O 병렬성을 활성화 할수 있고, 동시성을 팬아웃 하는 경우에 발생하는 스레드 시작 비용을 쉽게 줄일 수 있다.</br>
> - `ThreadPoolExecutor`를 사용하면, 스레드를 직접 사용할 때 발생하는 잠재적인 메모리 낭비 문제를 없애주지만, 스레드 개수를 한정해두고 써야 하므로 I/O 확장성을 제한함</br>


<br>

## BetterWay60. I/O를 할 때는 코루틴을 사용해 동시성을 높여라


- 병렬 I/O 문제를 해결하는 다양한 방법을 학습했다.
    - threading의 Thread, Lock
    - Queue
    - concurrent.future의 ThreadPoolExecutor

- Python은 높은 동시성을 처리학 위해 `코루틴(coroutine)`을 지원
- 코루틴은
    - 동시에 실행되는 것처럼 보이는 함수를 아주 많이 쓸 수 있음
    - `async`와 `await`키워드를 사용해 구현함
    - 제너레이터를 실행하기 위한 인프라를 사용
    - **동시성 프로그래밍 방식으로 병렬 프로그래밍은 아님!**

- 코루틴의 소모 비용
    - 함수 호출 뿐...
    - 활성화된 코루틴은 종료될 때까지 1KB 미만의 메모리 사용

- 코루틴 동작
    - 환경으로부터 입력을 소비하고 결과를 출력할 수 있는 독립적인 함수
    - 매 `await` 식에서 일시 중단되고, 대기 가능성이 해결된 다음 `async` 함수로부터 실행을 재개함
        (제너레이터의 `yield`와 비슷함)
    - 여러 `async` 함수가 적절히 실행되면 동시에 실행되는 것처럼 보임
    - 스레드처럼 컨텍스트 비용, 메모리 부가 비용, 시작비용 등이 들지 않음
    - `이벤트 루프` 메커니즘으로 다수의 I/O를 효과적으로 빠르게 전환하면서 실행할수있음


- 코루틴을 활용하여 생명게임을 구현
    - `async`함수는 `coroutine`인스턴스를 반환하고, 나중에 `await`를 사용해서 결과를 꺼낼 수 있음.
        - 이러한 메커니즘을 사용해서 많은 코루틴 인스턴스를 만드는 것으로 팬아웃을 함
    - `asyncio`내장 라이브러리가 제공하는 `gather()`는 팬인을 수행함.
    - 모든 실행이 단일 스레드에서 이뤄지므로 Grid에 Lock을 사용할 필요가 ㅇ벗음
    - 코루틴 안에서 에러를 발생시켜도 메인 스레트에서 감지할 수 있음
```python
# 60

import time
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
import asyncio

EMPTY = '-'
ALIVE = '*'

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state
    
    def __str__(self):
        result = ""
        for r in self.rows:
            for cell in r:
                result += cell
            result += '\n'
        return result


def count_neighbors(y, x, get):
    n_ = get(y-1, x+0)
    ne = get(y-1, x+1)
    e_ = get(y-0, x+1)
    se = get(y+1, x+1)
    s_ = get(y+1, x+0)
    sw = get(y+1, x-1)
    w_ = get(y-0, x-1)
    nw = get(y-1, x-1)
    neibor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    
    for state in neibor_states:
        if state == ALIVE:
            count += 1
    return count

## 게임 로직 구현 ( 블로킹 I/O 작업을 sleep으로 대체 )
async def game_logic(state, neighbors):
    # raise OSError('OSError 발생') # OSError: OSError 발생
    time.sleep(0.1) ## 0.1 초 블로킹 I/O 작업
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors >3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state

async def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_stage = await game_logic(state, neighbors) ## async 호출시 await
    set(y, x, next_stage)

async def simulate(grid: Grid):
    next_grid = Grid(grid.height, grid.width)
    
    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell(y, x, grid.get, next_grid.set) # 팬아웃
            tasks.append(task)
    
    await asyncio.gather(*tasks) # 팬인
    
    return next_grid


grid = Grid(5, 9)
grid.set(0, 3, ALIVE)
grid.set(1, 4, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 4, ALIVE)
print(grid)
print('=============')


for i in range(5):
    grid = asyncio.run(simulate(grid))
    print(grid)
    print('=============')

```

### 기억해야 할 Point
> - `async`키워드로 정의한 함수를 코루틴이라고 함. 코루틴을 호출하는 호출자는 `await` 키워드를 사용해 자신이 의존하는 코루틴의 결과를 받을 수 있음</br>
> - 코루틴은 수만 개의 함수가 동시에 실행되는 것처럼 보이게 만드는 효과적인 방법</br>
> - I/O 를 병렬화하면서 스레드로 I/O를 수행할 때 생기는 문제를 극복하기 위해 팬인과 팬아웃에 코루틴을 사용할 수 있음</br>

<br>

## BetterWay61. 스레드를 사용한 I/O를 어떻게 asyncio로 포팅할 수 있는지 알아두라

- 숫자 추측 게임 TCP 서버 게임 예제
    - 비동기 적용 X
    - 동작X
```python
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

## 서버로 전송할 명령 코드 정의
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
        
    ## 들어오는 입력 메시지 처리
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
```
- 위 코드를 비동기로 포팅한 코드
    - for, with, contextlib 등 비동기에 대응하는 라이브러리들이 있음
    - 하지만 `__iter__`, `__next__`에 해당하는 비동기 기능은 없음
        - 직접 `__aiter__`, `__anext__`등으로 메서드에 대해 await를 해야한다.
        - yield from에 대응하는 비동기 버전도 없어서 제너레이터를 함께 사용하면 어렵다.
```python
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
```

### 기억해야 할 Point
> - 파이썬은 for, with, 제너레이터, 컴프리헨션의 비동기 버전을 제공하고 코루틴 안에서 기존 라이브러리 도우미 함수를 대신해 즉시 사용할 수 있는 대안을 제공한다.<br>
> - `asyncio` 내장 모듈을 사용하면 스레드와 블로킹 I/O를 사용하는 기존 코드를 코루틴과 비동기 I/O를 사용하느 코드로 쉽게 포팅할 수 있다.<br>

<br>

## BetterWay62. asyncio로 쉽게 옮겨갈 수 있도록 스레드와 코루틴을 함께 사용하라

- 블로킹 IO에 스레드를 사용하는 부분과 비동기 IO에 코루틴을 사용하는 부분이 서로 호환되면서 공존할 수 있어야 함
    - 스레드가 코루틴을 실행
    - 코루틴이 스레드를 시작하거나 기다림

- 로그파일을 한 출력 스트림으로 병합해 디버깅을 돕는 프로그램 예제
    - 파일 핸들이 주어지면 데이터가 도착했는지 감지해서 다음 줄을 반환할 방법 필요
    - 파일 핸들의 `tell` 메서드를 활용해서 현재 읽기 중이 위치 확인 가능

    - 스레드와 코루틴의 상호작용 기능에 집중해보자
```python
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
```


- 위의 스레드 기반 구현으로부터 점진적으로 `asyncio`와 코루틴 기반으로 바꾸는 방법은?
    - 하향식과 상향식이 있음

- 하향식 방법
    - main진입점처럼 코드베이스에서 가장 높은 구성으로부터 시작
    - 점차 호출 계층의 잎 부분에 위치한 갭라 함수와 클래스로 내려가면서 작업
    - 공통 모듈이 많다면 이런 접근 방법이 유용

    - 구체적인 단계
        1. 최상위 함수가 `def`대신 `async def` 사용
        2. 최상위 함수가 I/O를 호출하는 모든 부분(이벤트 루프가 블록될 가능성이 있다.)을 `asyncio.run_in_executor`로 감싸라
        3. `run_in_executor` 호출이 사용하는 자원이나 콜백이 제대로 동기화 됐는지 확인(`Lock`이나 `asyncio.run_coroutine_threadsafe`함수를 사용)
        4. 호출 계층의 잎 쪽으로 내려가면서 중간에 있는 함수와 메서드를 코루틴으로 변환. `get_event_loop`와 `run_in_executor`호출을 없애려고 시도하자

    - 이 단계별로 반복 리팩터링 진행
        - `readline()`함수를 비동기 코루틴 함수로 변경할 수도 있다.
```python
## 하향식 1~3단계
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


## 하향식 4단계 추가
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
```


- 상향식 방법
    - 구체적인 단계
        1. 프로그램에서 잎 부분에 있는, 포팅하려는 함수의 비동기 코루틴 버전을 새로 작성
        2. 기존 동기 함수를 변경해서 코루틴 버전을 호출하고, 실제 동작을 구현하는 대신 이벤트 루프를 실행하게 하자
        3. 호출 꼐층으 한 단계 올려서 다른 코루틴 계층을 만들고, 기존에 동기적 함수를 호출하던 부분을 1단계에서 정의한 코루틴 호출로 바꿔라
        4. 이제 비동기 부분을 결합하기 위해 2단계에서 만든 동기적인 래퍼가 더이상 필요하지 않다. 이를 삭제한다.

    - 가장 밑단 함수라고 할 수 있는 `tail_file`함수부터 변환을 시작.
    - 다음 단계를 `run_thread`를 코루틴으로 변경
```python

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
```

### 기억해야 할 Point
> - `asyncio` 이벤트 루프의 `run_in_executor`메서드를 사용하면 코루틴이 `ThreadPoolExecutor`사용해 동기적인 함수를 호출할 수 있다. 하향식으로 `asyncio`로 마이그레이션할 수 있다.</br>
> - `asyncio` 이벤트 루프의 `run_until_complte`메서드를 사용하면 동기적인 코드가 코루틴을 호출하고 완료를 기다릴 수 있다. `asyncio.run_coroutine_threadsafe`도 같은 기능을 제고하지만 스레드 경계에서도 안전하게 작동한다. 두 메서드를 활용하면 상향식으로 asyncio에 마이그레이션에 도움이 된다.</br>


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
