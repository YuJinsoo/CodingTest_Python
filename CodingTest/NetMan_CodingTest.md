## NetMan 코딩테스트
2023-11-09 목요일

3시간 5문제

### 1번 문제: 100%
- n,m 크기의 직사각형을 x_axis, y_axis 로 잘랐을 때 가장 큰 사각형의 넓이 구하기
- x_axis, y_axis는 리스트로 전달됨

```python
def solution(n, m, x_axis, y_axis):
    x_start = [0]
    y_start = [0]
    x_axis.append(n)
    y_axis.append(m)
    x_base = x_start + x_axis
    y_base = y_start + y_axis
    print(x_base)

    for i in range(len(x_base)):
        x_gap = [x_base[i+1]-x_base[i] for i in range(len(x_base)-1)]
        y_gap = [y_base[i+1]-y_base[i] for i in range(len(y_base)-1)]

    x = max(x_gap)
    y = max(y_gap)

    answer = x*y
    return answer
```


### 2번 문제: 80%
- 숫자 리스트를 주는데 숫자의 합이 0이 되도록 부호를 주는 경우의 수를 리턴하는 문제.
- dfs 써도 효율성이 다 틀리게 나와서...
- 크기가 크면 5자리만 표기하라는게 무슨뜻인지 모르겠는 문제
```python
## ---1
def solution(numbers):
    answer = 0
    target = 0
    signed = [[x, x*(-1)] for x in numbers]

    def dfs(val, level):
        nonlocal answer
        ## 혹시 5자리라는게....
        # if answer >= 99999:
        #     return
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

```

```python
## ---2 
## 순열로 더하는 숫자의 경우를 모두 생성한 위 map(sum,~) 을 이용해서 연산
## 이후에 0 개수를 count
from itertools import product
def solution(numbers):
    signed = [(x, -x) for x in numbers]
    sum_list = list(map(sum, product(*signed)))
    return sum_list.count(0)
```

### 3번 문제: 80%
- 지그재그 배열(증가, 감소를 반복하는 배열) 문제
- 원소를 list로 줄 때 배열이 지그재그 배열 규칙에 맞도록 하는 추가해야하는 숫자 개수

- edge케이스를 못찾겠음
```python
def solution(s):
    count = 0
    same_cnt = 0
    for i in range(1, len(s)-1):
        if s[i-1] < s[i] and s[i] > s[i+1]:
            continue
        elif s[i-1] > s[i] and s[i] < s[i+1]:
            continue
        else:
            count += 1

    if s[0] >= s[1]:
        count += 1
    
    return count
```


### 4번 문제: 80%

- N by N 크기의 지도에 bus정류장 위치 좌표가 list로 주어짐
- 각 위치에서 가장 가까운 버스정류장까지의 거리가 표현되도록 N by N 리스트를 반환하는 문제

- [[1,2,3], [1,0,1], [1,2,1]] 이런식으로 나와야함

```python
from collections import deque

DIRECTION_X = [1,-1,0,0]
DIRECTION_Y = [0,0,1,-1]

def solution(N, bus_stop):
    answer=[[N]*(N) for i in range(N)]
    
    def bfs(y, x):
        q = deque()
        q.append((y, x, 0))

        while q:
            now_y, now_x, distance = q.popleft()
            
            if answer[now_y-1][now_x-1] > distance:
                answer[now_y-1][now_x-1] = distance
            else:
                continue
            
            for idx in range(4):
                next_x = now_x + DIRECTION_X[idx]
                next_y = now_y + DIRECTION_Y[idx]

                if next_x >= 1 and next_x <= N and next_y >= 1 and next_y <= N and (distance+1) < answer[next_y-1][next_x-1]:
                    q.append((next_y, next_x, distance+1))
    
    for stop in bus_stop:
        bfs(stop[0], stop[1])
    
    return answer
```


### 5번 문제: 60%

- 음식 포만도를 list로 주는데 1 ~ x, x ~ y, y ~ n 각각의 합이 일치하도록 하는 경우의 수를 구하는 문제

```python
def solution(foods):
    answer = 0
    sum_list = [sum(foods[:i]) for i in range(1, len(foods)+1)]
    # sum_list = [sum(foods[:i]) for i in range(1, len(foods))]
    # 인덱싱 실패인가?

    # p1은 0~
    for p1 in range(1, len(foods)-1):
        for p2 in range(p1, len(foods)):
            if sum_list[p1-1] == (sum_list[p2-1] - sum_list[p1-1]) and sum_list[p1-1] == (sum_list[-1] - sum_list[p2-1]):
                answer +=1

    return answer
```