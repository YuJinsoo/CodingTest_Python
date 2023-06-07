# 유형별 정리 : 정렬 (sort)

> 출제빈도 높음, 평균점수 높음
> 빈도가 높고 높은 점수이므로 실수하지 않고 정확하고 빠르게 푸는 것이 중요합니다.

## 문제 : K번째수

- https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3

```python
#1
def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1 : i[1]])[i[2]-1])
    return answer

##2 깔끔쓰
def solution(array, commands):
    answer = []
    for s, e, k in commands:
        answer.append(sorted(array[s-1 : e])[k-1])
    return answer

##3 한줄코딩
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```

## 문제 : 가장 큰 수

- https://school.programmers.co.kr/learn/courses/30/lessons/42746

```python
# https://yuna0125.tistory.com/145
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

#### 다시 풀어보기...
def solution(numbers):
    answer = ''
    tmp = sorted(list(map(lambda x: str(x) , numbers)), reverse=True)
    tmp2 = sorted(tmp, key=lambda x:(x[-len(x)], x[-len(x)+1]) , reverse=True)
    return ''.join(tmp2)
```

## 문제 : H-Index

- https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3

- 문제가 이상한 것 같다.. 인용수(citations의 요소 값) h로 판단해서 풀면 절대 풀이가 안 나옴.

```python
## 정답
# h-index 정의를 보고 풀어야함. 문제 설명이 너무 부족하고 잘못되어있는거라고 생각합니다.
def solution(citations):
    answer = 0
    citations.sort(reverse = True)

    # 위키에 정의된대로 풀이 https://en.wikipedia.org/wiki/H-index
    for i, v in enumerate(citations):
        if v >= i+1:
            answer += 1

    return answer

##
# h를 인용수라고 생각하면 아래처럼 푸는데, 이러면 예제만 통과하고 테스케이스는 2개 빼고 다 실패
def solution(citations):
    answer = 0
    paper_count = len(citations)
    citations.sort()

    for v in citations:
        if (paper_count - citations.index(v)) >= v:
            answer = v
        else:
            break

    return answer
```
