'''

실버2. https://www.acmicpc.net/problem/22233
'''
# key값을 0으로 만들고, 0이 값들의 수를 return or value값들 다 더하면 될 듯

from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = {}
r = 0
for _ in range(N):
    memo[input().rstrip()] = 1
    r+=1 
for _ in range(M):
    keyword = set(input().rstrip().split(','))
    for key in keyword:
        if key in memo.keys() and memo[key] == 1:
            memo[key] = 0
            r -= 1
    print(r)