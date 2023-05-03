# lv0 문법체크

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

  - A if 조건 else B if 조건 else C

- ~~map 함수 공부하기 >> 밑에 정리됨~~

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

## Built in function : map

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

## Built in Function : filter 함수

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

## Built in Function : locals()
