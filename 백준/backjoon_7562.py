import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]

ans = []
for _ in range(N):
    M = int(input())
    current_x, current_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    visited = [[0] * M for _ in range(M)]

    def bfs(x, y):
        q = deque()
        q.append([x, y])
        visited[y][x] = 1
        while q:
            cx, cy = q.popleft()

            if cx == target_x and cy == target_y:
                return visited[cy][cx] - 1

            for i in range(8):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < M and 0 <= ny < M and visited[ny][nx] == 0:
                    
                    q.append([nx, ny])
                    visited[ny][nx] = visited[cy][cx] + 1

    ans.append(bfs(current_x, current_y))
print(*ans, sep='\n')