### 예제 4-1 상하좌우
# n = 5
# direct = {
#     'L': [-1, 0],
#     'R': [1, 0],
#     'U': [0, -1],
#     'D': [0, 1],
# }

# x, y = 1, 1

# run = ['R', 'R', 'R', 'U', 'D', 'D']

# for r in run:
#     d = direct[r]
#     if x+d[0] >=1 and x+d[0]<=n and y+d[1]>=1 and y+d[1]<=n:
#         x += d[0]
#         y += d[1]

# print(x, y) 


### 예제 4-2

# n = 5

# h, m, s = 0,0,0
# count = 0

# while h < n+1 :
#     if s == 60:
#         m += 1
#         s = 0
#         if m == 60:
#             h += 1
#             m = 0
#     s+=1
#     if "3" in str(h)+str(m)+str(s):
#         count += 1
# print(count) # 11475


### 문제 왕실의 나이트

# n = 8
# pos = 'a1'
# temp = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
# move = [(-2, 1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,2)]
# count = 0
# x = temp[pos[0]]
# y = int(pos[1])

# for m in move:
#     if x + m[0] >=1 and x + m[0] <=n and y + m[1] >=1 and y+m[1]<=n:
#         count +=1

# print(count) #2

### 문제 개임개발

n, m = 4, 4
x, y = 1, 1
d = 0 ## 왼쪽으로 도는거는 (d + 3) % 4
map = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1],
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0

while True:
    d = (d+3)%4 ## 왼쪽회전
    nx = x + dx[d]
    ny = y + dy[d]
    if nx >= 0 and nx < m and ny >= 0 and ny < n and map[ny][nx] == 0:
        x, y = nx, ny
        map[ny][nx] = 2
        count += 1
    
    c = 0
    s = 0
    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < m and y+dy[i] >= 0 and y+dy[i] < n:
            c += 1
            s += map[y+dy[i]][x+dx[i]]
    
    if c <= s:
        d = (d+2) % 4 ##뒤로회전
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and nx < m and ny >= 0 and ny < n and map[ny][nx] != 1:
            count += 1
        break

print(count) #3
            