'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
'''

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = list(map(int, input().split()))
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (N+1)

def search(start):
    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == 0:
                visited[nx] = x
                q.append(nx)

search(1)
print(*visited[2:], sep='\n')
