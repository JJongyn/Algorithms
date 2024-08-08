'''
https://www.acmicpc.net/problem/1189
'''

import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
def dfs(x, y, k):
    global result

    if k == K and x == 0 and y == (C-1):
        result += 1
        
    else:
        graph[x][y] = 'T'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 'T':            
                #graph[nx][ny] = 'T'
                dfs(nx, ny, k+1)
                graph[nx][ny] = '.'

graph[R-1][0] = 'T'
dfs(R-1, 0, 1) # 왼쪽아래가 시작지점
print(result)