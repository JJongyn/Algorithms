'''

실버2. https://www.acmicpc.net/problem/21736
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 'O':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 'P':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            result = bfs(i,j)
            if result != 0:
                print(result)
            else:
                print('TT')