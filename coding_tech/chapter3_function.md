# 목록
1. [BetterWay19: 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹 하지 않습니다.](#)
2. [BetterWay20: 라](#)
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
# 결과가 많은경우

def get_stats(numbers):
    ...
    return minimum, maximum, average, median, count

minumum, maximum, average, median, count = get_stats(lengths)

# 줄바꿈할경우는
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
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
> - <br>

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