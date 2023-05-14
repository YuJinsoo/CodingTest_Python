# 클래스 class

- 클래스는 데이터(멤버)와 기능(메서드)을 가지고 있는 인스턴트 객체를 생성하기 위한 역할을 합니다.

- 멤버는 클래스 멤버와 인스턴스 멤버로 구분됩니다.

- 메서드는 매직메서드(`__init__`, `__add__`과 같이 양 끝에 `__`가 있는 함수)와 일반메서드로 구분됩니다.

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

# 인스턴스로 메서드를 호출할 수 있다.
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

### 인스턴스 멤버 확인하기 - `__dict__`어트리뷰트

- 파이썬은 인스턴스 필드를 위해 따로 특별한 자료구조가 있는 것이 하니라 dictionary 형태로 저장합니다.
- 그리고 인스턴스 필드에 선언된 멤버를 특정 어트리뷰트에 저장합니다.
- `__dict__` 어트리뷰트로 인스턴스 멤버를 확인할 수 있습니다.
- 오로지 인스턴스 멤버만 `__dict__`로 확인 가능합니다.
  <br> 함수, 클래스 멤버는 확인이 안됩니다.

```python
class MyClass():
    classmember = 0     # 클래스 멤버
    def __init__(self) :
        self.x = 0     # 인스턴스 멤버 x
        self.y = 0     # 인스턴스 멤버 y

    def foo(self):
        print('foofoo')


c1 = MyClass()

instance_members = c1.__dict__
print(type(instance_members))   # <class 'dict'>
print(instance_members)         # {'x': 0, 'y': 0}
```

### 클래스의 멤버 숨기기

- 클래스의 멤버 이름을 `__`로 시작하게 만들면 그 멤버는 인스턴스와 클래스로 접근할 수 없습니다.
- `__`로 시작하는 멤버는 어트리뷰트에 등록되지 않아서 접근할 수 없는 것으로 보입니다.
- 인스턴스 멤버를 확인하는 `__dict__` 어트리뷰트로 존재를 확인할 수 있습니다.

```python
class MyClass():
    classmember = 0     # 클래스 멤버
    __hide_mem = 0
    def __init__(self) :
        self.x = 0
        self.__HideInsMem = 0

    def foo(self):
        print('foofoo')


## 클레스에 선언된 클래스멤버 뿐만 아니라 모든 메서드를 확인할 수 있습니다.
class_members = MyClass.__dict__
print(class_members)
# {'__module__': '__main__',
# 'classmember': 0, '_MyClass__hide_mem': 0,
# '__init__': <function MyClass.__init__ at 0x7fd6630fb490>, ... 생략

c1 = MyClass()

instance_members = c1.__dict__
print(instance_members)         # {'x': 0, '_MyClass__HideInsMem': 0}

# c1.__HideInsMem # error : 'MyClass' object has no attribute '__HideInsMem'
# MyClass.__hide_mem # error : 'MyClass' object has no attribute '__hide_mem'
```

- 실제로는 접근이 완전히 불가능한 것이 아닙니다.
- 이름이 바뀌어서 해당 멤버가 어트리뷰트로 등록이 되지 않아서 접근이 불가능한 원리입니다.
- 바뀐 이름을 확인해서 접근하고 수정할 수 있습니다.

```python
class MyClass():
    classmember = 0     # 클래스 멤버

    def __init__(self) :
        self.x = 0
        self.__HideInsMem = 999

c1 = MyClass()
print(c1.__dict__)  ##dict 어트리뷰트에 숨겨진 인스턴스 멤버의 이름이 바뀌어 저장된걸 확인

print(c1._MyClass__HideInsMem)  # 999 # 수정된 이름으로 접근가능
c1._MyClass__HideInsMem = 1000
print(c1._MyClass__HideInsMem)  # 1000 # 수정된 이름으로 접근해서 수정 가능
```

## 메서드 method

- 인스턴스 메서드, 클래스 메서드, 스태틱 메서드, 매직메서드 등이 있다.
- 인스턴스의 내용을 변경해야 할 때는 인스턴스 메서드로 작성하고, 인스턴스 내용과는 상관없이 결과만 구하면 될 때는 정적 메서드로 작성하면 됩니다.
  <br>항상 그런것은 아니지만 대부분

  ```python
  class MyClass():

      def __init__(self) :  # 매직메서드
          self.x = 0
          self.__HideInsMem = 0

      def foo(self, arg1):  # 인스턴스 메서드
          print(f'인스턴스로 호출 - 인자: {self}, {arg1}')

      @classmethod
      def foo_class(cls, arg1): # 클래스메서드
          print(f'클래스로 호출 - 인자: {cls}, {arg1}')

      @staticmethod
      def foo_static(arg1, arg2):   #스태틱 메서드
          print(f'클래스로 호출 - 인자: {arg1}, {arg2}')


  c1 = MyClass()
  arg1 = 'argument1'
  arg2 = 'argument2'

  print(f'MyClass로 만든 인스턴스 c1 : {c1}')
  c1.foo(arg1)
  MyClass.foo_class(arg1)
  MyClass.foo_static(arg1,arg2)
  c1.foo_static(arg1,arg2)

  # MyClass로 만든 인스턴스 c1 : <__main__.MyClass object at 0x7fd6882f41f0>
  # 인스턴스로 호출 - 인자: <__main__.MyClass object at 0x7fd6882f41f0>, argument1
  # 클래스로 호출 - 인자: <class '__main__.MyClass'>, argument1
  # 클래스로 호출 - 인자: argument1, argument2
  # 클래스로 호출 - 인자: argument1, argument2
  ```

### 인스턴스 메서드

- 첫 번째 인자로 클래스 인스턴스를 받는 함수
- 관행적으로 함수를 호출한 인스턴스를 `self`라는 이름으로 인자로 받습니다.
- 아래 예시의 `increment`, `CheckInstance`가 인스턴스 메서드 입니다.
- 인스턴스 메서드는 반드시 클래스로 인스턴스를 생성한 후, 인스턴스로 호출해야 합니다.

```python
# 인스턴스 메서드에서 self와 인스턴스 메서드를 호출한 인스턴스가 동일하다
class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self, delta = 1):
        self.value += delta

    def CheckInstance(self):
        print(f'함수를 호출한 인스턴스 : {self}')

counter = Counter()
print(counter.value)    # 0
counter.increment(10)
print(counter.value)    # 10

print(counter)          # <__main__.Counter object at 0x7fd6882f66e0>
counter.CheckInstance() # 함수를 호출한 인스턴스 : <__main__.Counter object at 0x7fd6882f66e0>

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

- 클래스 메서드는 생성자 오버로딩에 유용하게 사용할 수 있습니다.
- `__init__` 생성자 매직메서드에서 전달받은 인자에 따라 분기해서 사용할 수 있을 것 같습니다.

```python
class UserInfo():

    def __init__(self, email, nickname):
        self.email = email
        self.nickname = nickname

    @classmethod
    def constfromList(cls, data):
        print('list로 생성하기')
        return cls(data[0], data[1]) # 생성자 함수로 데이터를 가공해서 넘겨줌

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

- `@staticmethod` 데코레이터를 사용해서 선언한 메서드 입니다.
- 첫 번째 인자로 클래스나 인스턴스가 **넘어가지 않습니다.**
- 스태틱 메서드 내에서 인스턴스 메서드 및 인스턴스 멤버에 접근하거나 호출할 수 없습니다. (인자로 없기 때문에)

- `@staticmethod`를 써주지 않아도 `self`인자가 없는 함수를 클래스로 호출하면 스태틱 인스턴스로 인식됩니다.
- `@staticmethod`를 써주면 인스턴스로도 스테틱 메서드를 호출할 수 있습니다.

```python
class Calc():

    def __init__(self):
        self.default = -10

    @staticmethod
    def add(a,b):
        return a + b

    def add_nondeco(a, b):
        return a + b

    def add_nondeco_self(self, a):
        return self.default + a

print(Calc.add(10,20))          # 30

# static method를 붙여주지 않았지만, staticmethod로 작동함
print(Calc.add_nondeco(10,20))  # 30
# print(Calc.add_nondeco(10))  # 30 #Calc.add_nondeco() missing 1 required positional argument: 'b'
# print(Calc.add_nondeco_self(10)) 인자에 self가 들어가면 클래스 이름으로 호출이 안됨

c = Calc()
print(c.add(10, 20))            # 30 # 인스턴스로 staticmethod를 호출할 수 있습니다.
print(c.add_nondeco(10, 20))    # @staticmethod가 없어 인스턴스로 호출할 수 없음
print(c.add_nondeco_self(10))   # 0
# print(c.add_nondeco(5)) ## 인스턴스로 호출 할 수 없음. self 인자가 없어서!
```

### 매직 메서드

- 앞뒤로 언더바2개 `__`가 붙은 함수이름을 가진 함수
- 예를 들어 `__add__`, `__iter__`, `__eq__` 등의 함수들을 매직 메서드라고 한다

- 매직메서드 - 오퍼레이터 정리

  - `__call__` : `()` >> 함수 호출
  - `__getattribute__` : `.`
  - `__getitem__` : `[]` >> 인덱스. 배열연산자
  - `__eq__` : `==`
  - `__add__` : `+`
  - `__sub__` : `-`
  - `__mul__` : `-`
  - `__truediv__` : `/`
  - `__floordiv__` : `//`
  - `__mod__` : `%`
  - `__pow__` : `**`
  - `__and__` : `&`
  - `__xor__` : `^`
  - `__or__` : `|`

- 매직메서드 - 비교연산자

  - `__lt__` : <
  - `__le__` : <=
  - `__eq__` : ==
  - `__ne__` : !=
  - `__gt__` : >
  - `__ge__` : >=

- 다른 매직메서드

  - `__name__` : 객체 이름
  - `__init__` : 생성자 함수

- 참고 : [링크](https://injun379.tistory.com/85)

### `__str__`과 `__repr__`의 차이?

- 두 함수 모두 str 문자열을 반환한다는 공통점이있습니다

- `__str__`은 서로 다른 자료형 간에 인터페이스를 제공하기 위해서 존재한다.(정보 출력용)

  - `str()`, `format()` 및 `print()`에 의해 호출됨
  - 객체의 '비공식적' 표현 또는 보기 좋게 인쇄 가능한 문자열 표현을 출력합니다
  - 객체정보를 str 클래스로 표현 ex) '[1, 2, 3]'

- `__repr__`은 해당 객체를 인간이 이해할 수 있는 표현으로 나타내기 위한 용도이다.(재구현, 디버깅용)

  - `repr()` 빌트인 함수로 호출되며 `__str__`이 정의되지 않았을 때 `print()`에 의해 호출됩니다
  - 동일한 객체를 다시 만드는데 사용될 수 있는 유효한 파이썬 표현식으로 나타나야 핮니다
  - 이것이 가능하지 않다면 `< function oject ~~~ >` 이러한 형식의 문자열이 반환되어야 합니다
  - 일반적으로 디버깅에 사용하므로 모호하지 않고 명확해야 합니다

```python
class Myclass():
    def __init__(self, value):
        self.member = value

    def __str__(self):
        return str({'member': self.member})

    def __repr__(self):
        return f'< Myclass object : Myclass({self.member})>'

inst = Myclass(10)
print(str(inst))    # {'member': 10}
print(repr(inst))   # < Myclass object : Myclass(10)>

print(inst.__str__())   # {'member': 10}
print(inst.__repr__())  # < Myclass object : Myclass(10)>

```

- `__str__`을 정의하지 않았을 때 `print()`는 `__repr__`를 호출한다.

```python
## __str__이 정의되지 않았을 때에는 __repr__이 호출된다
class Myclass():
    def __init__(self, value):
        self.member = value

    def __repr__(self):
        return f'< Myclass object : Myclass({self.member})>'

inst = Myclass(10)
print(inst)         #< Myclass object : Myclass(10)>
print(repr(inst))   #< Myclass object : Myclass(10)>

print(inst.__str__())   #< Myclass object : Myclass(10)>
print(inst.__repr__())  #< Myclass object : Myclass(10)>

```

- `datetime` 패키지로 `__str__`과 `__repr__` 비교하기

```python
import datetime as dt

today = dt.date.today()

print(today)        # 2023-05-11
print(repr(today))  # datetime.date(2023, 5, 11)
## repr 함수로 리턴된 문자열 그대로 입력함녀 같은 내용을 가진 객체를 생성할 수 있다.

second_today = dt.date(2023, 5, 11)
print(second_today)    # 2023-05-11
```

### 클래스에서 멤버 생성에 제약 걸기 : `__slots__` 어트리뷰트

- 클래스 혹은 인스턴스에서 사용할 수 있는 멤버(어트리뷰트) 를 `__dir__`어트리뷰트 혹은 `dir()`함수로 확인할 수 있습니다.
- 멤버를 생성하면 `__dict__`어트리뷰트에 저장되고, 외부에서 자유롭게 추가할 수 있습니다.
- 이러한 특징은 유연함으로 장점이 될 수 있지만, **멤버에 대한 제약 사항이 없기 때문에 버그의 원인**이 될 수 있습니다.
- 또한 멤버를 클래스 객체를 너무 많이 생성하면 메모리 문제가 발생할 가능성이 있습니다.

  ```python
  # 클래스 외부에서 클래스나 인스턴스를 호출해서 자유롭게 추가로 멤버를 생성할 수 있습니다.

  class Foo():
      a = 'a'

      def __init__(self):
          self.x = 0
          self.y = 0

  Foo.b = 0
  print(Foo.__dict__.get('b')) # 0

  f = Foo()
  f.z = 100
  print(f.z)                  # 100
  print(f.__dict__.get('z'))  # 100
  ```

> `__slots__`어트리뷰트를 정의하여 필드 생성에 대한 제약과 메모리 절약을 할 수 있습니다.

- 인스턴스 멤버를 생성할 때 `__slots__`에 등록되지 않은 이름은 생성할 수 없습니다.
- 클래스 멤버(스태틱 멤버)생성을 제한하지 않습니다.
- `__slots__`을 정의하면 인스턴스에는 `__dict__`어트리뷰트가 사라집니다.

```python
class FooSlot():
    __slots__ = ['x', 'y', 'k']

    def __init__(self):
        self.x = 0
        self.y = 0

## 클래스 멤버(스태틱멤버)의 멤버 생성을 제한하지 않습니다.
FooSlot.a = 'a'
print(FooSlot.a)
print(FooSlot.__dict__.get('a')) # 클래스의 __dict__는 사라지지 않습니다.


fs = FooSlot()

# __slost__ 에 정의한 이름으로만 변수를 생성할 수 있습니다.
# fs.z = 100  # AttributeError: 'FooSlot' object has no attribute 'z'
fs.k = 100
print(fs.k) # 100

# __slots__어트리뷰트를 정의하면 __dict__ 어트리뷰트가 사라집니다.
# print(fs.__dict__) # AttributeError: 'FooSlot' object has no attribute '__dict__'
```

- `__slots__`를 정의한 클래스와 정의하지 않은 클래스를 비교해보자
- `__slots__`를 정의한 클래스 : `__slots__`에 등록한 변수 이름과 `__slots__`어트리뷰트가 있음
- `__slots__`를 정의하지 않은 클래스 : `__dict__`와 `__weakref__` 어트리뷰트가 있음

```python
class FooSlot():
    __slots__ = ['x', 'y']

    def __init__(self):
        self.x = 0
        self.y = 0


class Foo():

    def __init__(self):
        self.x = 0
        self.y = 0

fs = FooSlot()
f = Foo()

print(fs.__slots__) ## list로 반환 ['x', 'y']
print(f.__dict__)   ## dict로 반환 {'x': 0, 'y': 0}

s = set(dir(FooSlot))
s2 = set(dir(Foo))

only_fooslot = s - s2
only_foo = s2 - s
print(only_fooslot, only_foo) # {'y', 'x', '__slots__'} {'__weakref__', '__dict__'}

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
    def fee(self):  # 추상클래스에서는 구현하지 않음
        pass


class Bus(Transport):
    def fee(self):
        print("Bus fee is 3 dollors")

maeul = Bus()
maeul.fee()

```

## 클래스에 property 활용하기

-

### getter와 setter

- C# 이나 JAVA에서 많이 사용되는 개념으로 객체의 필드에 직접적인 접극 대신 함수를 통해 접근하는 방식입니다.
- 이는 외부에서 변수(필드)에 주는 영향을 독립적으로 만들기 위함입니다.
  <br>
- Python의 변수는 자료형에 엄격하지 않기 때문에 `str`타입을 가지고 있다가 `int`로 바꿀 수 있습니다.
- 이러한 자유도 높은 특성은 원치 않는 오류를 발생시킵니다.
  <br> ex) 고객의 이름에 숫자가 들어가버린다던가.. 하는

```python
# 타입에 대한 강제성이 없는 파이썬에서는
# 외부에서 멤버에 접근해 엉뚱한 값으로 수정할 때 방어할 방법이 없습니다.

class User():

    def __init__(self, name : str , age : int): # 형을 강제하진 않고 쉽게 확인시키는 용도
        self.name = name
        self.age = age

u = User('홍길동', 35)
print(u.name, u.age)    # 홍길동 35

u.name = 999
u.age = -100
print(u.name, u.age)    # 999 -100 # 이름에 숫자, 나이에 음수??
```

- 위 예제와 같은 상황에 대비하여 함수를 만들어 값을 저장하고, 참조할 때 유효성 검사를 추가할 수 있습니다.
- get_name, get_age 같이 값을 조회하는 함수를 getter, set_name, set_age같이 멤버에 값을 수정하는 함수를 setter라고 합니다.
- 접근할 수 없는 변수명(`__변수명`)으로 변수명을 정의하고
  <br> getter, setter 함수에 잘못된 값에 대한 예외 처리를 하여 방어할 수 있습니다.

```python
class User():

    def __init__(self, name : str , age : int): # 형을 강제하진 않고 쉽게 확인시키는 용도
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('name have to be str type')

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('age have to be int type and positive value')

u = User('홍길동', 33)
print(u.get_name(), u.get_age()) # 홍길동 33

# u.set_name(999) # ValueError: name have to be str type
# u.set_age(-100) # ValueError: age have to be int type and positive value

u.set_name('Jack')
u.set_age(44)
print(u.get_name(), u.get_age())    # Jack 44
```

- getter, setter도 충분히 좋은 방법이지만, 함수 이름이 변수명보다 길고 ()연산자를 호출해주어야 하는 불편함이 있습니다.
- 프로퍼티 클래스는 이러한 번거로움을 줄이는데 좋은 해결책을 제시합니다.
- 프로퍼티를 사용하면 **getter, setter를 멤버 이름을 사용하는 것과 동일**하게 사용할 수 있습니다.

> `class property(fget = None, fset = None, fdel = None, doc = None)`
>
> - fget : 필드 값을 리턴하는 함수
> - fset : 필드 값을 셋팅하는 함수
> - fdel: 필드 값을 삭제하기 위한 함수
> - doc : 필드에 대한 문서 생성

- getter, setter에 의한 유호셩 검사는 그대로 적용됩니다.
- property의 리턴을 받은 변수로 호출 및 수정이 가능합니다.

```python
class User():

    def __init__(self, name : str , age : int): # 형을 강제하진 않고 쉽게 확인시키는 용도
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('name have to be str type')

    name = property(get_name, set_name) # name에 대한 프로퍼티

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('age have to be int type and positive value')

    age = property(get_age, set_age) # age에 대한 프로퍼티

u = User('홍길동', 33)
print(u.name, u.age) # 홍길동 33

# u.name = 999 # ValueError: name have to be str type
# u.age = -100 # ValueError: age have to be int type and positive value

u.name = 'Jack'
u.age = 44
print(u.name, u.age)    # Jack 44
```

- 만일 getter나 setter 중 한쪽만 필요한 경우에는 프로퍼티 객체 생성 시 인자에 None을 넘겨주면 됩니다.

```python
name = property(get_name, set_name) # getter와 setter 둘다 필요한 경우
name = property(get_name)           # getter만 필요한 경우
name = property(None, set_name)     # setter만 필요한 경우
```

# 매직 메서드

- 매직 메서드 정리한 내용 https://ziwon.github.io/post/python_magic_methods/
