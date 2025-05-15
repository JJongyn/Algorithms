'''
https://www.acmicpc.net/problem/17425
'''

import sys
input = sys.stdin.readline

MAX = 1000001
f = [0] * MAX
g = [0] * MAX

for i in range(1, MAX):
    for j in range(i, MAX, i):
        f[j] += i

for i in range(1, MAX):
    g[i] = g[i-1] + f[i]

data = list(map(int, input().split()))
T, tc = data[0], data[1:]

print('\n'.join(str(g[i]) for i in tc))
