# 목차
- 예외처리
- 로깅
- 비동기 프로그래밍
- 테스트와 디버깅


## 예외처리와 오류 관리

### 에러의 종류

- 모든 애러는 아래 공식문서에서 확인할 수 있습니다.
- https://docs.python.org/ko/3/library/exceptions.html

- 문법 에러(Syntax Error)
- 문법 에러는 파이썬 코드를 실행하기 전에 발생하는 에러로, 코드 작성 시 오타나 문법적인 오류가 있을 경우 발생합니다. 이 경우 파이썬 인터프리터는 해당 줄에서 에러가 발생했음을 알려주며, 발견된 오류의 위치와 종류를 알려줍니다.


```python
# Syntax Error
for i in range(10)
    print(i)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-3b184248ad5a> in <cell line: 1>()
    ----> 1 print(i)
    

    NameError: name 'i' is not defined


- 이름 에러(Name Error)
- 이름 에러는 정의되지 않은 변수나 함수를 호출했을 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 변수나 함수를 찾을 수 없다는 메시지를 출력합니다.


```python
# Name Error
print(x)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-e9e3baa318b0> in <cell line: 2>()
          1 # Name Error
    ----> 2 print(x)
    

    NameError: name 'x' is not defined


- 타입 에러(Type Error)
- 타입 에러는 서로 다른 타입의 변수 간 연산이나 함수 호출 시 발생합니다. 이 경우 파이썬 인터프리터는 해당 연산이나 함수 호출이 불가능하다는 메시지를 출력합니다.


```python
# Type Error
x = 10
y = '20'
print(x + y)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-62c7d5a446c2> in <cell line: 4>()
          2 x = 10
          3 y = '20'
    ----> 4 print(x + y)
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


- 인덱스 에러(Index Error)
- 인덱스 에러는 리스트나 튜플 등의 시퀀스 타입에서 존재하지 않는 인덱스를 호출했을 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 인덱스를 찾을 수 없다는 메시지를 출력합니다.
- 하지만 슬라이싱에서는 index가 넘어가도 에러를 발생시키지 않습니다.


```python
# Index Error
my_list = [1, 2, 3]
print(my_list[3])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-4-f79f21f7e49e> in <cell line: 3>()
          1 # Index Error
          2 my_list = [1, 2, 3]
    ----> 3 print(my_list[3])
    

    IndexError: list index out of range



```python
# 하지만 슬라이싱에서는 index가 넘어가도 에러를 발생시키지 않습니다.
my_list = [1, 2, 3]
print(my_list[:3])
```

    [1, 2, 3]


- 키 에러(Key Error)
- 값 에러는 내장 함수나 메서드의 인자로 전달된 값의 타입이나 값이 유효하지 않을 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 값을 처리할 수 없다는 메시지를 출력합니다.



```python
# Key Error
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])
```

- python의 dictionary에서 key값으로 조회할 때 key 값이 없다면 무조건 Error를 뱉지만, `get()` 이라는 메서드를 사용하면 에러가 발생하지 않고, key가 없을 때 지정한 값을 출력할 수 있습니다.


```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('c'))
print(my_dict.get('c', '없습니다.'))
```

    None
    없습니다.


- 값 에러(ValueError)
- 값 에러는 내장 함수나 메서드의 인자로 전달된 값의 타입이나 값이 유효하지 않을 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 값을 처리할 수 없다는 메시지를 출력합니


```python
# Value Error
int('a')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-7-b8f9f0574b88> in <cell line: 2>()
          1 # Value Error
    ----> 2 int('a')
    

    ValueError: invalid literal for int() with base 10: 'a'


- 제로 나누기 에러(ZeroDivisionError)
- 제로 나누기 에러는 0으로 나누기 연산을 수행할 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 연산이 불가능하다는 메시지를 출력합니다.


```python
# ZeroDivision Error
x = 10
y = 0
print(x / y)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-8-f17cbf29a9a4> in <cell line: 4>()
          2 x = 10
          3 y = 0
    ----> 4 print(x / y)
    

    ZeroDivisionError: division by zero


- 어트리뷰트 에러(Attribute Error)
- 어트리뷰트 에러는 객체에 존재하지 않는 속성이나 메서드를 호출했을 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 속성이나 메서드를 찾을 수 없다는 메시지를 출력합니다


```python
# Attribute Error
my_list = [1, 2, 3]
print(my_list.appeend(4))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-9-dceecff01ea8> in <cell line: 3>()
          1 # Attribute Error
          2 my_list = [1, 2, 3]
    ----> 3 print(my_list.appeend(4))
    

    AttributeError: 'list' object has no attribute 'appeend'


- 인자 개수 에러(TypeError)
- 인자 개수 에러는 함수나 메서드에 전달된 인자의 개수가 맞지 않을 때 발생합니다. 이 경우 파이썬 인터프리터는 해당 함수나 메서드에 전달된 인자의 개수가 맞지 않다는 메시지를 출력합니다.


```python
# Type Error
def add(x, y):
    return x + y

add(1, 2, 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-cbb8c8b9d43a> in <cell line: 5>()
          3     return x + y
          4 
    ----> 5 add(1, 2, 3)
    

    TypeError: add() takes 2 positional arguments but 3 were given


- 파일 입출력 에러(File I/O Error)
- 파일 입출력 에러는 파일을 열거나 쓰거나 읽을 때 발생할 수 있습니다. 파일이 존재하지 않거나 권한이 없는 경우 발생할 수 있으며, 이 경우 파이썬 인터프리터는 해당 파일을 찾을 수 없다는 메시지를 출력합니다.


```python
# File I/O Error
f = open('non-existent.txt', 'r')
f.read()
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-11-398bb0f309eb> in <cell line: 2>()
          1 # File I/O Error
    ----> 2 f = open('non-existent.txt', 'r')
          3 f.read()


    FileNotFoundError: [Errno 2] No such file or directory: 'non-existent.txt'


### python 예외처리

- 예외 상황에서 프로그램이 강제 종료되는 것을 방지하고, 예외 상황을 처리하는 방법을 "예외 처리"라고 합니다.
- 예외처리는 `try` 구문으로 처리합니다.
- 하지만, try를 범위를 너무 크게 잡는다던가 하는 식으로 오용/남용 하면 안됩니다.
- 구글 컨벤션에서도 try - except 구문은 최소단위로 사용하는것을 추천합니다.


```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
```

- try + except
    - try except 구문을 사용하여 예외 처리를 할 수 있습니다. try 블록 내에서 예외가 발생하면, except 블록이 실행되고 프로그램이 종료되지 않습니다.

- try + except + else
    - try except else 구문을 사용하여 예외 처리를 할 수 있습니다. try 블록 내에서 예외가 발생하지 않으면, else 블록이 실행됩니다.

- try + finally
    - try finally 구문을 사용하여 예외 처리를 할 수 있습니다. finally 블록은 예외 발생 여부와 상관없이 항상 실행됩니다.

- try + except + finally

- try + except + else + finally


```python
# else 는 while이나 for문 뒤에서 사용이 가능합니다.
# 반복문에서 사용할 때의 의미는
# 반복문 중간에 종료되지 않고 모든 반복을 완료한 후 반복문이 종료되었을 경우 실행되는 구문입니다.

```

### 에러 발생시키고 만들기

- 에러는 아래와 같이 raise를 사용하여 발생시킬 수 있습니다. 순차적으로 실행해보세요.


```python
raise  # RuntimeError
raise ValueError
raise ValueError('코드를 잘~~ 만들어주세요.') # ValueError 내용에 문자열이 들어감
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-15-b8cd38bac00c> in <cell line: 3>()
          1 # raise  # RuntimeError
          2 # raise ValueError
    ----> 3 raise ValueError('코드를 잘~~ 만들어주세요.')
    

    ValueError: 코드를 잘~~ 만들어주세요.


- 여러 에러가 발생할 가능성이 있는 곳에 여러 종류의 에러를 except에 지정해서 예외 종류에 따른 분기처리를 할 수 있습니다.


```python
try:
    1/0
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')

print(ZeroDivisionError)
print(type(ZeroDivisionError))
print(dir(ZeroDivisionError))
```

    ZeroDivisionError
    <class 'ZeroDivisionError'>
    <class 'type'>
    ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']


- 다음과 같이 에러를 만드는 것도 가능합니다.


```python
class Leehojun(Exception): #Exception을 상속받으면 됩니다.
    def __init__(self):
        super().__init__('입력된 값이 leehojun이 아닙니다.')

raise Leehojun
```


    ---------------------------------------------------------------------------

    Leehojun                                  Traceback (most recent call last)

    <ipython-input-17-b11d5076ad8d> in <cell line: 5>()
          3         super().__init__('입력된 값이 leehojun이 아닙니다.')
          4 
    ----> 5 raise Leehojun
    

    Leehojun: 입력된 값이 leehojun이 아닙니다.


### 오류처리와 로깅

- 로깅은 경고, 접근, 애러, 예외 처리, 특정 함수 사용 등에 대한 기록을 남기는 행위입니다. 주로 화면에 출력하거나 DB또는 일반 plane text로 남기는 방식을 사용합니다. 로그기록이 너무 많을 경우 시스템에 부하를 줄 수 있으며, 일반적인 편집기가 읽지 못할 수 있습니다.
- 로그를 남기는 것도 오류 관리의 중요한 부분입니다. logging 모듈을 사용하면 다양한 레벨의 로그를 쉽게 남길 수 있습니다.

- https://docs.python.org/ko/3/howto/logging.html


```python
import logging

logging.basicConfig(level=logging.INFO) # 어느 레벨부터 로깅할지, 기본으로 warning 부터 합니다.

logging.debug("This is a debug message") # 고쳐야 할 코드, 기록 필요
logging.info("This is an info message") # 정보성 메시지
logging.warning("This is a warning message") # 경고 메시지
logging.error("This is an error message") # 애러 메시지(프로그램은 동작)
logging.critical("This is a critical message") # 프로그램 중지(애러처리 안된경우)
```

    WARNING:root:This is a warning message
    ERROR:root:This is an error message
    CRITICAL:root:This is a critical message



```python
import logging.handlers

def logger():
    log_obj = logging.getLogger("log_name") # log name으로 log 객체 생성
    log_obj.setLevel(logging.DEBUG) # 어디부터 기록할지 설정

    fileHandeler = logging.FileHandler(filename="./test.txt") # 파일로 기록
    streamHandler = logging.StreamHandler() # 콘솔에 출력

    # DEBUG - INFO - WARNING - ERROR - CRITICAL
    # 파일에는 DEBUG 부터, 콘솔에는 INFO 부터 기록됨
    fileHandeler.setLevel(logging.INFO) # 파일 기록 레벨 설정
    streamHandler.setLevel(logging.DEBUG) # 콘솔 기록 레벨 설정

    formatter = logging.Formatter("%(name)s, %(asctime)s, %(levelname)s, %(message)s") #포멧 생성

    fileHandeler.setFormatter(formatter) # 파일 메시지 포멧 설정
    streamHandler.setFormatter(formatter) # 콘솔 메시지 포멧 설정

    log_obj.addHandler(fileHandeler) # log_obj handler에 파일 출력 방식 추가
    log_obj.addHandler(streamHandler) # log_obj handler에 파일 콘솔 방식 추가

    return log_obj

log = logger()

# 아래 코드를 기록하고 싶은 곳에 함께 설정
log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')
log.critical('critical')

print('---')

# 아래와 같이 사용합니다.
def f():
    try:
        x = 1 / 0
    except Exception as e:
        print(e)
        log.error(f'{e} error')
print('---')
f()
```

    log_name, 2023-07-09 03:44:05,076, DEBUG, debug
    DEBUG:log_name:debug
    log_name, 2023-07-09 03:44:05,088, INFO, info
    INFO:log_name:info
    log_name, 2023-07-09 03:44:05,091, WARNING, warning
    WARNING:log_name:warning
    log_name, 2023-07-09 03:44:05,096, ERROR, error
    ERROR:log_name:error
    log_name, 2023-07-09 03:44:05,101, CRITICAL, critical
    CRITICAL:log_name:critical
    log_name, 2023-07-09 03:44:05,105, ERROR, division by zero error
    ERROR:log_name:division by zero error


    ---
    ---
    division by zero


## 비동기 프로그래밍

- 비동기 프로그래밍이란 프로그램의 흐름을 블록(block)하지 않고 다른 작업을 계속 진행할 수 있도록 하는 프로그래밍 패러다임입니다. 즉, 하나의 작업이 완료될 때까지 기다리지 않고 다른 작업을 진행합니다.

> Google Colab의 환경에서는 이미 기본적으로 이벤트 루프가 실행 중입니다. 이 이벤트 루프는 Google Colab 환경의 비동기 작업을 처리하기 위해 사용됩니다. 그러므로, Google Colab에서는 asyncio.run() 함수를 직접 호출하면 "cannot be called from a running event loop"와 같은 에러 메시지가 출력됩니다. 이를 해결하려면 아래와 같은 코드를 추가해야 합니다.
> ```python
!pip install nest_asyncio
```

> ```python
import nest_asyncio
nest_asyncio.apply()
```

- 동기 프로그래밍: 코드가 순차적으로 실행되며, 특정 작업이 완료될 때까지 프로그램이 기다리는 방식입니다. 해당 실습은 로컬에서 진행합니다.


```python
import time

def job(number):
    print(f"Job {number} started")
    time.sleep(1)  # 매우 오래 걸리는 작업, 일반 sleep은 CPU를 쉬게 합니다.
    print(f"Job {number} completed")

job(1)
job(2)
job(3)
```

    Job 1 started
    Job 1 completed
    Job 2 started
    Job 2 completed
    Job 3 started
    Job 3 completed


- 비동기 프로그래밍: 동시에 여러 작업을 진행할 수 있습니다. 이때, 이벤트 루프와 콜백 함수 등을 활용하여 작업을 관리합니다.


```python
!pip install nest_asyncio
```

    Requirement already satisfied: nest_asyncio in /usr/local/lib/python3.10/dist-packages (1.5.6)



```python
import nest_asyncio

nest_asyncio.apply()
```


```python
import asyncio

async def job(number):
    print(f"Job {number} started")
    await asyncio.sleep(1) # 매우 오래 걸리는 작업, asyncio.sleep은 비동기 처리를 할 수 있도록 합니다.(다른 작업이 가능합니다.)
    print(f"Job {number} completed")

async def main():
    await asyncio.gather(job(1), job(2), job(3)) # await asyncio.wait([job(1), job(2), job(3)])

asyncio.run(main())
print('hello world')
```

    Job 1 started
    Job 2 started
    Job 3 started
    Job 1 completed
    Job 2 completed
    Job 3 completed
    hello world


- 아래와 같이 비동기 프로그래밍을 동기로 만들 수 있습니다.


```python
import asyncio

async def job(number):
    print(f"Job {number} started")
    await asyncio.sleep(1)  # 매우 오래 걸리는 작업
    print(f"Job {number} completed")

asyncio.run(job(1))
asyncio.run(job(2))
asyncio.run(job(3))
```

    Job 1 started
    Job 1 completed
    Job 2 started
    Job 2 completed
    Job 3 started
    Job 3 completed


- 위와 동작을 동일하기 하지만 colab에서만 사용 가능한 코드입니다. .py 파일에서는 await이 함수 밖에 사용되는 것을 허락하지 않습니다.


```python
import asyncio

async def job(number):
    print(f"Job {number} started")
    await asyncio.sleep(1)  # 매우 오래 걸리는 작업
    print(f"Job {number} completed")

await job(1)
await job(2)
await job(3)
```

    Job 1 started
    Job 1 completed
    Job 2 started
    Job 2 completed
    Job 3 started
    Job 3 completed


- 다음 코드는 .py 파일에서 위와 동일하게 작동하는 코드입니다.


```python
import asyncio

async def job(number):
    print(f"Job {number} started")
    await asyncio.sleep(1)  # 매우 오래 걸리는 작업
    print(f"Job {number} completed")

async def main():
    await job(1)
    await job(2)
    await job(3)

async def main2():
    asyncio.run(job(1))
    asyncio.run(job(2))
    asyncio.run(job(3))

asyncio.run(main())
print('---')
asyncio.run(main2())
```

    Job 1 started
    Job 1 completed
    Job 2 started
    Job 2 completed
    Job 3 started
    Job 3 completed
    ---
    Job 1 started
    Job 1 completed
    Job 2 started
    Job 2 completed
    Job 3 started
    Job 3 completed



```python
import time

## 코루틴 함수이더라도 그냥 sleep을 하면 그대로 기다립니다.
# 그리고 time.sleep은 async함수가 아니기 때문에 await로 실행이 불가능합니다.
async def job(number):
    print(f"Job {number} started")
    time.sleep(1)  # 매우 오래 걸리는 작업
    print(f"Job {number} completed")

async def main():
    await asyncio.gather(job(1), job(2), job(3))

asyncio.run(main())
```

    Job 1 started
    Job 1 completed
    Job 2 started
    Job 2 completed
    Job 3 started
    Job 3 completed



```python
import asyncio

# 비동기적으로 실행됩니다!
async def job(number):
    print(f"Job {number} started")
    await asyncio.sleep(1)  # 매우 오래 걸리는 작업
    print(f"Job {number} completed")

async def main():
    await asyncio.gather(job(1), job(2), job(3))

asyncio.run(main())
```

    Job 1 started
    Job 2 started
    Job 3 started
    Job 1 completed
    Job 2 completed
    Job 3 completed


### 코루틴 (coroutine)


- 아래 코드는 async를 붙인 함수, 코루틴 함수입니다. await 키워드를 만나면 코루틴 실행을 잠시 중단하고, 코루틴의 작업이 완료될 때까지 기다린 후 결과를 반환합니다.


```python
# 일반 함수
def fun():
    print('fun')

# 코루틴 함수
async def cofunc():
    print('coroutine function')
    return 100

print(cofunc)
print(cofunc())
print(await cofunc())
```

    <function cofunc at 0x7fd88d827eb0>
    <coroutine object cofunc at 0x7fd88d865930>
    coroutine function
    100


    <ipython-input-17-9755cf9711b8>:11: RuntimeWarning: coroutine 'cofunc' was never awaited
      print(cofunc())
    RuntimeWarning: Enable tracemalloc to get the object allocation traceback



```python
# 코루틴 함수
async def cofunc():
    print('coroutine function')

async def main():
    return await cofunc()

print(main()) # <coroutine object main at 0x7fc8cb22bf40>
print(await main()) # None
```

    <coroutine object main at 0x7fd8701e1850>
    coroutine function
    None


    <ipython-input-24-cbfe55bdfd4c>:8: RuntimeWarning: coroutine 'main' was never awaited
      print(main()) # <coroutine object main at 0x7fc8cb22bf40>
    RuntimeWarning: Enable tracemalloc to get the object allocation traceback


루틴과 관련된 주요 개념은 다음과 같습니다:

- `async def`: 코루틴 함수를 선언하는 데 사용됩니다. 이 함수는 비동기적으로 실행될 수 있는 코루틴 객체를 반환합니다.
- `await`: 코루틴의 작업이 완료될 때까지 기다린 후 결과를 반환합니다.
- `asyncio.sleep(n)` : n 초 동안 해당 코루틴 함수를 잠시 쉬고 다른 처리를 할 수 있도록 합니다. (병렬적으로 실행 가능하게 함) 이것도 await로 실행시켜줍니다.
- `asyncio.run()`: 코루틴을 실행하는 함수입니다. 이벤트 루프를 생성하고, 주어진 코루틴을 실행한 후 이벤트 루프를 닫습니다.
- `asyncio.gather()`: 여러 코루틴을 동시에 실행하도록 스케줄링하는 함수입니다.

참고로, 코루틴은 파이썬 3.5부터 `async` / `await` 구문을 통해 지원되기 시작했습니다.

> async가 설정된 비동기 함수(코루틴 함수)를 실행하기 위해서는 `await`를 붙여주어야 합니다. `await`로 실행하지 않으면 그저 함수 object를 조회하는 동작이 실행됩니다!

## 테스팅과 디버깅

- 단위 테스트(unit test)는 개별 함수나 메서드와 같은 코드의 가장 작은 단위가 예상대로 동작하는지 검증하는 테스트입니다. Python에서는 unittest 모듈을 이용해 단위 테스트를 작성하고 실행할 수 있습니다.
- 표준라이브러리는 아니지만 nose2, pytest와 같은 패키지를 사용하기도 합니다. 함께 사용하는 모듈로는 coverage(보고서 형태)가 있습니다.

> 해당 코드는 colab에서는 작동하지 않습니다. 로컬 환경에서 test.py로 만들어 실습하세요.


```python
# test.py
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

```

- unittest.TestCase를 상속받는 클래스를 생성하고 그 안에 테스트로 실행할 함수를 정의합니다.
- 함수의 이름은 **test**로 시작해야 합니다.


```python
## test2.py
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_true(self):
        self.assertTrue(add(1, 2)== 3)
        self.assertTrue(add(2, 3)== 5)
        self.assertTrue(add(3, 4)== 7)


    def test_false(self):
        self.assertFalse(add(-1, 2) == 3)
        self.assertFalse(add(1, -2) == 3)
        self.assertFalse(add(11, 12) == 3)

if __name__ == '__main__':
    unittest.main()

# Ran 2 tests in 0.008s
# OK

```

- 테스트 주도 개발(Test-Driven Development, TDD)은 테스트를 먼저 작성하고 그 테스트를 통과하도록 코드를 구현하는 개발 방법론입니다. 이를 통해 코드의 품질을 향상시키고, 버그를 줄일 수 있습니다.

- 같은 다양한 메서드를 제공합니다.


```python
self.assertEqual(1 + 2, 3)
self.assertTrue(10 == 10)
self.assertFalse(1 == 10)
self.assertGreater(10, 1)
self.assertLess(1, 10)
self.assertIn(1, [1, 2, 3, 4, 5])
self.assertIsInstance('a', str)
```

- 아래와 같이 여러가지 함수를 만들어 작동시켜볼 수 있습니다. 메서드 이름은 꼭 test로 시작해야 합니다. 함수 이름 순으로 실행합니다. 구현순서와는 상관 없습니다.


```python
import unittest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(sub(10, 2), 8)

if __name__ == '__main__':
    unittest.main()
```

테스트 주도 개발(TDD, Test-Driven Development)은 빠르게 개발하여 배포해야 하는 소프트웨어에 개발방법 중 하나입니다.

1. 명세 기준으로 테스트 케이스 정의
2. 테스트 케이스를 통과할 수 있는 코드 작성
3. 통과하면 새로은 기능 추가

이렇게 개발 할 경우 개발자는 요구사항 명세에 대해 보다 잘 이해할 수 있습니다.

### 디버깅

- pdb, breakpoint
- 디버깅은 프로그램에서 오류를 찾아내고 그 원인을 알아내어 수정하는 작업을 말합니다. Python에서는 pdb 모듈을 이용하여 디버깅을 할 수 있습니다. 또한, 대부분의 통합개발환경(IDE)들은 디버깅 도구를 제공합니다.


```python
import pdb

def add_to_ten(num):
    result = num + 10
    pdb.set_trace()  # 디버거를 실행합니다. break 포인트입니다.
    return result

add_to_ten(5)
```

    
    PYDEV DEBUGGER WARNING:
    sys.settrace() should not be used when the debugger is being used.
    This may cause the debugger to stop working correctly.
    If this is needed, please check: 
    http://pydev.blogspot.com/2007/06/why-cant-pydev-debugger-work-with.html
    to see how to restore the debug tracing back correctly.
    Call Location:
      File "/usr/lib/python3.10/bdb.py", line 336, in set_trace
        sys.settrace(self.trace_dispatch)
    


    > [0;32m<ipython-input-32-f6684ea06766>[0m(6)[0;36madd_to_ten[0;34m()[0m
    [0;32m      4 [0;31m    [0mresult[0m [0;34m=[0m [0mnum[0m [0;34m+[0m [0;36m10[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      5 [0;31m    [0mpdb[0m[0;34m.[0m[0mset_trace[0m[0;34m([0m[0;34m)[0m  [0;31m# 디버거를 실행합니다. break 포인트입니다.[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 6 [0;31m    [0;32mreturn[0m [0mresult[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      7 [0;31m[0;34m[0m[0m
    [0m[0;32m      8 [0;31m[0madd_to_ten[0m[0;34m([0m[0;36m5[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> x
    *** NameError: name 'x' is not defined
    ipdb> result
    15
    ipdb> num
    5
    ipdb> num
    5
    ipdb> n
    --Return--
    15
    > [0;32m<ipython-input-32-f6684ea06766>[0m(6)[0;36madd_to_ten[0;34m()[0m
    [0;32m      4 [0;31m    [0mresult[0m [0;34m=[0m [0mnum[0m [0;34m+[0m [0;36m10[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      5 [0;31m    [0mpdb[0m[0;34m.[0m[0mset_trace[0m[0;34m([0m[0;34m)[0m  [0;31m# 디버거를 실행합니다. break 포인트입니다.[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 6 [0;31m    [0;32mreturn[0m [0mresult[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      7 [0;31m[0;34m[0m[0m
    [0m[0;32m      8 [0;31m[0madd_to_ten[0m[0;34m([0m[0;36m5[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> num
    5
    ipdb> result
    15
    ipdb> q


    
    PYDEV DEBUGGER WARNING:
    sys.settrace() should not be used when the debugger is being used.
    This may cause the debugger to stop working correctly.
    If this is needed, please check: 
    http://pydev.blogspot.com/2007/06/why-cant-pydev-debugger-work-with.html
    to see how to restore the debug tracing back correctly.
    Call Location:
      File "/usr/lib/python3.10/bdb.py", line 361, in set_quit
        sys.settrace(None)
    


- `h` : 도움말
- `n` : 현재 라인 실행 후 다음 라인으로 넘어갑니다.
- `s` : 현재 라인 실행 후 다음 스탭을 진행합니다.
- `c` : break point가 있을 때까지 계속 실행합니다.
- `q` : 중단합니다.

- Python 3.7 버전에서는 breakpoint()로 간단하게 디버깅 할 수 있습니다


```python
def add(a, b):
    return a + b

def test():
    for i in range(10):
        x = add(i, 10)
        breakpoint()
    for i in range(10):
        y = add(i, 100)
        breakpoint()

test()
```

    > [0;32m<ipython-input-33-45bf2f3f9f40>[0m(5)[0;36mtest[0;34m()[0m
    [0;32m      3 [0;31m[0;34m[0m[0m
    [0m[0;32m      4 [0;31m[0;32mdef[0m [0mtest[0m[0;34m([0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 5 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      6 [0;31m        [0mx[0m [0;34m=[0m [0madd[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;36m10[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      7 [0;31m        [0mbreakpoint[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> n
    > [0;32m<ipython-input-33-45bf2f3f9f40>[0m(6)[0;36mtest[0;34m()[0m
    [0;32m      4 [0;31m[0;32mdef[0m [0mtest[0m[0;34m([0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      5 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 6 [0;31m        [0mx[0m [0;34m=[0m [0madd[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;36m10[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      7 [0;31m        [0mbreakpoint[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      8 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> i
    1
    ipdb> x
    10
    ipdb> i, x
    (1, 10)
    ipdb> n
    > [0;32m<ipython-input-33-45bf2f3f9f40>[0m(7)[0;36mtest[0;34m()[0m
    [0;32m      5 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      6 [0;31m        [0mx[0m [0;34m=[0m [0madd[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;36m10[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 7 [0;31m        [0mbreakpoint[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      8 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      9 [0;31m        [0my[0m [0;34m=[0m [0madd[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;36m100[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> i, x
    (1, 11)
    ipdb> n
    > [0;32m<ipython-input-33-45bf2f3f9f40>[0m(5)[0;36mtest[0;34m()[0m
    [0;32m      3 [0;31m[0;34m[0m[0m
    [0m[0;32m      4 [0;31m[0;32mdef[0m [0mtest[0m[0;34m([0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 5 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      6 [0;31m        [0mx[0m [0;34m=[0m [0madd[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;36m10[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      7 [0;31m        [0mbreakpoint[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> i, x
    (1, 11)
    ipdb> n
    > [0;32m<ipython-input-33-45bf2f3f9f40>[0m(6)[0;36mtest[0;34m()[0m
    [0;32m      4 [0;31m[0;32mdef[0m [0mtest[0m[0;34m([0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      5 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m----> 6 [0;31m        [0mx[0m [0;34m=[0m [0madd[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;36m10[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      7 [0;31m        [0mbreakpoint[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0m[0;32m      8 [0;31m    [0;32mfor[0m [0mi[0m [0;32min[0m [0mrange[0m[0;34m([0m[0;36m10[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
    [0m
    ipdb> q


### 코드 품질 개선을 위한 정적 분석

- 소프트웨어 테스팅
    - 기능 테스팅
        - 화이트 박스 테스팅 : 개별 기능, 메서드, 클래스, 모듈 테스트 (정적 분석이 여기 들어갑니다.)
        - 블랙 박스 테스팅 : 소프트웨어 코드에 가시성이 없는 테스트 (셀레니움 등을 사용하기도 합니다.)
    - 성능 테스팅(부하 테스팅, 스트레스 테스팅 등)
    - 보안 테스팅
    - 사용성 테스팅
    - 설치 테스팅
    - 접근성 테스팅

정적 분석(static analysis)은 프로그램을 실행하지 않고 코드를 분석하여 버그, 코드 스멜(code smell), 안티 패턴 등을 찾아내는 방법입니다. Python에서는 `pylint`, `flake8`, `Pyflakes`등의 도구를 이용하여 정적 분석을 수행할 수 있습니다.
- PEP8과 같은 표준
- 코드의 구문 오류, 들여쓰기 등
- 로직이나 나쁜 냄새(code smells)
    - God Object : 너무 많은 기능이 있는 객체
    - Parameter creep : 너무 많은 파라미터가 있을 경우 함수 호출과 테스트에 부하를 준다.
    - Cyclomatic complexity : 과도한 분기와 루프
    - 이외에 `코드의 나쁜 냄세`는 검색을 권합니다.
    - 복잡도가 높아질수록 테스트 용이성(오류를 노출하기 쉬운 정도)이 낮아집니다.


```python
!pip install pylint
```


```python
#test.py
def 구구단():
    for i in range(2, 10):
        for j in range(1, 10):
            print('{} * {} = {}'.format(i, j, i*j))

구구단()
```


      File "<ipython-input-35-54787920bc4c>", line 9
        pylint test.py
               ^
    SyntaxError: invalid syntax




```python
pylint test.py
```


      File "<ipython-input-36-62aa7b0c3394>", line 1
        pylint test.py
               ^
    SyntaxError: invalid syntax




```python
# 결과화면
'''
PS C:\Users\ABO\Desktop\Study_Python\python_middle> pylint pylint_test.py
************* Module pylint_test
pylint_test.py:8:0: C0304: Final newline missing (missing-final-newline)
pylint_test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pylint_test.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
pylint_test.py:3:0: C2401: Function name "구구단" contains a non-ASCII character, consider renaming it. (non-ascii-name)
pylint_test.py:6:18: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

-----------------------------------
Your code has been rated at 0.00/10

PS C:\Users\ABO\Desktop\Study_Python\python_middle>

'''

```

위와 같이 `pylint`를 이용하여 `my_module.py` 파일을 정적 분석할 수 있습니다. 분석 결과를 통해 코드의 품질을 개선하는 데 도움을 받을 수 있습니다.

- R : 모범 사례(Refactor)
- C : 표준 위반(Convention)
- W : 사소한 문제 경고 (Warning)
- E : 에러 (Error)
- F : 치명적 (Fatal)
