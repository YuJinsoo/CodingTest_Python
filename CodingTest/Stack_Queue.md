# Stack 과 Queue


## 문제 : 같은 숫자는 싫어
- https://school.programmers.co.kr/learn/courses/30/lessons/12906

```python
#1 deque를 이용해서. list로 pop(0)으로 풀면 시간초과
from collections import deque

def solution(arr):
    answer = []
    d = deque(arr)
    answer.append(d.popleft())
    
    while d:
        temp = d.popleft()
        if answer[-1] == temp:
            continue
        answer.append(temp)
    
    return answer

#2 list comprehension으로... 기가맥힙니다.
def solution(arr):
    answer = [v for i, v, in enumerate(arr) if arr[i-1:i]!=[arr[i]]]
    return answer

```

## 문제 : 기능개발
- https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

```python
#1
import math

def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    answer = []
    count = 0
    m = days[0]
    while days:
        tmp = days.pop(0)
        if m >= tmp:
            count += 1
            if len(days)==0:
                answer.append(count)
            continue
        else:
            m = tmp
            answer.append(count)
            count = 1
        
        if len(days)==0:
            answer.append(count)
        
    return answer

#2 try가 너무 인상적....
from math import ceil

def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList
```