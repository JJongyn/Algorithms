'''
실버2. https://www.acmicpc.net/problem/2644

'''
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

result = []
def dfs(v, num):
    num += 1
    visited[v] = True
    if v == B:
        result.append(num)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

dfs(A, 0)
if not result:
    print(-1) 
else:
    print(result[0])
            