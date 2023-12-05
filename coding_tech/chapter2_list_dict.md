# 목록
1. [BetterWay11: 시퀀스를 슬라이싱 하는 방법을 익혀라](#betterway-11-스퀀스를-슬라이싱하는-방법을-익혀라)
2. [BetterWay12: 라](#)
3. [BetterWay13: bytes와 str의 차이를 알아두라](#)
4. [BetterWay14: c스타일 형식 문자열을 strformat과 쓰기보다는 f-문자열 을 통한 인터폴레이션을 사용해라]()
5. [BetterWay15: 복성해라]()
6. [BetterWay16: 인패킹해라]()
7. [BetterWay17: ra용하라]()
8. [BetterWay18: 여러 수행하려면 zip을 사용해라]()
9. [BetterWay19: fo록을 사용하지 말아라](라)
10. [BetterWay20:  사용해 반복을 피해라]()


# Chapter2 : 리스트와 딕셔너리

- 반복적인 작업을 자동화할 때 조직적으로 관리하는 가장 일반적인 방법은 `list`를 사용하는 것입니다.
    - 아주 간편하며 다양한 문제 해결 가능합니다.
- `list`를 보완하는 것이 딕셔너리 `dictionary` 입니다.
    - 검색에 사용할 키와 키에 연관된 값을 저장합니다.
    - 일반적으로 **해시테이블** 이나 **연관 배열** 이라고 부르는 구조 안에 저장합니다.
    - 분할상환 복잡도로 상수 시간에 원소를 삽입하고 찾을 수 있습니다.
    - 그렇기 때문에 동적인 정보를 관리하는데 `dictionary`가 가장 이상적입니다.
<br>

## BetterWay 11. 스퀀스를 슬라이싱하는 방법을 익혀라

- 시퀀스를 여러 조각으로 나누는 `슬라이싱` 문법을 지원합니다.
- 어떤 파이썬 클래스에도 슬라이싱을 추가할 수 있습니다.
    - `__getitem__`과 `__setitem__`을 구현해주면 됩니다.

<br>

- 슬라이싱 구문의 기본 형태는 `리스트[시작:끝]`
    - `시작` 인덱스는 포함
    - `끝` 인덱스는 포함되지 않음
    - 맨 앞부터 시작할 때에는 굳이 `0`을 넣지 않습니다.
    - 길이 끝까지 슬라이싱 할 때에는 `끝`에 아무것도 넣지 않습니다.

```python
a = ['a','b','c','d','e','f','g','h']
print('가운데 2개:', a[3:5]) # 가운데 2개: ['d', 'e']
print('마지막을 제외한 나머지:', a[0:7]) # 마지막을 제외한 나머지: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

## 시작할때는 0을 넣지 않고 끝까지 할 때에는 마지막을 넣지 않음
assert a[0:5] == a[:5]
assert a[3:len(a)] == a[3:]
```

- 다양한 슬라이싱 방법
    - 음수 값으로 슬라이싱이 가능합니다.
    - 하지만 인덱싱을 음수로 하면 에러가 발생하니 주의합니다. (슬라이싱: [:], 인덱싱: [])
    - 전체 슬라이싱은 시작, 끝에 아무값도 넣지 않습니다.
    - 시퀀스의 범위를 넘어가도 슬라이싱이 가능합니다. 유효한 부분까지만 선택됨

```python
a = ['a','b','c','d','e','f','g','h']

print(a[:])     # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[:5])    # ['a', 'b', 'c', 'd', 'e']
print(a[:-1])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[4:])    #                     ['e', 'f', 'g', 'h']
print(a[-3:])   #                          ['f', 'g', 'h']
print(a[2:5])   #           ['c', 'd', 'e']
print(a[2:-1])  #           ['c', 'd', 'e', 'f', 'g']
print(a[-3:-1]) #                          ['f', 'g']
print(a[:20])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[-20:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```
<br>

- 리스트를 슬라이싱한 결과는 완전히 새로운 리스트입니다. (슬라이싱 결과로 얻은 리스트를 변경해도 원본은 보존)
- 슬라이싱으로 지정된 부분에 다른 리스트를 대입하면 슬라이싱으로 선택된 부분이 대입하는 리스트로 변경됩니다.(대입하는 리스트의 길이와는 무관합니다.)

```python
## 슬라이싱으로 쪼갠 리스트를 변수에 할당하면
## 원래 리스트와는 별개의 리스트입니다.
a = ['a','b','c','d','e','f','g','h']

b = a[:3]
print('인덱싱 할당 이전:', b)
b[1] = 99 # 하나에 할당
print('인덱싱 할당 이후:', b)
print('원본(변화없음):', a)

# 인덱싱 할당 이전: ['a', 'b', 'c']
# 인덱싱 할당 이후: ['a', 99, 'c']
# 원본(변화없음): ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

## 슬라이싱으로 지정한 부분에 다른 리스트를 대입해보자
# 대입되는 리스트 값과 슬라이싱 부분의 길이는 관계없습니다.
a = ['a','b','c','d','e','f','g','h']
print('슬라이싱 할당 이전:', a)
a[2:7] = [99, 22, 14]
print('슬라이싱 할당 이후:', a)
# 슬라이싱 할당 이전: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 슬라이싱 할당 이후: ['a', 'b', 99, 22, 14, 'h']
```
<br>

- 슬라이싱으로 전체 리스트를 복사한 case를 살펴봅시다.
    - `=`으로 할당하면 얕은복사라서 같은 list
    - 슬라이싱으로 할당하면 깊은복사라서 다른 list

```python
a = ['a','b','c','d','e','f','g','h']
b = a[:] ## 전체 리스트 복사 값은 같지만 다른 list
assert b == a and b is not a
print('a id:', id(a)) # a id: 1996685917440
print('b id:', id(b)) # b id: 1996685924672

## 얕은복사 되어서 같은 list를 가리키는 상황
b = a 
print('이전 a:', a)  # 이전 a: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('이전 b:', b)  # 이전 b: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:] = [101, 102, 103]
assert a is b
print('이후 a:', a)   # 이후 a: [101, 102, 103]
print('a id:', id(a)) # a id: 1941179284736
print('b id:', id(b)) # b id: 1941179284736
```
<br>

### 기억해야 할 Point
> - 슬라이싱할 때는 간결하게 합니다. (시작 인덱스에 0 이나 끝 인덱스에 시퀀스 길이를 넣지 않습니다.)<br>
> - 슬라이싱은 범위를 넘어가는 시작 인덱스나 끝 인덱스도 허용합니다. 시퀀스의 시작이나 끝에서 길이를 제한하는 슬라이스를 쉽게 표현할 수 있습니다.<br>
> - 리스트 슬라이스에 대입하면 원래 시퀀스에서 슬라이스가 가리키는 부분을 대입 연산자 오른쪽(대입하는 값) 시퀀스로 대체합니다. 이때 대입하는 값의 길이는 슬라이싱한 것과 길이가 달라도 됩니다.<br>

## BetterWay 12. 스트라이드와 슬라이스를 한 식에 함께 사용하지 말라

- 파이썬은 `[시작:끝:증가값]`으로 증가값으로 지정한 일정한 간격을 두고 슬라이싱을 할 수 있는 **스트라이드 구문**을 지원합니다.
    - 스트라이드를 사용해 짝수번째 그룹와 홀수번째 그룹을 쉽게 나눌 수 있습니다.
- 종종 예기치 못한 버그를 발생시킵니다.
    - `증가값`을 -1로 사용해 문자열을 뒤집는 경우
        - 바이트 문자열 가능
        - 유니코드 문자열 가능
        - utf-8로 인코딩한 문자열은 불가능

```python
x = ['빨','주','노','초','파','남','보']
odd = x[::2]    # ['빨', '노', '파', '보']
even = x[1::2]  # ['주', '초', '남']

## 문자열 거구로 예제. 유니코드 문자는 몰라서...
x = b'mongoose'
y = x[::-1]
print(y)

w = '스시'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
# Traceback (most recent call last):
#   File "c:\Users\ABO\Desktop\Study_Python\coding_tech\chapter2_list_dict.py", line 70, in <module>
#     z = y.decode('utf-8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9c in position 0: invalid start byte
```
<br>

> 왜냐하면 `utf-8` 인코딩은 멀티바이트 문자 형식으로 바이트 순서를 뒤집으면 2바이트 이상으로 구성된 문자들은 코드가 깨지게 됩니다. 단, `ascii code` 범위의 문자열로 이루어졌다면 모두 1바이트이기 떄문에 `utf-8`로 인코딩된 문자열 이더라도 오류가 발생하지 않습니다. 

<br>

- 중요한 점은 슬라이싱 구문에 스트라이딩까지 들어가면 매우 혼란스럽습니다.
- 그렇기 때문에 시작, 끝, 증가값 세 파라미터 모두를 한 번에 사용하는 것을 지양합니다.

<br>

- 스트라이딩 한 다음 슬라이싱을 하면 데이터를 한 번 더 얕게 복사하게 됩니다.
    - 첫 번째 연산(스트라이딩)은 결과 시퀀스의 크기를 가능한 한 줄일 수 있어야 합니다.
    - 두 번째연산에서는 슬라이싱을 통해 원하는 범위를 선택합니다.

```python
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(x[::2])       # ['a', 'c', 'e', 'g']
print(x[::-2])      # ['h', 'f', 'd', 'b']

print(x[2::2])      # ['c', 'e', 'g']
print(x[-2:2:-2])   # ['g', 'e']
print(x[2:2:-2])    # []

# 스트라이딩한 것을 얕은복사, 그리고 슬라이싱
y = x[::2] # ['a', 'c', 'e', 'g']
z = y[1:-1] # ['c', 'e']
```
<br>

- 만약 시퀀스가 너무 길어 연산에 필요한 시간과 메모리를 감당할 수 없다면 `itertools`내장 모듈의 `islice`메서드 사용을 고려합니다. --> BetterWay36

<br>

### 기억해야 할 Point
> - 슬라이스에 시작, 끝, 증가값을 함께 지정하면 코드의 의미를 혼동하기 쉽습니다.<br>
> - 시작이나 끝 인덱스가 없는 슬라이스를 만들 때는 양수 증가값을 사용하라. 가급적 음수 증가값은 피하세요.<br>
> - 한 슬라이스 안에서 시작, 끝, 증가값을 함께 사용하지 않습니다. 세 파라미터를 모두 사용해야 하는 경우 두 번 대입을 사용(한 번은 스트라이딩, 한 번은 슬라이싱) 하거나 itertools내장 모듈의 islice를 사용하세요. <br>
> - <br>

## BetterWay 13. 슬라이싱보다는 나머지를 모두 잡아내는 언패킹을 사용하라
### 기억해야 할 Point

- 시퀀스를 슬라이싱과 인덱싱으로 첫번째, 두번째, 나머지 로 가지고 오려면 가독성이 떨어집니다.
    - 가독성이 떨어지고
    - `off-by-one-error`(1차이로 인덱스를 잘못 주는 에러)가 발생할 수 있습니다.

```python
car_ages = [0,9,4,8,7,20,19,1,6,15]
car_ages_desc = sorted(car_ages, reverse=True)

# 일반적으로 슬라이싱과 인덱스를 사용하면 이렇게 가져와야함
oldest = car_ages_desc[0]
second_oldest = car_ages_desc[1]
others = car_ages_desc[2:]              # 나머지
print(oldest, second_oldest, others)    # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]
```
<br>

- 하지만 언패킹을 사용하면 간단하게 처리할 수 있습니다.
    - **별표식`(*var)`**을 활용합니다. (starred expression)
    - 순서를 어디에 두느냐에 따라 앞, 중간, 뒤의 나머지 값을 한 번에 처리할 수 있습니다.

```python
car_ages = [0,9,4,8,7,20,19,1,6,15]
car_ages_desc = sorted(car_ages, reverse=True)

# 하지만 나머지 언패킹을 사용하면 간단하게 처리할 수 있습니다.
oldest, second_oldest, *others = car_ages_desc
print(oldest, second_oldest, others)    # 20 19 [15, 9, 8, 7, 6, 4, 1, 0]

# 별표식 위치에 따라 원하는 방식으로 나눌 수 있습니다.
oldest, *others, youngest = car_ages_desc
print(oldest, others, youngest)         # 20 [19, 15, 9, 8, 7, 6, 4, 1] 0

*others, second_youngest, youngest = car_ages_desc
print(others, second_youngest, youngest)# [20, 19, 15, 9, 8, 7, 6, 4] 1 0
```
<br>

- 하지만 별표식만 활용해서 할당할 수는 없습니다. (SyntaxError)
- 한 번의 언패킹 패턴에서(한 계층의 언패킹)별표 식을 두 개 이상 쓸 수 없습니다.
- 하지만 여러 계층으로 이루어진 경우 별표식을 여러번 사용할 수 있습니다.

```python
*others = car_ages_desc 
# SyntaxError: starred assignment target must be in a list or tuple

start, *part1, *part2, end = car_ages_desc
# SyntaxError: multiple starred expressions in assignment

## 여러 계층으로 되어있는 자료인 경우
car_inventory = {
    '시내': ('그랜져', '아반떼', '티코'),
    '공항': ('제네시스', '소나타', 'K5', '엑센트'),
}

# items()는 dictionary를 tuple로 출력해줍니다.
((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()

print(f'{loc1} 최고는 {best1}, 나머지는 {len(rest1)}종')
print(f'{loc2} 최고는 {best2}, 나머지는 {len(rest2)}종')
# 시내 최고는 그랜져, 나머지는 2종
# 공항 최고는 제네시스, 나머지는 3종
```
<br>

- 별표식은 상항 `list` 인스턴스가 됩니다.
- 언패킹하는 시퀀으세 남는 원소가 없으면, 별표 식 부분은 빈 리스트가 됩니다.
    - 이런 특징을 활용해 최소 N개 들어있는 사실을 미리 아는 시퀀스를 처리할 때 유용합니다.

```python
# 최소 길이가 2개라는 사실은 안다면, others만 판별하면 됩니다.
short_list = [1, 2]
first, second, *others = short_list
print(first, second, others) # 1 2 []
# others 는 빈 list가 됩니다.
```
<br>

- 별표 식을 활용하면 언패킹할 이터레이터의 값을 깔끔하게 가져올 수 있습니다.
- 하지만 이터레이터를 별표식으로 언패킹하면 컴퓨터 메모리를 모두 다 사용해서 프로그램이 멈출 수 있습니다.
    - 즉, 결과 데이터의 크기가 메모리에 들어갈 수 있는 안전한 때에만 사용해야 합니다.

```python
# 중고차 정보 csv
def generate_csv():
    yield('날짜', '제조사', '모델', '연식', '가격')
    yield('2021', '제조사1', '모델1', '연식1', '가격1')
    yield('2021', '제조사2', '모델2', '연식2', '가격2')
    yield('2021', '제조사3', '모델3', '연식3', '가격3')
    yield('2021', '제조사2', '모델2', '연식2', '가격2')

# 인덱싱과 슬라이싱을 활용해서 이터레이터 값 가져오기
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV 헤더:', header)
print('행 수:', len(rows))
# CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# 행 수: 4

## * 연산을 활용하여 이터레이터 값 가져오기
it = generate_csv()
header, *rows = it
print('CSV 헤더:', header)
print('행 수:', len(rows))
# CSV 헤더: ('날짜', '제조사', '모델', '연식', '가격')
# 행 수: 4
```
<br>

> - 언패킹 대입에 별표 식을 사용하면 언패킹 패턴에서 대입되지 않는 모든 부분을 리스트에 담아낼 수 있습니다.<br>
> - 별표 식은 언패킹 패턴의 어떤 위치에든 놓을 수 있습니다. 별표 식에 대입도니 결과는 항상 리스트가 되면, 이 리스트에는 별표 식이 받은 값이 0개 또는 그 이상이 들어갑니다.<br>
> - 리스트를 서료 겹치지 않게 여러 조각으로나눌 경우, 슬라이싱과 인덱싱을 사용하기보다는 나머지를 모두 잡아내는 언패킹을 사용해야 실수의 여지가 없습니다.<br>

## BetterWay 14. 복잡한 기준을 사용해 정렬할 때에는 key 파라미터를 사용하라
### 기억해야 할 Point

- `list`컨테이너에는 원소를 정렬시키는 `sort()` 메서드가 있습니다. 
    - 리스트 자체를 변경시킴 (sorted(list) 는 새로운 리스트 반환)
    - 아무 설정이 없으면 오름차순으로 정렬합니다.
    - reverse 인자에 True를 넘기면 내림차순 정렬합니다.

```python
numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers) # [11, 68, 70, 86, 93]

numbers.sort(reverse=True)
print(numbers) # [93, 86, 70, 68, 11]
```
<br>

- `list`에 기본형이 아닌 객체가 들어있는 경우에는 sort메서드가 호출하는 객체 비교 특별 메서드가 정의돼 있지 않아 정렬할 수 없습니다.

```python
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f'Tool({self.name}, {self.weight})'

tools = [
    Tool('수준계', 3.5),
    Tool('해머', 0.5),
    Tool('슼크류드라이버', 1.25),
    Tool('끌', 2.0),
]

tools.sort() # TypeError: '<' not supported between instances of 'Tool' and 'Tool'
```
<br>

- 이런 경우에는 객체끼리 대소비교를 하는 매직메서드(`__lt__()`, `<`)를 구현하는 방법으로 sort() 메서드를 사용할 수 있지만, 여러가지 순서를 지원해야 하는 경우가 많기 때문에 큰 의미가 없습니다.
- 객체에 대해 정렬할 때 정렬에 기준이 되는 애트리뷰트로 정렬할 수 있도록 `sort()` 메서드에 `key`라는 파라미터가 있습니다.
    - `key`에는 함수가 전달되야 합니다.
    - `key` 함수가 반환하는 값은 원소 대신 정렬 기준으로 사용할 수 있는 비교 가능한(자연스러운 순서가 정의된)값이어야 합니다.
    - 일반적으로 `lambda`함수를 사용해서 정렬에 사용할 attribute를 지정합니다.
    - 시퀀스가 넘어갈 경우 인덱싱도 가능합니다.

```python

print('미정렬:', repr(tools))   
# 미정렬: [Tool(수준계, 3.5), Tool(해머, 0.5), Tool(슼크류드라이버, 1.25), Tool(끌, 2.0)]

# 이름으로 정렬
tools.sort(key=lambda x:x.name) 
print('정렬:', repr(tools))     
# 정렬: [Tool(끌, 2.0), Tool(수준계, 3.5), Tool(슼크류드라이버, 1.25), Tool(해머, 0.5)]

# 무게로 정렬
tools.sort(key=lambda x:x.weight) 
print('정렬:', repr(tools))
# 정렬: [Tool(해머, 0.5), Tool(슼크류드라이버, 1.25), Tool(끌, 2.0), Tool(수준계, 3.5)]
```
<br>

- 문자열같은 기본 타입의 경우 정렬하기 전에 key 함수를 사용해 원소 값을 변경할 수도 있습니다.
```python
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('대소문자 구분:', places)
places.sort(key=lambda x: x.lower())
print('대소문자 무시:', places)
# 대소문자 구분: ['New York', 'Paris', 'home', 'work']
# 대소문자 무시: ['home', 'New York', 'Paris', 'work']
```
<br>

- 여러 기준을 적용해서 정렬할 수 있습니다.
    - weight로 먼저 정렬 후 name으로 정렬하고 싶은 경우.
- 가장 쉬운 방법은 `tuple`을 사용하는 것입니다.
    - `tuple`에는 sort()에 필요한 매직메서드가 정의되어 있습니다.
    - 튜블의 각 위치를 이터레이션하면서 각 인덱스에 해당하는 원소를 한 번에 하나씩 비교하는 방식으로 구현되어 있습니다.
    - 비교하는 튜플의 첫 번째 위치에 있는 값이 같으면 튜블의 비교 메서드는 다음 위치에 있는 값을 비교합니다.
- 튜블 방식의 가장 큰 단점은 모든 요소가 같은 정렬(오름차순 or 내림차순)으로 결정되는 것입니다.
    - 숫자 attribute에 `-`를 붙여 숫자만 반대로 정렬하는것이 가능합니다.


```python
saw = (5, '원형 톱')
jackhammer = (40, '착암기')
assert not (jackhammer < saw) ## True

drill = (4, '드릴')
sander = (4, '연마기')
assert drill[0] == sander[0]    # True weight가같음
assert drill[1] < sander[1]     # True 드릴의 이름이 더 빠른 값
assert drill < sander           # True 그러므로 드릴이 먼저 정렬

# tuple을 이용한 정렬
power_tools=[
    Tool('드릴', 4),
    Tool('원형톱', 5),
    Tool('착암기', 40),
    Tool('연마기', 4),
]
power_tools.sort(key=lambda x:(x.weight, x.name), reverse=True)
print(power_tools)
# [Tool(착암기, 40), Tool(원형톱, 5), Tool(연마기, 4), Tool(드릴, 4)]

# attribute가 숫자인 경우 - 기호를 넣어 숫자만 반대로 정렬할 수 있습니다.
power_tools.sort(key=lambda x:(-x.weight, x.name), reverse=True)
print(power_tools)
# [Tool(착암기, 40), Tool(원형톱, 5), Tool(연마기, 4), Tool(드릴, 4)]
power_tools.sort(key=lambda x:(-x.weight, x.name), reverse=True)
print(power_tools)
# [Tool(연마기, 4), Tool(드릴, 4), Tool(원형톱, 5), Tool(착암기, 40)]
```
<br>

- 여러 기준으로 정렬하고 싶다면 sort()를 여러 번 걸어주어 구현할 수 있습니다.
- 어떤 정렬 기준을 A > B > C 기준으로 정렬하고 싶다면 아래와 같은 방법으로 여러 번 sort()를 합니다.
    - C에 대해 sort()
    - 결과에 대해 B에 대해 sort()
    - 결과에 대해 A에 대해 sort()
- 이런 경우 오름차순/내림차순을 원하는 대로 설정할 수 있지만, 같은 코드가 반복되는 느낌이라 가독성이 좋지 않을 수 있습니다.

```python
# 정렬 우선순위 무게 - 이름 인 경우
power_tools.sort(key=lambda x:x.name)  # 이름 오름차순 정렬
power_tools.sort(key=lambda x:x.weight, reverse=True)  # 무게 내림차순 정렬
print(power_tools)
# [Tool(착암기, 40), Tool(원형톱, 5), Tool(드릴, 4), Tool(연마기, 4)]
```
<br>

> - 리스트 타입에 들어 있는 `sort`메서드를 사용하며 원소 타입이 문자열, 정수, 튜플 등과 같은 내장 타입인 경우 자연스러운 순서(`__lt__()`)로 리스트의 원소를 정렬합니다.<br>
> - 원소 타입에 자연스러운 순서가 정의되어있지 않으면 sort를 사용할 수 없습니다. 하지만 `key`인자에 정렬 기준을 반환하는 함수를 전달하면 사용할 수 있습니다.<br>
> - `key`함수에 튜플을 반환하면 여러 정렬 기준을 하나로 엮을 수 있습니다.<br>
> - `sort`함수를 우선순우 역 순으로 사용하여 여러 기준에 대해 정렬할 수 있습니다.<br>
<br>

## BetterWay 15. 딕셔너리 삽입 순서에 의존할 때는 조심하라

- Python 3.5 이전에는 딕셔너리에 이터레이션을 수행하면 키를 임의의 순서로 반환했으며, 이터레이션 순서는 원소가 삽입된 순서와 일치하지 않았습니다.
    - 원인: `딕셔너리`의 구현이 내장 `hash` 함수와 파이썬 인터프리터가 시작할 때 초기화되는 난수 씨앗값(seed)을 사용하는 해시 테이블 알고리즘으로 되어있었기 때문입니다.
    - 즉 실행시마다 같은 딕셔너리 객체가 다른 순서로 원소를 뱉습니다.
    - 딕셔너리의 `items()`, `keys()`, `values()`, `popitem()` 함수도 이터레이션에 의존했기 때문에 매번 순서가 달라졌습니다.
    - 함수의 키워드 아규먼트(**kwarg) 도 순서가 매번 달랐습니다. (함수 호출 디버깅이 어려웠습니다.)
    - 클래스도 인스턴스 딕셔너리에 `dict`타입을 사용하기 때문에 object필드가 난수 같은 동작을 보였습니다. (class의 `__dict__()` 매직메서드 호출 할 경우, 반환되는 attribute에 대해 랜덤한 순서로 출력되었습니다.)

- **Python 3.6** 부터는 딕셔너리가 **삽입 순서를 보존**하도록 개선되었습니다.
    - 파이썬의 `dictionary`가 삽입 순서를 보존하는 것이 표준이므로, 앞으로 개발할 함수 및 API의 일부분을 dict가 순서를 보장하는 것으로 개발해도 됩니다.

```python
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
print(baby_names) # {'cat': 'kitten', 'dog': 'puppy'}
```
<br>

### Note!
> - python 3.5 까지는 순서를 보존하는 딕셔너리를 `collections`의 `OrderedDict`라는 클래스로 지원했습니다. <br>
> - python 3.6 이후의 `표준 dict`와 `OrderedDict`의 동작은 유사하지만, 성능 특성은 다릅니다.<br>
> - 키 삽입과 popitem호출을 매우 자주 처리해야 한다면(ex: LRU 캐시) 표준 python `dict`보다 `OrderedDict`를 사용하는 것이 더 좋습니다. (BetterWay70)<br>

- 하지만 딕셔너리를 처리할 때 삽입 순서 관련 동작이 항상 성립한다고 가정해서는 안됩니다.
- python 에서 list나 dict와 같은 구조이지만 커스터마이징이 추가된 클래스 개발이 쉬운데, 파이썬은 정적 언어가 아니기 때문에 덕타이핑에 의존해 커스터마이징한 클래스를 표준 dict와 혼동하여 함정에 빠지는 경우가 있습니다.
    - 덕타이핑 : 오리처럼 소리를 내고 오리 모양이면 오리이다. 라는 말에서 온 단어로, 동적 타입 지정의 일종입니다. 객체가 실생 시점에 어떻게 행동하는지를 기준으로 객체의 타입을 지정하는 방식입니다. 때문에 같은 함수, 어트리뷰트를 가지고 있다면 동작이 어떻든 같은 타입으로 판단할 수 있습니다.

```python
# 순위를 출력하는데 SortedDict는 key이름 순서로 정렬하는 dict일 때
# get_winner는 가장 첫 번째 원소를 출력하는데, dict는 득표수로 정렬되지만,
# __iter__()에서 출력 순서가 key 순서로 출력하기 때문에
# 득표수 1등인 otter가 아니라 fox가 나옴

## dict 와 같은 구조의 함수를 가지는 클래스
from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
        
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))

vote = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}

ranks = {}
populate_ranks(vote, ranks)
print(ranks)    # {'otter': 1, 'fox': 2, 'polar bear': 3}
winner = get_winner(ranks)
print(winner)   # otter


sorted_rank = SortedDict()
populate_ranks(vote, sorted_rank)
print(sorted_rank.data)  # {'otter': 1, 'fox': 2, 'polar bear': 3}
sorted_winner = get_winner(sorted_rank)
print(sorted_winner)    # fox
```
<br>

- 이런 문제를 해결하는 방법은 세가지 방법이 있습니다.
1. `ranks` 딕셔너리가 어떤 특정 순서로 이터레이션 된다고 가정하지 않고, `get_winner`함수를 구현. 가장 보수적이고 튼튼합니다.
```python
def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name
```
<br>

2. 함수 맨 앞에 `ranks`의 타입이 우리가 원하는 타입인지 검사하는 코드를 추가합니다. 원하는 타입이 아니면 타입 에러를 발생시킵니다.
```python
def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('dict 인스턴스가 필요합니다.')
    return next(iter(ranks))
```
<br>

3. 세 번째 방법은 타입 애너테이션(anootation)을 사용해서 `get_winner`에 전달되는값이 딕셔너리와 비슷한 동작을 하는 `MutableMapping`인스턴스가 아니라 `dict`인스턴스가 되도록 강제합니다.
```python
## 스크립트 실행 시
# python -m mypy --strict 파일명
# 명령어로 실행
from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))
```
<br>

### 기억해야 할 Point

> - 파이썬 3.7 부터는 인스턴스에 들어 있는 내용을 이터레이션 할 때 키를 삽입한 순서대로 돌려받는 것에 의존할 수 있습니다.<br>
> - 파이썬은 dict는 아니지만 표준 dict와 비슷한 객체를 쉽게 만들 수 있게 해줍니다. 이런 타입의 경우 삽입 순서가 그대로 보존된다고 보장할 수 없습니다.(`__iter__()` 메서드가 재정의 되어있으면 모름)<br>
> - dict와 비슷한 클래슬를 다루는 방법으로는 dict의 삽입 순서 보존에 의존하지 않는 방법, 실행 시점에 명시적으로 dict 타입을 검사하는 방법, 타입 애너테이션과 정적분석을 사용하는 방법이 있습니다.<br>


## BetterWay 16. in을 사용하고 딕셔너리 키가 없을 때 KeyError를 처리하기 보다는 get을 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

## BetterWay 17. 내부 상태에서 원소가 없는 경우를 처리할 때는 setdefault보다 defaultdict를 사용하라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>

## BetterWay 18. __missing__을 사용해 키에 따라 다른 디폴트 값을 생성하는 방법을 아라두라
### 기억해야 할 Point
> - <br>
> - <br>
> - <br>
