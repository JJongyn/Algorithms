'''
N과 M(2)
실버3. https://www.acmicpc.net/problem/15650

'''


N, M = map(int, input().split())
results = []
visited = [0] * (N+1)

def dfs(n, lst):
    if n == M and sorted(lst) not in results:
        results.append(lst)
        return

    for i in range(1, N+1):
        if visited[i] != 1:
            visited[i] = 1
            dfs(n+1, lst + [i])
            visited[i] = 0

dfs(0, [])
for result in results:
    print(*result)