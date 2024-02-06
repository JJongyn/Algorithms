from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x):
    check = [0 for _ in range(n)]
    que = deque([x])
    
    while que:
        q = que.popleft()
        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                check[i] = 1
                que.append(i)
                visited[x][i] = 1

for i in range(n):
    bfs(i)

for i in visited:
    print(*i)
