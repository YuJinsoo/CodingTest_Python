# 1분 Snack Python

## f-string 이중 괄호

- fstring 에 변수로 값 설정하기

```python
something = '볼펜'
EA = 2
one_length = 5.343
scale = 'cm'

print(f'{something} {EA}개의 길이는 {one_length*EA}{scale} 입니다.')
print(f'{something} {EA}개의 길이는 {one_length*EA:.1f}{scale} 입니다.')
```

- f-string 문법

```python
# f-string 문법

name = 'python'

print(f'{name}')
print(f'{name:^10}')
print(f'{name:>10}')
print(f'{name:<10}')

print(f'{name:$^10}')

char_a = '5'
int_a = 5
print(1234567890)
print(f'{char_a:>5}')   # >는 오른쪽정렬
print(f'{char_a:<5}')   # <는 왼쪽정렬
print(f'{char_a:^5}')   # ^는 가운데정렬
print(f'{char_a:$^5}')  # ^는 가운데정렬
print(f'{int_a:0<5}')   # <는 왼쪽정렬, 빈자리를 콜론: 다음 문자로 채울수 있음
print(f'{int_a:@^10.2f}')# ^ 가운데 정렬하면서 빈자리는 @로 채우고 소수점 2째 자리까지 표현

# python
#   python
#     python
# python
# $$python$$
# 1234567890
#     5
# 5
#   5
# $$5$$
# 50000
# @@@5.00@@@
```

- 자리수 표현을 변수로 사용할 수 있습니다.
- **이중 중괄호** 표현

```python
number= 10
digits = 10 # 자리수

print(f'{number:@>{digits}}')
print(f'{number:{digits}d}')

pi = 3.141592
digits = 3
print(f'{pi:.{digits}f}') # digits로 지정한 자리수 만큼 소수점 표시

# @@@@@@@@10
#         10
# 3.142
```

### f-string : python 3.8 버전 이후 디버깅용 출력

- f-string을 더 간단하게 작성할 수 있습니다.

```python
num = 10

## 이전 문법
print(f'num = {num}')

## 3.8 이후 추가된 것
print(f'{num = }')
print(f'{num=}')

```

## 왈러스 연산자 (:=)

- 변수에 값 할당과 동시에 할당된 값을 return 해주는 연산자

```python

count = 0
result = 0

# count에 1을 더하는 연산을 하고 count의 값과 101과 대소비교
# while 문 안에 count +=1 구문을 넣을 필요가 없어집니다.
while (count := count + 1) < 101:
    result += count

result # 5050
```

- 함수의 리턴을 할당하는 부분과 조건문에도 유용하게 사용할 수 있습니다.

```python
def sigma(n):
    count = 0
    result = 0

    # count에 1을 더하는 연산을 하고 count의 값과 101과 대소비교
    # while 문 안에 count +=1 구문을 넣을 필요가 없어집니다.
    while (count := count + 1) < 101:
        result += count

    return result

# 원래는 total _sum 에 함수결과를 할당해주는 부분이 필요하지만
# 왈러스 연산자가 있으면 할당과 결과출력이 되기 때문에 코드를 줄일 수 있습니다.
# total_sum = sigma(100)
if total_sum := sigma(100) :
    print(total_sum)
else:
    print('1부터 정수형태로 입력이 가능합니다.')

```

- 조건문 활용 2

```python
def sigma(n):
    count = 0
    result = 0

    # count에 1을 더하는 연산을 하고 count의 값과 101과 대소비교
    # while 문 안에 count +=1 구문을 넣을 필요가 없어집니다.
    while (count := count + 1) < 101:
        result += count

    return result

if (total_sum := sigma(100)) == 5050 :
    print('합이 5050이 출력되었습니다.)

else:
    print('1부터 정수형태로 입력이 가능합니다.')
```

## dictionary key error 처리

- dictionary에서 `[]`연산자로 없는 key를 호출하면 `key error`가 발생합니다.
- `key error`를 피하고 없는 key를 호출했을 때 출력할 default값을 설정하기 위해 `.get()`메서드를 사용합니다.

```python
## switch 문 대체로 dictionary 를 return 하는 식으로 많이 작성합니다.
def today(num):
    return {
        0: '일요일',
        1: '월요일',
        2: '화요일',
        3: '수요일',
        4: '목요일',
        5: '금요일',
        6: '토요일'
    }.get(num, '없는 요일입니다')

print(today(0))
print(today(8))
# 일요일
# 없는 요일입니다
```

## list와 list comprehension 성능 비교

- `dis`모듈을 사용하면 해당 코드의 바이트코드를 얻을 수 있습니다.
- `dis`모듈을 통해 확인하면 list comprehension에는 append() 메서드가 없는 것을 확인할 수 있습니다.

```python
# list comprehension
import dis

def test():
    x = [i for i in range(10)]
    return x

dis.dis(test)
## append 함수가 없는 것을 확인할 수 있습니다.
## 출력
#   4           0 LOAD_CONST               1 (<code object <listcomp> at 0x7efcd848ec30, file "<ipython-input-33-c4c5a8fd139f>", line 4>)
#               2 LOAD_CONST               2 ('테스트.<locals>.<listcomp>')
#               4 MAKE_FUNCTION            0
#               6 LOAD_GLOBAL              0 (range)
#               8 LOAD_CONST               3 (10)
#              10 CALL_FUNCTION            1
#              12 GET_ITER
#              14 CALL_FUNCTION            1
#              16 STORE_FAST               0 (x)

#   5          18 LOAD_FAST                0 (x)
#              20 RETURN_VALUE

# Disassembly of <code object <listcomp> at 0x7efcd848ec30, file "<ipython-input-33-c4c5a8fd139f>", line 4>:
#   4           0 BUILD_LIST               0
#               2 LOAD_FAST                0 (.0)
#         >>    4 FOR_ITER                 4 (to 14)
#               6 STORE_FAST               1 (i)
#               8 LOAD_FAST                1 (i)
#              10 LIST_APPEND              2
#              12 JUMP_ABSOLUTE            2 (to 4)
#         >>   14 RETURN_VALUE
```

```python
# list append로 list 생성
import dis

def test():
    x = []
    for i in range(10):
        x.append(i)
    return x

dis.dis(test)
## 출력
#   4           0 BUILD_LIST               0
#               2 STORE_FAST               0 (x)

#   5           4 LOAD_GLOBAL              0 (range)
#               6 LOAD_CONST               1 (10)
#               8 CALL_FUNCTION            1
#              10 GET_ITER
#         >>   12 FOR_ITER                 7 (to 28)
#              14 STORE_FAST               1 (i)

#   6          16 LOAD_FAST                0 (x)
#              18 LOAD_METHOD              1 (append) <<<<<<<<<<<< append 함수
#              20 LOAD_FAST                1 (i)
#              22 CALL_METHOD              1
#              24 POP_TOP
#              26 JUMP_ABSOLUTE            6 (to 12)

#   7     >>   28 LOAD_FAST                0 (x)
#              30 RETURN_VALUE
```

- jupyter notebook 의 %%timeit 를 사용해서 시간을 측정해보겠습니다.
- 환경에 따라 다르지만 결과는 아래와 같습니다.

> 1_000_000 까지 list 생성
> append는 284 ms
> comprehension 은 244 ms

```python
%%timeit

def test_append(n):
    s = []
    for i in range(n+1):
        i = i**2
        s.append(i)
    return sum(s)

test_append(1000000)
## 출력
# 284 ms ± 16.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

```python
%%timeit

def test_comprehension(n):
    s = [i**2 for i in range(n+1)]
    return sum(s)

test_comprehension(1000000)
## 출력
# 244 ms ± 7.37 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

- `psutil`모듈로 메모리 효율을 측정할 수 있습니다.
- comprehension으로 생성하는 것이 메모리 효율적으로도 굉장히 좋은것을 확인할 수 있습니다.

> append로 생성: 266.78906 MB - 210.78125 MB = 56.00781 MB
> comprehension으로 생성:296.66797 MB - 266.78906 MB = 29.87891 MB

```python
import psutil

def curr_memory_usage():
    p = psutil.Process()
    메모리사용 = p.memory_info().rss / 2 ** 20
    print(f'{메모리사용: 10.5f} MB')
def test_append(n):
    s = []
    for i in range(n+1):
        i = i**2
        s.append(i)
    return sum(s)

curr_memory_usage()
test_append(100000000)
curr_memory_usage()

def test_comprehension(n):
    s = [i**2 for i in range(n+1)]
    return sum(s)

curr_memory_usage()
test_comprehension(100000000)
curr_memory_usage()

## 출력
#  210.78125 MB
#  266.78906 MB
#  266.78906 MB
#  296.66797 MB
```

## sorted의 key 응용

- `sorted()`메서드는 순환 가능한 객체를 정렬해주는 메서드입니다.

```python
# dictionary는 key값 기준으로 정렬합니다.
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
```

- key에 정렬 기준을 적용할 함수를 입력할 수 있습니다.

```python
# string의 lower 값을 기준으로 정렬(대소문자 구분하지 않고 정렬)
# key를 쓴 것과 쓰지 않은 것의 차이가 있습니다.
print(sorted("This is a test string from Andrew".split(), key=str.lower))
print(sorted("This is a test string from Andrew".split()))

# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
# ['Andrew', 'This', 'a', 'from', 'is', 'string', 'test']
```

- 튜플도 정렬이 가능합니다. key 로 비교할 요소의 인덱스를 지정해 정렬할 수 있습니다.
- `from operator import itemgetter`를 이용해 비교할 요소를 지정할 수 있습니다.

```python
from operator import itemgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# 각 튜플의 세번째 인자를 기준으로 정렬한 리스트 반환
# 보통 기준은 오름차춘.
print(sorted(student_tuples, key=lambda student: student[2]))

# operator의 itemgetter를 이용해서 인덱싱 없이 비교할 요소를 정할 수 있습니다.
print(sorted(student_tuples, key=itemgetter(2), reverse=True))

# itemgetter로 여러개의 인자를 주어 우선순위를 여러개 지정할 수 있습니다. (다중 순회 허용)
print(sorted(student_tuples, key=itemgetter(1, 2))) # 1번인덱스 요소로 정렬 후 2번인덱스 순으로

# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

- 클래스도 같은 원리로 적용이 가능합니다.
- `from operator import attrgetter`를 이용해 비교할 요소를 지정할 수 있습니다.

```python
from operator import attrgetter
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda x:x.name))
print(sorted(student_objects, key=lambda x:x.age))
print(sorted(student_objects, key=attrgetter('age')))
print(sorted(student_objects, key=attrgetter('grade', 'age')))

# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

- 직접 정의한 함수를 기준으로 정렬할 수 있습니다.
- 우선순위 그룹에 있는 특정 원소를 먼저 정렬한 후 나머지 정렬이 가능합니다.

```python
test = [10, 2, 1, 2, 9, 3, 0, 5, 5, 5, 6, 9, 3, 11, 22]
group = [0, 1, 11, 111]

def func(value):
    if value in 우선group순위그룹:
        return (False, value)
    return (True, value)

print(sorted(test, key=func))

## 적용안됨
# False와 True만 넘어가기 때문에 정렬 기준이 없어져서 정렬 X
print(sorted(test, key=lambda x: False if x in group else True))

## 적용됨
# False와 True와 함께 정렬할 값을 넘겨주면 정렬 가능
print(sorted(test, key=lambda x: (False, x) if x in group else (True, x)))
```

- 위 원리는 sorted 정렬 시 False가 True보다 앞에 오는 원리를 이용한 것입니다.

```python
li = [True, False, False, False, True]

print(sorted(li)) # [False, False, False, True, True]
```

## 타입 힌트(type annotation)

- Python은 변수의 타입이 실행 시점에 결정되는 언어(동적 프로그래밍 언어)
- C와 JAVA는 변수를 선언할 때 반드시 타입을 명시, 컴파일 시점에 변수의 타입이 결정(정적 프로그래밍 언어)
- mypy 모듈을 사용하면 타입힌트에 오류가 있는지 확인할 수 있음

```python
# 파이썬이 동적 프로그래밍이기 때문에 자료형이 정해지지 않습니다
# 이런 실수를 줄이기 위해 주석으로 표시해왔었습니다.
number = 1 # type : int

def greeting(name):
    # tyep: (str) -> str
    return 'Hello, ' + name
```

- Python 3.5 이상 부터는 더 나은 타입 힌트를 위해
- 타입 어노테이션(type annotation)이라는 기능을 추가하였습니다.

```python
number: int = 1
name: str = "홍길동"
arr: list = ['a', 'b', 'c']

def greeting(name: str) -> str:
    return 'Hello, ' + name
```

- 타입 어노테이션을 사용해도 list나 tuple 내부의 요소의 자료형을 표현할수는 없었습니다.
- typing 모듈을 사용하면 리스트, 튜블 안에 들어가는 자료형도 명시할 수 있습니다.

```python
# 하지만 이것도 자료형을 강제하지 않습니다.
import typing

arr: typing.List[int] = [1, 2, 3]
alpha: typing.Tuple[str, str, str] = ('a', 'b', 'c')
student: typing.Dict[str, int] = {'홍길동': 1, '춘향': 2}
```

> 가장 중요한 것은 자료형을 표현할 수 는 있지만, 표현된 자료형으로 강제하지 않습니다.

```python
# 에러가 발생하지 않습니다.
num:int = '123'
print(num)
```

- `mypy` 모듈 (pip install mypy)
- 아래 내용을 실행하면 정상 동작합니다.
- 하지만 파일로 생성해서 터미널에 서 `mypy test.py`를 실행하면
  > test.py:1: error: Incompatible types in assignment (expression has type "str", variable has type "int") [assignment]
  > Found 1 error in 1 file (checked 1 source file)

```python
# 실행하면 에러 발생하지 않고 정상 동작합니다.

num: int = "1"
print(num) #1
```

## sum() 함수를 활용한 개별 요소 합치기

- `sum()`함수는 iterable한 객체의 요소들의 합을 구하는데 주로 사용합니다.
- 하지만 빈 오브젝트를 전달하여 개별 요소들을 합칠 수 있습니다.

  > 차원을 감소시키는 작업을 손쉽게 할 수 있습니다!!

- list에서 활용해봅시다.
- list객체와 함께 빈 리스트를 전달하면 빈 리스트에 전달된 리스트의 2차원 요소들이 빈 리스트에 추가되어 리턴됩니다.

```python
li = [['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z']]
print(sum(li, []))
print(sum(li, ['start']))
# ['a', 'b', 'c', 1, 2, 3, 'x', 'y', 'z']
# ['start', 'a', 'b', 'c', 1, 2, 3, 'x', 'y', 'z']
```

- tuple에서 활용해봅시다.
- list와 같은 용법으로 사용이 불가능합니다. 왜냐하면 tuple은 수정 불가능한 성질을 가지고 있기 때문입니다.

```python
t = (('a', 'b', 'c'), (1, 2, 3), ('x', 'y', 'z'))
sum(t, ()) # ('a', 'b', 'c', 1, 2, 3, 'x', 'y', 'z')
# sum(t, ('a'))
#tuple은 변경 불가능하기 때문에 시작값 설정해주면 에러

```

- dictionary

```python
#dictionary는 key들을 더해버립니다.
d = {1:'one', 2:'two'}
print(sum(d, 0))    # 3
print(sum(d, 5))    # 5


# dictionary key 가string이면 요소 합치기로 sum 활용이 불가능합니다..
d = {'one': 1, 'two':2 }
# sum(d, 0) TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sum(d, '') TypeError: sum() can't sum strings [use ''.join(seq) instead]
```

- 고차원 배열을 저차원으로 수정하고 그것을 반복해서 총합을 구할 수 있습니다.

```python
data = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

print(sum(data,[]))
print(sum(sum(data,[])))
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# 36
```

- 사실 이 방식보다 `numpy` 모듈을 사용하면 깔끔하게 처리됩니다.

```python
import numpy as np

data = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

print(np.sum(data, axis = 0)) # 2차원 배열간에 같은 인덱스 번호 요소끼리 sum
print(np.sum(data, axis = 1)) # 같은 리스트 끼리의 합
# [ 9 12 15]
# [ 3 12 21]

```

## generator를 활용한 특정 값 무한 반복자 만들기

- generator는 `yield` 키워드를 쓰는 함수입니다.
