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
