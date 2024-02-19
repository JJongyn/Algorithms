'''

실버1. https://www.acmicpc.net/problem/2468
'''
import copy
from collections import deque


N = int(input())

graph = []
max_height = 0
for _ in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    max_height = max(max_height, max(data))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, new_graph, h_max):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if new_graph[nx][ny] > h_max and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

best = 0
for h_max in range(max_height):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h_max and visited[i][j] == 0:
                bfs(i, j, graph, h_max)
                cnt += 1    
                    
    best = max(cnt, best)

print(best)
    
        
    