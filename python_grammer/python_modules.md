# re 모듈 (정규표현식)

## 공식문서

- python 3.11.3 에서의 정규표현식 HOWTO
- https://docs.python.org/ko/3/howto/regex.html

## 정규표현식(Regular Expressions)

- 복잡한 문자열을 처리할 때 사용하는 기법
- 파이썬만의 고유 문법이 아니라 모든 곳에서 사용

## 정규표현식의 필요성

- 문자열 처리 방식으로 했을 때 처리가 어려운 경우에도 간편하고 직관적으로 코드를 작성할 수 있다
- 찾으려는 문자여 ㄹ또는 바꿔야 할 문자열의 규칙이 복잡할수록 정규표현식의 효용성이 더욱 커진다.
- 예제<br>

## 메타문자

- 정규표현식의 기초
- 정규 표현식에서는 메타문를 사용하면 의미를 갖게 된다

> 메타문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자

```python
. ^ $ * ? { } [ ] \ | ( )
```

### 문자 클래스 [ ]

## 정규식을 이용한 문자열 검색

    -

---

# Collections 모듈

## collections.defaultdict

- dict 클래스의 subclass
- collections 라이브러리에 탑재되어 있는 defaultdict는 딕셔너리(dict)와 거의 똑같은 용법으로 사용할 수 있습니다.
- 다른 점은 없는 키로 접근을 해도 KeyError를 일으키지 않고 초기 값(default value)를 내뱉는다는 데 있습니다.
- 초기값은 따로 설정할 수 있습니다.

- 예제

```python
from collections import defaultdict
default_dict = defaultdict(int) # 초기값을 설정해줌
print(type(default_dict))
print(default_dict)         # defaultdict(<class 'int'>, {})

# 없는 키를 조회하면 원소가 추가됨
default_dict['key1']

# int 클래스의 기본 값인 0이 자동으로 들어감
print(default_dict)        # defaultdict(<class 'int'>, {'key1': 0})

# get함수는 조회만 하고 없는 키를 호출해도 생성되지는 않음
default_dict.get('hi')
print(default_dict)         # defaultdict(<class 'int'>, {'key1': 0})

default_dict['key2']
print(default_dict)         # defaultdict(<class 'int'>, {'key1': 0, 'key2': 0})

```

- 활용방법

```python
# 기본값으로 컨벤션 타입으로 지정할 수 있음
from collections import defaultdict
ddict = defaultdict(list) # 초기값을 설정해줌
print(ddict)    # defaultdict(<class 'list'>, {})

# 원소가 리스트이면 같은 key 값에 여러 value를 넣을 수 있게 된다.
l = [('A',123),('B', 45),('C', 6),('A',78),('B',9)]
for k, v in l:
    ddict[k].append(v)

# 없는 key더라도 에러발생하지 않고 생성해서 값을 넣어준다.

print(ddict)    # defaultdict(<class 'list'>, {'A': [123, 78], 'B': [45, 9], 'C': [6]})
```

- to be continue...

---

# itertools 모듈

## itertools.chain()

> 함수 형태 : itertools.chain(\*iterables)

- 첫 번째 이터러러블 객체가 끝날 원소를 반환하고 다음 이터러블로 넘어감
- iterables의 모든 이터러블이 소진될 때까지 진행하는 이터레이터를 만듭니다
- 여러 시퀀스를 단일 시퀀스처럼 처리하는 데 사용됩니다.

- 예제: 한 차원의 iterable만 함(2차원 배열의 경우 list채로 출력)

```python
import itertools

a = itertools.chain([1,2,3], ['AB'], 'hello@world!')

for i in a:
    print(i, end=' ')
# 1 2 3 AB h e l l o @ w o r l d !

print()
aa = itertools.chain([1,2,[10,20,30]],"ABC",(10.2, 22.2))
# 1단계 iterable 까지만 그대로 출력함
for i in aa:
    print(i, end=' ')

# 1 2 [10, 20, 30] A B C 10.2 22.2

```

# functools 모듈
