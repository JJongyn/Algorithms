'''
https://www.acmicpc.net/problem/4963
'''

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    

    def bfs(i, j):

        queue = deque()
        queue.append([i, j])
        visited[i][j] = True

        while queue:
            y,x = queue.popleft()

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < w and 0 <= ny < h and visited[ny][nx] is False and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append([ny, nx])

    result = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] is False:
                bfs(i,j)
                result += 1

    print(result)