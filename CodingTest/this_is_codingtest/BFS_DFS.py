### 음료수 얼려 먹기
#입력
# N, M = 4,5
# maps = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0],
# ]
# #기능
# answer = 0
# directions = [[0,1], [0,-1], [1,0], [-1,0]]

# def dfs(x, y, maps):
#     if maps[y][x] == 1:
#         return
    
#     maps[y][x] = 1
#     for direct in directions:
#         if x + direct[1] >= 0 and x + direct[1] < M and y + direct[0] >= 0 and y + direct[0] < N:
#             dfs(x+direct[1], y+direct[0], maps)
    
#     return 

# for y, ma in enumerate(maps):
#     for x, m in enumerate(ma):
#         if m == 1:
#             continue
        
#         answer += 1
#         dfs(x, y, maps)

# print(answer)


# ## 답안예시

# def dfs(x,y):
#     if x<= -1 or x >= N or y <= -1 or y > M:
#         return False
    
#     if maps[y][x] == 0:
#         maps[y][x] = 1 # 방문처리
        
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#     return False

# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i,j) == True:
#             result += 1

# print(result)


### 미로탈출
from collections import deque
N, M = 5, 6 # 5행 6열
maze = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
]

directions = [[0,1], [0,-1], [1,0], [-1,0]]

queue = deque()

def bfs(x, y):
    distance = 1
    queue.append((x, y))
    
    while queue:
        dx, dy = queue.popleft()
        
        if maze[dy-1][dx-1] == 0:
            continue
    
        if dy == M-1 and dx == N-1:
            distance += 1
            return distance
        
        distance += 1
        
        for dir in directions:
            if dx+dir[1] >= 0 and dx+dir[1] < M and dy+dir[0] >= 0 and dy+dir[0] < N:
                queue.append((dx+dir[1]+1, dy+dir[0]+1))
    return

print(bfs(1, 1))