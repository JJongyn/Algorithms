'''
https://www.acmicpc.net/problem/17086
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int ,input().split())

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

distance = [[-1] * M for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            distance[i][j] = 0  

while queue:
    x, y = queue.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

print(max(max(a) for a in distance))
          


                
            





                
            



             


                
            



