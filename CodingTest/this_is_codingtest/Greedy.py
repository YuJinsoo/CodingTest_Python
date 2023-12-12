# n = 1270

# def solution(n):
#     count = 0
    
#     coins = [500, 100, 50, 10]
    
#     for coin in coins:
#         count += n//coin
#         # n = n%coin
#         n %= coin
    
#     return count

# print(solution(n))


### 큰 수의 법칙

## 규칙상 M번 더할 때 K회까지 연속 반복할 수 있으므로..
## 가장큰수 K회, 두번째 수1회 를 반복하면 가장 큽니다.

# n, m, k = 5, 8, 3
# data = [2, 4, 5, 4, 6]

# answer = 0
# data.sort(reverse=True)
# first = data[0]
# second = data[1]

# for i in range(m):
#     if (i+1) % (k+1) != 0:
#         answer += first
#     else:
#         answer += second

# print(answer) #46
# # 6+6+6+5+6+6+6+5

# ### 반복문 없이
# n, m, k = 5, 8, 3
# data = [2, 4, 5, 4, 6]

# answer = 0
# data.sort(reverse=True)
# first = data[0]
# second = data[1]

# max_sum_count = (m//(k+1))*k + m%(k+1)

# answer += first * max_sum_count
# answer += second * (m - max_sum_count)
# print(answer)


# 숫자 카드 게임
# n, m = 3, 3
# card_list = [
#     [3,1,2],
#     [4,1,4],
#     [2,2,2],
# ]

# # n, m = 2, 4
# # cards = [
# #     [7,3,1,8],
# #     [3,3,3,4],
# # ]

# select = []

# for cards in card_list:
#     select.append(min(cards))

# print(max(select))


### 1이 될 때까지
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

print(count)
