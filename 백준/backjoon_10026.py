'''
https://www.acmicpc.net/problem/10026
'''

import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())

graph = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)] # N x N 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 예외 처리 해야 함
        if 0 <= nx < N and 0 <= ny < N and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

def start_loop(visited):
    result = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i,j)
                result += 1
    return result

            
### 적록색약 X
result1 = start_loop(visited)

### 적록색약 O
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False]*N for _ in range(N)]

result2 = start_loop(visited)

print(result1, result2)


            
