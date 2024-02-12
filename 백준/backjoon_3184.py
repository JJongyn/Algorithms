
'''
실버1. https://www.acmicpc.net/problem/status/3184
'''

from collections import deque

R, C = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*C for _ in range(R)]


graph = []
for i in range(R):
    graph.append(list(input()))

def check(x, y, cnt1, cnt2):
    if graph[x][y] == 'o':
        cnt1 += 1
    elif graph[x][y] == 'v':
        cnt2 += 1
    return cnt1, cnt2
        

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    a, b = 0, 0
    a, b = check(x,y,a,b)
    
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and visited[nx][ny] == 0:
                a, b = check(nx,ny,a,b)
                visited[nx][ny] = 1
                q.append((nx, ny))
    return a, b

life_a = 0
life_b = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and graph[i][j] != '#':
            a, b = bfs(i,j)
            if a > b:life_a+=a
            else:
                life_b+=b

print(life_a, life_b)