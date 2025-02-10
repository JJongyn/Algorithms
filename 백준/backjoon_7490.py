import sys
from collections import deque

input = sys.stdin.readline

L = int(input())

for _ in range(L):
    N = int(input()) # 1 ~ N
    data = list(range(1, N+1)) # [1, 2, .., N]

    def dfs(i, current):
        if i == N+1:
            # print(eval(current)) # unexpected EOF while parsing
            if eval(current.replace(' ', '')) == 0:
                print(current)
            return
        
        for sign in [' ', '+', '-']:
            dfs(i+1, current+sign+str(i)) # ex) '1' + '+' + '2'
    
    dfs(2, '1')
    print()


      






