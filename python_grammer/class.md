# 클래스 class

- 클래스는 데이터(멤버)와 기능(메서드)을 가지고 있는 인스턴트 객체를 생성하기 위한 역할을 합니다.

- 멤버는 클래스 멤버와 인스턴스 멤버로 구분됩니다.

- 메서드는 매직메서드(`__init__`, `__add__`과 같은이 양 끝에 `__`가 있는 함수)와 일반메서드로 구분됩니다.

- 데이터 모델 공식 사이트 : https://docs.python.org/3/reference/datamodel.html

## 파이썬에서 클래스 생성하기

- 함수 선언과 동일하지만 `def` 대신 `class`로 선언

> 클래스 선언 기본형: `class 클래스이름(상속받을클래스):`

- 상속받을 클래스가 없다면 빈 상태로 선언해도 된다
- 아무 클래스도 상속받지 않더라도 기본적으로 `object` 클래스를 상속받습니다

```python
class MyClass():
    pass

class MyObjectClass(object):
    pass

myc = MyClass()
myobjc = MyObjectClass()

print(dir(myc))
print(dir(myc) == dir(myobjc)) # attribute 목록이 동일함.

## 기본적으로 상속을 받지 않은 class도 object를 자동으로 상속받게 됨을 확인했음
```

## 클래스 멤버와 인스턴스 멤버

- 클래스 멤버 : 클래스 자체에 속한 멤버

  - 클래스의 함수 정의와 같은 레벨에서 선언된 변수(멤버) 들
    <br>이 부분에서는 `self.~`으로 선언하면 에러가 발생하는데, self는 instance를 뜻하기 때문이다.(class 자체는 인스턴스가 아님)
  - 모든 인스턴스가 공용으로 사용함

- 인스턴스 멤버 : 인스턴스에 속한 멤버
  - 일반적으로 생성자 메서드(`__init__`)에서 `self.변수명` 으로 선언됨
  - 클래스 멤버와 이름이 같더라도 `self.변수명 = ~`으로 할당 연산을 쓰는 순간 인스턴스 `변수명` 이 생성된다 (주의!!)
    - int형 클래스 멤버 변수에 대해 연산자 = , += , -=, \*=, /= 은 새로 생성된다.
    - list형 클래스 멤버는 = 만 멤버변수로 생성된다. (+= 사용하면 클래스 멤버 그대로)

```python

class Cup():    # 아무것도 넣어주지 않아도 기본적으로 object를 상속받음

    kinds = []
    size = 300

    def __init__(self, meterial):
        self.meterial = meterial    # 인스턴스 멤버

    def add_kinds(self, name):
        Cup.kinds.append(name)  # 클래스 이름으로 클래스멤버 호출
        self.kinds.append(name) # 인스턴스로 클래스멤버 호출

    def change_size(self, size):
        self.size = size        # 클래스 멤버와 이름은 같지만 인스턴스 멤버 size를 생성
        # self.size *= size     # =, +=, -=, *= /= 도 새로운변수 생성해버림.
        # self.kinds += ['이건 어떄?'] # list에 대한 +=, append 등 은 안바뀜.

mug = Cup('ceramic')
tumbler = Cup('stainless')

# 인스턴스로 멤버 부르기
print(mug.meterial, tumbler.meterial)    # 인스턴스 멤버 ## ceramic stainless
print(mug.size, tumbler.size)            # 클래스 멤버   ## 300 300

# 인스턴스로 함수를 호출할 수 있다.
mug.add_kinds('mug 컵!')

# 클래스 멤버 호출. 클래스 멤버는 모든 인스턴스에서 공유한다.
print(Cup.kinds)    #['mug 컵!', 'mug 컵!']
print(mug.kinds)    #['mug 컵!', 'mug 컵!']
print(tumbler.kinds)#['mug 컵!', 'mug 컵!']


tumbler.change_size(320)
print(mug.size, tumbler.size, Cup.size)             # 300 320 300
print(id(mug.size), id(tumbler.size), id(Cup.size)) # 140191215500048 140191215497296 140191215500048
# size의 값와 id를 확이해보니 tumbler에는 인스턴스 멤버 'size'가 생성되었음을 확인!

# ['mug 컵!', 'mug 컵!', '이건 어떄?'] ['mug 컵!', 'mug 컵!', '이건 어떄?'] ['mug 컵!', 'mug 컵!', '이건 어떄?']
print(mug.kinds, tumbler.kinds, Cup.kinds)
# 140397594236736 140397594236736 140397594236736
print(id(mug.kinds), id(tumbler.kinds), id(Cup.kinds))
```

## 메서드 method

- 인스턴스 메서드, 클래스 메서드, 스태틱 메서드, 매직메서드 등이 있다.
- 인스턴스의 내용을 변경해야 할 때는 인스턴스 메서드로 작성하고, 인스턴스 내용과는 상관없이 결과만 구하면 될 때는 정적 메서드로 작성하면 됩니다.
  <br>항상 그런것은 아니지만 대부분

### 인스턴스 메서드

- 아무 데코레이터 없이 선언되어 첫 번째 인자로 `self`를 받는 함수
- 아래 예시의 `__init__`, `increment`, `decrement`가 인스턴스 메서드 입니다.
- 인스턴스 메서드는 반드시 클래스로 인스턴스를 생성한 후, 인스턴스로 호출해야 합니다.

```python
class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self, delta = 1):
        self.value += delta

    def decrement(self, delta = 1):
        self.value -= delta

counter = Counter()
print(counter.value)    # 0
counter.increment(10)
print(counter.value)    # 10
counter.decrement(5)
print(counter.value)    # 5

```

### 클래스 메서드

- `@classmethod` 데코레이터를 사용해서 선언한 메서드
- 첫 번째 인자로 클래스가 넘어가게 됩니다.
- 그래서 첫 번째 인자를 관행적으로 `cls`라고 하며 `cls`를 통해 클래스 메서드 및 클래스 멤버를 호출할 수 있습니다.
- 클래스 메서드 내에서 인스턴스 메서드 및 인스턴스 멤버에 접근하거나 호출할 수 없습니다.
  <br> 클래스 멤버 및 클래스 메서드는 호출 가능합니다.

```python

class BookInfo(object):

    total_book_list = []    # 클래스 멤버

    def __init__(self, title, writer, number, price, publisher):
        self.title = title
        self.writer = writer
        self.number = number
        self.price = price
        self.publisher = publisher
        self.review = []
        self.total_book_list.append(self)

    def __str__(self):
        return f'제목:{self.title}, 저자:{self.writer}, 가격:{self.price}'

    def write_review(self, content):
        self.review.append(content)
        print(f'책 {self.title}의 후기가 작성되었습니다.')

    def view_review(self):
        print(f'{self.title}의 책 리뷰 :')
        print(self.review)

    @classmethod
    def book_count(cls):
        return len(cls.total_book_list)

파이썬길잡이 = BookInfo('파이썬 길잡이1', '자까', '800', '23000','빠빠')
파이썬길잡이2 = BookInfo('파이썬 길잡이2', '자까', '850', '25000','빠빠')

# 매직메서드 __str__
print(파이썬길잡이)
print(파이썬길잡이2)

# 인스턴스 메서드
파이썬길잡이.write_review('매우매우좋아요!')
파이썬길잡이.write_review('정말좋아요!')
파이썬길잡이.write_review('좋아요!')
파이썬길잡이.view_review()

# 클래스 메서드
print(BookInfo.book_count())    # 2
```

- 생성자 오버로딩에 유용하게 사용할 수 있다.

```python
class UserInfo():

    def __init__(self, email, nickname):
        self.email = email
        self.nickname = nickname

    @classmethod
    def constfromList(cls, data):
        print('list로 생성하기')
        return cls(data[0], data[1]) ## 생성자 함수로 생성한 오브젝트를 넘겨줌

    @classmethod
    def constfromDict(cls, data):
        print('dict로 생성하기')
        return cls(data.get('email'), data.get('nickname'))



user1 = UserInfo('aaa@ssss.com', 'miamia')
print(user1.email)
print(user1.nickname)

user2 = UserInfo.constfromList(['aaa@tutus.com', 'miatuple'])
print(user2.email)
print(user2.nickname)

user3 = UserInfo.constfromDict({'email' : 'ddd@dictdict.com', 'nickname' : 'dddd'})
print(user3.email)
print(user3.nickname)

# aaa@ssss.com
# miamia
# list로 생성하기
# aaa@tutus.com
# miatuple
# dict로 생성하기
# ddd@dictdict.com
# dddd
```

### 스태틱 메서드

- `@staticmethod` 데코레이터를 사용해서 선언한 메서드
- 첫 번째 인자로 클래스나 인스턴스가 **넘어가지 않습니다.**
- 스태틱 메서드 내에서 인스턴스 메서드 및 인스턴스 멤버에 접근하거나 호출할 수 없습니다.

```python
class Calc():

    @staticmethod
    def add(a,b):
        return a + b

    def sub(a,b):
        return a - b

print(Calc.add(10,20))  # 30
print(Calc.sub(10,20))  # -10
```

### 매직 메서드

- 앞뒤로 언더바2개 `__`가 붙은 함수이름을 가진 함수
- 예를 들어 `__add__`, `__iter__`, `__eq__` 등의 함수들을 매직 메서드라고 한다

- 정리
  - `__call__` : `()`
  - `__getattribute__` : `.`
  - `__eq__` : `==`
  - `__add__` : `+`
  - `__sub__` : `-`
  - `__mul__` : `-`
  - `__name__` : 객체 이름

### `__str__`과 `__repr__`의 차이?

-

## 클래스에서 클래스 메서드 호출

- 일반적으로 `self`를 인자로 받는 메서드는 클래스로 호출할 수 없다.
- 왜냐하면 `self`는 인스턴스를 가리키기는데 클래스 자체는 인스턴스가 아니기 때문

```python



```

## 추상 클래스 (abstract class)

- 추상 클래스(abstract class)란 메서드의 이름만 존재하는(메서드 구현은 없이) 클래스입니다.
- 보통 객체 지향 설계에서 부모 클래스에 메서드만을 정의하고 이를 상속 받은 클래스가 해당 메서드를 반드시 구현하도록 강제하기 위해서 사용합니다
- 추상 클래스는 객체를 생성할 수 없습니다.
- 추상 클래스는 meteclass=ABCMeta를 상속받고 함수에는 `@abstractmethod` 데코레이터를 사용한다.

- 모듈 `abc`를 모두 import 해주어야함 (`from abc import *`)

```python
from abc import *

class Transport(metaclass=ABCMeta):
    @abstractmethod
    def fee(self):
        pass


class Bus(Transport):
    def fee(self):
        print("Bus fee is 3 dollors")

maeul = Bus()
maeul.fee()

```
