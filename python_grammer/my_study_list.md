# 문법체크

- 배열의 합, 평균
- Buitin function: sum 함수, len 함수
- 다차원 배열(list)의 합은 numpy.sum 사용

- 배열에서 중복된 원소 개수

  - array.count(원소)
  - collections의 Counter 사용

  ```python
  from collections import Counter
  array = [1,1,2,3,4,2,1,2,1,1,1,5,2,3]
  Counter(array).get(1)
  ```

- 배열 뒤집기

  - 인덱싱 사용하기 [::-1]

  ```python
  my_list = [1,2,3,4,5]
  print(my_list[::-1])
  # [5,4,3,2,1]
  ```

  - list내장 메소드 reverse() 사용

- 3항 연산 문법

  - A if 조건a else B if 조건b else C

- 문자열 다루기
  - 문자열 뒤집기
    1. 인덱싱
    2. list로 변경 후 reversed 사용
    ```python
    mystring = "hello world!"
    ''.join(reversed(list(mystring)))
    ```
  - 문자열 중 문자열 찾기
    - string 의 find() 함수 사용
    - in 문구 사용 (return은 bool type으로 됨)

---

## Built in function : map()

> 함수 형태 : map(function, iterable, \*iterables)

- 첫 번째 매개변수는 iterable의 원소에 각각 적용할 function
  - lambda 로 처리하는 경우가 많습니다.
- 두 번째 매개변수는 반복 가능한 자료형(리스트, 튜플 등)
- 세 번째 인자는 가변인자로 function에 2개 이상의 인자가 필요할 때 사용함
- return 값

  - map object --> list 혹은 tuple로 변환시켜주어야 함
  - map object는 iterator입니다.
  - map object 상태에서는 print() 과 같은 함수로 값을 확인할 수 없음
  - 새로운 iterable 오브젝트가 생성됨(yielding)

- map 예제

  ```python
  ## map 없이 원소 두 배 만들기
  a = [1,2,3,4,5]

  for index in range(0,len(a)):
      a[index]*=2

  # 혹은
  for index, value in enumerate(a):
      a[index]*=2

  print(a) # [2, 4, 6, 8, 10]
  ```

  ```python
  ## map을 이용해 두 배 만들기
  a = [1,2,3,4,5]
  a = list(map(lambda x: x*2, a))

  # map 출력방법
  print(a) # [2, 4, 6, 8, 10]

  # return 인 map object가 iterable 이라서 for문 적용 가능
  for element in a:
    print(element)
  ```

  ```python
  a = [1,2,3]
  b = [4,5,6]
  map_res = map(lambda x, y: x+y*10, a, b) # 세 번째 인자 사용
  print(list(map_res)) #[41,52,63]
  ```

- map을 이용한 형변환

  ```python
  a = [1.1, 2.1, 3.1]
  b = list(map(int,a))

  print(b) # [1,2,3]
  ```

- map object의 값을 출력하는 방법

```python
a = [1,2,3,4,5]
b = map(lambda x: x*2, a) #a 원소를 각 2배한 리스트
#b 는 map object로 print() 함수로 값을 확인할 수 없음!

#출력하기
for i in b:
    print(i, end=" ") # 2 4 6 8 10
#혹은 next 함수 사용하기
print(next(b)) # 2
print(next(b)) # 4
print(next(b)) # 6
print(next(b)) # 8
print(next(b)) # 10
print(next(b)) # StopIteration Error -> map object가 더 보여줄 원소가 없음

#혹은 원소마다 하나씩 값을 받아두면 바로 출력할 수 있음
a1, a2, a3, a4, a5 = map(lambda x: x*2, a)
```

### map 객체

- map 함수의 return type이고, iterator 입니다.
- type(map object) : <class 'map'>
- dir(map object)<br/>
  ```python
  # '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
  ```

## Built in Function : filter() 함수

> 함수 형태 : map(function, iterable)

- 첫 번째 매개변수는 iterable의 원소에 각각 적용할 function
  - lambda 로 처리하는 경우가 많습니다.
  - fucntion 은 반드시 조건을 가르는 함수이어야 합니다. 조건에 True인 요소만 걸러짐
- 두 번째 매개변수는 반복 가능한 자료형(리스트, 튜플 등)
- return 값

  - filter object --> list 혹은 tuple로 변환시켜주어야 함
  - filter object는 iterator입니다.
  - filter object 상태에서는 print() 과 같은 함수로 값을 확인할 수 없음
  - 새로운 iterable 오브젝트가 생성됨(yielding)

- filter 함수 예제

```python
  ## map을 이용해 두 배 만들기
  a = [1,2,3,4,5,6,7,8,9,10]
  b = list(filter(lambda x: x%2==0, a))

  # map 출력방법
  print(b) # [2, 4, 6, 8, 10]

  # return 인 map object가 iterable 이라서 for문 적용 가능
  for element in b:
    print(element)
```

- filter 이용 방법. iterable 객체에서 원하는 조건을 가진 원소만 뽑아온다.

  ```python
  #예제 1
  a = [1.1, 5, 2.1, 3, 3.1, 7, 100, 845.1]
  b = list(filter(lambda x: x==int(x), a))

  print(b) # [5, 3, 7, 100]

  #예제 2
  s = "hello 33w55orld my n8a9m99e is jinsoo"
  b = list(filter(lambda x: x.isdigit(), s))

  print (b) # ['3', '3', '5', '5', '8', '9', '9', '9']
  ```

- filter object의 값을 출력하는 방법

```python
a = [1,2,3,4,5,6,7,8,9,10]
b = map(lambda x: x%2, a) #a 원소를 각 2배한 리스트
#b 는 map object로 print() 함수로 값을 확인할 수 없음!

#출력하기. __next__ 가 있기 때문에 next() 가능
for i in b:
    print(i, end=" ") # 2 4 6 8 10
#혹은 next 함수 사용하기
print(next(b)) # 2
print(next(b)) # 4
print(next(b)) # 6
print(next(b)) # 8
print(next(b)) # 10
print(next(b)) # StopIteration Error -> map object가 더 보여줄 원소가 없음

#혹은 원소마다 하나씩 값을 받아두면 바로 출력할 수 있음
a1, a2, a3, a4, a5 = map(lambda x: x*2, a)
```

### filter 객체

- filter 함수의 return type이고, iterator 입니다.
- type(filter object) : <class 'filter'>
- dir(filter object)<br/>
  ```python
  #['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
  ```

## Built in Function : ord(), chr() 함수

- chr(i)

  - 인자 정수 i 에 상응하는 유니코드 문자를 반환한다.
  - 유효한 i 범위는 0~ 1,113,111 (0x10FFFF) <br/> 범위 넘어가면 ValueError 발생

- ord(c)

  - 인자인 문자 c 에 상응하는 유니코드 숫자 정수를 반환한다.

- chr과 ord 는 inverse 관계입니다.

  ```python
  print(chr(97))  # a
  print(chr(8364)) # €
  print(ord('a')) # 97
  print(ord('€')) # 8364
  ```

## Built in Function : isinstance()

> 함수 형태 : isinstance(object, classinfo)

- 첫 번째 인자 : 특정 클래스의 인스턴스인지 확인할 object
- 두 번째 인자 : object의 타입을 판별할 class
- object가 classinfo의 인스턴스일 때 True, 아니면 False 를 return <br>정확히는 direct, indirect 또는 virtual subclass일때
- 요약 : object가 classinfo 객체인지 확인하는 빌트인 함수

- 예제

```python
# 정수인지 확인
res = isinstance(100, int)
print(res)  #true

# 실수인지 확인
res = isinstance(100, float)
print(res)  #false

# 문자열인지 확인
res = isinstance('is instance??', str)
print(res)  #true

# 리스트인지 확인
res = isinstance([1,2,3], list)
print(res)  #true

# 해당 클래스의 인스턴스인지 확인1
class Myclass:
    pass

mc = Myclass()
res = isinstance(mc, Myclass)
print(res)  #true

```

- 한 object에 대해 여러 클래스인지 확인이 가능

```python
# 판단하고 싶은 종류의 class를 tuple로 넘겨줌
# 전달한 tuple 중 1 개만 맞으면 True
res = isinstance(10.1, (int, float, str))
print(res)  #true
res = isinstance([1,2,3], (int, float, str))
print(res)  #false
```

- 특수한 경우 : bool class 는 int 클래스로 인식된다.
-

```python
# bool 타입은 int타입으로인식됨.
# 그렇다면 bool 클래스는 int를 상속받았다고 생각할 수 있을 것 같다.
# 그런데 진짜로 상속받았음
# builtins.pyi 파일 확인결과 아래와 같이 확인했다
'''
@final
class bool(int):
    def __new__(cls, __o: object = ...) -> Self: ...
    # The following overloads could be represented more elegantly with a TypeVar("_B", bool, int),
    # however mypy has a bug regarding TypeVar constraints (https://github.com/python/mypy/issues/11880).
'''

isinstance(True, int)   # True
isinstance(10, int)     # True
isinstance(10., int)    # False
isinstance(10.1, int)   # False

isinstance(True, float) # False
isinstance(10, float)   # False
isinstance(10., float)  # True
isinstance(10.1, float) # True

```

- 상속 관계에서 자식 클래스의 object인 경우 True를 반환(반대의 경우는 False)

```python
class Parent:
  pass

class Driven(Parent):
  pass

p = Parent()
d = Driven()

res = isinstance(d, Parnet)
print(res)  #True

res = isinstance(p, Driven)
print(res)  #False
```

- [참고](https://blockdmask.tistory.com/536)

## Built in Function : zip()

> 함수 형태 : zip(\*iterables, strict=False)

- iterable 객체들을 같은 인덱스에 있는 값 끼리 tuple로 묶어서 zip object로 return 함
- iterable의 길이가 짧은 것을 기준으로 짝지어주고 남는 요소들은 버려진다. (strict=False)
- return 값은 zip object

```python
li = [1,2,3]
st = ['VScode', 'Pycharm', 'Jupyter notebook']

z = zip(li, st)

print(z)
print(type(z))

list(z)[0]      # 이후에 z는 있지만 모든 원소가 사라져 비어있게됨 >> map object도 마찬가지!
print(z)        # 같은 객체 z 있기는 하지만....
tmp= list(z)
print(tmp)      # [] 빈 리스트.

# zip한 것을 list 변수로 저장한다음에 써야 함
tmp2 = list(zip(li, st))
print(tmp2)     # [(1, 'VScode'), (2, 'Pycharm'), (3, 'Jupyter notebook')]

#str
```

```python
li = [1,2,3]
st = [10, 20, 30, 40]

# 길이가 다른 두 리스트의 경우 짧은 것을 기준으로 남는 원소는 무시
z = zip(li,st)
print(list(z))

## zip object의 출력방식
## __iter__ atribute를 가지고 있으므로 next() 사용 가능
## list, dict로 형변환할 수 있음
z = zip(li,st)
print(next(z))
print(next(z))
print(next(z))

```

- strict는 디폴트로 False를 가지고 있다
- strict 를 True로 하면 iterable 객체의 길이가 동일하지 않으면 Error를 뱉음

```python
# 에러나는 코드
# zip 함수를 수행할 때에는 에러가 나지 않지만 접근하려고하면 에러 발생
li = [1,2,3]
st = [10, 20, 30, 40]
z = zip(li,st, strict=True)
print(list(z)) ## ValueError: zip() argument 2 is longer than argument 1

```

- zip()을 활용하여 컨벤션 객체를 생성할 수 있다

```python

# 짝짓는 것이므로 dictionary 만들기 편리하다
d = dict(zip('abcd',[1,2,3,4]))
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# list의 경우 tuple을 원소로 가지게 된다.
l = list(zip('abcd',(1,2,3,4)))
print(l)  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(type(l[0])) # <class 'tuple'>

t = tuple(zip('abcd',(1,2,3,4)))
print(t)  # (('a', 1), ('b', 2), ('c', 3), ('d', 4))
print(type(t[0])) # <class 'tuple'>

s = set(zip('abcd',(1,2,3,4)))
print(s)  # {('a', 1), ('c', 3), ('b', 2), ('d', 4)}
('a', 1) in s # True
```

## map object, zip object 등의 값을 참조하면 바로 사라지는 이유

- 비어있는 이유는 한 번 next가 되면 되돌아가지 못하기 때문입니다.
- 즉, 한 번 앞으로 가면 뒤로 되돌아가지 못해서 object가 비어있는 것입니다.
- 한 번 순회가 끝나면 메모리를 비우기 때문에 그렇습니다. 순회가 끝나면 다시 앞으로 되돌아가지 않아요.
- zip/map 함수 객체가 한 번 호출되서 값을 읽으면 모든 요소를 반환하고 iterator가 소멸됩니다.
  <br>따라서, 객체를 다시 사용하려면 새로운 iterator를 다시 생성해야 합니다.
- iterator는 소멸하지만 object 자체 변수의 메모리 값은 유지됩니다.
- 제너레이터를 한 번 만들어보시면 이해가 되실겁니다. 클래스에 `__iter__`도 관련이 있습니다.

> map object, zip object, range object 등등..

```python
li = [1,2,3]
st = ['VScode', 'Pycharm', 'Jupyter notebook']

z = zip(li, st)

print(z)
print(type(z))

list(z)[0]      # 이후에 z는 있지만 모든 원소가 사라져 비어있게됨 >> map object도 마찬가지!
print(z)        # 같은 객체 z 있기는 하지만....
tmp= list(z)
print(tmp)      # [] 빈 리스트.
```

- 아래 예제와 같이 한 번만 출력되는 것을 확인할 수 있습니다

```python
li = [1,2,3]
st = ['VScode', 'Pycharm', 'Jupyter notebook']
z = zip(li, st)

for i in z:
    print(i)

for i in z:
    print(i)
```

## Built in Function : sorted()

> 함수 형태 : sorted(iterable, /, key=None, reverse=False)

- iterbale 객체가 정렬된 **새로운 list object**를 리턴한다. (list의 sort() 는 본인을 바꿈)
- key 옵션 (key 파라메터): 어떤 기준으로 정렬할 것인가
- reverse 옵션 (reverse 파라메터): True : 오름차순, False : 내림차순

```python

li = [1,50,5,7,-5,100,3,76]

a = sorted(li)
b = sorted(li, reverse=True)

print(li)   # [1, 50, 5, 7, -5, 100, 3, 76]
print(a)    # [-5, 1, 3, 5, 7, 50, 76, 100]
print(b)    # [100, 76, 50, 7, 5, 3, 1, -5]
print(f'li:{id(li)}, a:{id(a)}, b:{id(b)}') # 모두 다른 객체

```

- key 파라메터 활용

```python
fee = [7700, 2300, 1200, 3500, 4700, 5500]
bus = ['a', 'b', 'c', 'd', 'e', 'f']

d = dict(zip(bus, fee))

# 각각 정렬해보기
li_items = sorted(d.items()) # dict.items()는 key-value를 tuple로 리턴
# [('a', 7700), ('b', 2300), ('c', 1200), ('d', 3500), ('e', 4700), ('f', 5500)]

li_keys = sorted(d.keys())
li_values = sorted(d.values())

print(li_items)
print(li_keys)
print(li_values)

# value 기준으로 item을 정렬하기
li_item_val = sorted(d.items(), key=lambda x: x[1])
li_item_val_rev = sorted(d.items(), key=lambda x: x[1], reverse=True)

print(li_item_val)
print(li_item_val_rev)
# [('c', 1200), ('b', 2300), ('d', 3500), ('e', 4700), ('f', 5500), ('a', 7700)]
# [('a', 7700), ('f', 5500), ('e', 4700), ('d', 3500), ('b', 2300), ('c', 1200)]
```

- `sorted()` 활용하기
- 정렬기준 key에 (우선조건, 다음조건) 등로 여러 조건을 넣을 수 있습니다

```python
# n에서 가장 거리가 먼 요소를 출력해보자
array = [3, 10, 25, 28, 15]
n = 20

# 정렬되는 값은 array의 요소들
# 기준은 거리이기 때문에 abs(x-n)을 기준으로 정렬한다. >> 이거만 하면 [25, 15, ...]
# 조건에 거리가 같다면 더 작은수가 앞으로 배치되어야 하기 때문에 두 번째 요소로 x-n 을 넣어준다.
print(sorted(array, key=lambda x: (abs(x-n), x-n)))
print(sorted(array, key=lambda x: (abs(x-n), x-n))[0])
```

## Built in Function : locals()

- 현재 스코프(scope)의 지역변수들을 리턴해준다.
- Return 값은 dictionary({str : str}) 타입으로 반환됨 <br/> '변수명': '값'

```python
class Myclass:
    pass

class_a = Myclass()

def outer():
    first_a = 10

    def inner():
        second_a = '10'
        print(locals())         # {'second_a': '10'}
        print(type(locals()))   # <class 'dict'>

    inner()
    print(locals())     # {'first_a': 10, 'inner': <function outer.<locals>.inner at 0x7fb91ddd0280>}

outer()

print(locals())         ## __main__이라는 scope 이름과 함께 정의한 함수, 클래스 등 내부의 모든 내용이 출력됨.
                        # Automatically created module for IPython interactive environment

```

## Built in Function : enumerate()

> 함수 형태 : enumerate(iterable, start=0)

- for문이나 iterable한 객체의 순서를 함께 확인하고 싶을 때 사용하는 내장 함수
- enumerate object를 리턴함
- `__next__()`메서드는 tuple을 리턴함
- 예제

```python
li = ['spring', 'summer', 'fall', 'winter']
print(list(enumerate(li)))      # [(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]
print(list(enumerate(li, 10)))  # [(10, 'spring'), (11, 'summer'), (12, 'fall'), (13, 'winter')]

for i in enumerate(li):
  print(i)

# tuple
# (0, 'spring')
# (1, 'summer')
# (2, 'fall')
# (3, 'winter')

for i, j in enumerate(li, 5):
  print(i, j) # unpacking

# 5 spring
# 6 summer
# 7 fall
# 8 winter

```

## Built in Function : hasattr()

> 함수형식 : hasattr(object, name)

- name 파라메터는 `str` 타입을 넣어줘야 한다
- object가 name의 attribute를 가지고 있으면 `True` 아니면 `False`를 리턴함
- 오브젝트가의 멤버 변수가 있는지 확인
- 사실 `dir()`메서드로 확인해볼 수 있음!

```python
li = [1,2,3]
print(hasattr(li, '__iter__'))  # True
print(hasattr(li, '__add__'))  # True

d = {'one': 1, 'two':2}
print(hasattr(d, '__iter__'))   # True
print(hasattr(d, '__add__'))    # False

```

## Built in Function : getattr()

> 함수양식 : getattr(object, name, default)

- 오브젝트에서 name에 해당하는 값을 리턴. 없다면 default를 리턴

## Built in Function : setattr()

> 함수양식 : setattr(object, name, value)

- 오브젝트에 name에 해당하는 변수를 생성해서 값을 할당 (이미 있다면 값을 수정)

## Built in Function : delattr()

> 함수양식 : delattr(object, name)

- 오브젝트에 name에 해당하는 변수를 제거

## bytes와 bytearray (클래스)

- byte 단위의 자료를 다룰 때 사용할 수 있습니다.
- 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형입니다.
- byte 단위이므로 iterable 객체의 값이 255를 넘는 순간 에러가 발생합니다.

- bytes 객체 생성하기

```python
# bytes 오브젝트 생성
byte_obj = bytes()
print(byte_obj) # b''

byte_obj = "hello world!".encode()
print(byte_obj) # b'hello world!'

byte_obj = b"hello world!"
print(byte_obj) # b'hello world!'

byte_obj = bytes(5)
print(byte_obj) # b'\x00\x00\x00\x00\x00'

byte_obj = bytes('abced', encoding='UTF-8') # encoding은 대문자로 써줘야하나봄..
print(byte_obj) # b'abced'

byte_obj = bytes('인사', encoding='UTF-8')
print(byte_obj) # b'\xec\x9d\xb8\xec\x82\xac'

byte_obj = bytes([1, 2, 3])
print(byte_obj) # b'\x01\x02\x03'

byte_obj = bytes(range(4))
print(byte_obj) # b'\x00\x01\x02\x03'

# byte_obj = bytes([1000, 2000, 3000]) ## ValueError: bytes must be in range(0, 256)
```

- bytes 객체 해독? 하기
- bytes 객체를 str문자열로 바꿔주는 `decode()` 메서드를 사용합니다.
  > decode(인코딩이름 = 'ascii')

```python
res = b'abcde'.decode()
print(type(res))
print(res)
# <class 'str'>
# abcde
res = b'abcde'.decode('utf-8')
print(type(res))
print(res)
# <class 'str'>
# abcde
res = bytes([65, 66, 67]).decode()
print(type(res))
print(res)
# <class 'str'>
# ABC
```

- bytearray 객체 생성, 해독 및 수정하기

```python
# obj = bytearray('hello') # error

obj = bytearray('hello', encoding='ascii')
print(obj)
obj = bytearray(b'hello')
print(obj)

obj[0] = ord('A') # array의 값 수정이 가능합니다
print(obj)
print(obj.decode()) # 해석하기

obj.append(ord('!'))
print(obj)
obj.pop() # pop 함수를 list같은 iterable과 같이 사용할 수 있습니다.
print(obj)
obj.pop(0)
print(obj)
```

> bytes와 bytearay의 차이점
> bytes는 요소를 변경할 수 없지만 bytearray는 요소를 변경할 수 있습니다.
