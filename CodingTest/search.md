# 유형별정리 : 완전탐색 (search)

## 문제 : 최소직사각형

- https://school.programmers.co.kr/learn/courses/30/lessons/86491

```python
# 문제설명 : https://readable-ko.site/168
# 넓이 a = w * h 이고 합 s=x+y이면 a = w * (s-w) = sw - w^2 이다.
# 이것은 길이 합이 같아도 x와 y의 차이가 클수록 넓이가 줄어든다는 의미입니다.
# 그래서 w-h 쌍에서 둘중 큰 값들 중 최대값과 둘중 작은 값들 중의 최대값을 곱하면 가장 작은 명함지갑 크기가 됩니다.
# 최대값으로 하는 이유는 더 작은 명함들이 모두 들어가야 하므로...
# 이해는 잘 안되지만... 문제설명 링크를 보면..

def solution(sizes):
    answer = max(max(x) for x in sizes) * max(min(x) for x in sizes)
    return answer
```

## 문제 : 모의고사

- https://school.programmers.co.kr/learn/courses/30/lessons/42840

```python
# 내풀이. 무식하게 다 비교하기
def solution(answers):
    answer = []
    correct = [0,0,0]
    one = [1, 2, 3, 4, 5]
    one = one * ((len(answers) // len(one)) + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    two = two * ((len(answers) // len(two)) + 1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    three = three * ((len(answers) // len(three)) + 1)

    for i, v in enumerate(answers):
        if v == one[i]:
            correct[0] += 1
        if v == two[i]:
            correct[1] += 1
        if v == three[i]:
            correct[2] += 1

    if correct.count(max(correct)) == 1:
        answer.append(correct.index(max(correct))+1)
    elif correct.count(max(correct)) == 2:
        answer = [1,2,3]
        answer.remove(correct.index(min(correct))+1)
    else:
        answer = [1,2,3]

    return answer
```

## 문제 : 소수 찾기

- https://school.programmers.co.kr/learn/courses/30/lessons/42839

```python
#1
## tip! 소수인 수를 찾는데 빨리찾고싶으면
## root 값까지만 나눠보면 된다!
## 속도가 훨씬 빠릅니다.
from itertools import permutations
import math

def solution(numbers):
    answer = 0
    p = []
    for i in range(1, len(numbers)+1):
        p += [int(''.join(x)) for x in permutations(numbers, i)]

    p = list(set(p))
    for i in p:
        if i == 0 or i == 1 or str(i)[-1] == 0:
            continue

        for idx in range(2, int(math.sqrt(i)) + 2):
            if idx == int(math.sqrt(i)) + 1:
                answer += 1
            if int(i)%idx == 0:
                break

    return answer

##2 다른사람 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

# set 에 | 는 union 함수 즉 합집합. |= 는 합집합 한걸 다시 넣는것.
```

## 문제 : 카펫

- https://school.programmers.co.kr/learn/courses/30/lessons/42842

```python
#1
def solution(brown, yellow):
    answer = []
    c = brown + yellow

    li = [[c/i, i] for i in range(3, c//2) if c%i == 0]

    for w, h in li:
        if (w-2) * (h-2) == yellow:
            answer = [w, h]
            break
    return answer
```

## 문제 : 피로도

- https://school.programmers.co.kr/learn/courses/30/lessons/87946

```python
#1 나만 무식하게 푼거같다..ㅠㅠ
from itertools import permutations

def solution(k, dungeons):
    answer = -1

    p = list(permutations(dungeons, len(dungeons)))
    li = []

    for o in p:
        kk = k
        count = 0
        for i in range(len(o)):
            if kk < o[i][0]:
                li.append(count)
            else:
                count += 1
                kk -= o[i][1]

            if i == len(o)-1:
                li.append(count)

    answer = max(li)
    return answer
```

## 문제 : 전력망을 둘로 나누기

- https://school.programmers.co.kr/learn/courses/30/lessons/86971

```python

```
