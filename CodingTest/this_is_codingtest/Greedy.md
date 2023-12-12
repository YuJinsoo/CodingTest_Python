# 그리디 알고리즘

- 현재 상황에서 가장 좋은 것만을 고르는 방법으로, 이후에 어떻게 되는지에 대해서는 고려하지 않습니다.

- 다익스트라 알고리즘이 그리디 알고리즘에 포함됩니다.

- 기준에 따라 가장 좋은 것을 선택하므로 문제에서 `가장 큰 순서대로` 혹은 `가장 작은 순서대로`와 같이 기준을 알게 모르게 제시합니다.

- 정렬 알고리즘과 합쳐서 출제됩니다.

## 대표 문제: 거스름돈 문제
- 87p
- 거스름돈을 거슬러 줄 때 최소한의 동전으로 거슬러 줄 때의 동전의 개수를 반환해라.
- 동전 종류: 500, 100, 50, 10
```python
n = 1270

def solution(n):
    count = 0
    coins = [500, 100, 50, 10]
    
    for coin in coins:
        count += n//coin
        # n = n%coin
        n %= coin
    
    return count

print(solution(n)) # 7
```

## 그리디 알고리즘의 정당성

- 대부분의 그리디 알고리즘 문제는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있습니다.
    - 거스름돈 문제가 그리디로 풀리는 이유는 동전들이 서로 정수배이기 때문입니다.
    - 800원 거스름돈을 500, 400, 100으로 하게 되면 우리가 푼 알고리즘으로는 500, 100, 100, 100 으로 4개가 되지만 최소의 개수는 400, 400 이기 때문입니다.


## 문제: 큰 수의 법칙

- 92p

```python
# 입력
n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

# 함수
answer = 0
data.sort(reverse=True)
first = data[0]
second = data[1]

for i in range(m):
    if (i+1) % (k+1) != 0:
        answer += first
    else:
        answer += second

print(answer) #46
# 6+6+6+5+6+6+6+5
```

- 반복되는 규칙을 이해했다면, 가장 큰수가 K번 반복후 두번째 수가 1회 나오는 것을 반복합니다.
- 이 내용을 응용하면 반복문 없이계산하는 것이 가능합니다.

```python
### 반복문 없이
n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

answer = 0
data.sort(reverse=True)
first = data[0]
second = data[1]

max_sum_count = (m//(k+1))*k + m%(k+1)

answer += first * max_sum_count
answer += second * (m - max_sum_count)
print(answer) # 46
```

## 문제: 숫자 카드 게임

- 각 행에서 가장 작은 값을 뽑고, 뽑은 값들 중 최대값을 가진 카드를 반환하도록 하는 코드.

```python
n, m = 3, 3
card_list = [
    [3,1,2],
    [4,1,4],
    [2,2,2],
]

# n, m = 2, 4
# cards = [
#     [7,3,1,8],
#     [3,3,3,4],
# ]

select = []

for cards in card_list:
    select.append(min(cards))

print(max(select))
```
<br>

## 문제: 1이 될 때까지

- 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 단 나누는 것은 나누어 떨어질때 가능합니다.
    1. N에서 1을 뺀다
    2. N을 K로 나눈다.

```python
n, k = 25, 5

value = n
count = 0

while value > 1:
    if value % k == 0:
        value //= k
        count += 1
    else:
        value -= 1
        count += 1

print(count) #2
```
