import sys
import copy
from collections import deque

input = sys.stdin.readline

N = int(input())

max_height = 0
graph = []
for _ in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    max_height = max(max_height, max(data))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, n_graph, ch, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <=ny < N:
                if visited[nx][ny] == 0 and n_graph[nx][ny] > ch:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        
best = -1
for h in range(max_height):
    cnt = 0
    ch = h+1
    visited = [[0] * N for _ in range(N)]
    n_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and n_graph[i][j] > ch:
                search(i, j, n_graph, ch, visited)
                cnt += 1
    best = max(best, cnt)
print(best)


