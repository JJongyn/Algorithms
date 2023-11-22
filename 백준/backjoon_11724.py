import sys
sys.setrecursionlimit(10000)

def dfs(i):
    visited[i] = True
    for j in array[i]: # i번째 노드와 인접한 노드를 방문해서 방문처리
        if not visited[j]:
            dfs(j)

N, M = map(int, sys.stdin.readline().split())
array = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split()) # 각각의 index가 node번호
    array[a].append(b)
    array[b].append(a)

result = 0
visited = [False] * (N+1)
for i in range(1, N+1): # 모든 노드를 방문해보며
    if not visited[i]:
        dfs(i)
        result += 1
print(result)