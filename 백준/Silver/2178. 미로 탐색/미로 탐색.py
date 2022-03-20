from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 이동가능한 방향은 최대 4
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            # 벽을 넘어갈 경우 x
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= M:
                continue

            # 막혀있음
            if graph[next_x][next_y] == 0:
                continue
            
            # 이전 grpah에 1을 더해서 이동
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))

    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(BFS(0,0))