from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (N+1)
# def bfs(x):
#     deq = deque([x])
#     visited[x] = True
#     count = 0
#     while deq:
#         node = deq.popleft()
#         for next in graph[node]:
#             if not visited[next]:
#                 visited[next] = True
#                 deq.append(next)
#                 count += 1
#     return count

# result = bfs(1)
# print(result)

def dfs(x, cnt):
    visited[x] = True
    for next in graph[x]:
        if not visited[next]:
            cnt = dfs(next, cnt+1)
    return cnt

result = dfs(1, 0)
print(result)

