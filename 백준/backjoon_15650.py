'''
N과 M(2)
실버3. https://www.acmicpc.net/problem/15650

'''

## 풀이 1 ##
# N, M = map(int, input().split())
# results = []
# visited = [0] * (N+1)

# def dfs(n, lst):
#     if n == M and sorted(lst) not in results:
#         results.append(lst)
#         return

#     for i in range(1, N+1):
#         if visited[i] != 1:
#             visited[i] = 1
#             dfs(n+1, lst + [i])
#             visited[i] = 0

# dfs(0, [])
# for result in results:
#     print(*result)

## 풀이 2 ##

# N, M = map(int, input().split())
# results = []
# visited = [0] * (N+1)

# def dfs(start, lst):
#     if len(lst) == M:
#         results.append(lst)
#         return

#     for i in range(start, N+1):
#         if visited[i] != 1:
#             visited[i] = 1
#             dfs(i+1,lst + [i])
#             visited[i] = 0

# dfs(1, [])
# for result in results:
#     print(*result)

## 풀이 3 ##
N, M = map(int, input().split())
results = []
visited = [0] * (N+1)

def dfs(start):
    if len(results) == M:
        print(*results)
    
    for i in range(start, N+1):
        if i not in results:
            results.append(i)
            dfs(i+1)
            results.pop()

dfs(1)
