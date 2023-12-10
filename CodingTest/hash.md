# 유형별 정리 hash (hash table)

> 출제빈도 높음, 평균점수 보통
> 빈도가 높고 보통 점수이므로 이쪽에서 잘하면 점수를 확보할 수 있을 것으로 생각합니다.

- key-value로 이뤄진 자료형으로 python에서는 dictionary를 사용하면 됩니다.
- key를 통해 데이터를 바로 받을 수 있는 자료구조로 배열로 해쉬테이블 사이즈만큼 생성 후에 사용(공간과 시간을 맞바꿈)

## 자료구조 hash table 이란?

- 위에서 설명한 것과 같이 key-value 쌍으로 이뤄진 데이터입니다.
- key값을 통해 value를 찾을 수 있는 자료구조입니다.
- hash 함수를 통해 key에대한 value 값을 한 번에 찾을 수 있어 검색속도 및 수정속도가 매우 빠릅니다.

- 해쉬충돌(Collison)에 대한 추가적인 내용이 있습니다.

  1. Chaining 기법
  2. Linear Probing 기법 (Open Adderssing 기법 중 하나)

- 유명한 해쉬 함수로는 SHA-256, SHA-512 등이 있습니다.
  <br> python의 `hash()`함수는 값이 달라질 수 있습니다.

> SHA-256과 같은 함수는 python의 `hashlib` 모듈을 통해 사용할 수 있습니다. hashlib.sha256() 으로 객체를 생성하여 사용합니다.

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

## 문제3 : 전화번호 >> 다시풀어보기

- https://school.programmers.co.kr/learn/courses/30/lessons/42577

- https://kid-do-developer.tistory.com/133

```python
# list이긴 한데 효율높여서 풀면 풀림
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) -1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True

# dictionary로 풀 수 있을까?
## phone_book의 번호를 모두 자리수별로 쪼개서 key로 저장
## 같은 번호가 나와도 한개만 저장됨.(key는 유일)
## 123 24 있으면 key는 1 12 2 이렇게됨
## 중복 번호는 없으므로 자기 자신을 넣지 않으면 간단하게 접두어인지 본인의 문자열인지 구분할 수 있습니다.
## 거기에 phone_book에서 일치하는 key가 있으면 False인 원리
## dictionary의 검색, 수정, 생성은 O(1)이라서 빠름
def solution(phone_book):
    d = dict()
    for p in phone_book:
        for i in range(1, len(p)):
            d[p[:i]] = 0

    for p in phone_book:
        if p in d:
            return False

    return True

## 역시나 list로 풀면 효율성 test 3, 4에서 실패
def solution(phone_book):
    #phone_book.sort() 정렬해도 실패
    for i in phone_book:
        for j in phone_book:
            if i == j :
                continue
            if i.find(j) == 0:
                return False

    return True
```

- 해설...
- 문자열 요소들을 sort하면 사전순으로 정렬이 되기 때문에 앞뒤의 요소끼리만 비교해주면 됩니다.

```python
li = ["1","12","111","11", "121", "122"]

li.sort()
li # ['1', '11', '111', '12', '121', '122']
```

## 문제 4: 의상

- https://school.programmers.co.kr/learn/courses/30/lessons/42578

```python
#1
def solution(clothes):
    answer = 1
    d = dict()
    for i in clothes:
        if d.get(i[1], None) == None:
            d[i[1]] = []
        d[i[1]].append(i[0])

    li = [len(d[i])+1 for i in d]

    for i in li:
        answer *= i
    return answer-1

# 언패킹 및 values() 까지 사용
def solution(clothes):
    clothes_type = {}

    for _, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

## Counter 사용풀이
## functools 의 reduce. 누적함수

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for item, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

```

## 문제 5 : 베스트앨범

- https://school.programmers.co.kr/learn/courses/30/lessons/42579

```python
#1 내 풀이
def solution(genres, plays):
    answer = []
    idd = dict()
    d = dict()

    # idd : dict 에 장르이름 - 재생횟수 - id list로..
    # 장르 순서 d
    z = zip(genres, plays)
    for i, (g, p) in enumerate(z):
        if idd.get(g, None) == None:
            idd[g] = dict()
        if idd[g].get(p, None) == None:
            idd[g][p] = []
        idd[g][p].append(i)

        if d.get(g, None) == None:
            d[g] = []
        d[g].append(p)
        d[g].sort(reverse=True)

    g_rank = sorted(d.items(), key =lambda x: sum(x[1]), reverse=True)

    # id가 저장된 딕셔너리에서 순차로 검색
    for g, li in g_rank:
        for i in range(len(li)):
            if i >= 2:
                break

            if li[i-1] == li[i]:
                answer.append(idd[g][li[i]][-1])
            else:
                print(idd[g][li[i]])
                answer.append(idd[g][li[i]][0])

    return answer

##2 개인적으로 제일 깔끔해보입니다.
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

##3 클래스로 구현
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play

##4 간단..
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
```
