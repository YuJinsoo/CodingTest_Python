# 유형별 정리 hash (hash table)

- key-value로 이뤄진 자료형으로 python에서는 dictionary를 사용하면 됩니다.
- key를 통해 데이터를 바로 받을 수 있는 자료구조로 배열로 해쉬테이블 사이즈만큼 생성 후에 사용(공간과 시간을 맞바꿈)

## 해쉬 용어

- 해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
- 해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
- 해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
- 해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
- 슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간

## hash는 언제 사용할까

1. 리스트를 쓸 수 없을 때

   - 인덱스 접근이 아닌 경우

2. 빠른 접근 / 탐색 /수정이 빈번할 때

   - 리스트보다 시간복잡도면에서 이득입니다.

3. 집계가 필요할 때

   - 원소의 개수를 세는 문제. 해쉬와 collection의 Counter를 사용하면 편함

## 해쉬 (해쉬테이블) 의 장단점

- 장점
  - 데이터 저장/읽기 속도가 빠르다. (검색 속도가 빠르다.)
  - 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
- 단점

  - 일반적으로 저장공간이 좀더 많이 필요하다.
  - 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함

- 주요 용도
  - 검색이 많이 필요한 경우
  - 저장, 삭제, 읽기가 빈번한 경우
  - 캐쉬 구현시 (중복 확인이 쉽기 때문)

## 시간복잡도

- Get Item : O(1)
- Insert Item : O(1)
- Update Item : O(1)
- Delete Item : O(1)
- Search Item : O(1)

## 문제 1 : 포켓몬

- https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

```python
from collections import Counter

def solution(nums):
    answer = 0
    maxnum = len(nums) // 2
    kind_num = len(Counter(nums))

    # answer = min(maxnum, kind_num) 으로 축약가능
    if maxnum >= kind_num:
        answer = kind_num
    elif maxnum < kind_num:
        answer = maxnum

    return answer

# min과 set 사용해서 간단히

def solution(nums):
    return min(len(nums)//2, len(set(nums)))
```

## 문제2 : 완주하시 못한 선수

- https://school.programmers.co.kr/learn/courses/30/lessons/42576

```python
from collections import Counter

def solution(participant, completion):
    pc = Counter(participant)

    for i in completion:
        pc[i] -= 1

    for i in pc:
        if pc[i] == 1:
            return i

## Counter의 사용법을 잘 알면 엄청 편리할 것 같다고 느낀 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

## zip을 이용해서 푼 풀이. 이것도 신박하네요...
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

## hash 함수를 이용해서 푼 풀이
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

## list로 풀면 시간초과
def solution(participant, completion):
    answer = ''

    for i in completion:
        participant.remove(i)

    answer = participant.pop()
    return answer
```
