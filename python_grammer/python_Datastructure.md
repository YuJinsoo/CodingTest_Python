# Python Datastructure (컨벤션 객체) 정리!

## List

### List 메서드

- `reverse()`
  - 함수를 호출한 list 객체의 순서를 거꾸로 바꿈. (원본 변경됨)
  - Return type은 None 입니다.

### List Comprehension

- 리스트를 간단하게 한 줄로 생성할 수 있는 파이썬 문법
  > 기본 형식: <br>`python [(변수를 활용한 값) for (사용할 변수 이름) in (순회할 수 있은 객체) ] `
- 예제

```python
# 정수 0 ~ 999 원소의 배열
array = [i for i in range(1000)]

# 0~9 를 각각 2 배 한 값의 배열
array = [ i*2 for i in range(10)]
print(array) # [0,2,4,6,8,10,12,14,16,18]

# iterable(순회 가능한 객체) 로 list 생성 가능
array = [ c for c in 'hello world'] # list('hello world') 와 같음

array = [c*2 for c in 'hello']
print(array) # ['hh', 'ee', 'll', 'll', 'oo']
```

- for 문을 사용하지 않고 길고 규칙적인 list를 생성할 수 있습니다.
- for 문에 append 메서드를 사용해서 생성하는 것 보다 속도가 빠릅니다.
- 속도 비교 예제 (jupyter notebook 에서 비교)

```python
%%time
ls = []
for i in range(10000):
    ls.append(i)
# CPU times: user 13.6 ms, sys: 869 µs, total: 14.4 ms, Wall time: 19.8 ms

%%time
ls = [i for i in range(10000)]
# CPU times: user 536 µs, sys: 0 ns, total: 536 µs, Wall time: 558 µs
```

- if 문을 사용해 조건문으로 필터링

```python
# 조건을 여러개 넣을 때에는 if (조건) 을 이어서 작성한다.
# if 문 단위로 and 나 or 로 이을 수 없음(syntax error)
array = [n for n in range(1, 100) if n%7==0 if n%2==0] # 2와 7의 공배수
print(array) # [14, 28, 42, 56, 70, 84, 98]
```

- 다중배열도 손쉽게 장성할 수 있다.(다음 기회에...)

```python
array2 = [[0 for n in range(3)] for k in range(3)]
print(array2) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## Tuple

## Dictionary

## Set
