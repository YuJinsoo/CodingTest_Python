# Index

- dataclasses
- 왈러스 연산자
- f-string
- docstring
- 컴프리헨션
- 제너레이터, 이터레이터
- collections 모듈
- 함수형 프로그래밍
- 객체지향 심화
- 모듈과 패키지


🧐 Python 출시 연도입니다. 여러분이 만약 2019년 이전에 나온 책을 보았다면 왈러스 연산자를 모르는 것이 당연합니다. 최신의 책(가능하면 인지도 있는 개정판 책)으로 공부하시는 것을 권해드립니다.

- Python 3.0: 2008년 12월
- Python 3.1: 2009년 6월
- Python 3.2: 2011년 2월
- Python 3.3: 2012년 9월
- Python 3.4: 2014년 3월
- Python 3.5: 2015년 9월
- Python 3.6: 2016년 12월
- Python 3.7: 2018년 6월
- Python 3.8: 2019년 10월
- Python 3.9: 2020년 10월


## dataclasses


```python
#dataclasses


# id, name, email이 각각 3번씩 반복
# -> 이러한 현상을  보일러 플레이트(boiler-plate)라 함
# -> print를 해도 필드값이 보이지 않아 불편
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
```


```python
# id, name, email이 각각 3번씩 반복
# -> 이러한 현상을  보일러 플레이트(boiler-plate)라 함
# -> print를 해도 필드값이 보이지 않아 불편
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return (f'{self.__class__.__qualname__}{self.id, self.name, self.email}')

user = User(123, 'hojun', 'hojun@gmail')
user
# User(123, 'hojun', 'hojun@gmail')

```


```python
## 이런걸 간단히 하기 하기위해 나온데 dataclasses
# 위 클래스에 매직메서드 하는것들을 구현해줌
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email : str

user = User(123, 'hojun', 'hojun@gmail')
user
```




    User(id=123, name='hojun', email='hojun@gmail')




```python
# 딕셔너리 결합연산자
x = {"key1": "value1"}
y = {"key2": "value2"}
z = x | y
z
```




    {'key1': 'value1', 'key2': 'value2'}




```python
# dict 합칠 때 이런거 쓰거나
x.update(y)
print(x)
#JSON 형태에서는 + 연산자를 이런식으로 해서 dict로 만들어주느 ㄴ경우가 있었ㅇㅅ빈다.
list(x.items()) + list(y.items())
```

    {'key1': 'value1', 'key2': 'value2'}





    [('key1', 'value1'), ('key2', 'value2'), ('key2', 'value2')]



## 왈러스 연산자

- Python 3.8에서 도입된 왈러스 연산자( := )는 할당 표현식(assignment expressions)를 사용하게 해주는 연산자입니다.
- 이 연산자는 "이름을 표현식의 결과에 연결"하거나 "값을 이름에 할당하면서 그 값을 평가"합니다. 이 기능은 표현식을 계산하면서 동시에 그 결과를 변수에 할당할 수 있게 해줍니다.


```python
# 기본적인 왈러스 연산자의 사용
# 할당과 동시에 그 값을 활용할 수 있게 해주는 연산자
x = (n := 10) * 2
print(x)  # 출력: 20
print(n)  # 출력: 10
```

    20
    10



```python
# 왈러스 연산자가 없을 때의 코드
import random
while True:
    x = random.randint(0, 10)
    if x == 7:
        break
    print(x)

# 왈러스 연산자를 사용한 코드
import random
while (x := random.randint(0, 10)) != 7:
    print(x)
```


```python
# 왈러스 예제
count = 0
s = 0
while count <= 10:
    s += count
    count += 1
print(s)
```

    55



```python
count = 0
s = 0
while (count := count+1) <= 10:
    s += count
print(s)
```

    55


## f-string 문법

- f-string은 Python 3.6에서 도입된 새로운 문자열 포매팅 방법입니다. f-string은 Formatted String Literals의 줄임말로, 문자열 내에 {}를 사용하여 변수나 표현식을 직접 삽입할 수 있습니다.


```python
# f-string
# 아래 문법들은 정규표현식에서 자주 사요합니다.

# 중괄호를 표현하고 싶을 때
print(f'{{1,2,3}}')

## 중괄호 세 개라면?
# 안에 있는 1, 2, 3 을 Tuple (1,2,3)으로 판단
f'{{{1,2,3}}}'
```

    {1,2,3}





    '{(1, 2, 3)}'




```python
one = 1
two =2
three = 3

f'{{{one}}}'
```




    '{1}'



## docstring


Python에서 독스트링(documentation strings)은 함수, 클래스, 모듈 등의 주석을 작성하는 표준 방법입니다. 독스트링은 삼중 따옴표로 둘러싸인 문자열로, 정의된 항목 바로 아래에 나타나야 합니다.

Python 공식 스타일 가이드인 PEP 257은 독스트링 작성을 위한 일반적인 가이드라인을 제시하고 있지만, 회사나 팀별로는 이를 더욱 세분화하거나 구체화한 자체 컨벤션을 가지고 있을 수 있습니다. 따라서 회사의 특정 컨벤션에 대한 자세한 정보는 해당 컨벤션을 관리하고 있는 문서나 기술 리드에게 직접 문의해야 합니다.

1. **일반적인 형식**: 독스트링은 항상 삼중 따옴표를 사용해 작성합니다. 이는 여러 줄에 걸친 독스트링을 작성할 때 유용하며, 일관성을 유지합니다.
2. **한 줄 독스트링**: 독스트링이 한 줄로 작성될 수 있는 경우에는, 닫는 따옴표는 같은 줄에 위치해야 합니다.


```python
def add(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

add(1, 3)
```




    4




```python
## google convention sample
# google coding convention
def fetch_smalltable_rows(table_handle, keys, require_all_keys = False):
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
          returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """

fetch_smalltable_rows(1,2,3)
```

## 컴프리헨션

- 여러개의 for문을  컴프리헨션에서 쓰지마세요. 여러개일 경우 for 문을 풀어서 사용해주세요



```python
result = []
```


```python
# dict 컴프리헨션

square_dict = {x: x**2 for x in range(5)}
square_dict
```




    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}




```python
books = ['python', 'javascript', 'html/css']

book_dict = {book: idx  for idx, book in enumerate(books)}
book_dict
```




    {'python': 0, 'javascript': 1, 'html/css': 2}




```python
# 문제 : {'python': 10000000, 'javascript': 24000000, 'html/css': 39000000}와 같은 형태로 출력되게 해주세요!
books = [('python', 1000, '10000원'),
 ('javascript', 2000, '12000원'),
  ('html/css',3000, '13000원')]

book_dict = {b: num*int(price[:-1]) for b, num, price in books}
book_dict
```




    {'python': 10000000, 'javascript': 24000000, 'html/css': 39000000}



- 제너레이터 컴프리헨션: 제너레이터 컴프리헨션은 소괄호(()) 안에 for문과 선택적 if문을 사용하여 제너레이터 객체를 생성합니다. 제너레이터는 반복을 위한 이터러블이지만, 모든 값을 메모리에 저장하지 않고 필요할 때마다 생성합니다.


```python
## generator comprehension
square_gen = (x**2 for x in range(10))
next(square_gen)
next(square_gen)
next(square_gen)
```




    4




```python
gen = (i for i in range(2, 10000000, 2))

for i, j in zip(range(10), gen):
    print(i, j)
```

    0 2
    1 4
    2 6
    3 8
    4 10
    5 12
    6 14
    7 16
    8 18
    9 20


## 제너레이터와 이터레이터

**이터레이터(Iterator)**

- 이터레이터란, 값을 차례대로 꺼낼 수 있는 객체를 의미합니다. 이는 파이썬의 리스트, 튜플, 문자열 같은 컬렉션 타입들을 의미합니다. 이러한 이터러블 객체들은 `iter()` 함수를 사용해 이터레이터로 변환될 수 있습니다. 이터레이터 객체는 `next()` 함수를 사용해 값을 순차적으로 꺼낼 수 있습니다.


```python
# 이터레이터를 클래스로 구현

class MyIterator:
    def __init__(self, stop):
        self.currentValue = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration
        result = self.currentValue
        self.currentValue += 1
        return result

my_iterator = MyIterator(5)

for i in my_iterator:
    print(i)
```

[링크 텍스트](https://pythontutor.com/visualize.html#mode=edit)




```python

```

**제너레이터(Generator)**

- 제너레이터는 이터레이터를 생성하는 특별한 종류의 함수입니다. 제너레이터는 `yield` 키워드를 사용해 값을 '생성'합니다. 이터레이터와 마찬가지로 `next()` 함수를 통해 값들을 순차적으로 꺼낼 수 있지만, 모든 값을 메모리에 저장하는 대신 필요할 때마다 값을 생성합니다. 이로 인해 메모리 사용량을 줄이고, 큰 시퀀스를 생성할 때 성능을 개선할 수 있습니다.


```python
# 제너레이터 컴프리헨션때 연습한 것
gen = (i for i in range(2, 10000000, 2))

for i, j in zip(range(10), gen):
    print(i, j)
```

    0 2
    1 4
    2 6
    3 8
    4 10
    5 12
    6 14
    7 16
    8 18
    9 20



```python
# 위에거를 함수형으로 한 것
def count():
    count=2
    while True:
        yield count
        count += 2

# zip 해서 넘길때에만 값을 하나씩 꺼내서 주기 때문에 메모리 효율 좋음
for i, j in zip(range(10), count()):
    print(i,j)
```

    0 2
    1 4
    2 6
    3 8
    4 10
    5 12
    6 14
    7 16
    8 18
    9 20



```python
class MyIterator:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.currentValue = 0
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration
        result = self.currentValue
        self.currentValue += 1
        return result

my_iterator = MyIterator(5)

for i in my_iterator:
    print(i)

for i in my_iterator:
    print(i)

# 결국 for는 iter먼저 실행하고, next로 StopIteration
# i = iter(li)
# next(i)
```


```python
## zip 은 한번돌면 못돌아가
## sorted는 여러번 가능

## 왜 이런차이??
## 매직메서드에서 초기화를 안해주고 해주고의 차이입니다.
## __iter__매직메서드에서 순회횟수를 초기화 안해줘서..
## 그래서 그런 용도로 사용하지 않기 때문에 구현이 안되어 있는 것입니다.

```

## collections


- deque
- deque는 양쪽 끝에서 요소를 추가하거나 제거할 수 있는 스레드-안전한 양방향 큐입니다.


```python
from collections import deque

d = deque()
d.append('a')  # 오른쪽 끝에 추가
d.appendleft('b')  # 왼쪽 끝에 추가
d.pop()  # 오른쪽 끝 요소 제거
d.popleft()  # 왼쪽 끝 요소 제거
```

- Counter
- Counter는 요소의 개수를 세는데 사용되는 컬렉션입니다.


```python
from collections import Counter

c = Counter('hello world')
print(c)  # 출력: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

# 함수형 프로그래밍 활용


**프로그래밍 패러다임: 함수형, 절차형, 객체지향**

- 프로그래밍 언어는 일반적으로 여러 가지 프로그래밍 패러다임을 지원합니다. 이 패러다임들은 프로그래머가 문제를 이해하고 해결하는 방법에 영향을 미칩니다. 다음은 함수형 프로그래밍, 절차형 프로그래밍, 객체지향 프로그래밍에 대한 간략한 설명입니다.

**1. 함수형 프로그래밍 (Functional Programming)**

- 함수형 프로그래밍은 계산을 일련의 함수 호출로 표현하는 패러다임입니다. 함수형 프로그래밍은 순수 함수(pure functions)와 불변성(immutability)에 중점을 둡니다. 이는 함수의 결과가 입력에만 의존하고, 프로그램의 상태를 변경하지 않아야 함을 의미합니다.

- 함수형 프로그래밍의 장점은 코드의 예측성과 테스트 용이성입니다. 그러나 함수형 프로그래밍을 완전히 이해하고 사용하는 것은 일부 프로그래머에게 어려울 수 있습니다.

**2. 절차형 프로그래밍 (Procedural Programming)**

- 절차형 프로그래밍은 프로그램을 일련의 절차 또는 단계로 묘사하는 패러다임입니다. 프로그램의 상태는 이러한 절차에 의해 변경됩니다.

- 절차형 프로그래밍은 코드를 재사용하고 구조화하는데 유용하며, 대부분의 프로그래밍 언어가 이 패러다임을 지원합니다. 하지만, 프로그램의 상태를 추적하는 것이 복잡해질 수 있으며, 이는 복잡한 프로그램에서 버그를 일으키는 원인이 될 수 있습니다.

**3. 객체지향 프로그래밍 (Object-Oriented Programming)**

- 객체지향 프로그래밍은 데이터와 그 데이터를 조작하는 메서드를 하나의 '객체'에 묶는 패러다임입니다. 이 패러다임은 '클래스'라는 템플릿을 통해 객체를 생성하며, 클래스는 객체의 초기 상태(state)와 가능한 동작(behavior)을 정의합니다.

- 객체지향 프로그래밍은 코드의 재사용성을 높이고, 코드의 구조를 개선하며, 복잡성을 관리하는 데 유용합니다. 그러나, 객체지향 설계와 프로그래밍은 초기 학습 곡선이 가파르고, 잘못 사용하면 코드의 복잡성을 높일 수 있습니다.

**일급 함수 (First-Class Function)**

일급 함수 (First-Class Function)는 프로그래밍 언어가 함수 (또는 메서드)를 ‘일급 시민(값)'으로 취급하는 것을 의미합니다. 이는 함수를 다른 객체와 동일하게 취급하며, 다음과 같은 동작을 가능하게 합니다:

1. 함수를 변수에 할당할 수 있습니다.
2. 함수를 데이터 구조에 저장할 수 있습니다.
3. 함수를 인자로 다른 함수에 전달할 수 있습니다.
4. 함수를 결과로서 반환할 수 있습니다.

**고차 함수 (Higher-Order Function)**

고차 함수 (Higher-Order Function)는 다른 함수를 인자로 받거나, 결과로서 함수를 반환하는 함수를 의미합니다. 이는 '일급 함수'의 특성을 활용하는 프로그래밍 패턴이며, 특히 함수형 프로그래밍에서 많이 사용됩니다.

Python에서는 일급 함수를 지원하기 때문에 고차 함수를 쉽게 사용할 수 있습니다. 예를 들어, `map()`, `filter()`, `reduce()` 등의 내장 함수는 모두 고차 함수입니다.

**람다 함수**

람다 함수는 Python의 강력한 기능 중 하나로, 이름이 없는 일회용 함수를 생성하는 데 사용됩니다. `lambda` 키워드를 사용하여 작성되며, 주로 작고 간단한 함수를 필요로 하는 곳에 사용됩니다.

람다 함수는 일반 함수(`def`를 사용한 함수)와 비슷하지만, 다음과 같은 차이점이 있습니다:

1. `def` 키워드를 사용하여 함수를 정의하는 대신 `lambda` 키워드를 사용합니다.
2. 람다 함수는 이름이 없습니다 (익명 함수).
3. 람다 함수는 주로 한 줄로 표현되며, 복잡한 로직을 포함하지 않습니다.

람다 함수의 기본적인 구조는 다음과 같습니다:

## 클로저


파이썬에서는 factory function이라고 부르기도 합니다. 클로저는 파이썬에만 있는 개념이 아니라 다른 프로그래밍 언어에서도 중요한 프로그래밍 개념으로, 특정 함수와 그 함수가 생성된 환경을 결합한 것을 의미합니다. 특히, 클로저는 함수가 생성된 시점의 범위에 있는 모든 변수를 기억하고 이에 접근할 수 있게 합니다.

Python에서 클로저는 다음의 특징을 가집니다:

1. **함수 내부에 함수가 정의됩니다.** 이러한 내부 함수를 중첩 함수(Nested Function)라고 부릅니다.
2. **내부 함수는 외부 함수의 변수를 참조합니다.**
3. **외부 함수는 내부 함수를 반환합니다.**


```python
## 이미 클로징 (닫힘) 되어야 했을 때를 기억해서 호출하는것.
## 함수가 리턴되어서 사라졌어야 할 메모리 영역을 기억하는 객체
```


```python
# 클로저가 아닌경우
def outer_function():
    def inner_function():
        return 100+100
    return inner_function

# 클로저인 경우
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

inner = outer_function(100)
inner(200) ## 100 에 즉 x에 접근할 수 있는 방법이 없습니다.
```




    300



## 데코레이터


데코레이터는 Python의 고급 기능 중 하나로, 함수나 메소드에 추가적인 기능을 동적으로 부여하려는 경우 사용합니다. Python에서 데코레이터는 "@" 기호와 함께 사용되며, 데코레이터로 지정된 함수가 바로 아래에 정의된 함수에 적용됩니다.

**데코레이터의 작동 원리**

데코레이터는 본질적으로 고차 함수(higher-order function)입니다. 고차 함수는 하나 이상의 함수를 인자로 받고, 함수를 결과로 반환하는 함수를 의미합니다. 데코레이터는 하나의 함수를 인자로 받고, 기능이 추가 또는 변경된 새로운 함수를 반환합니다.


```python
def simple_decorator(function):
    def wrapper():
        print("Before the function call")
        function()
        print("After the function call")
    return wrapper

@simple_decorator
def hello():
    print("Hello, World!")

def hello2():
    print("Hello, World!")

hello()

# 이거랑 hello()랑 같음 데코레이터의 동작 원리
simple_decorator(hello2)()
```

    Before the function call
    Hello, World!
    After the function call
    Before the function call
    Hello, World!
    After the function call



```python
def solution(tickets):
    answer = []
    cur = 'ICN'

    while tickets:
        tmp = [i for i in tickets if i[0] == cur]
        tmp.sort(key=lambda x:x[1])
        print(tmp)
        break

    return answer

li = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(li)
```

    [['ICN', 'ATL'], ['ICN', 'SFO']]





    []



## 객체 지향 프로그래밍 심화

### 클래스 메서드(@classmethod)

클래스 메서드는 클래스에 작용하는 메서드입니다. 클래스 메서드는 첫 번째 인자로 클래스 자체를 받습니다. 일반적으로 이 인자를 cls로 명명합니다. 클래스 메서드는 클래스 상태를 변경하는데 사용될 수 있습니다.


```python
class MyClass:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

MyClass.increment()
print(MyClass.count)  # 출력: 1
```

    1



```python

```

### 스태틱 메서드(@staticmethod)

스태틱 메서드는 클래스나 인스턴스와는 독립적으로 작동하는 메서드입니다. 스태틱 메서드는 self나 cls 같은 특별한 첫 번째 인자를 받지 않습니다. 스태틱 메서드는 주로 클래스와 연관은 있지만 인스턴스나 클래스 상태에는 접근하지 않는 메서드에 사용됩니다.


```python
class MyClass:
    @staticmethod
    def my_method(x, y):
        return x + y

print(MyClass.my_method(5, 3))  # 출력: 8
```

    8



```python
class CompletionList:
    def __init__(self):
        self.subject_list = []

    def show(self):
        print(self.subject_list)

    def append(self, subject):
        self.subject_list.append(subject)

    @staticmethod
    def academic_warning(subject):
        '''
        내부에서 클래스 변수, 인스턴스 변수 수정하는 것이 가능하지 않습니다.
        '''
        return abs(1.5 - subject['grades'])


c = CompletionList()

subject1 = {"name": "Python", "grades": 2.5}
subject2 = {"name": "HTML/CSS", "grades": 3.5}

c.append(subject1)
c.append(subject2)
c.show()

# 스태틱 메서드 호출 시 클래스 이름으로 호출합니다.
# 인스턴스로 호출 불가능
print(CompletionList.academic_warning(subject1))
```

    [{'name': 'Python', 'grades': 2.5}, {'name': 'HTML/CSS', 'grades': 3.5}]
    1.0


### 속성 접근자와 덕 타이핑

- 속성접근자
- Python에서는 @property 데코레이터를 사용하여 클래스의 메서드를 속성처럼 접근할 수 있게 만들 수 있습니다. 이를 통해 객체의 내부 상태를 보호하고, 특정 속성에 대한 접근을 제어할 수 있습니다.
- 호출연산자 `()` 사용이 불가능함. 호출연산자 없이 사용해서 속성처럼 사용할 수 있다는 뜻입니다.
- 또한, @property를 사용하여 setter를 정의할 수도 있습니다. 이를 통해 속성에 대한 값의 유효성 검사나 추가적인 연산을 수행할 수 있습니다.


```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

hojun = Person('lee', 'hojun')
hojun._first_name, hojun._last_name
hojun.full_name
# hojun.full_name() # TypeError발생.
```




    'lee hojun'



- 덕타이핑
- 덕 타이핑은 실제 타입은 상관치 않고 구현된 메서드로 확인하는 방법입니다. 좀 더 어려운 말로 객체의 변수 및 메서드의 집합이 객체의 타입을 결정하는 개념을 의미합니다. 이를 통해 유연한 인터페이스를 구현할 수 있습니다.
- 아래 코드에서 quack(obj) 함수는 obj가 실제로 Duck 타입이든 아니든 상관하지 않고, quack 메서드를 호출합니다. 이러한 접근법은 런타임에 메서드나 속성의 존재를 확인하기 때문에 코드가 더욱 유연해집니다.


```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def quack(obj):
    obj.quack()

duck = Duck()
person = Person()

quack(duck)  # 출력: Quack!
quack(person)  # 출력: I'm Quacking Like a Duck!
```

    Quack!
    I'm Quacking Like a Duck!


## 추상 클래스와 인터페이스

### 추상클래스  Abstract Class

- Python에서 추상 클래스는 기본적으로 구현하지 않아도 되는 메서드(추상 메서드)를 가진 클래스입니다.
- 추상클래스의 추상메서드는 서브클래스에서 반드시 구현해야 하는 메서드를 정의해야 합니다.
- Python에서는 abc 모듈의 ABC 클래스와 abstractmethod 데코레이터를 사용하여 추상 클래스와 추상 메서드를 정의합니다.
- 추상클래스는 인스턴스를 생성할 수 없습니다.


```python
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass

## 상속받는 AbstractClassExcample에서
## @abstractmethod 을 적용한 do_something을 반드시 정의해주어야 합니다.
class Person(AbstractClassExample):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f'제 이름은 {self.name}입니다.')

hojun = Person('hojun') # Type Error 인스턴스화할수없습니다.
hojun.print_name()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-20-711b7042dc3e> in <cell line: 19>()
         17         print(f'제 이름은 {self.name}입니다.')
         18 
    ---> 19 hojun = Person('hojun')
         20 hojun.print_name()


    TypeError: Can't instantiate abstract class Person with abstract method do_something



```python
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass

class Person(AbstractClassExample):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f'제 이름은 {self.name}입니다.')

    def do_something(self):
        pass

hojun = Person('hojun')
hojun.print_name()
```

    제 이름은 hojun입니다.


### 인터페이스

- 객체가 어떤 메서드를 구현해야 하는지 정의한 것입니다.
- Python에서는 다른 언어들과 달리 인터페이스라는 내장 키워드나 구조가 없습니다.
- 추상 클래스를 이용하여 인터페이스처럼 동작하는 클래스를 만들 수 있습니다.


```python
from abc import ABC, abstractmethod

class MyInterface(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass
```

- Python에서 인터페이스는 클래스가 특정 메서드를 구현함으로써 특정 타입에 속하도록 강제하는 방식으로 사용됩니다. 이는 덕 타이핑과 관련이 있습니다. 덕 타이핑에 따르면, 객체의 타입은 그 객체가 어떤 메서드나 속성을 지원하는지에 따라 결정됩니다. 이는 인터페이스를 통해 객체의 타입을 결정하는 것과 유사한 원리입니다.


```python

```

## 모듈과 패키지 관리

**Python 모듈**

- Python 모듈은 Python 코드를 담고 있는 `.py` 파일입니다. 모듈은 함수, 클래스, 또는 변수들을 포함할 수 있으며, 이를 다른 Python 프로그램에서 재사용할 수 있습니다.

```plaintext
# 설치된 패키지 확인
pip list

# 패키지 설치
pip install
python pip -m

# 패키지 설치 위치
python -m site
```

- `python -m site`의 결과물에서 `sys.path`를 볼 수 있는데, 여기에 추가되어야 모듈들을 검색해서 import 할 수 있습니다.

- pip를 이용해서 설치된 패키지 설정을 저장하고 다른 곳에서 동일하게 설치하는 방법.

- 아래같이 해당 파이썬 환경의 패키지를 pip freeze로 저장해둔 다음 저장한 텍스트 파일을 이식하고 싶읖 파이썬 환경에서 실행해주면 됩니다.

```plaintext
# requirements.txt 파일에 패키지 목록을 저장
pip freeze > requirements.txt

# 이 명령을 실행하면 requirements.txt 파일 내에 정의된 패키지를 같은 버전으로 설치한다.
pip install -r requirements.txt
```

**import문의 내부동작**

1. Python은 먼저 `sys.modules를 체크(Python이 실행될 때 자동으로 로드)`합니다. 이 딕셔너리는 이미 로드된 모듈들의 이름을 키로 하고, 해당 모듈 객체를 값으로 가집니다. 모듈이 이미 sys.modules에 존재한다면, 그것이 반환됩니다.




```python
import sys
sys.modules
```

2. sys.modules에 없다면, Python은 sys.path에 있는 디렉토리들을 순회하면서 모듈이 있는지 찾습니다. sys.path는 Python 인터프리터에서 모듈을 어디에서 찾아야 할지 알려주는 경로의 리스트입니다. 이 리스트는 다음과 같은 위치를 포함합니다.

  1. 스크립트가 실행되는 현재 디렉토리 (또는 Python 인터랙티브 세션을 시작한 디렉토리)
  2. `PYTHONPATH` 환경 변수에 명시된 모든 디렉토리 (환경 변수가 설정된 경우, window의 환경변수 설정하기로 검색하시면 됩니다.)
  3. Python 설치 시 지정된 라이브러리 디렉토리, 기본적으로 Windows에서는 "C:\PythonXX\Lib"와 같은 형태로 될 것입니다. 여기서 'XX'는 Python의 버전을 나타냅니다.
  4. 각각의 .egg 파일 (있을 경우)
  5. `sys.path`에 디렉토리를 동적으로 추가한 경우. 예를 들어, 스크립트에서 다른 디렉토리에 있는 모듈을 임포트하려는 경우, `sys.path.append('/path/to/directory')`를 사용하여 해당 디렉토리를 `sys.path`에 추가할 수 있습니다. 그러면 Python은 그 디렉토리를 검색하여 모듈을 찾을 수 있습니다.
  6. `site-packages` 는 `.pth` 파일을 참고합니다.

> .egg 파일이란?
> Python Egg라고도 하는 EGG 파일은 이전 배포 형식의 Python 배포입니다. 확장자가 .egg인 ZIP 압축 아카이브이며 배포에 대한 메타 정보와 함께 Python 응용 프로그램의 소스 파일을 포함합니다. EGG 파일은 Windows 실행 EXE 파일의 대안이지만 플랫폼 간입니다.
> .egg 확장자를 .zip으로 바꾸면 Corel WinZIP, Microsoft Explorer 또는 RARLAB WinRAR와 같은 표준 압축 해제 유틸리티로 열 수 있습니다.
> Python에서 제공하는 distutils 패키지를 사용하여 생성할 수 있습니다. EGG 파일을 만들고 열 수 있는 또 다른 도구는 SetupTools입니다. EGG 파일은 easy_install을 사용하여 패키지로 설치할 수 있습니다.

3. Python이 모듈을 찾았다면, 모듈의 코드를 읽고 실행합니다. 모듈의 이름이 sys.modules에 추가되고, 이 이름으로 모듈을 참조할 수 있습니다.


```python
# sample.py
name = 'hojun'
```


```python
import sample

sample.name
```




    'hojun'




```python
import sys

'sample' in sys.modules # True
```




    True



- 여러 폴더 경로 안에있는 py파일을 패키지로 불러오기
- content/a/b/c/sampletest.py


```python
# content/a/b/c/sampletest.py
name = 'js'

```


```python
# sampletest가 어느경로에있는지 알수없음..
# 새로만든거라 modules에 없고, path에도 등록안되어있어서..
import sampletest # ModuleNotFoundError

sampletest.name
```


```python
## 폴더경로를 다 입력해주면 찾을 수 있음
from content.a.b.c import sampletest
sampletest.name
```




    'js'




```python
import sys
'sampletest' in sys.modules
```




    False




```python
## sys.path에 모듈을 찾을 경로를 추가해줍니다.
## sys.modules에 추가됨. key - value 값
sys.path.append('content/a/b/c')
```




    'js'




```python
import sampletest
sampletest.name
```




    'js'




```python
import sys

'sampletest' in sys.modules # False
```




    True



** 모듈의 실행 **
- 모듈이 로드되면, 모듈의 코드는 최상위 레벨에서 실행되고, 모듈의 네임스페이스를 정의하는데 사용되는 이름들은 생성됩니다. 모듈의 네임스페이스는 import 문을 통해 접근할 수 있습니다.

### 모듈과 패키지의 재사용성

** 모듈과 패키지의 재사용성 이해하기 **


1. 재사용성의 중요성
    - 코드의 재사용성을 높이는 것은 개발 시간을 줄이고, 코드의 품질을 향상시키는 데 중요합니다. 재사용성이 높은 코드는 수정이 용이하고, 에러를 줄일 수 있습니다.
    - Python의 모듈과 패키지 시스템은 코드의 재사용성을 크게 향상시킵니다.
2. 모듈의 재사용성
    - 모듈은 Python 코드를 포함하는 .py 파일로, 함수, 변수, 클래스 등을 정의할 수 있습니다. 이렇게 정의된 모듈은 `import`문을 통해 다른 Python 코드에서 재사용할 수 있습니다.
    - 예를 들어, 특정 기능을 수행하는 함수를 여러 스크립트에서 사용해야 하는 경우, 이 함수를 모듈에 정의하고 필요한 스크립트에서 임포트하여 사용할 수 있습니다.
3. **패키지의 재사용성**
    - 패키지는 관련된 여러 모듈을 하나의 디렉토리에 모아놓은 것입니다. 패키지를 통해 모듈을 논리적으로 그룹화하고, 이를 재사용할 수 있습니다.
    - 예를 들어, **여러 모듈에서 공통으로 사용하는 클래스나 함수를 `utilities`라는 패키지에 모아놓고, 이 패키지를 임포트하여 코드를 재사용할 수 있습니다.**


```python
# utilities/math_tools.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```


```python
# main.py

from utilities.math_tools import add, subtract

def main():
    print(add(10, 5))  # 출력: 15
    print(subtract(10, 5))  # 출력: 5

if __name__ == "__main__":
    main()
```

    15
    5


** 모듈과 패키지의 재사용성 향상하기 **

1. 모듈과 패키지의 설계
    - 재사용성을 높이려면 모듈과 패키지를 잘 설계해야 합니다. 즉, 하나의 모듈은 하나의 주요 기능에 집중하고, 패키지는 관련된 모듈들을 그룹화하는 것이 좋습니다.
2. 명확한 API 제공
    - 모듈과 패키지는 재사용성을 위해 명확한 API(Application Programming Interface)를 제공해야 합니다. 즉, 외부에서 사용할 수 있는 함수와 클래스, 변수 등을 명확하게 정의하고, 그 사용법을 문서화하는 것이 중요합니다.
3. 테스트 코드 작성
    - 모듈과 패키지의 재사용성을 높이려면 이를 검증하는 테스트 코드가 필요합니다.

### 자주 사용되는 표준  라이브러리

1. `os` 모듈: 운영체제와 상호작용하는 데 사용되는 함수들을 제공합니다. 파일과 디렉토리를 만들고, 읽고, 쓰는 것을 비롯하여 환경 변수에 접근하거나 운영 체제 명령을 실행하는 등의 작업을 수행할 수 있습니다.
2. `sys` 모듈: Python 인터프리터와 상호작용하는 도구를 제공합니다. 이 모듈을 사용하면 명령행 인수를 처리하거나, 입/출력 스트림을 제어하거나, 인터프리터의 상태를 점검하고 제어할 수 있습니다.
3. `math` 모듈: 수학적 연산을 수행하는데 필요한 함수들을 제공합니다. 제곱근, 로그, 삼각함수 등의 기능이 포함되어 있습니다.
4. `datetime` 모듈: 날짜와 시간을 다루는 클래스를 제공합니다. 현재 날짜와 시간을 가져오는 것부터 날짜와 시간의 차이를 계산하는 것까지 다양한 기능을 제공합니다.
5. `json` 모듈: JSON 형식의 데이터를 읽고 쓰는 데 사용됩니다. Python 데이터 구조를 JSON 문자열로 직렬화하거나, JSON 문자열을 Python 데이터 구조로 역직렬화하는 기능을 제공합니다.
6. `collections` 모듈: 기본 데이터 컨테이너 외에도 다양한 데이터 컨테이너 타입을 제공합니다. deque, Counter, OrderedDict, defaultdict 등과 같은 고급 데이터 구조를 제공합니다.
7. `requests` 모듈: HTTP 요청을 쉽게 보낼 수 있는 기능을 제공하는 외부 라이브러리입니다. REST API와 통신하거나 웹 페이지를 스크래핑하는 등의 작업을 수행하는 데 유용합니다.


```python
!jupyter nbconvert --to markdown a.ipynb
```

    [NbConvertApp] Converting notebook a.ipynb to markdown
    [NbConvertApp] Writing 19992 bytes to a.md

