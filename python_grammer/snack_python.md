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
- `dis`모듈은 파이썬 바이트 코드를 역 어셈블하여 분석하도록 지원합니다.

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

print(sum(data,[])) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(sum(sum(data,[])))# 36
```

- 사실 이 방식보다 `numpy` 모듈을 사용하면 깔끔하게 처리됩니다.

```python
import numpy as np

data = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

print(np.sum(data)) # 36
print(np.sum(data, axis = 0)) # 2차원 배열간에 같은 인덱스 번호 요소끼리 sum
print(np.sum(data, axis = 1)) # 같은 리스트 끼리의 합
# [ 9 12 15]
# [ 3 12 21]

```

## generator를 활용한 특정 값 무한 반복자 만들기. generator 활용

- generator는 `yield` 키워드를 쓰는 함수입니다.
- `yield`구문을 가진 함수는 `generator object`를 리턴합니다.
- generator 는 `__iter__`와 `__next__`를 가져서 for 문에서 호출될 때마다 한 번씩 접근됩니다.

```python
def range_0_to_4():
    yield 0
    yield 1
    yield 2
    yield 3

for i in range_1_to_4():
    print(i, end=' ')

# 0 1 2 3

print(range_0_to_4()) # <generator object range_0_to_4 at 0x7f51b1814040>
```

- 다양한 호출 및 생성 방법
- generator expression(제너레이터 표현식) 사용할 수 있고, generator object <genexpr>를 반환합니다.

```python
def range_0_to_4():
    yield 0
    yield 1
    yield 2
    yield 3

g = range_0_to_4()
print(g) # <generator object range_0_to_4 at 0x7f51b18b2f80>
print(next(g)) #0
print(next(g)) #1
print(next(g)) #2
print(next(g)) #3
# print(next(g)) # error StopIteration

# generator expression
g2 = (i for i in range(0, 4))
print(g2)   # <generator object <genexpr> at 0x7f51b18b2d50>
for i in g2:
    print(i, end = ' ')
#0 1 2 3
```

- 무한 반복자를 생성해서 활용할 수 있습니다.
- 정확한 활용 방법은 생각나지 않지만, 길이가 정해지지 않은 iterable에 대해 반복적으로 라벨링 해야 하는 경우

```python
def repeat(반복할내용):
    if 반복할내용:
        while True:
            for i in 반복할내용:
                yield i

print(list(zip('11222453', repeat([1,2])))
# [('1', 1), ('1', 2), ('2', 1), ('2', 2), ('2', 1), ('4', 2), ('5', 1), ('3', 2)]
print(list(zip(range(5), repeat([1,2])))
# [(0, 1), (1, 2), (2, 1), (3, 2), (4, 1)]
print(list(zip(range(10), repeat('abc')))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'a'), (4, 'b'), (5, 'c'), (6, 'a'), (7, 'b'), (8, 'c'), (9, 'a')]
```

## 딕셔너리 언패킹(dictionary unpacking)

- 딕셔너리의 언패킹은 key값으로 진행됩니다.

```python
d = {'one': 100, 'two': 200}
a, b = d
## d의 key값
print(a, b) # one two

li = [{'one': 100, 'two': 200}, {'three': 300, 'four': 400}]

for i, j in li:
    print(i, j)
# one two
# three four
```

- asterisk(\*)을 이용해 value까지 unpacking 할 수 있습니다.
- 사실 `keys()`나 `values()`같은 함수를 더 많이 사용할 것 같습니다.

```python
def unpack(a, b = None):
    return a, b

d = {'a' : 10, 'b': 20}

#unpack함수와 d요소의 개수가 맞아야 가능합니다.
#value 값
print(unpack(**d)) # (10, 20) # tuple 리턴됨

#key값
print(unpack(*d)) # ('a', 'b') # tuple 리턴됨

# 그냥 a에 d가 들어감.
print(unpack(d)) # ({'a': 10, 'b': 20}, None)

```

### 스스로 추가 : list를 unpacking 하기

- list도 asterisk(\*)를 이용해서 unpacking이 가능하다.
- 한 리스트를 언패킹 할 때 애스터리스크 변수는 한 개만 가능합니다.

```python
# asterisk로 list unpakcing 하기
li = [1, 2, 3, 4, 5]

a, b, *c = li
print(a, b, c) # 1 2 [3, 4, 5]

*a, b, c = li
print(a, b, c) # [1, 2, 3] 4 5

a, *b, c = li
print(a, b, c) # 1 [2, 3, 4] 5

# SyntaxError: multiple starred expressions in assignment
# *a, b, *c = li
# print(a, b, c)
```

## 파이썬의 선과 PEP8

- python 에 `import this`를 하면 파이썬이 지향하는 스타일을 설명하는 문구를 확인할 수 있습니다.

```python
import this

'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
```

### PEP8 요약

- 스페이스 4번(탭X)
- 라인 길이는 79자 이하(한글일 때에는 32자 정도로 생각하시면 됩니다.)
- 파일 : 함수와 클래스 사이에는 2줄의 빈줄
- 클래스 : 메서드 사이에는 1줄의 빈줄
- 변수 대입에서 등호 양 옆에 스페이스 1개
- 딕셔너리에 키와 콜론 사이에는 공백X, 값과 콜론은 스페이스 1개
- 변수명은 스네이크 표기법을 권장
- 클래스명은 카멜표기법 권장
- 보호해야 하는 인스턴스의 애트리뷰트는 언더바 하나로 시작
- 공개되지 말아야 하는 애트리뷰트는 언더바 두개로 시작
- 조건문 안에 'len(컨테이너) == 0' 식으로 사용X 'if 컨테이너' 권장
- 한 줄의 import 문에서는 하나의 모듈만 가져오기
- 소스검사기 : 파이린트, 파이플레이크

## 0.1+0.2는 0.3이 아니다.(부동소수점 정확도 문제 해결하기)

- 부동소수점 표현 방식은 IEEE-754에 의해 정의됩니다. (https://ko.wikipedia.org/wiki/IEEE_754)
- 표현 방식 때문에 정확한 소수점 표현이 불가능합니다.

  - 소수점에 2를 곱해 1이 되면 1 아니면 0으로 처리하는데, 2를 계속 곱해도 소수점이 계속 생기는 경우 정확한 표현이 불가능하게 됩니다.
  - 0.1 (0) > 0.2 (0) > 0.4 (0) > 0.8 (0) > 1.6 (1) > 1.2 (1) > 0.4 (0) > ... 반복

- 언어에 관계 없이 컴퓨터가 2진수로 계산하기 때문에 발생하는 문제

```python
print(0.1 + 0.2)    # 0.30000000000000004
print(0.1 * 3)      # 0.30000000000000004
print(1.2 - 0.1)    # 1.0999999999999999
print(0.1*0.1)      # 0.010000000000000002
print(0.1 + 0.2 == 0.3) # False
```

- 해결하기 위해 `decimal` 모듈이나 `math`모듈을 사용하는 방법이 있습니다.

- decimal

```python
import decimal

# 조금더 근사한 무한소수점을 표현해줌..
decimal.Decimal(0.1) # Decimal('0.1000000000000000055511151231257827021181583404541015625')

# 10진 연산에서 좀더 정확한 연산을 위해 string 값 사용
decimal.Decimal('0.1') # Decimal('0.1')
decimal.Decimal('0.1') * 3 == 0.3 # False
```

- math : python 3.5 이상에서 사용 가능합니다.

```python
import math
print(math.isclose(0.1 + 0.2, 0.3)) # True
print(math.isclose(1.2 - 0.1, 1.1)) # True

```

## 배열 이진 분할 알고리즘으로 검색속도 개선하기

- `bisect`라는 모듈을 사용하면 이진탐색을 합니다.
- list는 없는 원소를 찾을 때 -1을 반환하는 find함수도 없고, index로 찾을 때에도 찾는 도중에 에러를 뱉음

```python
data = list(range(100_000_000))

data.index(-100) ## 어느정도 연산이 진행 된다가 Value Error 발생
# 맨 앞에서부터 검색을 하기 때문에 시간이 오래 걸립니다.
data.index(99_999_999)
```

- list의 index함수로 원소의 위치를 찾을 때, 원소가 배열의 뒷쪽에 위치한다면 배열의 길이만큼 탐색 시간이 소요됩니다.
- 위의 data를 그대로 사용합니다.

```python
%%time
data.index(99999999)
## 1.45 s ± 457 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

- 2진탐색 모듈을 사용해서 검색을 하면, 소요 시간이 매우 감소하는 것을 확인할 수 있습니다. (500배 가량 차이남)
- 시간복잡도가 log로 줄어듭니다

```python
%%timeit
from bisect import bisect_left #이진탐색
bisect_left(data, 99999999) #로그복잡도
# 2.23 µs ± 752 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

- 없는 요소를 검색할 때에는 0을 리턴해줍니다

```python
from bisect import bisect_left

bisect_left(data, -100) # 0
## 없는 요소일 경우 0을 반환합니다.

'''
이진탐색 bisect의 이진탐색 함수
bisect.bisect_left(Sorted_Collection, data)# 첫번째 만나는 data
bisect.bisect_right(Sorted_Collection, data) # 우리가 원하는 요소의 다음 값
bisect.bisect(Sorted_Collection, data) # 우리가 원하는 요소의 다음 값
bisect.insort_left(Sorted_Collection, data)
bisect.insort_right(Sorted_Collection, data)
'''
```

> 단, bisect를 사용하기 위해서는 data 즉 검색할 객체는 정렬된 상태이어야 합니다.
> 실제로는 Sorted_Collection에서 data가 들어갈 위치를 찾는 함수입니다.
> `bisect_left`같은 함수로 위치를 찾고, `insort_left`로 데이터를 추가합니다.

## 클로저를 활용한 환율 변환기로 알아보는 free variable / ??

- 어떤 영역에 속해있지 않은 변수를 `free variable`이라고 하는데, 클로저에서 쉽게 응용할 수 있습니다.
- 지역 범위가 사라져서 바인딩 되지 않은 변수를 `free variable`이라고 합니다.
- `free variable`을 클로저로 생성한 객체들이 공유하지 않습니다.

```python
def changer(country, ratio):
    changed_ratio = [] ## free variables(지역 범위가 사라져서 범위에 바인딩 되지 않은 변수)
    def calculator(won):
        changed_ratio.append(country)
        return f'입력값 : {country}, 반환값 : {format(ratio * won, ",")}원, {changed_ratio}'
    return calculator

dollor = changer('미국', 1300)
print(dollor(100))
#입력값 : 미국, 반환값 : 130,000원, ['미국']

yen = changer('일본', 1100)
print(yen(100))
#입력값 : 일본, 반환값 : 110,000원, ['일본']
```

- 변수들을 확인해보는 코드

```python
# 여기서는 free variable인 changed_raio를 확인할 수 없습니다.
dir(yen)
```

```python
# 여기서는 내부함수 인자인 won이 있음을 확인할 수 있습니다.
yen.__code__.co_varnames
```

```python
# 여기서는 changed_ratio, country, ratio 을 확인할 수 있습니다.
yen.__code__.co_freevars
```

## heapq는 얼마나 빠른가? - TODO

- 일단 heap이 뭔지 좀 공부하고 다시 해야 할듯 합니다.

## Document String(doc string)으로 정확하고 빠르게 개발합시다. (PEP 257)

- PEP 257 전문 (https://www.python.org/dev/peps/pep-0257/)
- 객체를(클래스, 함수, 메서드, 모듈) 설명하는 한 문장을 가장 앞에 배치
- 큰 따옴표
- 예외 발생에 대한 상황과 설명

```python
# docstring 유형
# """ """ : 일반 docstring
# r""" """ : 백슬래쉬 표현
# u""" """ : 유니코드 표현
```

- 한 줄 docstring일 경우 정말로 확실한경우에 사용

```python
## PEP 257 예제
def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root
    if _kos_root: return _kos_root

print(kos_root.__doc__) # Return the pathname of the KOS root directory.
```

- 한줄과 여러줄 출력 차이
- docstring이 작성되었다면 해당 객체 입력 후 `shift + tab`을 누르면 docstring을 볼 수 있습니다.

```python
def 제곱(수):
    """입력된 값을 제곱하는 함수"""
    return 수**2

class SearchTree:
    """
    서비스의 검색속도 개선을 위한 검색 트리
    """
    pass

## 출력
#입력된 값을 제곱하는 함수
#\n    서비스의 검색속도 개선을 위한 검색 트리\n
```

- 다른 파일/모듈의 doctring 확인하기

```python
# hello.py
def helloworld():
    """hello world 출력하는 함수"""
    print('hello world')

# 본문
from hello import helloworld

help(helloworld)

##
# Help on function hellowrold in module hello:
# helloworld()
#    hello world 출력하는 함수
```

## 프로파일링을 통한 코드 최적화 - TODO

- 이 챕터에서 다룰 내용 : 프로파일(https://docs.python.org/ko/3/library/profile.html)
- snakeviz 사용한 보고서 생성(https://jiffyclub.github.io/snakeviz/)

---

> 코드 최적화 방식
> 처리 속도 측정 후 가장 속도 개선이 필요한 부분부터 개선해나가는 것이 좋습니다. 통상 아주 짧은 반복문 등은 개선할 여지가 더이상 없을 가능성이 크니까요.
> 반복문을 사용하지 않고 문제를 해결할 수 있는 방법이 있는지 찾습니다.(zip, map, filter 등을 사용)
> 파이썬의 내장함수를 사용합니다.
> 파이썬의 내장함수보다 빠른 라이브러리가 있는지 찾습니다.
> 전역 변수를 사용하면 느려집니다. 지역변수를 사용하세요. global 사용을 권장하지 않습니다.
> 가비지 컬렉션이 있지만, 사용이 끝난 변수가 원시 객체일 때에는 메모리 영역을 캐시로 유지하는 경우가 있으니 크기가 큰 데이터는 del 키워드를 사용하여 삭제하거나 함수 안에서 사용하여 함수가 끝날 때 삭제되도록 유도합니다.
> numpy나 pandas에서 in-place로 원본을 직접 수정하거나 사본생성을 하는 flatten같은 것은 사본 생성을 안하는 ravel로 대체합니다.

```python
import random
import cProfile

def 문자열거꾸로_재귀함수(s):
    if len(s) == 1:
        return s
    else:
        return 문자열거꾸로_재귀함수(s[1:]) + s[0]

def 문자열거꾸로_슬라이싱(s):
    return s[::-1]

def 문자열거꾸로_반복문(s):
    answer = ''
    for i in s:
        answer = i + answer
    return answer


def test_set():
    s = ''.join([chr(random.randint(97, 122)) for _ in range(2000)])
    문자열거꾸로_재귀함수(s)
    문자열거꾸로_슬라이싱(s)
    문자열거꾸로_반복문(s)

## 테스트할 함수를 cProfile의 run 함수의 인자에 문자열로 전달
# tottime (total time)을 통해 가장 오래 걸리는 부분을 확인할 수 있고, 그 부분부터 수정해나가면 됩니다.
cProfile.run("test_set()")
```

## Cython 으로 C언어의 속도를! - TODO

- 실습 예제가 안됨.. 다른걸로 해보자...

```python
## test.pyx에 함수 정의
def list_append(i):
    return [i for i in range(1, i+1)]

## setup.py 에 작성
from distutils.core import setup
#from setuptools import setup
from Cython.Build import cythonize
setup( ext_modules = cythonize("test.pyx"))
```

> 아래 명령어로 c패키지 생성
> python setup.py build_ext --inplace

```python
#FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2).
# 위 명령어 수행시 에러가 발생한다면
# pyx파일 상단에
#cython: language_level=3
#을 추가해준다.
# 혹은 setup.py에 set에 설정해 주 수 있음.
```

## pypy

- PyPI(파이피아이)와 pypy(파이파이)는 발음에 주의해주세요.
- pypy는 별도의 인터프린터 이므로 개별 설치 해야함
- 속도 면에서 매우 우월하며 jupyter notebook에서 python3가 아닌 pypy로만 코딩할 수 있습니다.(모든 모듈을 지원하진 않습니다.)
- 넘파이도 많은 부분이 파이파이로 실행됩니다.
- cpython보다 속도가 우월합니다.(인터넷 벤치마크 참고해주세요.)
- 실행추적 JIT(Just In Time) 컴파일을 제공하기 때문입니다.
- 연산이 많이 사용되는 프로젝트(OpenGL 등)에 사용하세요.
- 코드 블록으로만 사용도 가능합니다.

> pypy설치 in jupyter notebook
> !apt-get install pypy

> pc에 설치하고자 한다면
> 공식 홈페이지 :https://www.pypy.org/ 에서 설치해야 합니다.
> 설치 후 경로 설정하고, 환경변수 설정도 해주어야 함(윈도우)

## tracemalloc 으로 메모리 누수 원인찾기!

- 인공지능 모듈이나 빅데이터 시각화에서 메모리 추적을 할 필요가 있음
- 예를 들어 데이터 시각화(matplotlib)에서 (시각화 그래프가 매우 늦게 그려지거나 이상하게 그려지는 등의 현상이 나타남) 메모리를 많이 사용하였다면 plt.close(fig) 필요
- garbage collection이 있긴 하지만 수거되지 않는 메모리가 있음!
- python 3.4부터 지원 (이전에는 gc moudle을 사용했는데 이건 어느 모듈마다 메모리 추적이 안됨)

```python
#testfunctions.py
def data():
    return [dict() for _ in range(10000)]

def dataList():
    return [data() for _ in range(1000)]
```

```python
import tracemalloc
import testfunctions

tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()

testfunctions.dataList()

snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)
```

```python
#출력
# [ Top 10 differences ]
# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/_pydevd_bundle/_debug_adapter/pydevd_schema.py:13622: size=4872 B (+4872 B), count=29 (+29), average=168 B

# /content/testfunctions.py:2: size=4808 B (+4808 B), count=71 (+71), average=68 B ##<<< testfunctions.py 모듈에서 쓴 메모리 크기

# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/pydevd.py:1232: size=4632 B (+4632 B), count=1 (+1), average=4632 B
# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/_pydevd_bundle/_debug_adapter/pydevd_schema.py:13674: size=3256 B (+3256 B), count=11 (+11), average=296 B
# /usr/local/lib/python3.10/dist-packages/google/colab/_variable_inspector.py:28: size=2208 B (+2208 B), count=1 (+1), average=2208 B
# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_process_net_command_json.py:171: size=1303 B (+1303 B), count=19 (+19), average=69 B
# /usr/lib/python3.10/json/encoder.py:257: size=1120 B (+1120 B), count=16 (+16), average=70 B
# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_net_command_factory_xml.py:191: size=1064 B (+1064 B), count=35 (+35), average=30 B
# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_comm.py:204: size=1057 B (+1057 B), count=1 (+1), average=1057 B
# /usr/local/lib/python3.10/dist-packages/debugpy/_vendored/pydevd/_pydevd_bundle/_debug_adapter/pydevd_schema.py:13511: size=832 B (+832 B), count=13 (+13), average=64 B
```

## Python의 동작 원리와 `__pycache__`, `__name__`

- 참고문헌 :

  - 러닝 파이썬
  - https://indianpythonista.wordpress.com/2018/01/04/how-python-runs/
  - https://velog.io/@doondoony/How-Python-works

- 소스코드 -> 컴파일 -> 바이트코드(.pyc 파일 생성) -> PVM(Python Virtual Machine, 모듈을 가지고 올 경우 이 단계에서 가지고 옴) -> 소스코드 실행
- Python 3.2 version 이후로는 소스 파일들이 위치한 디렉터리에 `__pycache__` 라는 이름의 하위 디렉터리 안에 자신의 .pyc 파일 생성
- CPython 말고도 Jython, IronPython, Stackless, PyPy 등이 존재. 예를 들어 Jython 같은 경우 파일은 .py로 저장하지만 바이트코드를 JVM으로 실행
- pyc파일을 계속 생성하면 간혹 협업에 문제가 생긴다던지(https://codingexplore.tistory.com/11) 성능상에 이슈가 발생할 수 있습니다. -B 플래그를 사용해서 억제하거나 주기적으로 삭제하는 것이 방법이 될 수 있습니다.

> pyc(pycache) 파일 때문에 충돌이 나는 경우가 있기 때문에 모두 삭제한 후에 push 하고 gitignore 적용해야 합니다.
> 리눅스 명령어인거같은데 `find . | grep -E("__pycache__|\.pyc|\.pyo$)" | xargs rm -rf` 으로 삭제 가능

- pycahe!

```python
#test.py
def 출력():
    l = [i for i in range(10000)]
    print(__name__)
    return
```

```python
import test

test.출력() ## __name__을 출력했지만 모듈이름 test가 출력됨

print(__name__) ## "__main__" 이 출력됨

if __name__ == "__main__":
    #실행할 코드
    # 해당 파일을 실행하는 주체가 이 파일이면 실행함.
    # 모듈로 임포트된 상황에서는 실행하지 않습니다.
    pass
```

## 메모리 누수 방지를 위한 contextlib 의 closing

- 참고문헌 :
  - https://docs.python.org/ko/3/library/contextlib.html
  - https://wikidocs.net/16079
  - https://sjquant.tistory.com/12

```python
from contextlib import closing
from urllib.request import urlopen

## page를 강제로 닫아 줄 필요가 없습니다.
#python 홈페이지의 페이지를 가져오는 기능
with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)
```

```python
# contextmanager의 구성
# 끝날 때 강제로 close()라는 함수를 호출하게 합니다.
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```

```python
class startCloseClass():

    def start(self):
        print("인스턴스 실행")

    def close(self):
        print("인스턴스 종료")


ins = startCloseClass()
ins.start()
ins.close()
```

```python
from contextlib import closing

with closing(startCloseClass()) as ins:
    ins.start()

# close()함수를 호출하지 않았지만, with 구문을 나올 때 ins의 close()메서드를 호출합니다.
```

## slots를 이용한 class의 효율 높이기!

- 클래스에 slots을 설정할 경우 `__dict__`를 생성하지 않음으로 메모리 개선
- dict와 유사하거나 좀 더 축소화된 자료형을 만들어서 사용될 때 자주 사용됨
- dictionary는 메모리 효율이 좋지 않기 때문..(대신 시간효율이 좋은 자료형)

### python_grammar 폴더의 class.md 에 정리된 내용 있음

### 테스트 항목

```python
테스트_기본_리스트 = [list() for i in range(10000)]
테스트_작성한_리스트 = [LinkedList() for i in range(10000)]
테스트_slot_반영_리스트 = [LinkedList() for i in range(10000)]
```

- 일반 LikedList와 `__slots__` 정의한 LinkedList

```python
## LikedList와
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.현재노드 = None
        self.데이터수 = 0

    def __str__(self):

        현재노드 = self.head
        현재노드 = 현재노드.next
        s = ''

        for i in range(self.데이터수):
            s += f'{현재노드.data}, '
            현재노드 = 현재노드.next

        return f'[{s[:-2]}]'

    def append(self, data):
        새로운노드 = Node(data)
        self.tail.next = 새로운노드
        self.tail = 새로운노드
        self.데이터수 += 1

## slots 선언된 LikedList
class Node_slot:
    __slots__ = ['data', 'next']
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList_slot:
    __slots__ = ['head', 'tail', '현재노드', '데이터수']

    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.현재노드 = None
        self.데이터수 = 0

    def __str__(self):

        현재노드 = self.head
        현재노드 = 현재노드.next
        s = ''

        for i in range(self.데이터수):
            s += f'{현재노드.data}, '
            현재노드 = 현재노드.next

        return f'[{s[:-2]}]'

    def append(self, data):
        새로운노드 = Node(data)
        self.tail.next = 새로운노드
        self.tail = 새로운노드
        self.데이터수 += 1

```

1. 기본 리스트의 효율

```python
%%timeit

basic_list = [list() for i in range(1_000_000)]
## 177 ms ± 29.6 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

2. 클래스로 만든 Linked List의 효율

```python
%%timeit

Linked_class = [LinkedList() for i in range(1_000_000)]
## The slowest run took 4.24 times longer than the fastest. This could mean that an intermediate result is being cached.
## 1.47 s ± 873 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

3. slots 정의한 Linked List의 효율

```python
%%timeit

Linked_slots = [LinkedList_slot() for i in range(1_000_000)]
## 676 ms ± 259 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

##Linked_slots.__dict__ 가 없습니다.
```

> 속도는 basic list > slots LinkedList > LikedList
> 확실히 클래스를 만든다면, slots로 변수를 제한해 주는 것(`__dict__`를 생성하지 않는 것)이 효율적으로 유리합니다.

## tqdm 을 이용한 진행바 만들기 & yaml (야믈) 파일 다운로드

- 프로그래스 바를 그려주는 `tqdm` 모듈
- `tqdm`모듈의 `tqdm()`메서드를 for문으로 순회하여 진행률을 확인할 수 있습니다.

```python
from tqdm import tqdm
import time

s = ""
for c in tqdm(['h', 'e', 'l', 'l', 'o']):
    s += c
    time.sleep(1) ## 시간을 두어야 천천히 올라가는거 보이니깐!

print(s)
```

- tqdm 함수에 iterable, 표현할 단어, 표현할 초소단위를 설정할 수 있습니다.

```python
s  = 0
# 0/10 에서 10/10, 표현될 단어 "진행율", 1/10 *2 단위만큼 지날 때마다 표현됨
for i in tqdm(range(1, 11), desc="진행율", mininterval=2):
    s += i
    time.sleep(1) ## 시간을 두어야 천천히 올라가는거 보이니깐!

print(s)
#진행율: 100%|██████████| 10/10 [00:10<00:00,  1.00s/it]55
```

- yaml(야믈)파읽 읽는 패키지 `yaml` 사용방법
- 코랩에서 yaml.load(text)는 에러날 수 있기 때문에 아래 주석으로 단 방법으로 에러를 해결하면 됩니다.

```python
## 야믈파일 읽기
import yaml

with open('test.yaml', 'r') as f:
    text = f.read()

# TypeError: load() missing 1 required positional argument: 'Loader'
# import yaml 후 yaml.load()를 사용하면 해당 에러를 만날 수 있다.
#### 방안
# 1. 버전 변경
# 버전을 강제로 변경해준다.
# !pip install pyyaml==5.4.1

# 2. 다른 함수 사용
# 버전을 변경하기 싫다면, load() 대신 full_load()를 사용한다.
####

# data = yaml.load(text)
data = yaml.full_load(text)
print(data)
## 파이썬에 맞게 변경이 됨!
# {'name': {'first': 'hojun', 'last': 'lee'}, 'company': {'name': 'weniv', '법인': True, '직원': ['하나', '둘', '셋']}}

data['company']['직원'][0]

## test.yaml
# name:
#     first: hojun
#     last: lee
# company:
#     name: weniv
#     법인: true
#     직원: [하나, 둘, 셋]
```
