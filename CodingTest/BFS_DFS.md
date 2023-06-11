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
