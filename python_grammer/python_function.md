# python 함수 관련 정리

## 제너레이터 (Generator)

1. Generator란?

- `yield` 구문을 가지고 있으면서 iterator를 반환하는 함수.

  > iterator란 next()메소드를 통해 데이터에 순차적으로 접근이 가능한 객체

- 모든 Genrator 는 Iterator이다.

2. 특징 : generator를 사용하는 이유!!

   1. 메모리 효율성

   - memory를 효율적으로 사용한다
   - list는 데이터를 한 번에 메모리에 적재하기 때문에 메모리가 부족하면 프로그램이 죽을 수 있음
   - 반면 제너레이터는 **데이터에 접근할 때 마다 메모리에 적재**하기 때문에 큰 데이터를 다루는 경우 list보다 안정적이고 효율적이다.
   - **genrator를 이용해서 iterator를 만들어야 하는 이유!**

   ```python
   # sys.getsizeof(object) : Return the size of object in bytes.

   import sys
   li1 = [i for i in range(100)]
   li2 = [i for i in range(1000)]

   print(sys.getsizeof(li1))   # 920
   print(sys.getsizeof(li2))   # 8856

   ge1 = (i for i in range(100))
   ge2 = (i for i in range(1000))
   print(sys.getsizeof(ge1))   # 104
   print(sys.getsizeof(ge2))   # 104

   # generator를 이용하면 크기가 커져도 항상 동일한 크기를 할당받는다.

   # list 는 list 안의 모든 데이터를 메모리에 적재하기 때문에 list의 크기만큼 차지하는 메모리 사이즈가 늘어남
   # generator의 경우 값을 한꺼번에 적재하지 않고, `next()`메소드를 통해 차례로 값에 접근할 때 마다 메모리에 적재하는 방식
   ```

   2. 게으른 연산 (지연 평가 방식)

   - 계산 결과 값이 필요할 때까지 계산을 늦춘다.
   - list comprehension을 수행할 때 모든 값의 연산을 먼저 수행하기 때문에 수행되는 연산이 오래걸리거나 연산된 값에 접근하는 시간이 걸린다
   - 반면, 제너레이터는 `yield` 로 값에 접근하기 때문에 수행 시간이 긴 연산을 필요한 순간까지 늦출 수 있다.

   ```python
   def sleep_f(x):
       print('sleep...')
       time.sleep(1)
       return x

   # list
   l = [sleep_func(x) for x in range(3)]
   for i in gen:
       print(i)
   # sleep...
   # sleep...
   # sleep...
   # 0
   # 1
   # 2

   # list comprehension을 수행할 때 list의 모든 값에 대한 계산을 먼저 수행하기 때문에
   # sleep_f() 함수가 range(n)의 n값 만큼 한 번에 수행한다.
   # sleep_f()의 수행 시간이 길거나 list 길이 가 길다면 프로그램에게 부담으로 작용


   # generator
   gen = (sleep_func(x) for x in range(5))
   for i in gen:
       print(i)

   # sleep...
   # 0
   # sleep...
   # 1
   # sleep...
   # 2

   # generator를 생성할때 실제 값을 로딩하지 않고, for문이 수행될 때 하나씩 sleep_f() 함수를 수행하며 값을 불러움
   # 수행 시간이 긴 ㅇ녀산을 필요한 순간까지 늦추는 효과를 가져옴

   ```

- generator를 시작하는 tip

```python
# 위의 코드 형식을 아래 코드 형식으로 바꿔본다!
def something():
result = []
for ... in ...:
    result.append(x)
	  return result

def iter_sometime():
    for ... in ...:
        yield x
# def something()  # 정말로 리스트 구조가 필요할때만
#     return list(iter_something())
```

3. generator expression( yield expression )

- generator 함수를 쉽게 사용할 수 있도록 generator expression을 제공한다
- list comprehension과 비슷하지만, `[]`대신 `()`를 사용하면 된다.

```python
li = [i for i in range(10) if i%2]
print(li)       # [1, 3, 5, 7, 9]

ge = (i for i in range(10) if i%2)
print(ge)           # <generator object <genexpr> at 0x7f0e61249770>
print(next(ge))     # 1
print(next(ge))     # 3
print(next(ge))     # 5
print(next(ge))     # 7
print(next(ge))     # 9
# print(next(ge))   # StopIteration

```

4. generator 예제

- generator는 `__iter__`와 `__next__`를 가지고 있다

```python
def generator_f():
    yield 1
    yield 2
    yield 3

print(generator_f())    # <generator object generator_f at 0x7f0e612493f0>
print(hasattr(generator_f(),'__iter__'))    # True
print(hasattr(generator_f(),'__next__'))    # True
```

- `yield`는 오른쪽값을 함수 밖으로 산출(생성해서 반환)하고, 실행을 양보합니다.
- return과 yield의 차이는 return은 값을 반환하고 함수를 종료하지만, yield는 함수내부에서 밖으로 값을 순차적으로 전달
- send를 통해 main routine의 값을 받아와 양방향 통신도 할 수 있습니다
- 즉, 제너레이터는 제너레이터의 객체(함수)가 호출되었을 때, yield 오른쪽의 값을 반환하고 바로 다음 yield의 위치를 기억한 상태로 다음 제네레이터 호출(실행 양보)을 기다립니다.

```python
def generator_f():
    yield 1
    yield 2
    yield 3

g = generator_f() # yield를 통해 생성된 제너레이터
print(g)
print(g.__next__()) # 1
print(g.__next__()) # 2
print(g.__next__()) # 3
```

- 제너레이터로 `range()` 함수 만들어보기

```python
def gen_range(start, stop):
    while start < stop:
        yield start
        start += 1

print(gen_range(0,10))  # <generator object gen_range at 0x7f0e612492a0>

li = [i for i in gen_range(0,10)]
print(li)           #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

- `send()`함수로 메인루틴에서 값 전달하기
- 아직 정확하게 이해가 되진 않음..

```python
# 메인 루틴인 함수 호출 영역에서 제너레이터로 값을 전달시킬 수 있다.
# yield는 왼쪽 변수를 할당하여 메인루틴에서 값을 전달받을 수 있다
# 이럴 통해 코루틴(coroutin)의 개념인 양방향 통신 가능

def generator_send():
    main_routine_value = 0
    while True:
        main_routine_value = yield
        yield main_routine_value * 2
gen = generator_send()
print(gen)
next(gen) # 주석처리하면 error # TypeError: can't send non-None value to a just-started generator
# print(next(gen)) ## 두번째부터 TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

print(gen.send(100))
next(gen) # next를 해줘야 다음 yield에서 대기하기 때문에 next 해주지 않으면 멈춰있음
print(gen.send(300))

```

- 참조 : [링크](https://velog.io/@jewon119/TIL30.-Python-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0Generator-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC)

### generator와 return

- generator는 함수 끝에 도달하면 StopIteraion 예외가 발생합니다.
- return도 함수를 끝내므로 return을 사용해서 함수 중간에 빠져나오면 StopIteration 예외가 발생합니다.
- generator안에서 return에 반환값을 지정하면 StopIterator 예외의 에러 메시지로 들어갑니다.

```python
def gen_ret():
    yield 1
    yield 2
    return 'return에 지정한 값'

try:
    g = gen_ret()
    print(next(g))
    print(next(g))
    print(next(g))  # 예외 발생
except StopIteration as e:
    print(e)    # return에 지정한 값

```

- 참조 : [링크](https://dojang.io/mod/page/view.php?id=2412)

### `yield from` 사용하기

- 반복 가능한 객체로 generator를 만들고 싶을 때 for 문을 사용하지 않아도 되는 문법
- iterble 객체, Iterator, generator 객체 모두 사용 가능 (python 3.3 이후 문법)

```python
## for문 사용하는 방법
def iter_gen(x):
    for i in x:
        yield i

x = [1,2,3]

for i in iter_gen(x):
    print(i)

## yield from 사용하는 방법
def iter_gen2(x):
    yield from x

for i in iter_gen2(x):
    print(i)

```

<br>

---

## 이터러블 (iterable)

- python에서 iterable 정의

  > 멤버를 하나씩 반환 가능한 object로 **list**, **tuple**,**str** 같은 sequence 타입
  > **dict** **file** 타입
  > `__iter__()`혹은 `__getitem__()` 메서드가 정의된 클래스의 object를 iterable object라고 한다.

- 컨벤션 오브젝트를 제외하고 예를 들면 대표적으로
  - range
  - enumerate
  - map
  - zip
  - sorted
  - reversed
  - filter
  - etc...

## 이터레이터 (Iterator)

- `next()`메서드를 호출할 때 다음값을 생성해내는 상태를 가진 헬퍼 객체.
- 값을 차례대로 꺼낼 수 있는 객체

- python 에서 Iterator 정의

  > 데이터 스트림을 나타내는 객체로 Iterator의 `next()` 메서드를 반복해서 호출하면 스트림의 연속 요소가 반환됩니다.<br>
  > 더 이상 사용할 수 있는 데이터가 없으면 대신 StopIteration 예외가 발생합니다. <br>
  > 이 시점에서 iterator 객체는 소진되어 빈 상태가 됩니다. (next를 다시 사용하면 StopIteration 발생)<br>
  > Iterator는 Iterator object를 반환하는 `__iter__()` 메서드를 가져야 하므로 모든 Iterator는 iterable입니다. (iterable 정의) <br>
  > Iterator는 iterable이 허용되는 대부분의 장소에서 사용될 수 있습니다.<br>

- iterable 하다고 모두 Itearator는 아니다.

```python
# list 객체는 iterable 하지만 Iterator는 아니다.
# Iterator는 next를 사용할 수 있어야 한다.
l = [1,2,3]
next(l)     # TypeError: 'list' object is not an iterator
```

- Iterator로 사용하고 싶다면 Iterator를 반환하는 `iter()`메서드를 사용해주면 됨

```python
l = [1,2,3]
next(l)     # TypeError: 'list' object is not an iterator

liter = iter(l)  # 혹은 liter = l.__iter__()
next(liter) # 1
next(liter) # 2
next(liter) # 3
# next(liter) # error StopIteration()

```

- `list` 나 `tuple` 같은 object 를 사용할때 굳이 `iter()` 함수를 사용하지 않아도 for 문을 사용하여 순차적으로 접근이 가능한 이유<br>
  --> for 문으로 looping 하는 동안, python 내부에서 임시로 list를 iterator로 자동 변환해주었기 때문

> `for`에 반복 가능한 객체를 사용했을 때, `__iter__`로 이터레이터를 얻고 `__next__`로 한 단계식 연산을 하고 StopIteration을 발생시켜 반복문을 끝낸다

> 시퀀스 객체와 반복 가능한 객체 <br>
> 요소의 순서가 정해져 있고 연속적으로 이어져 있으면 시퀀스 객체, 요소의 순서와는 상관없이 요소를 한 번에 하나씩 꺼낼 수 있으면 반복 가능한 객체입니다.

<br>

### Iterator 만들어보기 1 (`__iter__`)

- `__iter__`와 `__next__` 메서드를 구현하는 방식으로 이터레이터

```python
class Myiterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

for i in Myiterator(3):
    print(i, end=' ')   # 0 1 2

print()
it = Myiterator(3)
print(it.__next__())    # 0
print(it.__next__())    # 1
print(it.__next__())    # 2
# print(it.__next__()) # StopIteration

```

### Iterator 만들어보기 2 (`__getitem__`)

- `__getitem__`을 구현한 이터레이터
- 즉, 인덱스로 접근할 수 있는 이터레이터 만들어보기
- `_next__`메서드 정의 없이도 인덱스로 접근 가능한 Iterator생성이 가능하다. (단 next 메서드 사용은 안됨)

```python

class Myiterator:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

print(Myiterator(3)[0], Myiterator(3)[1], Myiterator(3)[2])

for i in Myiterator(3):
    print(i, end=' ')

# a = Myiterator(3)
# a.__next__()    # AttributeError: 'Myiterator' object has no attribute '__next__'
```

---

## 데코레이터 (decorator) - 함수

- 데코레이터는 파이썬에서 함수나 클래스를 꾸며주는 역할을 합니다.
- 데코레이터는 함수나 클래스를 감싸는 함수로, 기존의 함수나 클래스에 추가적인 기능을 제공합니다.

> 데코레이터를 정의한 후 `@decoratorname`을 데코레이터를 적용할 함수 정의 위에 적어주면 된다.

```python
# 함수 데코레이터 정의
def deco(func):
    def wrap_func():
        print('start')
        func()

    return wrap_func

# 데코레이터 적용한 함수
@deco
def say_hi():
    print('안녕하세요')


say_hi()
# start
# 안녕하세요
```

- 함수의 인자를 전달해야 하는 경우에는 데코레이터 내부 wrapper 함수 인자 개수를 맞추어 받아주어야 한다

```python
def pre(func):  # 제너레이터 적용된 함수가 호출된 것이 func로
    def wrapper(iterable): # 데코레이터가 적용된 함수의 인자를 iterable로 받아옴
        iterable = list(map(int, iterable))
        return func(iterable)
    return wrapper

@pre
def cal_avg(li):
    return sum(li) / len(li)

print(cal_avg(['1', 2, 3, '4']))    # 2.5

```

- 하나의 함수에 여러 개의 데코레이터 사용이 가능하다

```python
# 데코레이터 여러개 테스트해보기
def print_world(func):
    def wrap_func():
        print('world')
        func()
    return wrap_func

def print_hello(func): # def decorator_name(below function)
    def wrap_func():
        print('hello')
        func()
    return wrap_func

# 함수 선언부에서 한 줄씩 올라가면서 확인하는듯 하오...
@print_world
@print_hello
def func1():
    print('function1 입니다.')

func1()
# world
# hello
# function1 입니다.
```

- 여러개를 쓸 때는 어떻게 객체가 이동하는 것인지 확인
- 출력을 확인해보면 decorator2의 wrapper가 decorator1의 func로 전달된다.
- 함수 실행 순서는 hello > decoretor2 > decorator1 이 된다.

```python
def decorator1(func):
    def wrapper():
        func()
    print('decorator1 - func id:', id(func))
    print('decorator1 wapper id:', id(wrapper))
    return wrapper

def decorator2(func):
    def wrapper():
        func()
    print('decorator2 - func id:', id(func))
    print('decorator2 wapper id:', id(wrapper))
    return wrapper

# 데코레이터를 여러 개 지정 wrapper 함수가 위의 decorator의 func로 들어감
@decorator1
@decorator2
def hello():
    print('hello')

hello()
print(id(hello))
# 가장 바깥쪽 wrapper 함수와 id가 같다!

## 출력
# decorator2 - func id: 140661872843008
# decorator2 wapper id: 140661872846320
# decorator1 - func id: 140661872846320
# decorator1 wapper id: 140661872846464
# hello
# 140661872846464
```

- 데코레이터에 아규먼트를 전달하고 싶을 때에는 한번 더 함수로 감싸주면 된다.

```python
# 데코레이터에 argument를 넣는 방법
# 한번 더 감싸줘야 함. 여러개 전달 가능
def deco1(name, age):
    print(name, age)
    def function_getter(func):
        def wrapper():
            print('decorator1')
            func()
        return wrapper
    return function_getter

# 데코레이터를 여러 개 지정
@deco1('hello world!', 10)
def hello():
    print('hello')

hello()

# hello world! 10
# decorator1
# hello
```

<br>

---

## 데코레이터 (decorator) - 클래스

- 데코레이터를 클래스로 생성할 수 있습니다.

-

<br>

---

## 람다함수 (lambda)

- 람다는 식 형대로 되어있어 람다 표현식(lambda expression)이라고 부릅니다. <br> 함수 이름이 없어 익명 함수라고도 부릅니다.
- 간단하게 작성할 수 있어 다른 함수의 인자로 넣어 줄 때 주로 사용합니다.
- 람다식으로 표현한 object는 함수(function) 객체입니다.
- 대표적으로 map, filter 등의 함수의 function 인자로 자주 사용합니다.

> 기본 표현식 <br> `lambda` 인자1, 인자2, ... : 표현식(expression)

```python
# lambda로 생성한 object는 function 타입
lambda x: x+10
# <function <lambda> at 0x0000023EDDAEFAF0>

#식 자체로 함수를 사용할 수 있습니다.
(lambda x: x+10)(3)  #13

# 람다 함수 객체를 사용해봅시다
func = lambda x : x + 10
print(func(4)) #14

func2 = lambda x , y : x +y
func2(1,2) #3

func3 = lambda x, y, z : 100*x + 10*y + z
func3(1,2,3) # 123
```

<br>

---

## 클로저 (Closuer)

- 클로저(Closure)는 자신이 생성(선언)된 외부 환경을 기억(Capture)하는 함수 객체이다
- 대표적으로 Python, Javascript, Go lang 에서 지원한다
- 클로저를 지원하려면 언어 차원에서 함수를 일급 객체(First-class object)로 취급해야 한다

### Python 에서 클로저

- 파이썬에서는 함수도 객체(Object)이다
- 클로저에 저장되는 외부 변수는 함수 객체 내의 `__closure__`라는 특별한 변수에 저장된다
- 함수 객체에서 `__closure__` 를 통해 저장된 값을 확인할 수 있다
- `__closure__`의 타입은 `cell` 타입으로 인덱싱과 `cell_contents()` 메서드로 값을 확인할 수 있다

```python
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure_x10 = outer_func(10)
print(closure_x10(30))                  #40
dir(closure_x10)                        # attribute __closure__ 있음을 확인
print(closure_x10.__closure__)          # cell 속성. cell 객체에 int 값 1개 가지고있음
print(closure_x10.__closure__[0])       # 셀 객체에 접근 1개있으니까 index 0
print(type(closure_x10.__closure__[0])) # class cell
dir(closure_x10.__closure__[0])         # cell_contests라는 메서드가 있음
closure_x10.__closure__[0].cell_contents # 10
```

### 실무에서 클로저는 어떻게 활용될까?

- 일반적으로 클로저 패턴보다는 **데코레이터 패턴**으로 사용
- Python은 클로저 패턴이 활발하게 사용되는 언어는 아님
- 정보은닉의 이유로 사용.

<br>

---

## 순수함수

- 순수함수는 함수는 외부 환경을 변화시키지 않는 함수를 의미한다
- 순수함수는 주변 환경을 변화시키지 않기 때문에, 순수함수로 함수형 프로그래밍을 할 경우 오류를 줄이고 안정성을 높인다
- 단순 더하는 함수로 예제를 보자

  ```python
  # 순수함수
  def add_pure(a, b):
      return a + b
  # 함수 외부 환경에 영향이 전혀 없는 함수 구조. 순수함수이다

  # 비 순수함수
  c = 100
  def add1(a,b):
      return a + b + c
  # c 값이 변경됨에 따라 에러가 발생할 수도 있고, 리턴이 달라짐. 순수함수가 아님

  c = 100
  def add2(a,b):
      c = b
      return a + b
  # 함수 외부의 값을 변경하므로 순수함수가 아니다.
  ```
