# 목록
1. [BetterWay19: 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹 하지 않습니다.](#betterway-19-함수가-여러-값을-반환하는-경우-절대로-네-값-이상을-언패킹-하지-않습니다)
2. [BetterWay20: None을 반환하기보다는 예외를 발생시켜라](#betterway-20-none을-반환하기보다는-예외를-발생시켜라)
3. [BetterWay21: bytes와 str의 차이를 알아두라](#)
4. [BetterWay22: c스타일 형식 문자열을 strformat과 쓰기보다는 f-문자열 을 통한 인터폴레이션을 사용해라]()
5. [BetterWay23: 복성해라]()
6. [BetterWay24: 인패킹해라]()
7. [BetterWay25: ra용하라]()
8. [BetterWay26: 여러 수행하려면 zip을 사용해라]()


# Chapter3 : 함수

- 함수를 사용하면 큰 프로그램을 더 작고 간단한 조각으로 나누고, 각 조각이 더떤 일을 하는지 알려주는 이름을 붙일 수 있습니다.
- 함수를 사용하면...
    - 가독성이 좋아집니다.
    - 코드에 접근이 쉬워집니다.
    - 재사용과 리팩토링이 쉬워집니다.

- 파이썬 함수에는 개발자가 더 편하게 프로그래밍 할 수 있도록 해주는 여러 추가 기능이 있습니다.
- 이런 기능을 활용한다면
    - 함수의 목적을 분명히 표현
    - 코드 잡음을 줄여 함수 호출의 의도를 명확하게 함
    - 찾기 어려움 버그를 줄임


## BetterWay 19. 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹 하지 않습니다.

- BetterWay6에서 함수의 리턴이 둘 이상일 때 언패킹을 통해 받아올 수 있었습니다.
    - 원소가 두 개인 튜플에 여러 값을 넣어서 함께 반환하는 식으로 동작합니다.
    - 여러 값을 한꺼번에 처리하는 방법은 별표식(starred expression)을 통해 언패킹 처리를 할 수 있습니다.

```python

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)
print(f'최소:{minimum}, 최대:{maximum}')
# 최소:60, 최대:73

# 평균 대비 길이 비율
def get_avg_ration(numbers):
    average = sum(numbers)/len(numbers)
    scaled = [x/average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

# 별표식을 사용해서 나머지 값을 한번에 처리합니다.
longest, *middle, shortest = get_avg_ration(lengths)
print(f'최대길이 : {longest:>4.0%}') # 최대길이 : 108%
print(f'최소길이 : {shortest:>4.0%}') # 최소길이 :  89%

```

- 하지만 함수의 리턴값이 4개 이상인 경우 여러 가지 문제가 발생할 수 있습니다.
    - 반환된 변수의 타입이 겹칠 경우 어떤 값이 리턴되는 것인지 파악하기 어렵습니다.
    - 함수를 호출하는 부분과 반환 값을 언패킹 하는 부분이 길어지고, 여러가지 방법으로 줄바꿈이 일어날 수 있기 때문에 가독성이 나빠집니다.

- 이런 문제를 피하기 위해서는
    1. 함수에서 여러 값을 반환하더라도 네 개 이상을 언패킹하지 않도록 해야 합니다.
    2. 두 값을 변수에 넣고 나머지 모든 값을 한 변수에 넣거나
    3. 더 많은 값을 언패킹 해야 한다면 경량 클래스(lightweight class)나 `namedtuple`을 사용하고, 함수가 이런 값을 반환하게 설계합니다. 

```python
# 함수의 return 값이 4개 이상인 경우
def get_stats(numbers):
    ...
    return minimum, maximum, average, median, count

minumum, maximum, average, median, count = get_stats(lengths)

# 줄바꿈 경우에도 읽기 힘들어집니다.
minumum, maximum, average, median, count = get_stats(
    lengths)

minumum, maximum, average, median, count = \
    get_stats(lengths)

minumum, maximum, average, 
median, count = get_stats(lengths)

(minumum, maximum, average, median, count
 ) = get_stats(lengths)
```

### 기억해야 할 Point
> - 함수가 여러 값을 반환하기 위해 값을 튜플에 넣어서 반환하고, 호출하는 쪽에서는 파이썬 언패킹 구문을 사용할 수 있습니다.<br>
> - 함수가 반환한 여러 값을, 모든 값을 처리하는 별표 식을 사용해 언패킹이 가능합니다.<br>
> - 언패킹 구문에 변수가 네 개 이상 나오면 실수하기 쉬우므로 변수를 3개 이하로 사용합니다.<br>
> - 4개 이상이 반환되어야만 한다면, 작은 클래스를 반환하거나, `namedtuple`인스턴스를 반환합니다.<br>

<br>

## BetterWay 20. None을 반환하기보다는 예외를 발생시켜라

- 파이썬 프로그래머들은 유틸리티 함수(도우미 함수)를 작성할 때 반환 값을 `None`로 하면서 이런 경우에 대한 로직을 처리하려는 경향이 있습니다.
    - 경우에 따라서 맞는 결정으로 보일 수 있습니다.
    - 하지만 `None`을 반환하는 경우 반환 값에 대해 조건문`if`를 수행하는 경우 다른 반환값의 경우가 `0`인 경우 `False`처럼 동작하기 때문에 `None`와 `0`을 구분할 수 없습니다.

```python
## 이렇게 특이한 경우 None을 반환하는 경우
def careful_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

## 제수가 0이 입력되면 None을 반환하는 위 함수를 활용해 문자열이 출력됩니다.
x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('잘못된 입력')

## 숫자 0 을 반환하지만 False처럼 행동
x, y = 0, 5
result = careful_divide(x, y)
if not result: ## result = 0 인데 조건식에 들어가면 False로 적용됨(None과 같은 동작을 함)
    print('잘못된 입력') # 이 코드가 실해오디는데 사실 이 코드가 실행되면 안됨..

## 조건문에서 0의 동작
assert not 0 == True
assert 0 == False
```

- `None`반환으로 인한 혼동을 막기 위해서 두 가지 방법을 사용합니다.
    1. 반환값을 2-tuple(Betterway19)로 분리하는 것입니다.
        - 이 방법은 호출하는 쪽에서 튜플을 언패킹해야 합니다.
        - 이 방법의 문제점은 호출하는 쪽에서 튜플의 첫 번째 결과를 쉽게 무시할 수 있다는 것입니다.
        
    2. 이렇게 특이한 경우의 결과를 `None`으로 반환하지 않고 `Exception`을 호출한 쪽으로 발생시켜서 호출자가 이를 처리하게 합니다.
        - `ZeroDivisionError`가 발생한 경우 `ValueError`로 바꿔 던져 호출한 쪽에 입력 값이 잘못되었음을 알립니다.

```python
## 첫 번째 해결방법 - 2-tuple 사용
def careful_divide(a, b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

x, y = 0, 5
success, result = careful_divide(x, y)
if not success:
    print('잘못된 입력') # 이 코드가 실행되면 안됨..

## 문제점.. _ 를 통해 사용하지 않는 변수로 지정하고 무시당할 수 있습니다.
## 이렇게 무시했을 때 원인을 찾기 어려워집니다.
x, y = 0, 5
_, result = careful_divide(x, y)
if not success:
    print('잘못된 입력') # 이 코드가 실행되면 안됨..
```

```python
## 두 번째 해결방법 - Exception 날리기
def careful_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력입니다.')

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('잘못된 입력')
else:
    print('결과는 %.1f 입니다.' % result)

# 결과는 2.5 입니다.
```
<br>

- 두 번째 해결방법을 확장해서 타입 애너테이션을 사용하는 코드에도 적용할 수 있습니다.
    - 반환값이 항상 `float`이고 `None`이 반환되지 않음을 알릴 수 있습니다.
    - 파이썬의 점진적 타입 지정(Gradual typing)에는 함수 인터페이스에 예외가 표현되는지 표현하는 방법(검증 오류(checked exception))이 의도적으로 제외되었습니다.
    - 그 대신에 호출자가 어떤 Exception을 잡아내야 할 지 결정할 때 문서를 참조할 것으로 가정하고, 예외를 문서에 명시애햐 합니다.

> 검증 오류(checked exception): 에러 종류 중 반드시 명시적으로 처리해야 하기 때문에 Checked Exception이라고 합니다. 프로그램의 제어 밖에 있는 예외들입니다. 예외처리 참고: https://exponential-e.tistory.com/53

> 점진적 타입 지정(Gradual typing): 프로그램의 일부는 동적으로 타이핑하고 다른 부분은 정적으로 타이핑하는 방법입니다. 즉, 프로그래머는 자신이 입력하고 싶은 프로그램 부분을 선택할 수 있습니다.

```python
def careful_divide(a: float, b: float) -> float:
    """a를 b로 나눕니다.
    Raise:
        ValueError: b가 0이어서 나눗셈을 할 수 없을 때
    """
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력입니다.')
```
<br>

### 기억해야 할 Point
> - 특별한 의미를 표시하는 `None`을 반환하는 함수를 사용하면 `None`과 다른값(0이나 빈 문자열)이 조건문에서 `False`로 평가될 수 있기 때문에 실수하기 쉽습니다.<br>
> - 특별한 상황을 표현하기 위해 `None`대신 예외를 발생시킵니다. 또한 문서에 예외 정보를 기록해 호출자가 예외를 제대로 처리하도록 알려줍니다.<br>
> - 함수가 특별한 경우를 포함하는 그 어떤 경우에도 `None`을 반환하지 않는다는 사실을 타입 애너테이션으로 명시할 수 있습니다.<br>

<br>

## BetterWay 21. 변수 영역과 클로저의 상호작용 방식을 이해해라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay 22. 변수 위치 인자를 사용해 시각적인 잡음을 줄여라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay 23. 키워드 인자로 선택적인 기능을 제공하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay 24. None과 독스트링을 사용해 동적인 디폴트 인자를 지정하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay 25. 위치로만 인자를 지정하게 하거나 키워드로만 인자를 지정하게 해서 함수 호출을 명확하게 만들어라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>

## BetterWay 26. functools.wrap을 사용해 함수 데코레이터를 정의하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

<br>