# lv0 문법체크

- 배열의 합, 평균

  - sum 함수, len ㅎ마수
  - 다차원 배열의 합은 numpy.sum 사용

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

- map 함수 공부하기

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

## map 함수

---

- 함수 형태 : map(function, iterable)
- 첫 번째 매개변수는 function
- 두 번째 매개변수는 반복 가능한 자료형(리스트, 튜플)
- return 값은 map object --> list 혹은 tuple로 변환시켜주어야 함. map object 상태에서는 print() 과 같은 함수로 값을 확인할 수 없음

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

  print(a) # [2, 4, 6, 8, 10]
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

- type(map object) : <class 'map'>
- dir(map object)<br/>
  ```python
  # '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
  ```

## Python Collections 모듈

- to be continue...

## lambda 함수!
