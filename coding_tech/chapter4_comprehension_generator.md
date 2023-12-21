# 목록
1. [BetterWay27. map과 filter 대신 컴프리헨션을 사용하라](#betterway27-map과-filter-대신-컴프리헨션을-사용하라)
2. [BetterWay28. 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라](#betterway28-컴프리헨션-내부에-제어-하위-식을-세-개-이상-사용하지-말라)
3. [BetterWay29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라](#betterway29-대입식을-사용해-컴프리헨션-안에서-반복-작업을-피하라)
4. [BetterWay30. 리스트를 반환하기보다는 제너레이터를 사용하라](#betterway30-리스트를-반환하기보다는-제너레이터를-사용하라)
5. [BetterWay31. 인자에 대해 이터레이션 할 때는 방어적이 되어라](#betterway31-인자에-대해-이터레이션-할-때는-방어적이-되어라)
6. [BetterWay32. 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라](#betterway32-긴-리스트-컴프리헨션보다는-제너레이터-식을-사용하라)
7. [BetterWay33. yield from을 사용해 여러 제너레ㅔ이터를 합성하라](#betterway33-yield-from을-사용해-여러-제너레ㅔ이터를-합성하라)
8. [BetterWay34. send로 제너레이터에 데이터를 주입하지 말라](#betterway34-send로-제너레이터에-데이터를-주입하지-말라)
8. [BetterWay35. 제너레이터 안에서 throw 상태를 변화시키지 말라](#betterway35-제너레이터-안에서-throw-상태를-변화시키지-말라)
8. [BetterWay36. 이터레이터나 제너레이터를 다룰 때에는 itertools를 사용하라](#betterway36-이터레이터나-제너레이터를-다룰-때에는-itertools를-사용하라)

# Chapter4 : 컴프리헨션과 제너레이터

> 컴프리헨션
- 리스트, 딕셔너리, 집합등의 타입을 간결하게 이터레이션하면서 원소로부터 파생되는 데이터 구조를 생성하는 기능이비다.
- 컴프리헨션을 사용하면 일반적인 작업을 수행하는 코드의 가독성을 높일 수 있습니다.

> 제너레이터
- 함수가 점진적으로 반환하는 값으로 이뤄지는 스트림을 만들어줍니다.
- 이터레이터를 사용할 수 있는 곳(for 루프, 별표 식 등)이라면 어디든 사용할 수 있습니다.
- 제너레이터를 사용하면 성능을 향상시키고 메모리 사용량을 줄이고 가독성을 높일 수 있습니다.


## BetterWay27. map과 filter 대신 컴프리헨션을 사용하라

- python은 시퀀스나 이터러블에서 새 리스트를 만들어내는 간결한 구분을 제공합니다. **리스트 컴프리헨션**
- 인자가 하나의 함수를 적용하는 경우가 아니라면 간단한 경우에도 `map()`내장 함수보다 `리스트 컴프리헨션`이 더 명확합니다.

```python
a= [1,2,3,4,5,6,7,8,9,10]

## 기존방법
squares = []
for x in a:
    squares.append(x**2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## map()
alt = map(lambda x:x**2, a)
print(alt)

## list comprehension
squares = [x**2 for x in a]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
<br>

- 만일 조건을 추가해서 짝수의 제곱만 계산한다고 한다면 다음과 같습니다.
    - 이 때에도 리스트 컴프리헨션이 맵과 필터를 사용한 것 보다 가독성이 좋습니다.

```python
## list comprehension
even_squares = [x**2 for x in a if x%2==0]
print(even_squares) # [4, 16, 36, 64, 100]

## map and filter
## 읽기힘들다
alt = map(lambda x:x**2, filter(lambda x:x%2==0, a))
print(alt) # [4, 16, 36, 64, 100]
```
<br>

- `딕셔너리`와 `집합`에도 리스트 컴프리헨션과 동등한 컴프리헨션이 있습니다.
    - 딕셔너리 컴프리헨션
    - 셋 컴프리헨션
- 이 또한 map과 filter를 사용할 수 있지만 컴프리헨션의 가독성이 더 좋습니다.
```python
## 컴프리헨션
even_squares_dict = {x: x**2 for x in a if x%2==0}
threes_cubed_set = {x**3 for x in a if x%3 == 0}
print(even_squares_dict) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
print(threes_cubed_set) # {216, 729, 27}

## map and filter
alt_dict = dict(map(lambda x: (x,x**2), filter(lambda x: x%2==0, a)))
alt_set = set(map(lambda x:x**3, filter(lambda x:x%3==0, a)))
print(alt_dict)
print(alt_set)
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
# {216, 729, 27}
```
<br>

### 기억해야 할 Point
> - 리스트 컴프리헨션은 `lambda`식을 사용하지 않기 때문에 같은 일을 하는 `map`과 `filter`내장 함수를 사용하는 것보다 명확합니다.<br>
> - 리스트 컴프리헨션을 사용하면 쉽게 입력 리스트의 원소를 건너뛸 수 있습니다.<br>
> - 딕셔너리와 셋도 컴프리헨션을 사용할 수 있습니다.<br>

<br>

## BetterWay28. 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라

- 컴프리헨션은 기본적인 사용법 외에도 루프를 여러 수준으로 내포하도록 허용합니다.
- 행렬을 1차원으로 변환하는 예제
    - 왼쪽 `for`문 부터 차례대로 순회하면서 출력합니다.
    - 컴프리헨션에서 다중 루프를 사용하는 좋은 예
    - 

```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<br>

- 행렬 원소를 제곱하는 예제를 하려면 컴프리헨션 안에 컴프리헨션을 추가로 해야 합니다.
```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
squared = [[x**2 for x in row] for row in matrix]
print(squared) # [[1, 4, 9], [16, 25, 36], [49, 64, 81]] 
```
<br>

- 리스트 안에 더 깊은 리스트 계층이 있으면 컴프리헨션이 복잡해집니다.
- 하지만 for문으로 구현하면 가독성이 좋아지고 순회 대상이 명확해집니다.
```python
my_list = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
flat = [x for sublist1 in my_list
        for sublist2 in sublist1
        for x in sublist2]

print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

flat2 = []
for sublist1 in my_list:
    for sublist2 in sublist1:
        flat2.extend(sublist2)

print(flat2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```
<br>

- 또한 컴프리헨션 식 바로 뒤에 `if`문을 추가해서 각 수준마다 조건을 지정할 수 있습니다.
- 행렬에서 3으로 나워 떨어지는 셀만 남기고 합계가 10 보다 더 큰 행만 맘기고 싶다고 하자.
    - 코드가 길어지지느 않지만 읽기가 힘들어집니다.

```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
filtered = [[x for x in row if x%3==0] for row in matrix if sum(row)>=10]
print(filtered) # [[6], [9]]
```
<br>

> 컴프리헨션에 들어가는 하위 식이 세 개 이상 되지 않게 제한하는 규칙을 꼭 지키는 것을 권합니다.
- 조건식 두 개, 루프 두 개, 혹은 조거문 한개와 루프 한 개 까지만 사용 권장합니다.
- 이보다 복잡해지면 컴프리헨션 보다 일반 if와 for를 사용하는 것을 지향합니다.


### 기억해야 할 Point
> - 컴프리헨션으 여러 수준의 루프를 지원하며 각 수준마다 여러 조건을 지원합니다.<br>
> - 제어 하위 식이 세 개 이상인 컴프리헨션은 이해하기 매우 어려우므로 가능하면 피해야 합니다.<br>

<br>

## BetterWay29. 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay30. 리스트를 반환하기보다는 제너레이터를 사용하라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay31. 인자에 대해 이터레이션 할 때는 방어적이 되어라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay32. 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay33. yield from을 사용해 여러 제너레ㅔ이터를 합성하라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay34. send로 제너레이터에 데이터를 주입하지 말라


### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay35. 제너레이터 안에서 throw 상태를 변화시키지 말라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>

## BetterWay36. 이터레이터나 제너레이터를 다룰 때에는 itertools를 사용하라

### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

<br>


## 여러 이터레이터 연결하기
## 이터레이터 원소 거리그
## 이터레이터 원소의 조합 만들어내기