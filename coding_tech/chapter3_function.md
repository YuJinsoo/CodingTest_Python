# 목록
1. [BetterWay19: 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹 하지 않습니다.](#betterway-19-함수가-여러-값을-반환하는-경우-절대로-네-값-이상을-언패킹-하지-않습니다)
2. [BetterWay20: None을 반환하기보다는 예외를 발생시켜라](#betterway-20-none을-반환하기보다는-예외를-발생시켜라)
3. [BetterWay21: 변수 영역과 클로저의 상호작용 방식을 이해해라](#betterway-21-변수-영역과-클로저의-상호작용-방식을-이해해라)
4. [BetterWay22: 변수 위치 인자를 사용해 시각적인 잡음을 줄여라](#betterway-22-변수-위치-인자를-사용해-시각적인-잡음을-줄여라)
5. [BetterWay23: 키워드 인자로 선택적인 기능을 제공하라](#betterway-23-키워드-인자로-선택적인-기능을-제공하라)
6. [BetterWay24: None과 독스트링을 사용해 동적인 디폴트 인자를 지정하라](#betterway-24-none과-독스트링을-사용해-동적인-디폴트-인자를-지정하라)
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

- 숫자로 이루어진 list를 정렬할 때 list의 앞 부분에는 우선순위를 부여한 몇몇 숫자를 위치시켜야 하는 예제를 생각해보자.
    - 이 패턴은 사용자 인터페이스를 표시하면서 중요한 메시지나 예외적인 이벤트를 다른 것보다 우선해 표시하고 싶을 때 유용합니다.
- 가장 일반적인 방법은 list의 `sort()`메서드에 `key`인자로 도우미 함수를 전달하는 것입니다.
    - list는 각 원소를 정렬할 때 이 도우미 함수가 반환하는 값을 기준으로 사용합니다.
    - 도우미 함수는 주어진 원소의 우선순위를 검사해서 정렬 기준값을 적절히 조절해줍니다.

```python
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(numbers, group)
print(numbers) # [2, 3, 5, 7, 1, 4, 6, 8]
```

### 위 예제가 정확하게 동작하는 이유 세 가지
1. python은 클로저를 지원합니다.
    - `클로저`란 자신이 정의된 영역 밖의 변수를 참조하는 함수입니다.
    - `클로저`로 인해 도우미 함수가 `sort_priority()`함수의 `group` 인자를 접근할 수 있습니다.
2. 파이썬에서 함수는 일급객체(일급 시민) 입니다.
    - 일급 객체라고 하면...
    - 직접 가리킬 수 있고,
    - 변수에 대입하거나
    - 다른 함수에 인자로 전달할 수 있으며,
    - 식이나 if문에서 함수를 비교하거나 함수에서 반환하는 것이 가능합니다.
    - 이런 특징으로 인해 `sort`메서드는 클로저 함수를 `key`인자로 받을 수 있습니다.
3. python에는 시퀀스(튜플 포함)을 비교하는 구체적인 규칙이 있습니다.
    - python의 시퀀스는 0번 시퀀스부터 차례대로 서로 순서 비교를 하여 모든 원소를 다 비교하거나 경과가 정해질 때까지 계속합니다.
    - 이로 인해 `helper()`클로저가 반환하는 튜플이 서로 다른 두 그룹을 정렬하는 기준 역할을 합니다.

<br>

- 위 예제에 추가적인 기능으로 우선순위가 있는 요소가 들어왔을 때 알림을 플래그를 통해 전달하는 기능을 추가하는 경우를 생각해봅시다.
- found라는 변수를 플래그로 활용하여 `group`에 해당하는 원소가 있다면 found에 True를 대입하여 반환하면 될 것이라고 생각하기 쉽습니다. **하지만 실제로 반환되는 값은 `True`가 아니라 `False` 입니다.**
    - `found`변수는 `helper` 도우미 함수 의 영역에서 `True`로 대입됩니다. `helper`함수 영역 안에 새로운 `found`변수를 정의하는 것으로 취급되어 `sort_priority2()` 내부의 `found` 변수에 값이 대입하는 것으로 취급되지 않습니다.

- 이 문제는 `영역 지정 버그`라고 부르기도 합니다.
    - 이 동작은 언어 설계에서 의도된 부분입니다.
    - 함수에서 사용한 지역 변수가 그 함수를 포함하고 잇는 모듈 영역을 더럽히지 못하게 막는 역할을 합니다.
    - 즉, 이런 식으로 처리하지 않으면 함수 내에서 사용한 모든 대입문이 전역 모듈 영역에 쓰레기 변수를 추가하게 됩니다. 

```python
def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found
    
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
result = sort_priority2(numbers, group)
print(numbers, result) # [2, 3, 5, 7, 1, 4, 6, 8] False
```

- 클로저 안에서 사용하는 변수가 클로저를 감싼 영역의 변수를 사용하고 싶을 때에는 `nonlocal`이라는 예약어를 사용하면 됩니다.
    - `nonlocal`은 대입할 데이터가 클로저 밖에 있어 다른 영역에 속한다는 것을 알려줍니다.
    - 변수 대입시 직접 모듈 영역(전역 영역)을 사용해야 한다고 지정하는 `global`을 보완합니다.
    - **하지만 간단한 함수 외에는 어떤 경우라도 `nonlocal`사용을 지양합니다.**
    - 특히 함수가 길고 `nonlocal`문이 지정한 변수와 대입이 이뤄지는 위치와의 거리가 멀면 함수 동작을 이해하기 힘들어지기 때문입니다.

> Python에서 변수를 찾는 순서<br>
> 1. 현재 함수의 영역
> 2. 현재 함수를 둘러썬 영역 (현재 함수를 둘러싸고 있는 함수 등)
> 3. 현재 코드가 들어 있는 모듈의 영역 (전역영영(global-scope)이라고도 부름)
> 4. 내장 영역(built-in scope)

<br>


```python
def sort_priority2(values, group):
    found = False
    def helper(x):
        nonlocal found ## hleper영역에 클로저 함수 밖의 found임을 알려줌
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found
    
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
result = sort_priority2(numbers, group)
print(numbers, result) # [2, 3, 5, 7, 1, 4, 6, 8] True
```

<br>

- `nonlocal`사용을 피하려면, 도우미 함수를 사용하거나 클래스를 작성해서 정의하여 활용하는 것이 코드는 길어지지만, 이해하기 쉽습니다.
```python
class Sorter():
    def __init__(self, group):
        self.group = group
        self.found = False
    
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1,)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
```
<br>

### 기억해야 할 Point
> - 클로저 함수는 자신의 정의된 영역 외부에서 정의된 변수도 참조할 수 있습니다.<br>
> - 기본적으로 클로저 내부에 사용한 대입문은 클로저를 감싸는 영역에 영향을 끼칠 수 없습니다.<br>
> - 클로저가 자신을 감싸는 영역의 변수를 변경한다는 사실을 표시할 때는 `nonlocal`문을 사용합니다.<br>
> - 간단한 경우가 아니라면 `nonlocal`사용을 지양합니다.<br>

<br>

## BetterWay 22. 변수 위치 인자를 사용해 시각적인 잡음을 줄여라

- 위치 인자(positional argument)를 가변적으로 받을 수 있으면 함수 호출이 더 깔끔해지고 시각적 잡음도 줄어듭니다.
    - 이런 위치 인자를 가변인자(varargs)나 스타인자(star args)라고 부르기도 합니다.
- 예시
    - 디버깅 정보를 로그에 남기도 싶을 때, 인자 수가 고정되어 있으면 메시지와 값의 `list`를 받는 함수가 필요합니다.
    - 이 경우, 로그에 남길 값이 따로 없을 때도 빈 리스트를 전달해야 합니다.
    - 전달할 필요가 없을 때 전달하지 않도록 두 번째 인자(값의 list)를 생략할 수 있습니다.
    - `*` 연산자를 생략이 필요한 인자 앞에 붙이면 됩니다.

```python
# 로그 출력 함수 예제
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는', [1, 2]) # 내 숫자는: 1, 2
log('안녕', []) # 안녕

## *연산자로 두번째 인자 생략
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는', 1, 2) # 내 숫자는: 1, 2
log('안녕') # 안녕
```
<br>

- 해당 구문은 언패킹 대입문에 쓰인 별표 식과 비슷하게 활용됩니다.
- 시퀀스 자체로 전달하고 싶은 경우에는 `*` 연산자를 사용해서 전달하면, `*` 연산자는 파이썬이 시퀀스의 원소들을 함수의 위치 인자로 넘길 것입니다.
```python
favorites = [7,33,99]
log('좋아하는 숫자는', *favorites) # 좋아하는 숫자는: 7, 33, 99
```

- 이 방법에는 두 가지 문제점이 있습니다.
    1. 선택적인 위치 인자가 함수에 전달되기 전에 항상 튜플로 변환됩니다. 이런 동작 방식은 함수를 호출하는 쪽에서 제너레이터 앞에 * 연산자를 사용하면 제너레이터의 모든 원소를 얻기 위해 반복한다는 뜻입니다.
        - 이렇게 생성된 튜플은 제너레이터가 만들어낸 모든 값을 포함하며, 이로 인해 메모리를 아주 많이 소비하거나 프로그램이 중단될 수 있습니다.
        - 즉 제너레이터를 사용하는 의미가 사라집니다.
    2. 함수에 새로운 위치 인자를 추기하면 해당 함수를 호출한느 모든 코드를 변경해야 합니다. 이미 가변 인자가 존재하는 함수 인자 목록의 앞부분에 위치 인자를 추가하려고 시도하면, 기존 코드를 변경하지 않는 경우 호출하는 코드가 미묘하게 깨질 수도 있습니다.
        - 즉 가변인자 앞에 새로운 일반 인자를 추가하는 경우 동작하는 부분의 코드를 확인해서 수정이 필요합니다.
        - 이렇게 해서 발생한 버그의 경우 원인을 추적하기 어려워집니다.
        - **이런 가능성을 없애려면 `*args`를 받아들이는 함수를 확장할 때는 키워드 기반의 인자만 사용해야 합니다.**
        - 혹은 더 방어적으로 프로그래밍 하려면, 타입 애너케이션을 사용해도 됩니다.

```python
## 첫 번째 문제점. 제너레이터의 모든 값을 한번에 불러와 메모리 문제 발생
def my_generator():
    for i in range(10):
        yield i
        
def my_func(*args):
    print(args)
    
it = my_generator()
my_func(*it) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
## 제너레이터가 아니라 제너레이터로 생성되는 모든 값을 한 번에 인자로 넘겨줍니다.

def my_func2(args):
    print(args)

it = my_generator()
my_func(it) # (<generator object my_generator at 0x000001871B1C0A50>,)



## 두 번째 문제점. 
def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {value_str}')

log(1, '좋아하는 숯자는', 7, 33)     # 1 - 좋아하는 숮자는: 7, 33
log(1, '안녕')                      # 1 - 안녕
log('좋아하는 숮자는', 7, 33)        # 좋아하는 숮자는 - 7: 33 ## 예전코드 호출
```
<br>

- `*args`를 받는 함수는 인자 목록에서 가변적인 부분에 들어가는 인자의 개수가 처리하기 좋을 정도로 충분이 작다는 사살을 이미 알고 있으 때에 적합합니다.
- `*args`는 여러 리터럴이나 변수 이름을 함께 전달하는 함수 호출에 이상적입니다.
- `*args`는 주로 프로그래머의 편의와 코드 가독성을 위한 기능입니다.


### 기억해야 할 Point
> - `def`문에서 `*args`를 사용하면 함수가 가변 위치 기반 인자를 받을 수 있습니다.<br>
> - `*`연산자를 사용하면 가변 인자를 받는 함수에게 시퀀스 내의 원소들을 전달할 수 있다.<br>
> - 제너레이터에 `*`연산자를 사용하면 프로그램이 메모리를 모두 소진하고 중단될 수 있다.<br>
> - `*args`를 받는 함수에 새로운 위치 기반 인자를 넣으면 감지하기 힘든 버그가 생길 수 있다.<br>

<br>

## BetterWay 23. 키워드 인자로 선택적인 기능을 제공하라

- Python도 다른 언어와 마찬가지로 함수를 호출할 때 위치에 따라 인자를 넘길 수 있습니다.

```python
def remainder(num, div):
    return num % div

## 파라메터 num에 인자 20, 파라메터 div에 인자 7이 넘어갑니다.
assert remainder(20, 7) == 6
```
<br>

- Python 함수에서는 모든 일반적인 인자를 키워드르 사용해 넘길 수 있습니다.
- 키워드를 사용해 인자를 넘길 떄에는 함수 호출 괄호 내부에서 파라미터 이름을 사용합니다.
    - 파라미터 이름을 사용한 인자 할당 이후의 변수들은 모두 키워드를 사용해 인자를 넘겨주어야 에러가 발생하지 않습니다.

```python
def remainder(num, div):
    return num % div

assert remainder(20, 7) == 6
assert remainder(20, div=7) == 6
assert remainder(num=20, 7) == 6 ## StntaxError
assert remainder(num=20, div=7) == 6
assert remainder(div=7, num=20) == 6
```

- 딕셔너리를 이용해 키워드 인자를 넘길 수 있습니다.
- 딕셔너리를 함수의 인자로 넘겨줄 때에는 `**`연산자를 붙여주어야 합니다.
    - `**`연산자는 파있너이  딕셔너리에 들어 있는 값을 함수에 전달하되, 각 값에 대응하는 키를 키워드로 사용하도록 명령합니다.
    - 파라메터이름과 딕셔너리의 key 이름이 일치하는 것으로 할당됩니다.

- `**`연산자를 위치인자나 키워드 인자와 섞어서 함수 호출이 가능합니다.
```python
## 딕셔너리로 키워드 인자 전달
my_kwargs = {
    'num': 20,
    'div': 7
}

def remainder(num, div):
    return num % div

assert remainder(**my_kwargs) == 6

## 위치인자와 딕셔너리로 키워드 인자 전달 같이 사용
my_kwargs = {
    'div': 7
}

def remainder(num, div):
    return num % div

assert remainder(num = 20, **my_kwargs) == 6
```
<br>

- 아무 키워드 인자를 받는 함수를 만들고 싶다면, 모든 키워드 인자를 `dict`에 모아주는 **kwargs라는 파라미터를 사용합니다.

```python
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_parameters(alpha=1.5, beta=9, 감마=4)
# alpha: 1.5
# beta: 9
# 감마: 4
```

### 키워드 인자가 제공하는 유연성 활용으로 얻는 세 가지 이점
1. 코드를 처음 보는 사람들에게 함수 호출의 의미를 명확히 알려줄 수 있습니다.
    - 구현을 보지 않고 어떤 목적으로 사용하는 파라미터인지 알 수 있기 때문입니다.
2. 키워드 인자의 경우 함수 정의에서 디폴트 값을 지정할 수 있습니다.
    - 기본값을 사용하고 싶은 경우 따로 지정을 해주지 않아도 되기 때문에 가독성이 코드 중복이 줄어듭니다.
3. 어떤 함수를 사용하던 기존 호출자에게 하위 호환성(backward compatibility)를 제공하면서 함수 파라미터를 확장할 수 있습니다.
    - 새로운 버그가 생길 여지가 줄어듭니다.
    - 예를 들어 2번예제에 kg단위가 아니라 다른 단위로 측정하고 싶을 때(즉 함수의 기능을 확장할 때) unit부분을 추가하여 단위를 변환할 수 있습니다.

```python
## 장점 2번 예제
## 유속을 측정하는 함수.
def flow_rate(weight_diff, time_diff):
    return weight_diff/time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg/s') # 0.167 kg/s

# 전형적인 경우 시간당 유립량이 초당 킬로그램(kg/s)입니다.
# 더 긴 시간 단위의 양을 계산하고 싶어 period 파라메터를 추가하게되면 아래와 같습니다.
# 하지만 이럴 겨웅 flow_rate의 모든 호출 부분에 period를 추가해야 하고,
# 일반적인 경우에도 period를 1로 지정해주어야 합니다.
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff/time_diff)*period

# 하지만 default 값을 설정하면 period 파라미터로 값을 전달하지 않으면 default로 설정된 값으로 인자가 전달됩니다.
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff/time_diff)*period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
```
<br>

- 파라미터를 추가하여 손쉽게 기능을 확장했습니다.
- 이 경우 period와 weight_unit을 위치인자(순서대로 대입)을 할 수 있지만, 함수에서 어떤 동작을 하는 파라미터인지 알기 어렵고 순서를 혼동할 수 있기 때문에 **위치인자를 절대 사용하지 않고 키워드 인자를 사용**합니다.

```python
## 장점 3번 예제
## 예를 들어 2번예제에 kg단위가 아니라 다른 단위로 측정하고 싶을 때
## 아래와 같이 파라미터를 추가하면 됩니다.
## weight_unit에는 1키로그램와 같은 무게를 가지는 다른 단위의 크기를 쓰면 됩니다.
def flow_rate(weight_diff, time_diff, period=1, weight_unit=1):
    return ((weight_diff*weight_unit)/time_diff)*period

## 1 kg = 2.2 poound
pound_per_hour = flow_rate(weight_diff, time_diff, period=3600, weight_unit=2.2)
```
<br>

### 기억해야 할 Point
> - 함수 인자의 위치에 따라 지정할 수도 있고, 키워드를 사용해 지정할 수 있습니다.<br>
> - 키워드를 사용하면 위치 인자만 사용할 대는 혼동할 수 있는 여러 인자의 목적을 명확히 할 수 있습니다.<br>
> - 키워드 인자와 디폴트 값을 함께 사용하면 기본 호출 코드를 마이그레이션 하지 않고도 함수에 새로운 기능을 쉽게 추가할 수 있습니다.<br>
> - 선택적 키워드는 인자는 항상 위치가 아니라 키워드를 사용해 전달되어야 합니다.<br>

<br>

## BetterWay 24. None과 독스트링을 사용해 동적인 디폴트 인자를 지정하라

- 키워드 인자의 값으로 정적으로 정해지지 않는 타입의 값을 써야 할 때가 있습니다.
    - 현재시간을 디폴트로 하는 키워드 인자로 로그 함수 예제
    - `datetime.now()`를 디폴트로 설정하지만 다른 시간에 호출해도 같은 시간이 나옵니다.
    - 이런 현상이 나오는 이유는 default인자의 값은 모듈이 로드될 때 한 번만 평가되는데, 보통 프로그램이 시작하 ㄹ때 모듈을 로드하는 경우가 많습니다.
    - 즉 default에 넣은 값은 함수가 정의되는 시점에 `datetime.now()`가 한 번 호출되고 그 값이 유지되기 때문입니다.

```python
## 지금 시간을 입력해서 로그 출력하는 함수 예제
from time import sleep
from datetime import datetime

def log(message, when=datetime.now()):
    print(f'{when}: {message}')

log('안녕!')
sleep(0.1)
log('다시안녕!')
# 2023-12-15 18:59:57.989971: 안녕!
# 2023-12-15 18:59:57.989971: 다시안녕!
```
<br>

- 위의 예제와 같은 경우 원하는 동작을 하게 하려면, 디폴트 값을 `None`으로 설정하고 실제 동작을 독스트링에 문서화하는 것입니다.

```python
from time import sleep
from datetime import datetime

def log(message, when=None):
    """메시지와 타임스탬프를 로그에 남깁니다.

    Args:
        message (_type_): 출력할 메시지
        when (_type_, optional): 메시지가 발생한 시각(datetime). 디폴트 값은 현재 시간이다.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log('안녕!')
sleep(0.1)
log('다시안녕!')
# 2023-12-15 19:08:32.024760: 안녕!
# 2023-12-15 19:08:32.138589: 다시안녕!
```
<br>

- 키워드인자의 디폴트 값으로 `None`을 사용하는 것은 인자가 가변적인(mutable)경우 특히 중요합니다.
    - 다음 예제를 봅시다
    - 이 예제는 `datetime.now()`를 지정한 것과 같은 문제가 발생합니다.
    - 모듈을 로드하는 시점에 한번 호출되므로 default에 특정 빈 `dictionary` 오브젝트가 할당됩니다.
    - 그래서 함수의 리턴에 값을 넣으면 또 다른 호출에서 default를 호출 했을 때 같은 객체가 리턴됩니다.

```python
## JSON 데이터로 인코딩된 값을 읽으려고 하는데, 데이터 디코딩에 실패하면 디폴트로 빈 딕셔너리를 반환하고 싶을 때
import json

def decode(data, default={}):
    try:
        return json.loads(data) # 그냥 string을 넣을거기 때문에 에러
    except ValueError:
        return default

foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
print('Foo:', foo) # Foo: {'stuff': 5, 'meep': 1}
print('Bar:', bar) # Bar: {'stuff': 5, 'meep': 1}
```
<br>

- 앞에서 말한 해법으로 default 키워드 인자에 `None`을 설정해줍니다. 
    - 함수 내부에서 `None`일 때 빈 딕셔너리를 새로 생성해서 반환해줍니다.

```python
import json

def decode(data, default=None):
    try:
        return json.loads(data) # 그냥 string을 넣을거기 때문에 에러
    except ValueError:
        if default is None:
            default = {}
        return default

foo = decode('잘못된 데이터')
foo['stuff'] = 5
bar = decode('또 잘못된 데이터')
bar['meep'] = 1
print('Foo:', foo) # Foo: {'stuff': 5}
print('Bar:', bar) # Bar: {'meep': 1}
```
<br>

- 이런 해결 방법은 타입 애너테이션(BetterWay90)을 사용해도 잘 작동합니다.
```python
from typing import Optional
from datetime import datetime

def log_typed(message:str, when:Optional[datetime]=None) -> None:
    """메시지와 타임스탬프를 로그에 남긴다.

    Args:
        message (str): 출력할 메시지
        when (Optional[datetime], optional): 메시지가 발생한 시각(datetime). 디폴트 값은 현재 시간입니다.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')
```
<br>

### 기억해야 할 Point
> - 디폴트 인자 값은 그 인자가 포함된 함수 정의가 속한 모듈이 로드되는 시점에 단 한번 평가됩니다. 이로인해 동적인 설정(`dict()`, `list()`, `datetime.now()`같은 경우) 이상한 동작이 일어날 수 있습니다.<br>
> - 동적인 값을 가질 수 있는 키워드 인자의 디폴트 값을 표현할 때에는 `None`을 사용하고, 함수의 독스트링에 동적인 디폴트 인자가 어떻게 동작하는지 작성합니다.<br>
> - 타입 애너테이션을 사용할 때도 `None`을 사용해 키워드 인자의 디폴트 값을 표현하는 방식을 적용할 수 있습니다.<br>

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