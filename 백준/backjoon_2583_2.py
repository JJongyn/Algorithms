import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N, K = map(int, input().split())
visited = [[False] * N for _ in range(M)]


'''
0 2 4 4
x1, x2 = 0 ~ 4
y1, y2 = 2 ~ 4

'''

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = True

def bfs(x,y):

    visited[y][x] = True
    q = deque()
    q.append((x,y))
    cnt = 1

    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= ny < M and 0 <= nx < N and visited[ny][nx] is False:
                visited[ny][nx] = True
                q.append((nx, ny))
                cnt += 1
    return cnt

ans = []

for i in range(N):
    for j in range(M):
        if visited[j][i] is False:
            ans.append(bfs(i,j))


print(len(ans))
print(*sorted(ans))
                
