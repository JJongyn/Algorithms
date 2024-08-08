'''
https://www.acmicpc.net/problem/1389

케빈 베이컨의 6단계 법칙

'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(x):

    visited[x] = 1

    queue = deque()
    queue.append(x)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                #######################################
                visited[i] = visited[a] + 1 # 여기서 못 품
                ####################################### 
                queue.append(i)
    
answer = []
for i in range(1, N+1): # 모든 친구 탐색
    visited = [0] * (N+1)
    bfs(i)
    answer.append(sum(visited))

# print(answer)
print(answer.index(min(answer)) + 1)

