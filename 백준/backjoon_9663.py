'''
https://www.acmicpc.net/problem/9663
'''

import sys

input = sys.stdin.readline
N = int(input())

def safe(x, y, q_location):
    for cx, cy in q_location:
        if x == cx or y == cy:
            return False
        elif abs(cx-x) == abs(cy-y):
            return False
    return True

def dfs(x, q_location = None):
    result = 0

    if x == N:
        return 1

    if q_location is None:
        q_location = []
    
    for y in range(N): # (1,1) (1,2) (1,3)
        if safe(x, y, q_location):
            q_location.append((x,y))
            result += dfs(x+1, q_location) # 만약 끝까지 갔으면 1더해서 나오겟지
            q_location.pop()
    return result

print(dfs(0))
