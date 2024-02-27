'''

실버1. https://www.acmicpc.net/problem/2583
'''
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N, K = map(int, input().split())

def fill_visited(x1, y1, x2, y2):
    for j in range(y1, y2):
        for i in range(x1, x2):
            graph[j][i] = 1


graph = [[0] * (N) for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    fill_visited(x1, y1, x2, y2)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[y][x] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
                cnt += 1
                q.append((nx, ny))
                graph[ny][nx] = 1
    return cnt 

answer = []
for y in range(M):
    for x in range(N):
        if graph[y][x] == 0:
            answer.append(bfs(x, y))
            
print(len(answer))
print(*sorted(answer))
