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
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay54. 스레드에서 데이터 경합을 피가히 위해 Lock을 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay55. Queue를 사용해 스레드 사이의 작업을 조율하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

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
