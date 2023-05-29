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
