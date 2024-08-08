'''
https://www.acmicpc.net/problem/2636
'''
import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


def search(x, y):
    q = deque()
    q.append((x,y))
    visited = [[False] * M for _ in range(N)]
    
    ch = 0
    check_flag = False
    while q:
        x, y = q.popleft()

        # 주변 탐색하면서 1이 있는지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] ##  ny = y = dy[i]!!!!!!!!!!!!!!!!

            if 0 <= ny < M and 0 <= nx < N:
                if visited[nx][ny] is False and graph[nx][ny] == 0: # 방문안했고 / 공기부분
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif visited[nx][ny] is False and graph[nx][ny] == 1: # 방문안했고 / 치즈부분
                    ch += 1
                    visited[nx][ny] = True
                    graph[nx][ny] = 0

                    check_flag = True

    return ch, check_flag

flag = True
time = 0
result = []
while flag:
    ch, flag = search(0, 0)
    time += 1
    result.append((time, ch))
print(result[-2][0])
print(result[-2][1])