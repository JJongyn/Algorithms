'''
https://www.acmicpc.net/problem/15651
'''

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
def dfs(s):
    if len(result) == M:
        print(*result)
        return
    for i in range(1, N+1):
        result.append(i)
        dfs(i)
        result.pop()

result = []
dfs(1)