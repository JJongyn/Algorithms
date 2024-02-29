'''
실버3. https://www.acmicpc.net/problem/21921
'''

import sys
from collections import Counter

input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int, input().split()))

if max(visited) == 0:
    print("SAD")
else:
    v = sum(visited[:X]) # 0, 1
    max_v = v
    cnt = 1
    
    for i in range(X, N):
        v += visited[i]
        v -= visited[i-X]
        
        if v > max_v:
            max_v = v
            cnt = 1
        
        elif v == max_v:
            cnt += 1
    
    print(max_v)
    print(cnt)