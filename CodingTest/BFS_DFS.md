# 유형별정리 : DFS 깊이우선탐색/ BFS 넓이우선탐색

## 문제 : 타겟 넘버

- https://school.programmers.co.kr/learn/courses/30/lessons/43165

```python
#1
def solution(numbers, target):
    answer = 0
    signed = [[x, x*(-1)] for x in numbers]

    def dfs(val, level):
        nonlocal answer
        if level == len(numbers):
            if val == target:
                answer += 1
            return

        dfs(val + signed[level][0], level+1)
        dfs(val + signed[level][1], level+1)
        return

    dfs(signed[0][0], 1)
    dfs(signed[0][1], 1)

    return answer

#다른사람풀이1 - 재귀.
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

#다른사람풀이2 - product
# 엄청나게 pythonic 하네...
# *l 과 같이 unpacking활용하는 것도 눈에 띄네요
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
```

## 문제 : 네트워크

- https://school.programmers.co.kr/learn/courses/30/lessons/43162

```python
#1 원래풀이
from collections import deque

def solution(n, computers):
    answer = 0
    visit = [ 0 for x in range(n)]
    q = deque()
    q.append((0, computers[0]))

    visit.index(0)

    def bfs(node):
        nonlocal answer
        while 0 in visit:
            while q:
                idx, node_net = q.popleft()
                if visit[idx] == 1:
                    continue
                else:
                    visit[idx] = 1

                for i, wired in enumerate(node_net):
                    if i == idx:
                        continue
                    if wired == 1:
                        q.append((i, computers[i]))
            answer +=1
            if 0 in visit:
                q.append((visit.index(0), computers[visit.index(0)]))
                bfs(visit.index(0))
        return

    bfs(0)
    return answer

##
```

## 문제 : 게임 맵 최단거리

- https://school.programmers.co.kr/learn/courses/30/lessons/1844

```python
# 1원래풀이
from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])

    q = deque()
    q.append((0,0,1))

    def bfs(y,x):
        while q:
            y, x, distance = q.popleft()

            if y==row-1 and x==col-1:
                return distance

            if maps[y][x] == 0:
                continue
            maps[y][x] = 0

            if y+1 < row:
                q.append((y+1, x, distance + 1))
            if x+1 < col:
                q.append((y, x+1, distance + 1))
            if y-1 >=0:
                q.append((y-1, x, distance + 1))
            if x-1 >=0:
                q.append((y, x-1, distance + 1))

        return -1
    return bfs(0,0)

```

## 문제 : 단어변환

- https://school.programmers.co.kr/learn/courses/30/lessons/43163

```python
# bfs
from collections import deque

def solution(begin, target, words):
    if not target in words:
        return 0

    answer = 0
    q = deque()
    q.append((begin, 1))
    v = []

    def bfs(v):
        while q:
            cur, distance = q.popleft()
            v.append(cur)
            for w in words:
                if w in v :
                    continue

                count = 0
                for i in range(len(w)):
                    if cur[i] != w[i]:
                        count += 1

                if count == 2:
                    continue

                if count == 1:
                    q.append((w, distance + 1))
                    print(w, distance)

                    if w == target:
                        return distance
        return 0
    return bfs(v)

## 다른풀이
## yield로 단어를 뱉고 zip으로 틀린글자수 활용
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
```

## 문제 : 여행경로

- https://school.programmers.co.kr/learn/courses/30/lessons/43164

```python
# test case 1 만 실패.. ㅠㅠ 다시풀기
import copy

def solution(tickets):
    answer = []
    cur = 'ICN'
    
    while tickets:
        answer.append(cur)
        can = list(filter(lambda x:x[0]==cur, tickets))
        can.sort(key=lambda x:x[1])
        
        nowticket = []
        if len(can) == 1:
            nowticket = can.pop()
            cur = nowticket[1]
            k = tickets.pop(tickets.index(nowticket))
            if tickets == []:
                answer.append(k[1])
            continue
        else:
            for go in can:
                i = 0
                for t in tickets:
                    if t == go:
                        continue

                    if go[1] == t[0]:
                        i += 1
                
                if i == 0:
                    continue
                nowticket = copy.deepcopy(go)
                tickets.pop(tickets.index(nowticket))
                cur = nowticket[1]
                break
                
        
#         if nowticket == []:
#             answer.append(cur)
#             break
        
#         answer.append(nowticket[0])
#         cur = nowticket[1]
        
    return answer
```


## 스킬체크
- https://programmers.co.kr/skill_checks/499021?challenge_id=2538
```python
def solution(array, commands):
    answer = []
    for i, j ,k in commands:
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer
```

- https://programmers.co.kr/skill_checks/499021?challenge_id=9107
```python

```