'''
차이를 최대로
실버2. https://www.acmicpc.net/problem/10819

6
20 1 15 8 4 10
'''
import math

N = int(input())
data = list(map(int, input().split()))

def dfs(lst):
    global best
    if len(lst) == N:
        ans = sum(abs(lst[i] - lst[i+1]) for i in range(N-1))
        best = max(best, ans)
        return
    
    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(lst + [data[i]])
            visited[i] = 0   

best = -1
lst = []
visited = [0] * (N+1)
dfs(lst)
print(best)