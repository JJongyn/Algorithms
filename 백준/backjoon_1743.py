from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M, K = map(int, input().split())

graph = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1


def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = 1    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    return cnt


best = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            best = max(best, bfs(i,j))
print(best)
            
    
    
    
    