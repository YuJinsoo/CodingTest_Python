# 재귀 피보나치

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1)+fibo(x-2)

# print(fibo(6)) # 8

# # DP

# d = [0] * 100

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
    
#     if d[x] != 0:
#         return d[x]
    
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(99)) # 218922995834555169026



# dd = [0]*100
# dd[1] = 1
# dd[2] = 1
# n = 99

# for i in range(3, n+1):
#     dd[i] = dd[i-1] + dd[i-2]

# print(dd[99]) # 218922995834555169026


## 문제: 1로 만들기

# x = 26
# d = [0] * 30001

# for i in range(2, x + 1):
#     ## -1 연산하는경우로 먼저 가정해서 값을 넣음
#     d[i] = d[i-1] + 1
    
#     ## 2, 3, 5 로 나누어지는 경우 계산이 달라지므로..
#     if i%2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
#     if i%3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)
#     if i%5 == 0:
#         d[i] = min(d[i], d[i//5] + 1)
    
# print(d[:27])
# # [0, 0, 1, 1, 2, 1, 2, 3, 3, 2, 2, 3, 3, 4, 4, 2, 3, 4, 3, 4, 3, 4, 4, 5, 4, 2, 3]

# n = 4 
# container = [1, 3, 1, 5]

# d[0]*(n+1)

# d[0] = container[0]
# d[1] = max(container[1], container[0])

# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2] + container[i])

# print(d[n-1]) # 8

## 문제 : 타일링
# ##
# d2 = [0]*1001
# d2[1] = 1
# d2[2] = 3

# for i in range(3, n+1):
#     d2[i] = d2[i-1] + d2[i-2]*2

# print(d2[n])
# print(d2[:n])

## 효율적인 화폐 구성

n, m = 2, 15
coin = [2, 3]

## m 원을 만드는 최소한의 경우를 구해야 함..

# 0  1 2 3 4 5 6 7 8 9 10 11 12
# 0 -1 1 1 2 2 2 3 3 3  4  4  4

d = [m+1]*(m+1)
d[0] = 0

for c in coin:
    for i in range(c, m+1):
        if d[i-c] != (m+1):
            d[i] = min(d[i], d[i-c]+1)

if d[m] == m+1:
    print(-1)
else:
    print(d[m])

print(d)

n, m = 3, 4
coin = [3, 5, 7]
