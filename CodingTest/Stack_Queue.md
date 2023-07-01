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

## 문제: 올바른 괄호
- https://school.programmers.co.kr/learn/courses/30/lessons/12909
``` python
#1
def solution(s):
    answer = True
    
    left = s.find('(')
    right = s.find(')')
    
    if left == -1:
        return False
    
    while s:
        if left > right:
            answer = False
            break
        
        left = s.find('(', left+1)
        right = s.find(')', right+1)
        
        if left == -1 and right != -1:
            answer = False
            break
        elif left != -1 and right == -1:
            answer = False
            break
        
        if left == -1 and right == -1:
            answer = True
            break
    
    return answer

#2 stack으로 풀기
def solution(s):
    answer = True
    
    stack = []
    if s[0] == ')':
        return False
    try:
        for b in s:
            if b == '(':
                stack.append(b)
            else:
                stack.pop()
        
    except IndexError:
        return False
    
    if len(stack) != 0:
        answer = False
    
    return answer
```

## 문제 : 프로세스
- https://school.programmers.co.kr/learn/courses/30/lessons/42587

```python
#1 내풀이 deque
from collections import deque

def solution(priorities, location):
    li = [[i, p] for i, p in enumerate(priorities)]    
    d = deque(li)
    
    count = 1
    answer = 0
    while d:
        m = max(d, key=lambda x:x[1])
        
        curp = d.popleft()
        if curp[1] == m[1]:
            if curp[0] == location :
                answer = count
                break
            else:
                count += 1
                continue
        else:
            d.append(curp)
    
    return answer

#2 any를 사용한 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
```